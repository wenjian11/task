from numpy import nan
import pandas as pd
import json

def cookie2dict(cookies):
    res = {}
    for pair in cookies.split(';'):
        k, v = pair.split('=', 1)
        res[k.strip()] = v.replace('"', '')

    print(res)
    return res

cookies = pd.read_excel('cookie.xlsx', usecols=[1], engine='openpyxl')
# Transfer cookies from string form to json dict.
results = {}
for i, cookie in enumerate(cookies.values):
    if str(type(cookie[0])) == '<class \'str\'>':
        cookie_dict = cookie2dict(cookie[0])
        results[i] = cookie_dict

# Save it to cookie.json
with open('cookie.json', 'w') as f:
    json.dump(results, f, sort_keys=True, indent=4)