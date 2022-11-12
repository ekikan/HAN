#前準備
import pandas as pd
import matplotlib.pyplot as plt
plt.rcParams["font.sans-serif"] = "SimHei"

#データの読み込み
data = pd.read_csv(r"C:\Users\ekish\Desktop\data\housing\成都房价.csv")

#描述性分析可以更好的看出数据的大小，主要分为集中趋势和离散趋势
#集中趋势表示数据的中心位置，能够代表的描绘总体数据的某一特征
#求房子总价和建筑面积的平均数与中位数
price_mean = data["房子总价/万"].mean()
price_median = data["房子总价/万"].median()

area_mean = data["建筑面积(平方)"].mean()
area_median = data["建筑面积(平方)"].median()


#直方图是展示数据发布的图表
#绘制成都房价和建筑面积的直方图
plt.subplot(2,2,1)
plt.hist(data["房子总价/万"],bins=100)
plt.xlabel("房子总价/万")
plt.title("成都房价分布图")

plt.subplot(2,2,2)
plt.hist(data["建筑面积(平方)"],bins=100)
plt.xlabel("建筑面积(平方)")
plt.title("成都房子建筑面积分布图")
plt.show()

#离散趋势代表数据偏离中心值的特征，通常用方差和标准差来表示，方差和标准差越大说明每个数据距离均值的距离越远，数据就越分散。
#求成都房价和建筑面积的方差，标准差，众数和四分位数等数据
price_var = data["房子总价/万"].var()
price_std = data["房子总价/万"].std()
price_mode = data["房子总价/万"].mode()[0]
print(f"成都房子的平均价格是{price_mean}万元，中位数是{price_median}万元，平均建筑面积是{area_mean}平方，中位数是{area_median}平方。")

print(f"成都房价的方差为{price_var}，标准指为{price_std}，众数为{price_mode}")

area_var = data["建筑面积(平方)"].var()
area_std = data["建筑面积(平方)"].std()
area_mode = data["建筑面积(平方)"].mode()[0]
print(f"成都建筑面积的方差为{area_var}，标准差为{area_std}，众数为{area_mode}")

print(data.describe())

#统计所在区域的分布频度并排列
data["所在区域"] = data["所在区域"].astype("category")
housePosition = data["所在区域"].value_counts
print(housePosition)

plt.show()