# Import rpy2 packages
import rpy2.robjects.packages as rpackages
from rpy2.robjects.vectors import StrVector

utils = rpackages.importr('utils')
utils.chooseCRANmirror(ind=1) # Choose Mirror for installing the R packages

# You can add as many packages as you want to import
packages = ('germinationmetrics',)

names_to_install = [x for x in packages if not rpackages.isinstalled(x)] # filters out the already installed ones

if len(names_to_install) > 0:
    utils.install_packages(StrVector(names_to_install))

# Ymport GerminationMetrics package
gm = rpackages.importr('germinationmetrics')

help(gm)
