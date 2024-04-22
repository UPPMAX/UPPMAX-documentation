import argparse
import logging
import os
import pdb
from natsort import natsorted
import urllib.parse
import urllib.request
import json


# get arguemnts
parser = argparse.ArgumentParser(description='Generate software pages.')
parser.add_argument('-o','--output_file', help='Path to the file that will have the software list in it.', required=True)
parser.add_argument('-i','--input-file', help='Path or URL to the JSON file containing the software list.', required=True)
args = vars(parser.parse_args())

# readability
output_file   = args['output_file']
input_file = args['input_file']

# get directory name of the output file
output_dir  = os.path.dirname(output_file)
if not output_dir:
    output_dir = './'

# check if the input file is a URL or path
input_file_parsed = urllib.parse.urlparse(input_file)
if input_file_parsed.scheme:

    # download the file
    with urllib.request.urlopen(input_file) as response:
        categories = json.loads(response.read().decode())
else:

    # load the file
    with open(input_file, 'r') as input_file:
        categories = json.load(input_file)


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






