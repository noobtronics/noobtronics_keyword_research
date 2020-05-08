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


keywords = keywords.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])
related = related.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])
preposition = preposition.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])
question = question.sort_values(['Search Difficulty', 'CPC','Paid Difficulty',], ascending=[True, False, True])

cols = keywords.columns

generate_files(keywords, 'keywords', cols)
generate_files(related, 'related', cols)
generate_files(preposition, 'preposition', cols)
generate_files(question, 'question', cols)
