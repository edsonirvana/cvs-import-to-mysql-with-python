import pymysql #import pymysql librarie
from config import config #import config librarie
import csv #import csv librarie

cnx = pymysql.connect(**config, charset='utf8') #Connection
cursor = cnx.cursor() #Execute the queries

imput_file = csv.DictReader(open("file.csv", encoding='utf-8')) #read .CSV and set enconding

for row in imput_file:
    cursor.execute("""INSERT INTO database.Table (field_01, field_02, field_03, field_04, field_05) \
                    VALUES (%s, %s, %s, %s, %s)""",(row['field_01'],row['field_02'],row['field_03'],row['field_04'], row['field_05']))
    cnx.commit()