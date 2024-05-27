import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Line
from pyecharts.globals import ThemeType
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot

if __name__ == '__main__':
    df = pd.read_csv("data_analysis/jl_change.csv", encoding='gbk')
    # print(df)
    # 视频标题, up主, 观看量, 弹幕数, 点赞数, 投币数, 收藏数, 转发数
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
    df_time = df['时间']

    Watch = []
    Dm = []
    Dz = []
    Tb = []
    Sc = []
    Zf = []
    Sj = []

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
    for element in df_time:
        Sj.append(element)

    line = Line(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    line.add_xaxis(Sj)
    # line.add_yaxis('播放量', Watch)
    line.add_yaxis('弹幕数', Dm)
    line.add_yaxis('点赞数', Dz)
    line.add_yaxis('投币数', Tb)
    line.add_yaxis('收藏数', Sc)
    line.add_yaxis('转发数', Zf)

    line.set_global_opts(
        title_opts=opts.TitleOpts(title='星穹铁道镜流角色pv剑出无回各指数变化趋势折线图',pos_left="25%", pos_top="6%"),
        xaxis_opts=opts.AxisOpts(axislabel_opts=opts.LabelOpts(rotate=45), name="时间"),
        yaxis_opts=opts.AxisOpts(name="参数")
    )

    line.render('星穹铁道镜流角色pv剑出无回各指数变化趋势折线图.html')
    make_snapshot(snapshot, '星穹铁道镜流角色pv剑出无回各指数变化趋势折线图.html', 'picture/星穹铁道镜流角色pv剑出无回各指数变化趋势折线图.png')


