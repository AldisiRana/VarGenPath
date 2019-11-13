# -*- coding: utf-8 -*-

"""Pipeline for VarGenPath"""
from typing import Optional

from .constants import VARIANT_LIST_PATH, LINKSET_PATH
from .utils import (
    get_cytoscape_connection, file_reader, get_associated_genes, var_genes_network, extend_vargen_network, save_session,
    save_image
)


def get_vargenpath_network(
        *,
        variant_list_path: str = VARIANT_LIST_PATH,
        network_name: Optional[str] = 'VarGenPath network',
        linkset_path: Optional[str] = LINKSET_PATH,
        session_path: Optional[str],
        image_path: Optional[str],
        extend_network: bool = True,
):
    """
    Pipeline for creating vargenpath network.

    Parameters
    ----------
    variant_list_path: the path to a list of variants.
    network_name: the name of the network.
    linkset_path: the path to the linkset to extend network.
    session_path: if input path, the cytoscape session will be saved.
    image_path: if input path, the image of the network will be saved.
    extend_network: if true, the network will be extended.

    Returns cytoscape network.
    -------

    """
    try:
        cy = get_cytoscape_connection()
    except Exception:
        raise Exception('Uh-oh! Make sure that cytoscape is open then try again.')
    variants = file_reader(variant_list_path)
    vargen_df = get_associated_genes(variants)
    network = var_genes_network(variants_genes_df=vargen_df, client=cy, network_name=network_name)
    if extend_network:
        extend_vargen_network(linkset_path)
    if session_path is not None:
        save_session(session_file=session_path, client=cy)
    if image_path is not None:
        save_image(network_image=image_path)
    return network
