from selenium import webdriver
import csv
import datetime
from time import strftime

if __name__ == '__main__':

    url = "https://www.bilibili.com/video/BV1vw411r7yL/?spm_id_from=333.337.search-card.all.click&vd_source=5bfdd9c5aae2db8e974ef5d8db543de8"
    driver = webdriver.Chrome()
    driver.get(url)

    csv_file = "data_analysis/jl_change.csv"
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['视频标题', '观看量', '弹幕数', '点赞数', '投币数', '收藏数', '转发数', ['时间']])
        all_datas_part0 = driver.find_elements_by_xpath('// *[ @ id = "viewbox_report"] / h1')
        data_title = all_datas_part0[0].text  ###### 视频标题

        all_datas_part2 = driver.find_elements_by_xpath('// *[ @ id = "viewbox_report"] / div / div / span')
        data_watch = all_datas_part2[0].text  ###### 播放量
        if data_watch[-1] in '万':
            num = float(data_watch[0:-1])
            num *= 10000
            data_watch = str(num)

        data_dm = all_datas_part2[1].text  ###### 弹幕数
        if data_dm[-1] in '万':
            num = float(data_dm[0:-1])
            num *= 10000
            data_dm = str(num)

        all_datas_part3 = driver.find_elements_by_xpath('// *[ @ id = "arc_toolbar_report"] / div[1] / div')
        data_video_like_info = all_datas_part3[0].text  ###### 点赞数
        if data_video_like_info[-1] in '万':
            num = float(data_video_like_info[0:-1])
            num *= 10000
            data_video_like_info = str(num)

        data_video_coin_info = all_datas_part3[1].text  ###### 投币数
        if data_video_coin_info[-1] in '万':
            num = float(data_video_coin_info[0:-1])
            num *= 10000
            data_video_coin_info = str(num)

        data_video_fav_info = all_datas_part3[2].text  ###### 收藏数
        if data_video_fav_info[-1] in '万':
            num = float(data_video_fav_info[0:-1])
            num *= 10000
            data_video_fav_info = str(num)

        data_video_share_info = all_datas_part3[3].text  ###### 分享数
        if data_video_share_info[-1] in '万':
            num = float(data_video_share_info[0:-1])
            num *= 10000
            data_video_share_info = str(num)

        data_time = datetime.datetime.now().strftime("%Y-%m-%d")
        # print(data_time)

        row = [data_title, data_watch, data_dm, data_video_like_info, data_video_coin_info,data_video_fav_info, data_video_share_info]
        writer.writerow(row)