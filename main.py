import requests
import pandas as pd

page = 1
url = f"https://eproc.setadiran.ir/eproc/needs.do?pager=true&d-146909-p={page}"

r = requests.get(url)

if r.status_code == 200:
    print("Get Data Successfully")
    table = pd.read_html(r.text)[0]
    result = table.to_excel('test.xlsx')

else:
    print("something went wrong")
