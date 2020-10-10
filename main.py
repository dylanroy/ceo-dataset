import re

import pandas as pd

def scrape_wiki_table(url, table_index=0):
    df = pd.read_html(url, header=0)[table_index]
    return re.sub(r"\[?\s*(\d+)(?=(?:, \d+)|\])(?=[^\[]*\]).", "", df.to_csv(index=False))

if __name__ == '__main__':
    with open('data.csv', 'w+') as f:
        f.write(scrape_wiki_table('https://en.wikipedia.org/wiki/List_of_chief_executive_officers'))
