import pandas as pd
from django.http import HttpResponse
from django.http import FileResponse
from . import variable as var
from .to_rdf import AED, CareService, MedicalEquipment, CulturalProperty, Tourist, Event, PublicWirelessLan, PublicToilet, FireHydrant, EvacuationSite, Population, PublicFacility, ChildcareFacility
import io

# データ項目定義書に準ずるデータフレームに変換
def to_csv(df, category, select_col):
    # 該当するカラム名と選択したカラム名を対応させる辞書を作成
    dic = {}
    for i, l in enumerate(select_col):
        dic.setdefault(l, []).append(df.columns[i])

    # 選択されたカテゴリーのデータフレームをsample_dfに格納
    sample_df = pd.DataFrame(columns=var.DATASET_COL[category])
    sample_df.iloc[:, 0] = [None]*df.shape[0]

    for col in dic.keys():
        if col == 'NotUse':
            continue
        elif len(dic[col]) >= 2 or col == "備考":
            for i in range(len(df)):
                bool_list = df.loc[df.index[i], dic[col]] != ''
                if bool_list.sum() != 0:
                    sample_df.loc[sample_df.index[i], col] = df.loc[df.index[i], list(df.loc[df.index[i], dic[col]][bool_list].index)].to_json(orient='columns', force_ascii=False)
        else:
            sample_df[col] = df[dic[col][0]]

    return sample_df

# CSVファイルに変換
def res(sample_df, file_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
    sample_df.to_csv(path_or_buf=response, encoding='utf-8', index=False)
    return response

# RDF(N-Triples形式)に変換
def to_rdf(df, file_name, category):
    w = io.StringIO()
    df = df.fillna('').replace('\n', ' ', regex=True)

    # AED設置一覧
    if category == '0':
        AED.to_rdf(w, df)
    # 介護サービス事業所一覧
    elif category == '1':
        CareService.to_rdf(w, df)
    # 医療機器一覧
    elif category == '2':
        MedicalEquipment.to_rdf(w, df)
    # 文化財一覧
    elif category == '3':
        CulturalProperty.to_rdf(w, df)
    # 観光施設一覧
    elif category == '4':
        Tourist.to_rdf(w, df)
    # イベント一覧
    elif category == '5':
        Event.to_rdf(w, df)
    # 公共無線LANアクセスポイント一覧
    elif category == '6':
        PublicWirelessLan.to_rdf(w, df)
    # 公衆トイレ一覧
    elif category == '7':
        PublicToilet.to_rdf(w, df)
    # 消防水利施設一覧
    elif category == '8':
        FireHydrant.to_rdf(w, df)
    # 指定緊急避難場所一覧
    elif category == '9':
        EvacuationSite.to_rdf(w, df)
    # 地域・年齢別人口
    elif category == '10':
        Population.to_rdf(w, df)
    # 公共施設一覧
    elif category == '11':
        PublicFacility.to_rdf(w, df)
    # 子育て施設一覧
    elif category == '12':
        ChildcareFacility.to_rdf(w, df)

    response = HttpResponse(w.getvalue(), content_type='text/plain')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
    return response


