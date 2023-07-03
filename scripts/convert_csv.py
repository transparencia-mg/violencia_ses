import os
import sys
import pandas as pd
import re
from unidecode import unidecode

def convert_csv():
  upload_files = os.listdir('upload')
  for file in upload_files:
    read_file = pd.read_excel (f'upload/{file}')
    columns = read_file.columns
    new_columns = []
    for column in columns:
      new_columns.append(snake_small_case(column))
    csv_name = file.split('.xlsx')[0]
    read_file.columns=new_columns

    # Remove white spaces from the beginning and the end of all columns
    for column in new_columns:
        if read_file[column].dtype == object and isinstance(read_file.iloc[0][column], str):
            read_file[column] = [read_file[column][i].strip() for i in range(0, len(read_file))]

    read_file.to_csv (f'dataset/data/{csv_name}.csv', index = None, header=True, sep = ';', decimal = ',', encoding = 'utf-8-sig', na_rep = "")

def snake_small_case(column):
  column_lower = column.lower()
  column_unidecode = unidecode(column_lower)
  column_alphanumeric = re.sub('[^A-Za-z0-9]+', ' ', column_unidecode)
  column_split = column_alphanumeric.split(' ')
  column_empty = [x for x in column_split if x != '']
  column = '_'.join(column_empty)
  return column

if __name__ == '__main__':
  convert_csv()
