# イベント一覧
import random
import string

def to_rdf(w, df):
    # 空白ノードの生成
    dat = string.digits + string.ascii_lowercase
    node = '_:node' + ''.join([random.choice(dat) for i in range(9)]) + 'x'
    node_num = 1
    df = df.replace('新潟', '石川')
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
        # イベント名
        name = row[4]
        # イベント名_カナ
        name_kana = row[5]
        # イベント名_英語
        name_eng = row[6]
        # 開始日
        start_day = row[7]
        # 終了日
        end_day = row[8]
        # 開始時間
        start_time = row[9]
        # 終了時間
        end_time = row[10]
        # 開始日時特記事項
        day_detail = row[11]
        # 説明
        explanation = row[12]
        # 料金（基本）
        fee_basic = row[13]
        # 料金（詳細）
        fee_detail = row[14]
        # 連絡先名称
        contact_name = repr(row[15])
        # 連絡先電話番号
        phone_number = row[16]
        # 連絡先内線番号
        contact_extension = row[17]
        # 主催者
        corporate_name = row[18]
        # 場所名称
        area = row[19]
        # 住所
        address = row[20]
        # 方書
        direction = row[21]
        # 緯度
        latitude = row[22]
        # 経度
        longitude = row[23]
        # アクセス方法
        access = row[24]
        # 駐車場情報
        position = row[25]
        # 定員
        capacity = row[26]
        # 参加申込終了日
        application_end_day = row[27]
        # 参加申込終了時間
        application_end_time = row[28]
        # 参加申込方法
        how_to_apply = row[29]
        # URL
        url = row[30]
        # 備考
        remark = row[31]
        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベント型> .\n')
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

        if name or name_kana or name_eng:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#名称> ' + f'{node + str(node_num)} .\n')
            if name:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
            if name_kana:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
            if name_eng:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{name_eng}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if start_day or end_day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[1]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"開催" .\n')
            node_next_num = node_num + 1
            if start_day:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#開始日> ' + f'{node + str(node_next_num)} .\n'
                        + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#標準型日付> ' + f'"{start_day}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
                node_next_num += 1
            if end_day:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#終了日> ' + f'{node + str(node_next_num)} .\n'
                        + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#標準型日付> ' + f'"{end_day}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
                node_next_num += 1
            node_num = node_next_num

        if start_time or end_time or day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[1]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n')
            if start_time:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#開始時間> ' + f'"{start_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if end_time:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{end_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            if day_detail:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num
    
        if explanation:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{explanation}" .\n')

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

        if corporate_name:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関連組織> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#役割> ' + '"主催者" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#組織> ' + f'{node + str(node_num+1)} .\n'
                    + f'{node + str(node_num+1)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{corporate_name}" .\n')
            node_next_num = node_num + 2
            node_num = node_next_num

        if area or address or direction or latitude or longitude:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#開催場所> ' + f'{node + str(node_num)} .\n')
            node_next_num = node_num + 1
            if area:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{area}" .\n')
            if address or direction:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#住所> ' + f'{node + str(node_next_num)} .\n')
                if address:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
                if direction:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')
                node_next_num += 1
            if latitude or longitude:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#地理座標> ' + f'{node + str(node_next_num)} .\n')
                if latitude:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
                if longitude:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')
                node_next_num += 1
            node_num = node_next_num

        if access:
            w.writelines(subject + ' <http://imi.go.jp/ns/core/2#記述[1]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"アクセス方法" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{access}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if position:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[2]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"駐車場情報" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{position}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#人数> ' + f'"{capacity}"^^<http://www.w3.org/2001/XMLSchema#decimal> .\n')

        if application_end_day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[2]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"参加申込" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#終了日> ' + f'"{application_end_day}"^^<http://www.w3.org/2001/XMLSchema#date> .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if application_end_time:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#期間[2]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#イベントスケジュール型> .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#終了時間> ' + f'"{application_end_time}"^^<http://www.w3.org/2001/XMLSchema#time> .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if how_to_apply:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参加方法> ' + f'"{how_to_apply}" .\n')

        if url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#参照> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[3]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"備考" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{remark}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        w.write('\n')