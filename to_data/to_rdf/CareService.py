# 介護サービス事業所一覧
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
        # 介護サービス事業所名称
        name = row[4]
        # 介護サービス事業所名称_カナ
        name_kana = row[5]
        # 実施サービス
        service = [6]
        # 住所
        address = row[7]
        # 方書
        direction = row[8]
        # 緯度
        latitude = row[9]
        # 経度
        longitude = row[10]
        # 電話番号
        phone_number = row[11]
        # 内線番号
        extension_number = row[12]
        # FAX番号
        fax_number = row[13]
        # 法人番号
        corporate_number = row[14]
        # 法人の名称
        corporate_name = row[15]
        # 事業所番号
        office_number = row[16]
        # 利用可能曜日
        day = row[17]
        # 利用可能日時特記事項
        day_detail = row[18]
        # 定員
        capacity = row[19]
        # URL
        url = row[20]
        # 備考
        remark = row[21]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(
            subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#施設型> .\n')

        if id or prefecture or city:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#メタデータ> ' + f'{node + str(node_num)} .\n')
            node_next_num = node_num + 1
            if id:
                w.write(
                    f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#発行者> ' + f'{node + str(node_next_num)} .\n'
                    + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#ID> ' + f'{node + str(node_next_num + 1)} .\n'
                    + f'{node + str(node_next_num + 1)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{id}" .\n')
                node_next_num += 2

            if prefecture or city:
                w.write(
                    f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#発行者> ' + f'{node + str(node_next_num)} .\n'
                    + f'{node + str(node_next_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#組織型> .\n'
                    + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#住所> ' + f'{node + str(node_next_num + 1)} .\n')
                if prefecture:
                    w.write(
                        f'{node + str(node_next_num + 1)}' + ' <http://imi.go.jp/ns/core/2#都道府県> ' + f'"{prefecture}" .\n')
                if city:
                    w.write(
                        f'{node + str(node_next_num + 1)}' + ' <http://imi.go.jp/ns/core/2#市区町村> ' + f'"{city}" .\n')
                node_next_num += 2
                node_num = node_next_num

        if no:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{no}" .\n')
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

        if service:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別> ' + f'"{service}" \n')

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

        if phone_number or extension_number or fax_number or corporate_number or office_number or corporate_name:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + f'{node + str(node_num)} .\n')
            node_next_num = node_num + 1
            if phone_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if extension_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extension_number}" .\n')
            if fax_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#FAX番号> ' + f'"{fax_number}" .\n')
            if corporate_number:
                w.write(
                    f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#ID> ' + f'{node + str(node_next_num)} .\n'
                    + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{corporate_number}" .\n')
                node_next_num += 1
            if office_number:
                w.write(
                    f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/rdf#ID> ' + f'{node + str(node_next_num)} .\n'
                    + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{office_number}" .\n'
                    + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/rdf#体系> ' + f'{node + str(node_next_num + 1)} .\n'
                    + f'{node + str(node_next_num + 1)}' + ' <http://imi.go.jp/ns/core/2#名称> ' + '"事業所番号" .\n')
                node_next_num += 2
            if corporate_name:
                w.write(
                    f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#名称> ' + f'{node + str(node_next_num)} .\n'
                    + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{corporate_name}" .\n')
                node_next_num += 1
            node_num = node_next_num

        if day:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"週間" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#開催期日> ' + f'"{day}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if day_detail:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#利用可能時間> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#定期スケジュール型> .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{day_detail}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#収容人数> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{capacity}" .\n')
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