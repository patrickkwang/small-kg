"""Initialize."""
import os

_package_dir, _ = os.path.split(__file__)

nodes_file = os.path.join(_package_dir, "nodes.csv")

edges_file = os.path.join(_package_dir, "edges.csv")
