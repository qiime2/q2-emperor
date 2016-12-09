# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Emperor development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import pkg_resources

import qiime
import skbio
import q2templates
from emperor import Emperor

TEMPLATES = pkg_resources.resource_filename('q2_emperor', 'assets')


def plot(output_dir: str, pcoa: skbio.OrdinationResults,
         metadata: qiime.Metadata, custom_axis: str=None) -> None:

    mf = metadata.to_dataframe()
    viz = Emperor(pcoa, mf, remote='.')

    if custom_axis is not None:
        # put custom_axis inside a list to workaround the type system not
        # supporting lists of types
        html = viz.make_emperor(standalone=True, custom_axes=[custom_axis])
    else:
        html = viz.make_emperor(standalone=True)
    viz.copy_support_files(output_dir)
    with open(os.path.join(output_dir, 'emperor.html'), 'w') as fh:
        fh.write(html)

    index = os.path.join(TEMPLATES, 'index.html')
    q2templates.render(index, output_dir)
