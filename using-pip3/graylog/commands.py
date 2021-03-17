import click
import os
from os.path import expanduser

def installGraylog():
    setup_sh = os.path.dirname(os.path.realpath(__file__))+'/setup.sh'
    excute = expanduser(setup_sh)
    os.system(excute)
    return True

@click.command('graylog', short_help="Create graylog")
def graylog():
    installGraylog()