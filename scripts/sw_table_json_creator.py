import argparse
import collections
import os
import pdb
import sqlite3
import json

# nested dicts
def nested_dict():
    """
    Recursive construction of default dicts.
    """
    return collections.defaultdict(nested_dict)


# get arguemnts
parser = argparse.ArgumentParser(description='Generate software pages.')
parser.add_argument('-o','--output_file', help='Path to the file that will have the JSON software list in it.', required=True)
parser.add_argument('-d','--database', help='Path to the sqlite3 database containing the software list.', default='/sw/infrastructure/swdb.db')
args = vars(parser.parse_args())

# readability
output_file   = args['output_file']
database_file = args['database']

# get directory name of the output file
output_dir  = os.path.dirname(output_file)
if not output_dir:
    output_dir = './'

# connect to db
db = sqlite3.connect(database_file)
db.row_factory = sqlite3.Row
cur = db.cursor()

# query all software
cur.execute("SELECT * FROM yamlfiles")

# structure data
categories = nested_dict()
for software in cur.fetchall():

    # skip unnamed modules
    if not software['TOOL']:
        continue

    categories[software['SECTION'].capitalize() if software['SECTION'] else "Uncategorized"][software['TOOL']][software['VERSION'] if software['VERSION'] else '-'] = {
                                                                              'CLUSTER'     : software['CLUSTER'],
                                                                              'DESCRIPTION' : software['DESCRIPTION'],
                                                                              'KEYWORDS'    : software['KEYWORDS'],
                                                                              'LICENSE'     : software['LICENSE'], 
                                                                              'LICENSEURL'  : software['LICENSEURL'],
                                                                              'MODULE'      : software['MODULE'],
                                                                              'WEBSITE'     : software['WEBSITE'],
                                                                              'path'        : software['path'],
                                                                              }

#pdb.set_trace()


### reorganize softwares that don't have a SECTION defined

# create a lookup table for all softwares
soft2cat = {}
for category,softwares in categories.items():

    # skip the general category
    if category == 'Uncategorized':
        continue

    # for each software in the category
    for software,versions in softwares.items():
        soft2cat[software] = category

# move softwares from general to other categories if possible
for software,versions in categories['Uncategorized'].copy().items():

    # check if they exist in any other category
    if software in soft2cat:

        # if so, move them there
        categories[soft2cat[software]][software].update(versions)
        del categories['Uncategorized'][software]


# create output dir if needed
os.makedirs(output_dir, exist_ok=True)

# open file for writing
with open(output_file, 'w', encoding='utf-8') as output_file_json:

    # write json to file with as little whitespace as possible
    json.dump(categories, output_file_json, separators=(',',':'), sort_keys=True)

print(f"Done, wrote JSON to {output_file}")






