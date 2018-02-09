# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import pkg_resources

import qiime2
import skbio
import q2templates
from emperor import Emperor

TEMPLATES = pkg_resources.resource_filename('q2_emperor', 'assets')


def plot(output_dir: str, pcoa: skbio.OrdinationResults,
         metadata: qiime2.Metadata, custom_axes: str=None) -> None:

    mf = metadata.to_dataframe()
    viz = Emperor(pcoa, mf, remote='.')

    html = viz.make_emperor(standalone=True, custom_axes=custom_axes)
    viz.copy_support_files(output_dir)
    with open(os.path.join(output_dir, 'emperor.html'), 'w') as fh:
        fh.write(html)

    index = os.path.join(TEMPLATES, 'index.html')
    q2templates.render(index, output_dir)
