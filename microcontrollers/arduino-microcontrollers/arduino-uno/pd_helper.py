import pandas as pd
import yaml


style = """

<style>
  table {
    border-collapse: collapse;
    white-space: nowrap;

  }


  table, th, td{
    border: 1px solid #c0c0c0;
    padding: 4px 10px;
    padding-right: 30px;
    font-family: Verdana;
  }
  th{
    text-align: center !important;
  }
</style>

"""


def generate_files(data, name, concept_cols):
    html_str = data.to_html()
    html_str = style + html_str

    with open('{0}_keywords.html'.format(name), 'w') as fil:
        fil.write(html_str)


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
