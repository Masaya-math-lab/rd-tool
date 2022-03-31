# 子育て施設一覧
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
        No = row[1]
        # 都道府県名
        prefecture = row[2]
        # 市区町村名
        city = row[3]
        # 名称
        name = row[4]
        # 名称_カナ
        name_kana = row[5]
        # 種別
        kinds = row[6]
        # 住所
        address = row[7]
        # 方書
        direction = row[8]
        # 緯度
        latitude = row[9]
        # 経度
        longitude = row[10]
        # アクセス方法
        access = row[11]
        # 駐車場情報
        parking = row[12]
        # 電話番号
        phone_number = row[13]
        # 内線番号
        extention_number = row[14]
        # FAX番号
        fax_number = row[15]
        # 法人番号
        corporate_number = row[16]
        # 団体名
        group_name = row[17]
        # 許可等年月日
        permission = row[18]
        # 収容定員
        capacity = row[19]
        # 受入年齢
        age = row[20]
        # 利用可能曜日
        day = row[21]
        # 開始時間
        start_time = row[22]
        # 終了時間
        end_time = row[23]
        # 利用可能日時特記事項
        day_detail = row[24]
        # 一時預かりの有無
        custody = row[25]
        # URL
        url = row[26]
        # 備考
        remark = row[27]

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

        if No:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{No}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if name or name_kana:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + f'{node + str(node_num)} .\n')
            if name:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
            if name_kana:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if kinds:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別> ' + f'"{kinds}" .\n')

        if address or direction:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#住所> ' + f'{node + str(node_num)} .\n')
            if address:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
            if direction:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#地理座標> ' + f'{node + str(node_num)} .\n')
            if latitude:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
            if longitude:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if access:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"アクセス方法" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{access}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if parking:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#駐車場> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{parking}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if phone_number or extention_number or fax_number or corporate_number or group_name:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + f'{node + str(node_num)} .\n')
            node_next_num = node_num + 1
            if phone_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if extention_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extention_number}" .\n')
            if fax_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#FAX番号> ' + f'"{fax_number}" .\n')
            if corporate_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#ID> ' + f'{node + str(node_next_num)} .\n'
                        + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{corporate_number}" .\n')
                node_next_num += 1
            if group_name:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#組織> ' + f'{node + str(node_next_num)} .\n'
                        + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#名称> ' + f'{node + str(node_next_num+1)} .\n'
                        + f'{node + str(node_next_num+1)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{group_name}" .\n')
                node_next_num += 2
            node_num = node_next_num

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#収容人数> ' + f'"{capacity}" .\n')

        if day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"週間" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#開催期日> ' + f'"{day}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

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

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')