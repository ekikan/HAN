# 准备
import pandas as pd
# 读取文件
data = pd.read_csv(r"C:\Users\ekish\Desktop\data\book_data\BookRates.csv")
# 构建数据透视表
userratings = data.pivot_table(index="ISBN",columns="user_id",values="rating")
# 通过皮尔逊系数找出与编号638的相似用户
userpearson = userratings.corr(method="pearson",min_periods=5)
user638pearson = userpearson[638].drop(index=638)
targetUser =user638pearson.idxmax()
# 推荐和用户638相似评分在8分以上并却没有看过的书籍
targetUserRating = userratings[targetUser]
targetUserRating = targetUserRating[targetUserRating.values>8]
user638Rating = userratings[638].dropna()
targetUser = targetUserRating.index
user638 = user638Rating.index
targetISBN = targetUser[~targetUser.isin(user638)]
# 通过访问index对象的.values并输出
ISBMList = targetISBN.values
print(f"推荐给目标638的书籍列表为{ISBMList}")