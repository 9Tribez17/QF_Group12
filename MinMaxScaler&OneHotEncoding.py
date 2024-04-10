import pandas as pd
from sklearn.preprocessing import LabelEncoder
#导入数据
data = pd.read_csv('clean_churn.csv')
#查看数据类型
#print(data.dtypes)

#数据归一化
def min_max_scaler(data):
    #找出数值列
    numerical_cols = [col_name for col_name in data.columns if data[col_name].dtype in ['int64', 'float64'] and col_name != 'CustomerId']
    for col in numerical_cols:
        min_val = data[col].min()
        max_val = data[col].max()
        data[col] = (data[col] - min_val) / (max_val - min_val)
    return data

#one hot encoding
def OHE(data):
    categorical_cols = ['Gender', 'Geography']
    for col in categorical_cols:
        one_hot = pd.get_dummies(data[col])
        #找出出现次数最少的类别对应的列并删除
        counts = data[col].value_counts()
        min_count_category = counts.idxmin()
        one_hot = one_hot.drop(min_count_category, axis=1)
        #修改列名
        one_hot.columns = [str(f)+col+"_OHE" for f in one_hot.columns]
        #合并
        data = pd.concat([data, one_hot], axis='columns')
        #删除重复列
        data = data.loc[:, ~data.columns.duplicated()]
        #将TRUE,False转为1,0
        for col in one_hot.columns:
            data[col] = LabelEncoder().fit_transform(data[col])
    #删除类别特征
    for col in categorical_cols:
        data = data.drop([col], axis=1)
    return (data)

data = OHE(min_max_scaler(data))
