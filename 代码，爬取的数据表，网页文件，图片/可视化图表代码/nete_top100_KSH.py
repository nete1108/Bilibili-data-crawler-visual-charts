import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

if __name__ == '__main__':
    df = pd.read_csv("data/top100_details.csv")
    # print(df)
    # 视频标题, up主, 观看量, 弹幕数, 点赞数, 投币数, 收藏数, 转发数
    # df_title = df['视频标题'].head(10)
    df_title = df['视频标题']
    # df_up = df['up主']
    # df_watch = df['观看量'].head(10)
    df_watch = df['观看量']
    # df_dm = df['弹幕数'].head(10)
    df_dm = df['弹幕数']
    # df_dz = df['点赞数'].head(10)
    df_dz = df['点赞数']
    # df_tb = df['投币数'].head(10)
    df_tb = df['投币数']
    # df_sc = df['收藏数'].head(10)
    df_sc = df['收藏数']
    # df_zf = df['转发数'].head(10)
    df_zf = df['转发数']
    Title = []
    Watch = []
    Dm = []
    Dz = []
    Tb = []
    Sc = []
    Zf = []
    for element in df_title:
        Title.append(element)
    # print(Title)
    for element in df_watch:
        Watch.append(element)
    # print(Watch)
    for element in df_dm:
        Dm.append(element)
    # print(Dm)
    for element in df_dz:
        Dz.append(element)
    # print(Dz)
    for element in df_tb:
        Tb.append(element)
    # print(Tb)
    for element in df_sc:
        Sc.append(element)
    # print(Sc)
    for element in df_zf:
        Zf.append(element)
    # print(Zf)


    bar1 = Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE, width="4500px", height="1200px"))
    bar1.add_xaxis(Title)
    # line.set_global_opts(xaxis_opts=opts.AxisOpts(name_rotate=60, axislabel_opts={"rotate": 15}))
    bar1.set_global_opts(
        title_opts=opts.TitleOpts(title="b站热门榜top100数据统计柱状图", pos_left="50%", pos_top="5%"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45)))
    # bar1.add_yaxis('播放量', Watch)
    bar1.add_yaxis('弹幕数', Dm)
    bar1.add_yaxis('点赞数', Dz)
    bar1.add_yaxis('投币数', Tb)
    bar1.add_yaxis('收藏数', Sc)
    bar1.add_yaxis('转发数', Zf)
    bar1.render('b站热门榜top100数据统计柱状图.html')
    make_snapshot(snapshot, "b站热门榜top100数据统计柱状图.html", "./picture/b站热门榜top100数据统计柱状图.png")

# bar2 = Bar(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE, width="2500px", height="1000px"))
    # bar2.add_xaxis(Title)
    # bar2.add_yaxis('播放量',Watch)
    # bar1.overlap(bar2)
    # bar1.reversal_axis()


