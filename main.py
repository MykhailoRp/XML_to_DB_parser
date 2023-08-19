import xml.etree.ElementTree as ET
import sqlite3
import re

connection = sqlite3.connect("projectDB.db")
db_cursor = connection.cursor()

file_name = input("File name: ")
# file_name = "test_data.xml"

tree = ET.parse(file_name)
root = tree.getroot()


def strip_url(text): return re.sub(r'\{.*?\}', '', text)


def parse_teasers(teasers):
    for t in teasers:

        sub_data = {strip_url(i.tag): i.text for i in t.iter()}

        db_cursor.execute(f'''
        INSERT INTO TEASERS (T_ID, C_ID, URL, PICTURE, TITLE, VENDOR, TEXT, ACTIVE)
        VALUES ({t.attrib['id']}, {sub_data['categoryId']}, '{sub_data['url']}', '{sub_data['picture']}', '{sub_data['title']}', '{sub_data['vendor']}', '{sub_data['text']}', {t.attrib['active']})
        ''')

def parse_categories(categories):

    for c in categories:

        db_cursor.execute(f'''
        INSERT INTO CATEGORIES (C_ID, CATEGORY)
        VALUES ({c.attrib['id']}, '{c.text}')
        ''')


parse_routes = {
    'categories': parse_categories,
    'teasers': parse_teasers,
}

for collections in root:
    cleaned_tag = strip_url(collections.tag)

    print(f"Parsing {cleaned_tag.upper()}...")

    try:
        parse_routes[cleaned_tag](collections)
    except IndexError:
        print(f"!!!Failed to find parse function for {cleaned_tag.upper()}!!!")
    else:
        print(f"Done parsing {cleaned_tag.upper()}!")


connection.commit()