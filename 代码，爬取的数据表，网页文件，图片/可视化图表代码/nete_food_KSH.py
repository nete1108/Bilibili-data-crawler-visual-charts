import pyecharts.options as opts
from pyecharts.charts import WordCloud
import pandas as pd
from pyecharts.globals import SymbolType
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot


if __name__ == '__main__':

    df = pd.read_csv("data_analysis/food_video_label.csv")
    # print(df)
    df_label = df.groupby('标签').size().sort_values(ascending=False)
    # print(df_label)
    datas = list(zip(df_label.index.to_list(),df_label.to_list()))
    # print(datas)
    cloud = WordCloud(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    cloud.add('', datas,shape='circle')
    cloud.set_global_opts(
        title_opts=opts.TitleOpts(title="b站美食热点标签统计分析云图", pos_left="37%", pos_top="3%")
    )
    cloud.render("b站美食热点标签统计分析云图.html")
    # make_snapshot(snapshot, "b站美食热点标签统计分析云图.html", "./picture/b站美食热点标签统计分析云图.png")

