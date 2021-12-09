import pandas as pd
from django.http import HttpResponse

def to_csv(df, file_name):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="{}"'.format(file_name)
    df.to_csv(path_or_buf=response, encoding='utf-8-sig', index=False)
    return response
