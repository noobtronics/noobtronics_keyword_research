import pandas as pd
import yaml
from bs4 import BeautifulSoup
import shutil
from pd_helper import generate_files
from pprint import pprint

with open("config.yml", "r") as ymlfile:
    config = yaml.load(ymlfile, Loader=yaml.Loader)


# to read csv file named "samplee"
raw_data = pd.read_csv(config['keyword_file'], sep='\t', na_filter=False, skiprows=2,encoding='utf-16')

cols = raw_data.columns
concept_cols = [k for k in cols if k.startswith('Concept')]

raw_data['wordcount'] = raw_data['Keyword'].str.split().str.len()

raw_data['splitwords']= "'" + raw_data['Keyword'].str.split().str.join("','") + "'"

raw_data.sort_values(by=['wordcount'], inplace=True, ascending=False)


selected_cols = [
    'Keyword',
    'splitwords',
    'wordcount',
    'Min search volume',
    'Max search volume',
]
selected_cols.extend(concept_cols)

data_list = []
for c in selected_cols:
    data_list.append(raw_data[c])

extracted_data = pd.DataFrame(data_list).transpose()
generate_files(extracted_data, 'all', concept_cols)

exact_negative = []
for n in config['negative_exact_keywords']:
    exact_negative.append("'{0}'".format(n))

extracted_data_n = extracted_data[~extracted_data['splitwords'].str.contains('|'.join(exact_negative))]
generate_files(extracted_data_n, 'filtered', concept_cols)
