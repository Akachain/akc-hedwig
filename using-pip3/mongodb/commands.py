import click
import os
from os.path import expanduser

def installMongodb():
    setup_sh = os.path.dirname(os.path.realpath(__file__))+'/setup.sh'
    excute = expanduser(setup_sh)
    os.system(excute)
    return True

@click.command('mongodb', short_help="Create mongodb for graylog")
def mongodb():
    installMongodb()