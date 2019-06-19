#!/usr/bin/env python3
#
# Contributors: Ryan Habershaw, Joselynn Wallace
#
# Date started: 11 June, 2019
#
# Purpose: This code will search through the SRA database
#         and pull down the relevant metadata. Conversion
#         from xml to json will also be performed to
#         appropriately represent retrieved data.
#
######################################################

###Required modules###
import json
from Bio import Entrez
import pandas as pd
import ast
from collections import OrderedDict
from xml.etree.ElementTree import fromstring
from xmljson import Abdera  # import the class
######################

ab = Abdera(dict_type=OrderedDict)  # pick dict class


def sra_query(email, samplemeta_id):
    """
    This function will establish the Entrez email and actually retrieve the data from the
    SRA database.

    :param email: The user's email
    :param samplemeta_id: The specified SRA_SRX id
    :return: The xml data to be converted

    """

    Entrez.email = email  # Tells 'Entrez' who the user is
    srs = samplemeta_id.split("_")[0]
    srx = samplemeta_id.split("_")[1]
    sra_handle = Entrez.esearch(db='sra', term=srs)  # Searches sra database using the provided ID
    sra_results = Entrez.read(sra_handle)  # Reads in the results of 'esearch' above
    sra_id = sra_results['IdList'][0]
    # Using this ^ for 'efetch' id parameter because just using the id throws a bad HTTP request
    sra_fetch = Entrez.efetch(db='sra', id=sra_id, rettype='text', retmode='xml')
    sra_query.sra_table = sra_fetch.read()

    sra_handle.close()
    sra_fetch.close()

    return sra_query.sra_table


sra_query('ryan_habershaw@brown.edu', 'SRS643408_SRX612442')

# sra_dump = json.dumps(ab.data(fromstring(sra_query.sra_table)))


def table_builder():

    val = ast.literal_eval(sra_query.sra_table)
    val1 = json.loads(json.dumps(val))
    val2 = val1['age'][0]['hometown'][0]['gender']
    print(pd.DataFrame(val2, columns=['Sample_ID', 'PH', 'PH']))
