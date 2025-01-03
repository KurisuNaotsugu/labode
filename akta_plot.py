import streamlit as st
import pandas as pd
import altair as alt

# グラフの描画用関数を定義
def get_chart(data, text_input):
    # 第一軸(UV吸収)
    hover = alt.selection_point(
        fields=["time"],
        nearest=True,
        on="mouseover",
        empty=False,
    )
    line1 = (
        alt.Chart(data)
        .mark_line()
        .encode(
            x= alt.X("time", title="Running time [min]"),
            y= alt.Y("UVabsorbance"),
        )
        .properties(
            title=text_input
        )
    )
    # Draw points on the line, and highlight based on selection
    points = line1.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x= alt.X("time"),
            #y= alt.Y("UVabsorbance"),
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("time", title="Time"),
                alt.Tooltip("UVabsorbance", title="UVabs."),
                alt.Tooltip("concB", title="Conc.B [%]"),
            ],
        )
        .add_selection(hover)
    )
    # 第二軸(B液濃度)
    line2 = (
        alt.Chart(data, title="Chromatograph")
        .mark_line(color="orange")
        .encode(
            x= alt.X("time2", title=""),
            y=alt.Y("concB", title="Conc.B [%]", scale=alt.Scale(domain=[0, 120]))
        )
    )
    chart = alt.layer(line1 + points + tooltips, line2).resolve_scale(y="independent")
    return chart.interactive()

# ページのタイトル（なくてもいい）
st.title('Create Chromatograph Plot')
# テキストボックスの配置
text_input = st.text_input("グラフタイトルを入力してください", "Chromatograph")
# ファイルアップローダーの準備
uploaded_file = st.file_uploader("unicornの標準エクスポートファイルをアップロード", type="csv")

# uploadファイルが存在するときだけ、CSVファイルの読み込みがされる。
if uploaded_file is not None:
	# コメント行をスキップして読み込んでくれる
    dataframe = pd.read_csv(uploaded_file, comment="#")
    st.dataframe(dataframe)
    chart = get_chart(dataframe, text_input)
    st.altair_chart(chart, use_container_width=True)