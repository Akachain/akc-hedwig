import click
import os
from os.path import expanduser

def installElasticsearch():
    setup_sh = os.path.dirname(os.path.realpath(__file__))+'/setup.sh'
    excute = expanduser(setup_sh)
    os.system(excute)
    return True

@click.command('elasticsearch', short_help="Create elasticsearch for graylog")
def elasticsearch():
    installElasticsearch()