# -*- coding: utf-8 -*-

"""Pipeline for VarGenPath"""
from typing import Optional

from .constants import VARIANT_LIST_PATH
from .utils import get_cytoscape_connection, file_reader, get_associated_genes, var_genes_network, \
    extend_vargen_network, save_session, save_image


def get_vargenpath_network(
        *,
        variant_list_path: str = VARIANT_LIST_PATH,
        network_name: Optional[str] = 'VarGenPath network',
        linkset_path: Optional[str],
        session_path: Optional[str],
        image_path: Optional[str]
):
    try:
        cy = get_cytoscape_connection()
    except Exception:
        raise Exception('Uh-oh! Make sure that cytoscape is open then try again.')
    variants = file_reader(variant_list_path)
    vargen_df = get_associated_genes(variants)
    network = var_genes_network(variants_genes_df=vargen_df, client=cy, network_name=network_name)
    if linkset_path is not None:
        extend_vargen_network(linkset_path)
    if session_path is not None:
        save_session(session_file=session_path, client=cy)
    if image_path is not None:
        save_image(network_image=image_path)
    return network
