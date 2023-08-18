import sys
import yaml
import pdb
import logging
import argparse
import os
import jinja2
import shutil
import sqlite3
from datetime import datetime
import collections
from natsort import natsorted, ns
import shutil
import re

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

# get output dir
try:
    output_file = sys.argv[1]
except:
    sys.exit(f"""Usage:

python3 {sys.argv[0]} <path to output file> [-d]
ex.
python3 {sys.argv[0]} /path/to/uppmaxdocs/software/overview.md
python3 {sys.argv[0]} /path/to/uppmaxdocs/software/overview.md -d

-d will recursivly delete the folder the specified output file is in
(/path/to/uppmaxdocs/software/ in the example above).
""")

# get directory name of the output file
output_dir  = os.path.dirname(output_file)

# get delete flag if any
try:
    delete_flag = sys.argv[2]
except:
    delete_flag = False

# connect to db
db = sqlite3.connect("/sw/infrastructure/swdb.db")
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
                                                                              'CLUSTER': software['CLUSTER'],
                                                                              'DESCRIPTION' : software['DESCRIPTION'],
                                                                              'KEYWORDS' : software['KEYWORDS'],
                                                                              'LICENSE': software['LICENSE'], 
                                                                              'LICENSEURL': software['LICENSEURL'],
                                                                              'WEBSITE' : software['WEBSITE'],
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





### DANGER ZOME ###
# delete all files in the output dir if requested with -d
if delete_flag == '-d':
    shutil.rmtree(output_dir)    



# create output dir if needed
os.makedirs(output_dir, exist_ok=True)

# open file for writing
with open(output_file, 'w') as output_file_md:

    # write page header
    output_file_md.write("# Software")

    for category,softwares in sorted(categories.items()):

        # write category header
        output_file_md.write(f"""
 
## {category}
 
| Name | Latest version | Keywords |
| ---- | -------------- | -------- |""")

        # write category softwares
        for software,versions in natsorted(softwares.items(), key=lambda e: e[0].lower()):

            # sort versions, but exclude -
            latest_version = natsorted([ version for version in versions.keys() if version != '-'], key=str.casefold)

            # add - back as latest version if all versions were -
            if not latest_version:
                latest_version = ['-']
            latest_version = latest_version[-1]

#            if software == 'bwa-meth':
#                pdb.set_trace()

            # search through all versions for metadata and keep the most current non-missing one
            keywords    = None
            description = None
            website     = None
            for version,data in natsorted(versions.items(), key=lambda e: e[0].lower()):
                keywords    = data['KEYWORDS']    if data['KEYWORDS']    else keywords
                description = data['DESCRIPTION'] if data['DESCRIPTION'] else description
                website     = data['WEBSITE']     if data['WEBSITE']     else website


            # handle empty metadata
            keywords    = keywords if keywords else ''
            description = description if description else ''
            website     = f"**Website:** <{website}>" if website else ''

            # write link to software page
            output_file_md.write(f"""
| [{software}]({slugify(category)}/{slugify(software)}.md) | {latest_version} | {keywords} |""")
    
            # create software page
            os.makedirs(f"{output_dir}/{slugify(category)}", exist_ok=True)
            with open(f"{output_dir}/{slugify(category)}/{slugify(software)}.md", 'w') as software_file_md:

                # format keywords
                if keywords:
                    keywords = f"**Keywords:** {keywords}"

                # write software page header
                software_file_md.write(f"""# {category} - {software}

{description}

{keywords}

{website}

| Version | Clusters | License |
| ------- | -------- | ------- |
""")
                # print info about each version
                for version,data in natsorted(versions.items(), key=lambda e: e[0].lower()):

#                    # website url
#                    version_str = version
#                    if data['WEBSITE']:
#                        version_str = f"[{version_str}]({data['WEBSITE']})"

                    # license url
                    license_str = data['LICENSE']
                    if data['LICENSEURL']:
                        license_str = f"[{license_str}]({data['LICENSEURL']})"


                    software_file_md.write(f"""| {version} | {data['CLUSTER']} | {license_str} |
""")











