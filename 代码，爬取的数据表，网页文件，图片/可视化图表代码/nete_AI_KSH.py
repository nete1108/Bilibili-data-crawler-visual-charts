import pandas as pd
import numpy as np
from pyecharts import options as opts
from pyecharts.charts import Pie
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

if __name__ == '__main__':

    df = pd.read_csv('./data_analysis/comments_finish.csv', encoding='gbk')

    df_mood = df.groupby('感情').size().sort_values(ascending=False)
    datas = list(zip(df_mood.index.to_list(),df_mood.to_list()))
    # print(datas)
    title = "有关'AI越来越“变态”了，10大AI神器闻所未闻！'的相关评论的情感分析饼状图"
    pie = Pie(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    pie.add("", datas)
    pie.set_global_opts(
        title_opts=opts.TitleOpts(title=title),
        legend_opts=opts.LegendOpts(pos_right="right")
    )
    pie.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}: {d}%"))
    pie.render('AI_视频情感态度分析统计饼状图.html')

    make_snapshot(snapshot, "AI_视频情感态度分析统计饼状图.html", "./picture/AI_视频情感态度分析统计饼状图.png")

