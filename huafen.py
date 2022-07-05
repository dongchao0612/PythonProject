import os

'''
说明:
    将爬取到的新闻按照年份汇总,保存到yearpath目录,每个文件文件名为年份
'''
if __name__ == '__main__':
    path = "result/"
    yearpath = "resultByyear/"
    # 按年进行新闻合并
    every_year_lst = {}
    # print(os.listdir("./result"))
    text = ''
    for in_ in os.listdir(path):
        fp = open(path + in_, mode="r", encoding='utf-8')

        # 比较时间
        if int(in_[:4]) == 2022:
            f = fp.read().replace("\n", "")
            f = f.replace(" ", "")
            text += f
            every_year_lst[2022] = text

        if int(in_[:4]) == 2021:
            f = fp.read().replace("\n", "")
            f = f.replace(" ", "")
            text += f
            every_year_lst[2021] = text

        if int(in_[:4]) == 2020:
            f = fp.read().replace("\n", "")
            f = f.replace(" ", "")
            text += f
            every_year_lst[2020] = text

        if int(in_[:4]) == 2019:
            f = fp.read().replace("\n", "")
            f = f.replace(" ", "")
            text += f
            every_year_lst[2019] = text

        if int(in_[:4]) == 2018:
            f = fp.read().replace("\n", "")
            f = f.replace(" ", "")
            text += f
            every_year_lst[2018] = text

        if int(in_[:4]) == 2017:
            f = fp.read().replace("\n", "")
            f = f.replace(" ", "")
            text += f
            every_year_lst[2017] = text

        if int(in_[:4]) == 2016:
            f = fp.read().replace("\n", "")
            f = f.replace(" ", "")
            text += f
            every_year_lst[2016] = text

        if int(in_[:4]) == 2015:
            f = fp.read().replace("\n", "")
            f = f.replace(" ", "")
            text += f
            every_year_lst[2015] = text

    # 分年份保存
    for x, y in every_year_lst.items():
        filepath = yearpath + str(x) + ".txt"
        with open(filepath, encoding="utf-8", mode="w", ) as fp:
            print(x, "年的保存完成！")
            fp.write(y)
