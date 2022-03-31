# 観光施設一覧
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
        # 名称＿英語
        name_en = row[6]
        # POIコード
        poi_code = row[7]
        # 住所
        address = row[8]
        # 方書
        direction = row[9]
        # 緯度
        latitude = row[10]
        # 経度
        longitude = row[11]
        # 利用可能曜日
        day_of_week = row[12]
        # 開始時間
        start_time = row[13]
        # 終了時間
        end_time = row[14]
        # 利用可能日時特記事項
        day_detail = row[15]
        # 料金（基本）
        fee_basic = row[16]
        # 料金（詳細）
        fee_detail = row[17]
        # 説明
        explanation = row[18]
        # 説明_英語
        explanation_eng = row[19]
        # アクセス方法
        access = row[20]
        # 駐車場情報
        position = row[21]
        # バリアフリー情報
        barrier_free = row[22]
        # 連絡先名称
        contact_name = row[23]
        # 連絡先電話番号
        phone_number = row[24]
        # 連絡先内線番号
        contact_extension = row[25]
        # 画像
        image = row[26]
        # 画像_ライセンス
        #image_license = row[27]
        # URL
        url = row[28]
        # 備考
        remark = row[29]

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

        if name or name_kana or name_en:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + f'{node + str(node_num)} .\n')
            if name:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
            if name_kana:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
            if name_en:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{name_en}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if poi_code:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{poi_code}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

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

        if day_of_week:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"週間" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#開催期日> ' + f'"{day_of_week}" .\n')
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

        if fee_basic or fee_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#料金> ' + f'{node + str(node_num)} .\n')
            node_next_num = node_num + 1
            if fee_basic:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#金額> ' + f'{node + str(node_next_num)} .\n'
                + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#通貨> ' + '"円" .\n'
                + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{fee_basic}"^^<http://www.w3.org/2001/XMLSchema#decimal> .\n')
                node_next_num += 1
            if fee_detail:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{fee_detail}" .\n')
            node_num = node_next_num

        if explanation:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{explanation}" .\n')

        if explanation_eng:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明[英語]> ' + f'"{explanation_eng}" .\n')

        if access:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"アクセス方法" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{access}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if position:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#駐車場> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{position}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if barrier_free:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[2]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"バリアフリー情報" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{barrier_free}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if contact_name or phone_number or contact_extension:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + f'{node + str(node_num)} .\n')
            if contact_name:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{contact_name}" .\n')
            if phone_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if contact_extension:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{contact_extension}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if image:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#画像> ' + f'"{image}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')