import pymysql
import csv
import os

# read database configuration from file
with open('config.txt') as f:
    config = dict(line.strip().split('=') for line in f)

# set directory of CSV file
directory = './'

# loop through CSV files in directory
for filename in os.listdir(directory):
    if filename.endswith('.csv'):
        filepath = os.path.join(directory, filename)
        
        # set table name based on filename
        tablename = os.path.splitext(filename)[0].replace('.', '_')
        
        # read CSV file and get column names
        with open(filepath, encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            columns = reader.fieldnames
            
            # generate insert statement with dynamic column names
            insert_statement = f"INSERT INTO {config['database']}.{tablename} ({', '.join(columns)}) VALUES "
            
            # generate value placeholders for each row
            value_placeholders = []
            for row in reader:
                value_placeholders.append(f"({', '.join(['%s']*len(columns))})")
            
            # join all value placeholders
            insert_statement += ', '.join(value_placeholders)
            
            # connect to database and execute insert statement
            cnx = pymysql.connect(**config, charset='utf8')
            cursor = cnx.cursor()
            cursor.execute(insert_statement, [row[column] for row in reader for column in columns])
            cnx.commit()