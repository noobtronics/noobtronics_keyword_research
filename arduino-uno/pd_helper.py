import pandas as pd
import yaml

def generate_files(data, name, concept_cols):
    data.to_html('{0}_keywords.html'.format(name))


    concept_info = {}

    for c in concept_cols:
        uniq_raw = data[c].unique()
        unique_word = set()
        for k in uniq_raw:
            for x in k.split(','):
                p = x.strip()
                if len(p)> 0:
                    unique_word.add(p)
        concept_info[c] = sorted(list(unique_word))


    with open('{0}_concept.yml'.format(name), 'w') as fil:
        fil.write(yaml.dump(concept_info))
