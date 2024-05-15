# NCBI taxonomy databases

Uppmax maintains local copies of the full set of NCBI Taxonomy databases. Note that:

- The local copies are found at /sw/data/ncbi_taxonomy/latest
- The data module ncbi_taxonomy/latest defines the environment variable NCBI_TAXONOMY_ROOT to this location. We recommend loading this module and using this environment variable to access these data.
- This also contains the subdirectories new_taxdump, accession2taxid and biocollections containing those databases, see the tables below for their contents
- latest is a symbolic link to a directory named from the date of the most recent update
- There is also a subdirectory download containing the files as downloaded from NCBI
- The installation of new versions begins Sunday of each week at 00.10. The update may take several minutes up to an hour, depending on network speeds.
- When new versions are successfully installed, the latest/ symbolic link is updated to point to the new dated directory
- The previous version of the taxonomy databases are removed when the new versions have completed installation

See the links for each database for specifics on file format and contents. Many tools know how to make use of these databases; follow each tool's specific instructions. The files can be found in the indicated directories.

The databases available within /sw/data/ncbi_taxonomy/latest are below. For more on each, see the links.

Name               | Source  | Notes
-------------------|---------|---------------------
taxdump            | NCBI    | NCBI taxonomic database, in multiple .dmp files (see taxdump_readme.txt or link)
taxcat             | NCBI    | NCBI taxonomic categories, in categories.dmp (see taxcat_readme.txt or link)
taxdump_readme.txt | NCBI    | NCBI taxdump file description
taxcat_readme.txt  | NCBI    | NCBI taxcat file description
gi_taxid_nucl.dmp  | NCBI    | Mappings of nucleotide GI to taxid (DEPRECATED)
gi_taxid_prot.dmp  | NCBI    | Mappings of protein GI to taxid (DEPRECATED)

The databases available within /sw/data/ncbi_taxonomy/latest/new_taxdump are below. For more on each, see the links.

Name                | Source  | Notes
--------------------|---------|--------------------------------------------------
new_taxdump         | NCBI    | NCBI new-format taxonomic database, in multiple .dmp files (see this taxdump_readme.txt or link)
taxdump_readme.txt  | NCBI    | NCBI new-format taxonomic database file description

The databases available within /sw/data/ncbi_taxonomy/latest/accession2taxid are below. The dead_ files contain accession-to-TaxID mappings for dead (suppressed or withdrawn) sequence records. For more on each, see the links.

Name                      | Source  | Notes
--------------------------|---------|----------------
nucl_wgs.accession2taxid  | NCBI    | TaxID mapping for nucleotide records of type WGS or TSA
nucl_gb.accession2taxid   | NCBI    | TaxID mapping for nucleotide records not of the above types
prot.accession2taxid      | NCBI    | TaxID mapping for protein records
pdb.accession2taxid       | NCBI    | TaxID mapping for PDB protein records
dead_nucl.accession2taxid | NCBI    | TaxID mapping for dead nucleotide records
dead_prot.accession2taxid | NCBI    | TaxID mapping for dead protein records
dead_wgs.accession2taxid  | NCBI    | TaxID mapping for dead WGS or TSA records

The biocollections databases contain collections location information. coll_dump.txt is located within the /sw/data/ncbi_taxonomy/latest directory. Those marked biocollections are located within the /sw/data/ncbi_taxonomy/latest/biocollections directory.

Name                          | Source  | Notes
------------------------------|---------|------
coll_dump.txt                 | NCBI    | .
Collection_codes.txt          | NCBI    | biocollections
Institution_codes.txt         | NCBI    | biocollections
Unique_institution_codes.txt  | NCBI    | biocollections
