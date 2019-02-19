from distutils.core import setup, Extension
from Cython.Build import cythonize
import numpy

# call as python setup_cython.py build_ext --inplace
setup(
    ext_modules = cythonize("particlescv2.pyx"),
    include_dirs=[numpy.get_include()]
)