"""Initialize."""
import os

from small_kg import ctd
from small_kg import hetio
from small_kg import mychem

_package_dir, _ = os.path.split(__file__)

synonyms_file = os.path.join(_package_dir, "synonyms.csv")
