# -*- coding: utf-8 -*-

"""Utilities for VarGenPath."""

import pandas as pd
from click import File
from py2cytoscape.cyrest.base import api
from py2cytoscape.data.cynetwork import CyNetwork
from py2cytoscape.data.cyrest_client import CyRestClient
import py2cytoscape.util.util_dataframe as df_util
from pybiomart import Dataset


def get_cytoscape_connection() -> CyRestClient:
    """Connect to cytoscape."""
    cy = CyRestClient()
    cy.network.delete_all()
    cy.session.delete()
    return cy


def file_reader(file: File) -> list:
    """
    Read text file.

    :param file: text file containing the variants.
    :return: a list of variants.
    """
    return [line.strip() for line in file.readlines()]


def get_associated_genes(variants_list: list) -> pd.DataFrame:
    """
    Get variant gene information from BioMart.

    :param variants_list: the list with variant ids.
    :return: dataframe with variant and gene information
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
        client) -> CyNetwork:
    """
    Create cytoscape network from dataframe.

    :param variants_genes_df: dataframe containing the vaiants, genes and their interaction
    :param network_name: the name of the network.
    :param client: the cystocape client.
    :return: cytoscape network
    """
    data = df_util.from_dataframe(variants_genes_df, source_col='Variant name', target_col='Gene name')
    network = client.network.create(data=data, name=network_name)
    return network


def extend_vargen_network(linkset_path: str):
    """
    Extend network with linkset.

    :param linkset_path:  the path to the linkset used to extended the network.
    :return:
    """
    return api(namespace="cytargetlinker", command="extend", PARAMS={'linkSetFiles': linkset_path})


def save_session(
        *,
        session_file: str,
        client: CyRestClient,
) -> str:
    """
    Save cystoscape session.

    :param session_file: path to save the session.
    :param client: cystoscape client.
    :return:
    """
    client.session.save(session_file)
    return 'Session has been saved in ' + session_file


def save_image(
        *,
        network_image: str,
        image_type: str = 'SVG (*.svg)',
) -> str:
    """
    Save network image.

    :param network_image: path to save the network image.
    :param image_type: type of image to be saved.
    :return:
    """
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
