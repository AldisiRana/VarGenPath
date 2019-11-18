# -*- coding: utf-8 -*-

"""Command Line Interface for VarGenPath."""
import json

import click
from vargenpath.utils import file_reader

from .constants import LINKSET_PATH
from .pipeline import get_vargenpath_network


@click.command()
@click.option('--variants-file', type=click.File('r'), required=True, help='A list with variants.')
@click.option('--network-name', default='VarGenPath network', help='The name of your network.')
@click.option('--image-path', type=str,
              help='If input, the network will be saved as an image in the provided path.')
@click.option('--image-type',
              type=click.Choice(['jpeg', 'jpg', 'pdf', 'png', 'ps', 'svg']), default='svg',
              help='type of image to be saved.')
@click.option('--session-path', type=str,
              help='If input, the cytoscape session will be saved in the provided path.')
@click.option('--extend-network', is_flag=True, help='if true, the network will be extended.')
@click.option('--linkset-path', type=click.Path(exists=True), default=LINKSET_PATH,
              help='if input network will be extended using the linkset, otherwise will use default.')
@click.option('--network-path', type=str,
              help='If input, the cytoscape network will be saved in the provided path.')
@click.option('--network-file-type',
              type=click.Choice(['cx', 'cyjs', 'graphml', 'xgmml', 'nnf', 'psi_mi_level_1', 'psi_mi_level_2.5', 'sif']),
              default='cyjs', help='type of image to be saved.')
def main(
    variants_file,
    network_name,
    image_path,
    session_path,
    extend_network,
    linkset_path,
    image_type,
    network_path,
    network_file_type,
):
    """Command Line Interface for VarGenPath."""
    variants_list = file_reader(variants_file)
    network = get_vargenpath_network(
        variant_list=variants_list,
        network_name=network_name,
        image_path=image_path,
        image_type=image_type,
        session_path=session_path,
        extend_network=extend_network,
        linkset_path=linkset_path,
        network_path=network_path,
        network_file_path=network_file_type,
    )
    click.echo(json.dumps(network, indent=2, sort_keys=True))


if __name__ == '__main__':
    main()
