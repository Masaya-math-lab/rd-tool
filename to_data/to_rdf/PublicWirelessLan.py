# 公共無線LANアクセスポイント一覧
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
        # 緯度
        latitude = row[9]
        # 経度
        longitude = row[10]
        # 設置者
        position = row[11]
        # 電話番号
        phone_number = row[12]
        # 内線番号
        extension_number = row[13]
        # SSID
        ssid = row[14]
        # 提供エリア
        area = row[15]
        # URL
        url = row[16]
        # 備考
        remark = row[17]

        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#設置型> .\n')
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

        if name or name_kana or name_eng or address or direction or latitude or longitude or phone_number or extension_number or url:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#設置地点> ' + f'{node + str(node_num)} .\n')
            node_next_num = node_num + 1
            if name or name_kana or name_eng:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#名称> ' + f'{node + str(node_next_num)} .\n')
                if name:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{name}" .\n')
                if name_kana:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#カナ表記> ' + f'"{name_kana}" .\n')
                if name_eng:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#表記[英語]> ' + f'"{name_eng}" .\n')
                node_next_num += 1
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
            if phone_number or extension_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#連絡先> ' + f'{node + str(node_next_num)} .\n')
                if phone_number:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
                if extension_number:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extension_number}" .\n')
                node_next_num += 1
            if url:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#参照> ' + f'{node + str(node_next_num)} .\n'
                        + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#参照先> ' + f'"{url}"^^<http://www.w3.org/2001/XMLSchema#anyURI> .\n')
                node_next_num += 1
            node_num = node_next_num


        if position:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#設置者> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' +' <http://imi.go.jp/ns/core/2#表記> '+ f'"{position}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if ssid:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#ID[SSID]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{ssid}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if area:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述[提供エリア]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{area}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if remark:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#備考> ' + f'"{remark}" .\n')

        w.write('\n')