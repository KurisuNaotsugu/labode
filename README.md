# Chromatograph Plotter for AKTA Systems

タンパク質精製用低圧液体クロマトグラム（AKTAシステム）のUnicornソフトウェアからエクスポートされたCSVファイルを読み込み、クロマトグラムをプロットするStreamlitアプリです。

## 特徴

- 左軸: UV吸収 (UVabsorbance)
- 右軸: B液濃度 (Conc.B)
- 2軸のラインチャートをPlotlyで描画
- ホバーで両方の値を同時に表示
- CSVファイルをアップロードして簡単に可視化

## インストール

Python 3.12以上を推奨。
```bash
# 仮想環境を作成 (任意)
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate     # Windows

# 必要なライブラリをインストール
pip install streamlit pandas plotly
```

## 使い方

1. CSVファイルを用意（Unicornの標準エクスポート形式）
2. Streamlitアプリを起動

```bash
streamlit run app.py
```

3. ブラウザで開いたアプリにCSVをアップロード
4. グラフタイトルを入力
5. クロマトグラムを確認

## CSVフォーマット例
```
time,UVabsorbance,concB
1,0,0
2,2,0
3,3,2
4,8,4
5,10,6
6,6,8
...
```
- time : ランニングタイム（分）
- UVabsorbance : UV吸収
- concB : B液濃度 [%]

## ライセンス
MIT License © 2025 Kurisu Naotsugu