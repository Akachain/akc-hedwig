import click
from elasticsearch.commands import elasticsearch
from mongodb.commands import mongodb
from graylog.commands import graylog
# from fluentbit import fluentbit
@click.group()
def hedwid():
    pass

hedwid.add_command(mongodb)
hedwid.add_command(elasticsearch)
hedwid.add_command(graylog)
# graylog.add_command(fluentbit)

if __name__ == '__main__':
    hedwid()