import csv
from selenium import webdriver
import pandas as pd

if __name__ == '__main__':

    # url = 'https://www.bilibili.com/v/food'
    # driver = webdriver.Chrome()
    # driver.get(url)
    #
    # # //*[@id="i_cecream"]/div/main/div/div[3]/div/div[1]/div[1]/a/span
    # # //*[@id="i_cecream"]/div/main/div/div[4]/div/div[1]/div[1]/a/span
    # # //*[@id="i_cecream"]/div/main/div/div[7]/div/div[1]/div[1]/a/span
    # # //*[@id="i_cecream"]/div/main/div/div[3]/div/div[1]/div[2]/a
    # # //*[@id="i_cecream"]/div/main/div/div[4]/div/div[1]/div[2]/a
    # # //*[@id="i_cecream"]/div/main/div/div[7]/div/div[1]/div[2]/a
    # csv_file = "data/food_part_url.csv"
    # with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['栏目', '链接'])
    #
    #     i = 3
    #     while(i < 8):
    #         all_part_name = (driver.find_elements_by_xpath(f'//*[@id="i_cecream"]/div/main/div/div[{i}]/div/div[1]/div[1]/a/span'))[0].text
    #         all_part_url = driver.find_elements_by_xpath(f'//*[@id="i_cecream"]/div/main/div/div[{i}]/div/div[1]/div[2]/a')
    #         href_values = [element.get_attribute("href") for element in all_part_url]  # 栏目链接
    #         writer.writerow([all_part_name, href_values[0]])
    #         i += 1

#######################################################################################################################################################
    # df = pd.read_csv("data/food_part_url.csv")
    # all_urls = df['链接']
    # name = df['栏目']
    # driver = webdriver.Chrome()
    # csv_file = "data/food_part_video_url.csv"
    #
    # with open(csv_file, 'w', newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['栏目', '视频标题', '视频链接'])
    #
    #     j = 0
    #     for url in all_urls:
    #         driver.get(url)
    #         # //*[@id="i_cecream"]/div/main/div/div[3]/div[2]/div[1]/div[2]/div/div/h3/a
    #         # //*[@id="i_cecream"]/div/main/div/div[3]/div[2]/div[2]/div[2]/div/div/h3/a
    #         # //*[@id="i_cecream"]/div/main/div/div[3]/div[2]/div[1]/div[2]/div/div/h3
    #         i = 1
    #         while(i < 51):
    #             video_name = (driver.find_elements_by_xpath(f'//*[@id="i_cecream"]/div/main/div/div[3]/div[2]/div[{i}]/div[2]/div/div/h3'))[0].text
    #             video_element = driver.find_elements_by_xpath(f'//*[@id="i_cecream"]/div/main/div/div[3]/div[2]/div[{i}]/div[2]/div/div/h3/a')
    #             href_values = [element.get_attribute("href") for element in video_element]  # 视频链接
    #             video_url = href_values[0]
    #             writer.writerow([name[j], video_name, video_url])
    #             i += 1
    #         j += 1
########################################################################################################################################################

    # df = pd.read_csv("data/food_part_video_url.csv")
    # all_urls = df['视频链接']
    # # print(all_urls)
    # driver = webdriver.Chrome()
    # csv_file = 'data/food_video_label.csv'
    #
    # with open(csv_file, 'a', newline='', encoding='utf-8') as f:
    #     writer = csv.writer(f)
    #     writer.writerow(['序号', '标签'])
    #
    #     xh = 1
    #     for url in all_urls:
    #         driver.get(url)
    #         # //*[@id="v_tag"]/div
    #         label_str = (driver.find_elements_by_xpath('//*[@id="v_tag"]/div'))[0].text.split('\n')
    #         label_len = len(label_str)
    #         i = 1
    #         while(i < label_len):
    #             label = label_str[i]
    #             writer.writerow([xh, label])
    #             i += 1
    #             xh += 1

    pass




