import pandas as pd
from django.http import HttpResponse
from django.http import FileResponse
from . import variable as var
from .to_rdf import AED
import io

# データ項目定義書に準ずるデータフレームに変換
def to_csv(df, category, select_col):
    # 該当するカラム名と選択したカラム名を対応させる辞書を作成
    dic = {}
    for i, l in enumerate(select_col):
        dic.setdefault(l, []).append(df.columns[i])
    print(dic)

    # 選択されたカテゴリーのデータフレームをsample_dfに格納
    sample_df = pd.DataFrame(columns=var.DATASET_COL[category])
    sample_df.iloc[:, 0] = [None]*df.shape[0]

    for col in dic.keys():
        if col == 'NotUse':
            continue
        elif len(dic[col]) >= 2 or col == "備考":
            print(col)
            for i in range(len(df)):
                sample_df.loc[sample_df.index[i], col] = df.loc[df.index[i], dic[col]].to_json(orient='columns', force_ascii=False)
        else:
            sample_df[col] = df[dic[col][0]]

    return sample_df

# CSVファイルに変換
def res(sample_df, file_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
    sample_df.to_csv(path_or_buf=response, encoding='utf-8-sig', index=False)
    return response

# RDF(N-Triples形式)に変換
def to_rdf(df, file_name, category):
    w = io.StringIO()
    df = df.fillna('')
    if category == '0':
        AED.to_rdf(w, df)
    response = HttpResponse(w.getvalue(), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
    return response


