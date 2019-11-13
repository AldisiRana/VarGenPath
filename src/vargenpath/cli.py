# -*- coding: utf-8 -*-

import click

from .constants import LINKSET_PATH
from .pipeline import get_vargenpath_network

@click.command()
@click.option('--variants-list', required=True, help='A list with variants.')
@click.option('--network-name', default='VarGenPath network', help='The name of your network.')
@click.option('--image-path', help='If input, the network will be saved as an image in the provided path.')
@click.option('--session-path', help='If input, the cytoscape session will be saved in the provided path.')
@click.option('--extend-network', is_flag=True, help='if true, the network will be extended.')
@click.option('--linkset-path', Default=LINKSET_PATH,
              help='if input network will be extended using the linkset, otherwise will use default.')
def main(
    variants_list,
    netwok_name,
    image_path,
    session_path,
    extend_network,
    linkset_path,
):
    """Command Line Interface for VarGenPath."""
    get_vargenpath_network(
        variant_list_path=variants_list,
        network_name=netwok_name,
        image_path=image_path,
        session_path=session_path,
        extend_network=extend_network,
        linkset_path=linkset_path,
    )
    click.echo('Task is done.')


if __name__ == '__main__':
    main()