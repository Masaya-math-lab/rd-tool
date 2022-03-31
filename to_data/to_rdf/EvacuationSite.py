# 指定緊急避難場所一覧
import random
import string

def to_rdf(w, df):
    # 空白ノードの生成
    dat = string.digits + string.ascii_lowercase
    node = '_:node' + ''.join([random.choice(dat) for i in range(9)]) + 'x'
    node_num = 1
    for i in range(len(df)):
        row = df.iloc[i]
        # NO
        No = row[0]
        # 名称
        name = row[1]
        # 名称_カナ
        name_kana = row[2]
        # 住所
        address = row[3]
        # 方書
        direction = row[4]
        # 緯度
        latitude = row[5]
        # 経度
        longitude = row[6]
        # 標高
        elevation = row[7]
        # 電話番号
        phone_number = row[8]
        # 内線番号
        extension_number = row[9]
        # 市区町村コード
        id = row[10]
        # 都道府県名
        prefecture = row[11]
        # 市区町村名
        city = row[12]
        # 災害種別_洪水
        kinds1 = row[13]
        # 災害種別_崖崩れ、土石流及び地滑り
        kinds2 = row[14]
        # 災害種別_高潮
        kinds3 = row[15]
        # 災害種別_地震
        kinds4 = row[16]
        # 災害種別_津波
        kinds5 = row[17]
        # 災害種別_大規模な火事
        kinds6 = row[18]
        # 災害種別_内水氾濫
        kinds7 = row[19]
        # 災害種別_火山現象
        kinds8 = row[20]
        # 指定避難所との重複
        duplication = row[21]
        # 想定収容人数
        capacity = row[22]
        # 対象となる町会・自治会
        area = row[23]
        # URL
        url = row[24]
        # 備考
        remark = row[25]


        # 空白ノード作成
        subject = "<?s" + str(i) + ">"

        # 書き込み
        w.write(subject + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#施設型> .\n')
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

        if address or direction:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#住所> ' + f'{node + str(node_num)} .\n')
            if address:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{address}" .\n')
            if direction:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#方書> ' + f'"{direction}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if latitude or longitude or elevation:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#地理座標> ' + f'{node + str(node_num)} .\n')
            node_next_num = node_num + 1
            if latitude:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#緯度> ' + f'"{latitude}" .\n')
            if longitude:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#経度> ' + f'"{longitude}" .\n')
            if elevation:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#測地高度> ' + f'{node + str(node_next_num)} .\n'
                        + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#数値> ' + f'"{elevation}"^^<http://www.w3.org/2001/XMLSchema#decimal> .\n')
                node_next_num += 1
            node_num = node_next_num

        if phone_number or extension_number:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#連絡先> ' + f'{node + str(node_num)} .\n')
            if phone_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#電話番号> ' + f'"{phone_number}" .\n')
            if extension_number:
                w.write(f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#内線番号> ' + f'"{extension_number}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if id or prefecture or city:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関与> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#役割> ' + '"設置主体" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#関与者> ' + f'{node + str(node_num+1)} .\n'
                    + f'{node + str(node_num+1)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#組織型> .\n')
            node_next_num = node_num + 2
            if id:
                w.write(f'{node + str(node_num+1)}' + ' <http://imi.go.jp/ns/core/2#ID> ' + f'{node + str(node_next_num)} .\n'
                    + f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{id}" .\n')
                node_next_num += 1
            if prefecture or city:
                w.write(f'{node + str(node_num+1)}' + ' <http://imi.go.jp/ns/core/2#住所> ' + f'{node + str(node_next_num)} .\n')
                if prefecture:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#都道府県> ' + f'"{prefecture}" .\n')
                if city:
                    w.write(f'{node + str(node_next_num)}' + ' <http://imi.go.jp/ns/core/2#市区町村> ' + f'"{city}" .\n')
                node_next_num += 1
            node_num = node_next_num

        if area:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#関与> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#役割> ' + '"対象となる町会・自治会" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#関与者> ' + f'{node + str(node_num+1)} .\n'
                    + f'{node + str(node_num+1)}' + ' <http://www.w3.org/1999/02/22-rdf-syntax-ns#type> ' + '<http://imi.go.jp/ns/core/2#組織型> .\n'
                    + f'{node + str(node_num+1)}' + ' <http://imi.go.jp/ns/core/2#名称> ' + f'{node + str(node_num+2)} .\n'
                    + f'{node + str(node_num+2)}' + ' <http://imi.go.jp/ns/core/2#表記> ' + f'"{area}" .\n')
            node_next_num = node_num + 3
            node_num = node_next_num

        if kinds1:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_洪水]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds1}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if kinds2:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_崖崩れ、土石流及び地滑り]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds2}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if kinds3:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_高潮]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds3}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if kinds4:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_地震]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds4}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if kinds5:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_津波]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds5}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if kinds6:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_大規模な火事]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds6}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if kinds7:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_内水氾濫]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds7}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if kinds8:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[災害種別_火山現象]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{kinds8}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if duplication:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#種別コード[指定避難所との重複]> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#識別値> ' + f'"{duplication}" .\n')
            node_next_num = node_num + 1
            node_num = node_next_num

        if capacity:
            w.write(subject + ' <http://imi.go.jp/ns/core/2#記述> ' + f'{node + str(node_num)} .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#種別> ' + '"想定収容人数" .\n'
                    + f'{node + str(node_num)}' + ' <http://imi.go.jp/ns/core/2#説明> ' + f'"{capacity}" .\n')
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