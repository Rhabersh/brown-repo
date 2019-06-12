#!/usr/bin/env python
#
#Author: Ryan Habershaw
#
#Date: 11 June, 2019
#
#Purpose: This code will search through the SRA database
#         and pull down the relevant metadata.
#
######################################################

import Bio

from Bio import Entrez

from astropy.table import Table, Column

import numpy as np

Entrez.email = "ryan_habershaw@brown.edu"
#Lets Entrez know who is using it

sra_handle = Entrez.esearch(db = "sra", term = "SRS643408", retmax = "10000")
#Searches the specified database for primary UIDs to be used by 'efetch'

#sra_post = Entrez.epost(db = "sra", id = "SRS643408")

sra_results = Entrez.read(sra_handle)
#Reads in the results of 'esearch' above

sra_id = sra_results["IdList"][0]
#Stores the required ID in a variable to be used by 'efetch'

sra_fetch = Entrez.efetch(db = "sra", id = sra_id, rettype="text", retmode="xml")
#Retrieves the records (specified by the id)

sra_table = sra_fetch.read()

#print(sra_fetch.readline().strip())
#print(sra_table)


#Everything contained in this box is for final output

table = Table()
table['Sample ID'] = [0]
table['Library Read Type'] = Column([2.0])
table['Experiment ID'] = ['x']
table['Run Date'] = [1]
table['Updated Date'] = [1]
table['Spots'] = [1]
table['Bases'] = [1]
table['Run Center'] = [1]
table['Experiment Name'] = [1]
table['Library Name'] = [1]
table['Library Strategy'] = [1]
table['Library Source'] = [1]
table['Library Selection'] = [1]
table['Platform'] = [1]
table['Instrument Model'] = [1]
table['Instrument Name'] = [1]
table['Taxon ID'] = [1]
table['Common Name'] = [1]
table['Study Type'] = [1]
table['Center Proj. Name'] = [1]
table['Submission Center'] = [1]
table['Submission Lab'] = [1]
table['JSON'] = [1]

print(table)

#####################################################

sra_handle.close()
sra_fetch.close()
#Close both of the previously opened handles from 'esearch' and 'efetch'

