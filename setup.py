# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from setuptools import setup, find_packages
import versioneer

setup(
    name="q2-emperor",
    version=versioneer.get_version(),
    cmdclass=versioneer.get_cmdclass(),
    packages=find_packages(),
    install_requires=['qiime2 == 2017.3.*', 'q2-types == 2017.3.*',
                      'q2templates == 2017.3.*', 'emperor', 'scikit-bio',
                      'numpy', 'pandas'],
    author="Yoshiki Vazquez-Baeza",
    author_email="yoshiki@ucsd.edu",
    description="Display ordination plots",
    license='BSD-3-Clause',
    url="https://qiime2.org",
    entry_points={
        'qiime2.plugins':
        ['q2-emperor=q2_emperor.plugin_setup:plugin']
    },
    package_data={'q2_emperor': ['assets/index.html']},
    zip_safe=False,
)
