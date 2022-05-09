import requests
from lxml import etree
import time

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
}
if __name__ == '__main__':
    url = "https://www.sdtbu.edu.cn/index/ssyw.htm"
    index = 1
    MAXINDEX = 151
    TOPURL = "https://www.sdtbu.edu.cn/"
    while index <= MAXINDEX:
        response = requests.get(url=url, headers=headers)
        response.encoding = response.apparent_encoding
        print(url, f"列表页{index}:", response.status_code)

        # 创建解析器
        html = response.text
        parse = etree.HTML(html)

        # 解析页面中的新闻详情页url
        a_path = "//div[4]/div[2]/ul/li/a/@href"
        a_lst = parse.xpath(a_path)
        t_path = '//div[4]/div[2]/ul/li/a/@title'
        t_lst = parse.xpath(t_path)
        # print(len(t_lst))
        # 对每个详情页面进行请求
        for a, t in zip(a_lst, t_lst):
            newurl = TOPURL + a[2:]
            newresponse = requests.get(newurl, headers=headers)
            newresponse.encoding = newresponse.apparent_encoding
            # print("\t", newurl, "详情页:", newresponse.status_code)
            newhtml = newresponse.text

            # 创建解析器
            newparse = etree.HTML(newhtml)

            # 文字
            infopath = '//*[@id="vsb_content"]//text()'
            info = newparse.xpath(infopath)
            text = ""
            for in_ in info:
                text += in_
            t = t.replace(r'"', r'”')

            filepath = "result/" + t + ".txt"
            #print(filepath)
            with open(filepath, encoding=newresponse.encoding, mode="w") as fp:
                fp.write(text)

        # 获取"下页"的url
        nextpath = '//table//div/a[@class="Next"]/@href'
        nexturl = parse.xpath(nextpath)  # https://www.sdtbu.edu.cn/index/ssyw/332.htm
        url = TOPURL + "index/ssyw/" + nexturl[0][-7:]

        index += 1
