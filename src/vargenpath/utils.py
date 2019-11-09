# -*- coding: utf-8 -*-

"""Utilities for VarGenPath."""

import pandas as pd
from py2cytoscape.data.cyrest_client import CyRestClient
from pybiomart import Dataset
from urllib3.exceptions import NewConnectionError


def file_reader(path: str) -> list:
    """
	Read text file.
	:param path: text file containing the variants
	:return: list of variants
	"""
    file = open(path, "r")
    content = [line.strip() for line in file.readlines()]
    return content


def get_associated_genes(variants_list: list):
    """
	Get variant gene information from BioMart.
	:param variants_list: the list with variant ids.
	:return: dataframe with variant and gene information.
	"""
    snp_dataset = Dataset(name='hsapiens_snp', host='http://www.ensembl.org')
    variant_gene_df = snp_dataset.query(attributes=['refsnp_id', 'ensembl_gene_stable_id'],
                                        filters={'snp_filter': variants_list})
    gene_dataset = Dataset(name='hsapiens_gene_ensembl', host='http://www.ensembl.org')
    gene_df = gene_dataset.query(attributes=['ensembl_gene_id', 'external_gene_name'], only_unique=False,
                                 filters={'link_ensembl_gene_id': list(variant_gene_df['Gene stable ID'])})
    merged_df = pd.merge(variant_gene_df, gene_df, on='Gene stable ID')
    return merged_df


def snps_genes_network(variants_genes_dict):
    pass
