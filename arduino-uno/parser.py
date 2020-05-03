import pandas as pd

# to read csv file named "samplee"
raw_data = pd.read_csv("arduino-uno-keywords.csv", sep='\t', na_filter=False, skiprows=2,encoding='utf-16')

cols = raw_data.columns
concept_cols = [k for k in cols if k.startswith('Concept')]


selected_cols = [
    'Keyword',
    'Min search volume',
    'Max search volume',
]
selected_cols.extend(concept_cols)

data_list = []
for c in selected_cols:
    data_list.append(raw_data[c])


extracted_data = pd.DataFrame(data_list).transpose()

print(extracted_data)
