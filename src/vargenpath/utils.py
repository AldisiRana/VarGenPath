# -*- coding: utf-8 -*-

"""Utilities for VarGenPath."""

import pandas as pd
from py2cytoscape.data.cyrest_client import CyRestClient
import py2cytoscape.util.util_dataframe as df_util
from pybiomart import Dataset


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
    interaction = ['association' for ind, row in merged_df.iterrows()]
    merged_df['interaction'] = interaction
    return merged_df


def var_genes_network(variants_genes_df):
    """Create cytoscape network from dataframe."""
    try:
        cy = CyRestClient()
        cy.network.delete_all()
        cy.session.delete()
    except Exception as e:
        raise Exception('Uh-oh! Make sure that cytoscape is open then try again.')
    data = df_util.from_dataframe(variants_genes_df, source_col='Variant name', target_col='Gene name')
    network = cy.network.create(data=data, name='VarGen network')
    return network
