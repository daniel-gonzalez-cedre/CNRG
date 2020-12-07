# script for running CNRG
datadir="./data"
graph="clique-ring-500-4"
path="${datadir}/${graph}"
#python runner.py -g "${graph}" -i "${path}.g" -N "${path}.nodes" -E "${path}.edges" -T "${path}.timestamps"
python runner.py -g "${graph}" -i "${path}.g" -N "${path}.nodes" -E "${path}.edges"
#python runner.py -g "${graph}" -i "${path}.g" -N "${path}.nodes"
#python3 runner.py -g "${graph}" -i "${path}.g" -E "${path}.edges"
