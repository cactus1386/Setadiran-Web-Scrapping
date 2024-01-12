import requests
import pandas as pd
from bs4 import BeautifulSoup

page = 1
url = f"https://eproc.setadiran.ir/eproc/needs.do?pager=true&d-146909-p={page}"

all_rows_data = []

for i in range(0, 30):
    page += 1
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    table = soup.find("table", {"id": "aList"})

    rows_data = []
    for row in table.find("tbody").find_all("tr"):
        span_title = row.find("span", {"title": lambda t: t and "گاز" in t})
        if span_title:
            link = row.find("a", {"class": "hyperlink"})["href"]

            row_data = [
                cell.get_text(strip=True) for cell in row.find_all(["td", "th"])
            ]

            row_data.append(link)

            rows_data.append(row_data)

    all_rows_data.extend(rows_data)

columns = [
    "ردیف",
    "شماره نیاز",
    "شرح کلي نياز",
    "نام دستگاه خريدار",
    "استان محل تحویل",
    "نوع نياز",
    "طبقه بندی موضوعی",
    "گروه کالا ",
    "گروه خدمت",
    "تاريخ اعلام نیاز",
    "مهلت ارسال پاسخ",
    "لینک"
]

df = pd.DataFrame(all_rows_data, columns=columns)

df.to_excel("output.xlsx", index=False)
