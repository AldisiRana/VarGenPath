# -*- coding: utf-8 -*-

"""Utilities for VarGenPath."""

import pandas as pd
import py2cytoscape.util.util_dataframe as df_util
from py2cytoscape.data.cyrest_client import CyRestClient
from py2cytoscape.cyrest.base import api
from pybiomart import Dataset

from .constants import IMAGE_PATH, LINKSET_PATH, SESSION_PATH

def get_cytoscape_connection():
	cy = CyRestClient()
	cy.network.delete_all()
	cy.session.delete()
	return cy


def file_reader(path: str) -> list:
    """
	Read text file.
	:param path: text file containing the variants
	:return: list of variants
	"""
    file = open(path, "r")
    content = [line.strip() for line in file.readlines()]
    return content


def get_associated_genes(variants_list: list) -> pd.DataFrame:
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


def var_genes_network(
        *,
        variants_genes_df: pd.DataFrame,
        network_name: str = 'VarGenPath network',
        client):
    """Create cytoscape network from dataframe."""
    data = df_util.from_dataframe(variants_genes_df, source_col='Variant name', target_col='Gene name')
    network = client.network.create(data=data, name=network_name)
    return network


def extend_vargen_network(linkset_path: str = LINKSET_PATH):
    """Extend network with linkset."""
    return api(namespace="cytargetlinker", command="extend", PARAMS={'linkSetFiles': linkset_path})


def save_session(
        *,
        session_file: str = SESSION_PATH,
        client: CyRestClient,
):
    client.session.save(session_file)
    return 'Session has been saved in ' + session_file


def save_image(
        *,
        network_image: str = IMAGE_PATH,
        image_type: str = 'SVG (*.svg)',
):
    api(
        namespace="layout",
        command="apply preferred",
    )
    api(
        namespace="view",
        command="export",
        PARAMS={'outputFile': network_image, "view": 'current', 'options': image_type}
    )
    return 'Image has been saved in ' + network_image + 'using ' + image_type + 'format.'


def save_network():
    pass
