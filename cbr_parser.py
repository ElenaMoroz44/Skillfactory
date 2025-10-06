# cbr_parser.py
import requests
import xml.etree.ElementTree as ET
import pandas as pd

def fetch_cbr_rates_xml(date_req=None):
    """
    Загружает XML с курсами валют с сайта Центробанка РФ.
    date_req: str в формате 'DD/MM/YYYY', например '01/01/2025'.
              Если None — берётся текущая дата.
    """
    url = "https://www.cbr.ru/scripts/XML_daily.asp"
    if date_req:
        url += f"?date_req={date_req}"
    resp = requests.get(url, timeout=10)
    resp.raise_for_status()
    return resp.content

def parse_cbr_xml(xml_bytes):
    """
    Парсит XML-данные и возвращает список словарей с валютами.
    """
    root = ET.fromstring(xml_bytes)
    date = root.attrib.get('Date')
    rows = []

    for valute in root.findall('Valute'):
        charcode = valute.findtext('CharCode')
        nominal = valute.findtext('Nominal')
        name = valute.findtext('Name')
        value_text = valute.findtext('Value')

        try:
            nominal_i = int(nominal) if nominal else 1
        except:
            nominal_i = 1
        try:
            value_f = float(value_text.replace(',', '.'))
        except:
            value_f = None

        rate_per_unit = (value_f / nominal_i) if (value_f is not None and nominal_i) else None

        rows.append({
            'Date': date,
            'CharCode': charcode,
            'Name': name,
            'Nominal': nominal_i,
            'ValueText': value_text,
            'RatePerUnit': rate_per_unit
        })
    return rows

def save_to_excel(rows, out_path='cbr_rates.xlsx'):
    """
    Сохраняет список валют в Excel.
    """
    df = pd.DataFrame(rows)
    df.to_excel(out_path, index=False)
    return df

# ---------------------------------------------------------
# Этот блок выполнится только если запустить файл напрямую
# ---------------------------------------------------------
if __name__ == "__main__":
    # Пример использования
    date_for_rates = "06/10/2025"  # можно изменить на любую дату DD/MM/YYYY
    xml_bytes = fetch_cbr_rates_xml(date_for_rates)
    rows = parse_cbr_xml(xml_bytes)
    df = save_to_excel(rows, f'cbr_rates_{date_for_rates.replace("/", "-")}.xlsx')
    print(f"Готово! Сохранено {len(df)} строк для {date_for_rates}. Файл создан.")
