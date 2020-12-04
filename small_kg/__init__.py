"""Initialize."""
import os

import small_kg.ctd
import small_kg.hetio
import small_kg.mychem

_package_dir, _ = os.path.split(__file__)

synonyms_file = os.path.join(_package_dir, "synonyms.csv")
