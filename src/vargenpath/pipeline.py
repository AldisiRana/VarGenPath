# -*- coding: utf-8 -*-

"""Pipeline for VarGenPath"""
from typing import Optional

from click import File

from .constants import LINKSET_PATH, FILE_TYPES
from .utils import (
    get_cytoscape_connection, file_reader, get_associated_genes, var_genes_network, extend_vargen_network, save_session,
    save_image,
    save_network)


def get_vargenpath_network(
        *,
        variant_file: File,
        network_name: Optional[str] = 'VarGenPath network',
        linkset_path: Optional[str] = LINKSET_PATH,
        session_path: Optional[str] = None,
        image_path: Optional[str] = None,
        extend_network: bool = True,
        image_type: Optional[str] = 'svg',
        network_path: Optional[str] = None,
        network_file_path: Optional[str] = 'cyjs',
) -> dict:
    """
    Pipeline for creating vargenpath network.

    :param network_file_path: the type of network file to be saved.
    :param network_path: if input path, the cytoscape network will be saved to this path.
    :param variant_file: file containing a list of variants.
    :param network_name: the name of the network.
    :param linkset_path: the path to the linkset to extend network.
    :param session_path: if input path, the cytoscape session will be saved to this path.
    :param image_path: if input path, the image of the network will be saved to this path.
    :param extend_network: if true, the network will be extended.
    :param image_type: the type of the image to be saved.
    :return: cytoscape network
    """
    try:
        cy = get_cytoscape_connection()
    except Exception:
        raise Exception('Uh-oh! Make sure that cytoscape is open then try again.')
    variants = file_reader(variant_file)
    vargen_df = get_associated_genes(variants)
    network = var_genes_network(variants_genes_df=vargen_df, client=cy, network_name=network_name)
    if extend_network:
        network = extend_vargen_network(linkset_path, client=cy)
    if session_path is not None:
        save_session(session_file=session_path, client=cy)
    if image_path is not None:
        save_image(network_image=image_path, image_type=FILE_TYPES[image_type])
    if network_path is not None:
        save_network(network_path=network_path, file_type=FILE_TYPES[network_file_path])
    return network
