from os import linesep
from os.path import join
from random import random

def edge_attrs(filename):
    with open(f'{filename}.g') as infile, open(f'{filename}.edges', 'w') as outfile:
        for line in infile:
            u, v = line.strip().replace('\t', ' ').replace(',', ' ').split(' ')
            outfile.write(f'{u} {v} {1 if random() > 0.5 else 0}\n')
        outfile.truncate(outfile.tell() - len(linesep))
    return

def node_attrs(filename):
    with open(f'{filename}.g') as infile, open(f'{filename}.nodes', 'w') as outfile:
        nodes = set()
        for line in infile:
            u, v = line.strip().replace('\t', ' ').replace(',', ' ').split(' ')
            nodes.add(u)
            nodes.add(v)
        for v in nodes:
            outfile.write(f'{v} {1 if random() > 0.5 else 0}\n')
        outfile.truncate(outfile.tell() - len(linesep))
    return

def timestamps(filename):
    with open(f'{filename}.g') as infile, open(f'{filename}.timestamps', 'w') as outfile:
        t = 0
        for line in infile:
            u, v = line.strip().replace('\t', ' ').replace(',', ' ').split(' ')
            outfile.write(f'{u} {v} {t}\n')
            t += (1 if random() > 0.8 else 0)
        outfile.truncate(outfile.tell() - len(linesep))
    return

if __name__ == '__main__':
    filename = 'clique-ring-500-4'
    attribute = 'edges'

    if attribute == 'edges':
        edge_attrs(filename)
    elif attribute == 'nodes':
        node_attrs(filename)
    elif attribute == 'times':
        timestamps(filename)
