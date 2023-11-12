import argparse
import collections
import logging
import os
import pdb
import re
import shutil
import sqlite3
import sys
import yaml
from datetime import datetime
from natsort import natsorted, ns

# nested dicts
def nested_dict():
    """
    Recursive construction of default dicts.
    """
    return collections.defaultdict(nested_dict)


def slugify(s):
    """
    Slugify a string to a url friendly format.
    """
    s = s.lower().strip()
    s = re.sub(r'[^\w\s-]', '', s)
    s = re.sub(r'[\s_-]+', '-', s)
    s = re.sub(r'^-+|-+$', '', s)
    return s



# get arguemnts
parser = argparse.ArgumentParser(description='Generate software pages.')
parser.add_argument('-o','--output_file', help='Path to the file that will have the software list in it.', required=True)
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

software_counter = 0
version_counter  = 0
# open file for writing
with open(output_file, 'w', encoding='utf-8') as output_file_md:

    # write page header
    output_file_md.write("""# Software
 
| Category | Name | Module | Cluster | Versions | Licence |
| -------- | ---- | ------ | ------- | -------- | ------- |""")

    for category,softwares in sorted(categories.items()):

        # write category softwares
        for software,versions in natsorted(softwares.items(), key=lambda e: e[0].lower()):

            # sort versions, but exclude -
            versions_list = natsorted([ version for version in versions.keys() if version != '-'], key=str.casefold)

            # add - back as latest version if all versions were -
            if not versions_list:
                versions_list = ['-']

            if software == 'BLAST':
                pdb.set_trace()

            # search through all versions for metadata and keep the most current non-missing one
            keywords    = None
            description = None
            website     = None
            for version,data in natsorted(versions.items(), key=lambda e: e[0].lower()):
                keywords    = data['KEYWORDS']    if data['KEYWORDS']    else keywords
                description = data['DESCRIPTION'] if data['DESCRIPTION'] else description
                website     = data['WEBSITE']     if data['WEBSITE']     else website


            # handle empty metadata
            keywords     = keywords if keywords else ''
            description  = description if description else ''
            software_str = f"[{software}]({website})" if (website and len(website)>8) else software
            license_str  = f"[{data['LICENSE']}]({data['LICENSEURL']})" if data['LICENSEURL'] else data['LICENSE']

            # write link to software page
            output_file_md.write(f"""
| {category} | {software_str} | {data['MODULE']} | {data['CLUSTER']} | {", ".join(versions_list)} | {license_str} |""")

            software_counter += 1
            version_counter  += len(versions_list)

    

print(f"Done, wrote {software_counter} softwares ({version_counter} versions) to the table in {output_file}")





