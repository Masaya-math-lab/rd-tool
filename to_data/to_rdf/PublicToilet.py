# 公衆トイレ一覧
import random
import string

def to_rdf(w, df):
    # 空白ノードの生成
    dat = string.digits + string.ascii_lowercase
    node = '_:node' + ''.join([random.choice(dat) for i in range(9)]) + 'x'
    node_num = 1
    for i in range(len(df)):
        row = df.iloc[i]

        # 都道府県コード又は市区町村コード
        id = row[0]
        # NO
        no = row[1]
        # 都道府県名
        prefecture = row[2]
        # 市区町村名
        city = row[3]
        # 名称
        name = row[4]
        # 名称_カナ
        name_kana = row[5]
        # 名称_英語
        name_eng = row[6]
        # 住所
        address = row[7]
        # 方書
        direction = row[8]
        # 設置位置
        area = row[9]
        # 緯度
        latitude = row[10]
        # 経度
        longitude = row[11]
        # 男性トイレ総数
        mens_toilet = row[12]
        # 男性トイレ数（小便器）
        mens_toilet_urinal = row[13]
        # 男性トイレ数（和式）
        mens_toilet_japanese_style = row[14]
        # 男性トイレ数（洋式）
        mens_toilet_western_style = row[15]
        # 女性トイレ総数
        womens_toilet = row[16]
        # 女性トイレ数（和式）
        womens_toilet_japanese_style = row[17]
        # 女性トイレ数（洋式）
        womens_toilet_western_style = row[18]
        # 男女共用トイレ総数
        unisex_toilet = row[19]
        # 男女共用トイレ数（和式）
        unisex_toilet_japanese_style = row[20]
        # 男女共用トイレ数（洋式）
        unisex_toilet_western_style = row[21]
        # 多機能トイレ数
        multifunctional_toilet = row[22]
        # 車椅子使用者用トイレ有無
        wheelchair_user_toilet = row[23]
        # 乳幼児用設備設置トイレ有無
        infants_toilet = row[24]
        # オストメイト設置トイレ有無
        ostomate_toilet = row[25]
        # 利用開始時間
        start_time = row[26]
        # 利用終了時間
        end_time = row[27]
        # 利用可能時間特記事項
        day_detail = row[28]
        # 画像
        image = row[29]
        # 画像_ライセンス
        image_licence = row[30]
        # 備考
        remark = row[31]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#施設型> .\n')
        if id or prefecture or city:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#メタデータ> ' + f'{node + str(node_num)} .\n')
            node_next_num = node_num + 1
            if id:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#発行者> ' + f'{node + str(node_next_num)} .\n'
                        + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#ID> ' + f'{node + str(node_next_num+1)} .\n'
                        + f'{node + str(node_next_num+1)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{id}" .\n')
                node_next_num += 2
            if prefecture or city:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#発行者> ' + f'{node + str(node_next_num)} .\n'
                        + f'{node + str(node_next_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#組織型> .\n'
                        + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#住所> ' + f'{node + str(node_next_num+1)} .\n')
                if prefecture:
                    w.write(f'{node + str(node_next_num+1)}' + ' <http://imi.go.jp/ns/core/2#都道府県> ' + f'"{prefecture}" .\n')
                if city:
                    w.write(f'{node + str(node_next_num+1)}' + ' <http://imi.go.jp/ns/core/2#市区町村> ' + f'"{city}" .\n')
                node_next_num += 2
            node_num = node_next_num
            

        if no:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{no}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if name or name_kana or name_eng or address or direction or latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関連施設> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#役割> ' + '"設置施設" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#施設> ' + f'{node + str(node_num+1)} .\n')
            node_next_num = node_num + 2
            if name or name_kana or name_eng:
                w.write(f'{node + str(node_num+1)}' + ' <http://imi.go.jp/ns/core/2#名称> ' + f'{node + str(node_next_num)} .\n')
                if name:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
                if name_kana:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
                if name_eng:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{name_eng}" .\n')
                node_next_num += 1
            if address or direction:
                w.write(f'{node + str(node_num+1)}' + ' <http://imi.go.jp/ns/core/2#住所> ' + f'{node + str(node_next_num)} .\n')
                if address:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
                if direction:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')
                node_next_num += 1
            if latitude or longitude:
                w.write(f'{node + str(node_num+1)}' + ' <http://imi.go.jp/ns/core/2#地理座標> ' + f'{node + str(node_next_num)} .\n')
                if latitude:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
                if longitude:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')
                node_next_num += 1
            node_num = node_next_num

        if area:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{area}" .\n')

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n')
            if start_time:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if end_time:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if day_detail:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if image:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#画像> ' + f'"{image}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')