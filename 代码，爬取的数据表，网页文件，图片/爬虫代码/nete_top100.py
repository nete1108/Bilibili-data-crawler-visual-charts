import csv
from selenium import webdriver
import pandas as pd

# b站实时排行榜前100的视频url的批处理

if __name__ == '__main__':

    url = 'https://www.bilibili.com/v/popular/rank/all'
    driver = webdriver.Chrome()
    driver.get(url)

    csv_file = "data/top100_url.csv"

    with open(csv_file, 'a',newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['b站实时排行榜前一百视频url','up主昵称'])

        i = 1
        print()
        while(i < 101):
            all_datas = driver.find_elements_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/ul/li[{i}]/div/div[2]/a')
            all_up_name = driver.find_elements_by_xpath(f'//*[@id="app"]/div/div[2]/div[2]/ul/li[{i}]/div/div[2]/div/a/span')
            href_values = [element.get_attribute("href") for element in all_datas]    # 视频链接
            up_name = all_up_name[0].text                                             # up主昵称
            print(href_values)
            print(href_values[0])
            print(type(href_values[0]))
            writer.writerow([href_values[0], up_name])
            print(f'第{i}个视频已经爬取完成')
            i += 1

        # print(url_list)

#######################################################################################################################
    all_urls = pd.read_csv('./data/top100_url.csv')
    # print(all_urls)
    # 'b站实时排行榜前一百视频url'
    all_video_urls = all_urls['b站实时排行榜前一百视频url']
    all_video_up = all_urls['up主昵称']

    driver = webdriver.Chrome()
    csv_file = "data/top100_details.csv"
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['视频标题', 'up主', '观看量', '弹幕数', '点赞数', '投币数', '收藏数', '转发数'])

        i = 0
        for url in all_video_urls:
            driver.get(url)
            # // *[ @ id = "viewbox_report"] / h1
            all_datas_part0 = driver.find_elements_by_xpath('// *[ @ id = "viewbox_report"] / h1')
            data_title = all_datas_part0[0].text  ###### 视频标题

            # data_up = all_datas_part1[0].text                            ###### up主
            data_up = all_video_up[i]

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

            row = [data_title, data_up, data_watch, data_dm, data_video_like_info, data_video_coin_info,
                   data_video_fav_info, data_video_share_info]
            writer.writerow(row)
            print(f'第{i + 1}个视频已经爬取成功！')
            i += 1

    pass

