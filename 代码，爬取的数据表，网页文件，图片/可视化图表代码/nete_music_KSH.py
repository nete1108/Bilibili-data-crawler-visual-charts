# import pandas as pd
# from pyecharts import options as opts
# from pyecharts.charts import Bar
# from pyecharts.render import make_snapshot
# from snapshot_selenium import snapshot
#
# if __name__ == '__main__':
#
#     df = pd.read_csv('data_analysis/music_hank.csv', encoding='gbk')
#     # print(df)
#     type_sums = df.sum()
#     print(type_sums)
#     df_type_sum = list(zip(type_sums.index.to_list(),type_sums.to_list()))
#
#     x_type = [i[0] for i in df_type_sum]
#     y_type = [i[1] for i in df_type_sum]
#
#     bar_type = Bar()
#     bar_type.add_xaxis(x_type)
#     bar_type.add_yaxis("", y_type)
#
#     bar_type.set_global_opts(
#         xaxis_opts=opts.AxisOpts(name="Music_Type"),
#         title_opts=opts.TitleOpts(title="热歌榜各曲风音乐播放排行帮（各曲风选前150个视频）"),
#         yaxis_opts=opts.AxisOpts(name="播放总量(/次)"),
#         legend_opts=opts.LegendOpts(pos_top="10%")
#     )
#
#     bar_type.render("热歌榜各曲风音乐播放排行榜柱状图.html")
#
#     make_snapshot(snapshot, "热歌榜各曲风音乐播放排行榜柱状图.html", "./picture/热歌榜各曲风音乐播放排行榜柱状图.png")

import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Funnel
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.globals import ThemeType

if __name__ == '__main__':

    df = pd.read_csv('data_analysis/music_hank_new.csv', encoding='gbk')
    # print(df)
    type_sums = df.sum()
    print(type_sums)
    df_type_sum = list(zip(type_sums.index.to_list(),type_sums.to_list()))
    # print(df_type_sum)
    sort_type_sum = sorted(df_type_sum, key=lambda x:x[1])
    # print(sort_type_sum)
    funnel = Funnel(init_opts=opts.InitOpts(theme=ThemeType.VINTAGE))
    funnel.add("", sort_type_sum,
               gap=0.9,
               label_opts=opts.LabelOpts(formatter="{b} : {d}%"),
               )
    funnel.set_global_opts(
        title_opts=opts.TitleOpts(title="热歌榜各曲风音乐播放排行榜漏斗图", pos_left="center"),
        legend_opts=opts.LegendOpts(pos_left='70%',pos_bottom='40%'),  # 将图例放到右侧
    )

    funnel.render('热歌榜各曲风音乐播放排行榜漏斗图.html')
    make_snapshot(snapshot, "热歌榜各曲风音乐播放排行榜漏斗图.html", "./picture/热歌榜各曲风音乐播放排行榜漏斗图.png")

