import csv
from selenium import webdriver

if __name__ == '__main__':

    url = "https://www.bilibili.com/v/musicplus/video"
    driver = webdriver.Chrome()
    driver.get(url)

    csv_file = "data_analysis/music_hank.csv"
    i = 50
    music_type_list = []
    while(i < 120):
        data_type_elements = driver.find_elements_by_xpath(f'//*[@id="main"]/div/div[2]/ul[2]/li[{int(i/5)}]')
        data_type = data_type_elements[0].text
        i += 1

    # print(music_type_list)
        with open(csv_file, 'a', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerow([data_type])

            j = 1
            while j:
                data_bf_element = driver.find_elements_by_xpath(f'//*[@id="main"]/div/div[3]/div[{j}]/div/a/div[1]/div[1]/span[1]')
                if not data_bf_element:
                    break
                else:
                    data_bf = data_bf_element[0].text
                    if data_bf[-1] in '万':
                        num = float(data_bf[0:-1])
                        num *= 10000
                        data_bf = str(num)
                    writer.writerow([data_bf])
                    j += 1