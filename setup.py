#! /usr/bin/env python
#
# Copyright 2020 Peter Dowell <p.g.dowell@gmail.com>

def get_version():
    version_re = re.compile("""__version__[\s]*=[\s]*['|"](.*)['|"]""")
    init_file = os.path.join( os.path.dirname(__file__), DISTNAME, "__init__.py" )
    with open(init_file) as file:
        content = file.read()
        match = version_re.search(content)
        version = match.group(1)
    return version

#Define constants
DISTNAME="covid-electricity-demand"
MAINTAINER="Peter Dowell"
MAINTAINER_EMAIL="p.g.dowell@gmail.com"
DESCRIPTION="Analysis of electricity useage data"
LICENSE=""
URL="https://github.com/condensedWeasel/covid-electricity-demand"
NUMPY_MIN_VERSION="1.18"
PANDAS_MIN_VERSION="1.0"
MATPLOTLIB_MIN_VERSION="3.1"
PLOTLY_MIN_VERSION="4.9"
SEABORN_MIN_VERSION="0.10"
FP_PROPHET_VERSION=""

import os, sys, re

# Get description from README.md
readme = os.path.join( os.path.dirname(__file__),"README.md" )
LONG_DESCRIPTION = open( readme ).read()

# Version number is contained in package
VERSION = get_version()

def setup_package():
    """ Sets up package metadata """
    from setuptools import setup, find_packages

    metadata = dict(name=DISTNAME,
                    maintainer=MAINTAINER,
                    maintainer_email=MAINTAINER_EMAIL,
                    description=DESCRIPTION,
                    long_description=LONG_DESCRIPTION,
                    license=LICENSE,
                    url=URL,                    
                    version=VERSION,                    
                    classifiers=['Intended Audience :: Science/Research',
                                 'Intended Audience :: Developers',
                                 'Programming Language :: Python',
                                 'Topic :: Software Development',
                                 'Topic :: Scientific/Engineering',
                                 'Operating System :: Microsoft :: Windows', 				                 
                                 'Programming Language :: Python :: 3.7',
                                 'Programming Language :: Python :: 3.8'
                                 ],                   
                    python_requires=">=3.7",
                    install_requires=[
                        'numpy>={}'.format(NUMPY_MIN_VERSION),
                        'pandas>={}'.format(PANDAS_MIN_VERSION),
                        'matplotlib>={}'.format(MATPLOTLIB_MIN_VERSION),
                        'plotly>={}'.format(PLOTLY_MIN_VERSION),
                        'seaborn>={}'.format(SEABORN_MIN_VERSION),                        
                        'fbprophet>={}'.format(FP_PROPHET_VERSION)
                        ],
		            )
    metadata['packages'] = find_packages()
    setup(**metadata)

if __name__ == "__main__":
    setup_package()