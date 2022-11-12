#準備段階
from pydoc import plain
import matplotlib.pyplot as plt
import pandas as pd

#CSVを読み込む
data = pd.read_csv(r"C:\Users\ekish\Desktop\yequ\荵ｦ蠎怜崟荵ｦ髞驥丞柱蟷ｿ蜻願ｴｹ逕ｨ.csv")
data2 = pd.read_csv(r"C:\Users\ekish\Desktop\yequ\data2.csv")
data3 = pd.read_csv(r"C:\Users\ekish\Desktop\yequ\data3.csv")

#准备画布
plt.rcParams["font.sans-serif"]="SimHei"
plt.figure(figsize=(7,7),facecolor="white")

#子图像1【随着时间变化曝光率和转化率关系双y轴对比图】
plt.subplot(2,2,1)
plt.bar(data3["month"],data3["CVR"],width=0.7,color="blue",label="转化率")
plt.xlabel("时间")
plt.ylabel("转化率")
plt.title("2019年8月到2020年7月的曝光与转化率的关系")
plt.xticks(rotation=90)
plt.legend(loc="upper right")

plt.twinx()

plt.plot(data3["month"],data3["exposure"],color="orange",marker="o",label="曝光度")
plt.ylabel("曝光度")
plt.legend()

#子图像2【2019年8月到2020年7月广告费和销量的关系发布散步图】
plt.subplot(2,2,2)
plt.scatter(data["ads_fee"],data["sales"],label="销量")
plt.xlabel("广告费")
plt.ylabel("销量")
plt.title("2019年8月到2020年7月广告费与销量关系趋势")
plt.legend()

#子图像3【三层楼的销售量的横向对比簇形柱状图】
plt.subplot(2,2,3)
data2.plot.bar("month",["first_floor","second_floor","third_floor"],ax=plt.gca())
plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月到2020年7月三层楼的销售横向对比")

#子图像4【2019年8月到2020年7月三层楼百分比堆积柱状图】
plt.subplot(2,2,4)
data2["一楼"] = data2["first_floor"]/data2["sum"]
data2["二楼"] = data2["second_floor"]/data2["sum"]
data2["三楼"] = data2["third_floor"]/data2["sum"]
data2.plot.bar("month",["一楼","二楼","三楼"],stacked=True,ax=plt.gca())
plt.xlabel("月份")
plt.ylabel("销量")
plt.title("2019年8月待2020年7月三层楼的销售百分比堆积柱状图")

#展示图表
plt.tight_layout()
plt.show()
