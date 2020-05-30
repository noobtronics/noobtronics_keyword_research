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

<script src="https://beta.noobtronics.ltd/static/js/tablefilter/tablefilter.js"></script>


"""

script = """
<script>
    var tf = new TableFilter('demo',{
        base_path: 'https://beta.noobtronics.ltd/static/js/tablefilter/',
        extensions:[{ name: 'sort' }],
        col_types: [
            'number', 'number', 'string',
            'number', 'number', 'number',
            'number'
        ],
    });

    tf.init();
</script>
"""


def generate_files(data, name, concept_cols):
    html_str = data.to_html()
    html_str = html_str.replace('<table border="1" class="dataframe">', '<table border="1" id="demo" class="dataframe">')
    html_str = style + html_str + script

    with open('{0}_keywords.html'.format(name), 'w') as fil:
        fil.write(html_str)
