import requests
from lxml import etree
from datetime import datetime

'''
说明:
    本部分完成的是数据的获取,通过endtime控制爬取数据的截止日期,将每条新闻分别保存到path目录下
'''
if __name__ == '__main__':
    url = "https://www.sdtbu.edu.cn/index/ssyw.htm"
    path = "result/"
    endtime = "2015-01-01"
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36'
    }
    TOPURL = "https://www.sdtbu.edu.cn/"
    statue = {
        200: "OK",
        404: "Not Found"
    }

    i = 1
    # 爬虫部分
    while True:
        try:
            # 新闻列表页进行请求
            response = requests.get(url=url, headers=headers)
            response.encoding = response.apparent_encoding
            print(url, f"第{i}页:的爬取状态:", statue[response.status_code])

            # 创建解析器
            html = response.text
            parse = etree.HTML(html)

            # 解析页面中的新闻详情页url
            a_path = "//div[4]/div[2]/ul/li/a/@href"  # 获取新闻详情页url
            a_lst = parse.xpath(a_path)
            t_path = '//div[4]/div[2]/ul/li/a/@title'  # 获取新闻title
            t_lst = parse.xpath(t_path)
            ti_path = '//div[4]/div[2]/ul/li/p/text()'  # 获取时间time
            ti_lst = parse.xpath(ti_path)

            # 对每个详情页面进行请求
            for a, t, ti in zip(a_lst, t_lst, ti_lst):
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
                # 去除转义字符
                for in_ in info:
                    if in_ == "\r\n" or in_ == "\r\n  " or in_ == "\ufeff" or in_ == "\xa0\xa0":
                        pass
                    else:
                        text += in_
                t = t.replace(r'"', r'”')

                y = datetime.strptime(ti, '%Y-%m-%d')  # 新闻发布的时间
                z = datetime.strptime(endtime, '%Y-%m-%d')  # 截止日期

                diff = z - y
                chazhi = diff.days * 86400 + diff.seconds  # 时间差

                # 设置时间限制
                if chazhi <= 0:
                    # print("y = ", y, "diff = ", diff)
                    filepath = f"{path}" + ti + " " + t + ".txt"

                    with open(filepath, encoding=newresponse.encoding, mode="w") as fp:
                        fp.write(text)
                else:
                    exit(0)

            # 获取"下页"的url
            nextpath = '//table//div/a[@class="Next"]/@href'
            nexturl = parse.xpath(nextpath)
            url = TOPURL + "index/ssyw/" + nexturl[0][-7:]

        except Exception as e:
            print(e)

        i += 1
