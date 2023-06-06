
import pandas as pd
import numpy as np

def preprocessing(data, s_imputer, cat, scaler, k_imputer, simpute_cols, x_cols) :
    # input : data, s_imputer, cat, scaler, k_imputer
    # output : 전처리된 데이터셋
    drop_cols = ['PassengerId','Ticket','Name', 'Cabin']
    
    # (1)불필요한 변수 삭제
    data1 = data.drop(drop_cols, axis = 1)

    # (2) NaN 조치
    data1[simpute_cols] = s_imputer.fit_transform(data1[simpute_cols])

    # (3) FE
    data1['Family'] = data1['SibSp'] + data1['Parch'] + 1
    data1.drop(['SibSp', 'Parch'], axis = 1, inplace = True)

    # (4) 가변수화
    for k, v in cat.items():
        data1[k] = pd.Categorical(data1[k], categories=v, ordered=False)

    data1 = pd.get_dummies(data1, columns =cat.keys(), drop_first = True)

    # (6) 스케일링
    x_val_s = scaler.fit_transform(data1)

    # (7) NaN 조치2 : KNNImputer
    x_val_s = k_imputer.fit_transform(x_val_s)
    x_test = pd.DataFrame(x_val_s, columns = x_cols)

    return x_test
