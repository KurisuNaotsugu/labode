import streamlit as st
import pandas as pd
import altair as alt

# グラフの描画用関数を定義
def get_chart(data):
    hover = alt.selection_single(
        fields=["month"],
        nearest=True,
        on="mouseover",
        empty="none",
    )

    lines = (
        alt.Chart(data, title="temperature")
        .mark_line()
        .encode(
            x="month",
            y="temperature",
            color="symbol",
            strokeDash="symbol",
        )
    )

    # Draw points on the line, and highlight based on selection
    points = lines.transform_filter(hover).mark_circle(size=65)

    # Draw a rule at the location of the selection
    tooltips = (
        alt.Chart(data)
        .mark_rule()
        .encode(
            x="month",
            y="temperature",
            opacity=alt.condition(hover, alt.value(0.3), alt.value(0)),
            tooltip=[
                alt.Tooltip("month", title="Month"),
                alt.Tooltip("temperature", title="Temp (degree)"),
            ],
        )
        .add_selection(hover)
    )

    return (lines + points + tooltips).interactive()

# ページのタイトル（なくてもいい）
st.title('My first Streamlit app')
# ファイルアップローダーの準備
uploaded_file = st.file_uploader("CSVファイルのアップロード", type="csv")

# uploadファイルが存在するときだけ、CSVファイルの読み込みがされる。
if uploaded_file is not None:
	# コメント行をスキップして読み込んでくれる
    dataframe = pd.read_csv(uploaded_file, comment="#")
    chart = get_chart(dataframe)
    st.altair_chart(chart, use_container_width=True)