import streamlit as st
import pandas as pd
import plotly.graph_objects as go


###############
# Functions
###############
def get_plotly_chart(data:pd.DataFrame, 
                    graph_title:str, 
                    x_col:str='time', 
                    y1_col:str='UVabsorbance', 
                    y2_col:str='concB',
                    x_label:str='Running time [min]',
                    y1_label:str='UVabsorbance',
                    y2_label:str='Conc.B [%]'
                    ) -> go.Figure:
    """Create a Plotly figure with dual y-axes."""
    fig = go.Figure()

    # First y-axis (Left)
    fig.add_trace(
        go.Scatter(
            x=data[x_col],
            y=data[y1_col],
            mode='lines',
            name=y1_label,
            marker=dict(size=8),
            hovertemplate=
                'Time: %{x}<br>' +
                'UVabs.: %{y}<br>' +
                'Conc.B: %{customdata[0]}<extra></extra>',
            customdata=data[[y2_col]],
            line=dict(color='blue')
        )
    )

    # Second y-axis (Right)
    fig.add_trace(
        go.Scatter(
            x=data[x_col],
            y=data[y2_col],
            mode='lines',
            name=y2_label,
            marker=dict(size=8),
            yaxis='y2',
            line=dict(color='orange')
        )
    )

    # Layout settings
    fig.update_layout(
        title=graph_title,
        xaxis=dict(title=x_label),
        yaxis=dict(title=y1_label, side='left'),
        yaxis2=dict(title=y2_label, overlaying='y', side='right'),
        hovermode='x unified'
    )

    return fig

###############
# Streamlit UI
###############
st.title('Chromatograph Plotter for AKTA systems')
st.markdown("""
タンパク質精製用低圧液体クロマトグラム、AKTAシステムのUnicornソフトウェアからエクスポートされたCSVファイルを使用して、クロマトグラムをプロットします。  
- 左軸: UV吸収 (UVabsorbance)  
- 右軸: B液濃度 (Conc.B)  
ファイルをアップロードし、グラフタイトルを入力してください。
""")
graph_title = st.text_input("グラフタイトルを入力してください", "Chromatograph")
uploaded_file = st.file_uploader("unicornの標準エクスポートファイルをアップロード(csv)", type="csv")

if uploaded_file:
    dataframe = pd.read_csv(uploaded_file, comment="#")
    st.dataframe(dataframe.head())
    fig = get_plotly_chart(dataframe, graph_title)
    st.plotly_chart(fig, use_container_width=True)
