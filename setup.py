# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Emperor development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages

setup(
    name="q2-emperor",
    # todo stop duplicating version string
    version='0.0.5',
    packages=find_packages(),
    install_requires=['qiime >= 2.0.5', 'q2-types >= 0.0.5', 'emperor',
                      'scikit-bio', 'q2templates'],
    author="Yoshiki Vazquez-Baeza",
    author_email="yoshiki@ucsd.edu",
    description="Display ordination plots",
    license='BSD-3-Clause',
    url="http://emperor.microbio.me",
    entry_points={
        'qiime.plugins':
        ['q2-emperor=q2_emperor.plugin_setup:plugin']
    },
    package_data={'q2_emperor': ['assets/index.html']}
)
