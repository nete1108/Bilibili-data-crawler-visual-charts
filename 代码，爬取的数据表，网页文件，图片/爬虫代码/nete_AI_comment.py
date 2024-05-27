from selenium import webdriver
import csv
from selenium.webdriver.common.action_chains import ActionChains


if __name__ == '__main__':

    url = 'https://www.bilibili.com/video/BV1Dh4y1B7hL/?vd_source=aa7ea87c008d6da6708ad822cc3ba7e0'
    driver = webdriver.Chrome()
    driver.get(url)

    # //*[@id="comment"]/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[3]/span/span
    # //*[@id="comment"]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[3]/span/span
    # //*[@id="comment"]/div/div/div/div[2]/div[2]/div[3]/div[2]/div[2]/div[3]/span/span

    # //*[@id="comment"]/div/div/div/div[2]/div[2]/div[1]/div[2]/div[2]/div[2]/div
    # //*[@id="comment"]/div/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/div[2]/div

    count_comment = driver.find_elements_by_xpath('//*[@id="comment"]/div/div/div/div[1]/div/ul/li[1]/span[2]')
    num = int(count_comment[0].text)

    csv_file = "data/comment.csv"
    with open(csv_file, 'a', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['序号', '评论者', '评论内容'])

        i = 1
        while(i < num):
            comment_data = driver.find_elements_by_xpath(f'//*[@id="comment"]/div/div/div/div[2]/div[2]/div[{i}]/div[2]/div[2]/div[3]/span/span')
            commenter_data = driver.find_elements_by_xpath(f'//*[@id="comment"]/div/div/div/div[2]/div[2]/div[{i}]/div[2]/div[2]/div[2]/div')

            comment = comment_data[0].text
            commenter = commenter_data[0].text
            # print(comment)
            # print(commenter)
            xh = str(i)
            row = [xh, commenter, comment]
            writer.writerow(row)
            print(f'成功爬取第{i}条评论')
            print(commenter)
            i += 1