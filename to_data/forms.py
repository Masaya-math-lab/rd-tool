from django import forms

CATEGORIES = (
    ('0', 'AED設置箇所一覧'),
    ('1', '介護サービス事業所一覧'),
    ('2', '医療機器一覧'),
    ('3', '文化財一覧'),
    ('4', '観光施設一覧'),
    ('5', 'イベント一覧'),
    ('6', '公共無線LANアクセスポイント一覧'),
    ('7', '公衆トイレ一覧'),
    ('8', '消防水利施設一覧'),
    ('9', '指定緊急避難場所一覧'),
    ('10', '地域・年齢別人口'),
    ('11', '公共施設一覧'),
    ('12', '子育て施設一覧'),
)

class GetData(forms.Form):
    data = forms.FileField(required=True, widget=forms.widgets.FileInput)
    category = forms.ChoiceField(required=True, widget=forms.RadioSelect, choices=CATEGORIES, initial='0')