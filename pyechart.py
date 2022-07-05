from pyecharts.charts import Bar
from pyecharts import options as opts
import os
import jieba
from pyecharts.globals import ThemeType

if __name__ == '__main__':
    yearpath = "resultByyear/"
    pic = "pic/"
    for in_ in os.listdir(yearpath):
        timelst = []
        wordlst = []
        # print("年份：",in_[:4])
        fp = open(yearpath + in_, mode="r", encoding='utf-8')
        text = fp.read()
        cut_text = (jieba.lcut(text))

        dic = {}
        for word in cut_text:
            if word not in dic:
                dic[word] = 1
            else:
                dic[word] += 1

        swd = sorted(list(dic.items()), key=lambda lst: lst[1], reverse=True)  # 统计每个词出现次数，从高到第排序

        f1 = open('中文虚词列表.txt', encoding="utf-8")  # 排除那些虚词，连词，标点符号等
        stop_wds = f1.read()
        f1.close()
        count = 0
        for kword, times in swd:
            if kword not in stop_wds and count <= 10:  # 当前词未包含在排除的那些词里面，就输出现次数
                count += 1
                timelst.append(times)
                wordlst.append(kword)
        # 使用pyechart绘制柱状图
        bar = (
            Bar(init_opts=opts.InitOpts(theme=ThemeType.WALDEN))
                .add_xaxis(wordlst)
                .add_yaxis(str(in_[:4]), timelst)
                .set_global_opts(title_opts=opts.TitleOpts(title=f'{in_[:4]}年份词频统计'))
        )
        bar.render(f'{pic + in_[:4]}年份词频统计.html')
        # break
