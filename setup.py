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
    version='0.0.0-dev',
    packages=find_packages(),
    install_requires=['emperor', 'scikit-bio',
                      'qiime >= 2.0.0', 'q2-types'],
    author="Yoshiki Vazquez-Baeza",
    author_email="yoshiki@ucsd.edu",
    description="Display ordination plots",
    license="bsd",
    url="http://emperor.microbio.me",
    entry_points={
        'qiime.plugin':
        ['q2-emperor=q2_emperor.plugin_setup:plugin']
    }
)
