import pandas as pd
import yaml
from bs4 import BeautifulSoup
import shutil
from pprint import pprint
from pd_helper import generate_files

keywords = pd.read_csv('keywords.csv')
related = pd.read_csv('related.csv')
preposition = pd.read_csv('preposition.csv')
question = pd.read_csv('question.csv')
comparison = pd.read_csv('comparison.csv')


def convert_to_int(table, column):
    try:
        table[column] = table[column].str.replace('$','')
        table[column] = table[column].str.replace(',','')
    except:
        pass
    table[column]  = table[column].astype('float')

convert_to_int(keywords, 'CPC')
convert_to_int(related, 'CPC')
convert_to_int(preposition, 'CPC')
convert_to_int(question, 'CPC')
convert_to_int(comparison, 'CPC')


keywords['word_count'] = keywords['Keyword'].str.split(' ').str.len()
related['word_count'] = related['Keyword'].str.split(' ').str.len()
preposition['word_count'] = preposition['Keyword'].str.split(' ').str.len()
question['word_count'] = question['Keyword'].str.split(' ').str.len()
comparison['word_count'] = comparison['Keyword'].str.split(' ').str.len()



keywords = keywords.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])
related = related.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])
preposition = preposition.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])
question = question.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])
comparison = comparison.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])


cols = keywords.columns

generate_files(keywords, 'keywords', cols)
generate_files(related, 'related', cols)
generate_files(preposition, 'preposition', cols)
generate_files(question, 'question', cols)
generate_files(comparison, 'comparison', cols)
