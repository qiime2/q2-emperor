# ----------------------------------------------------------------------------
# Copyright (c) 2016--, Emperor development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import qiime
import skbio

from qiime.plugin import Plugin, Metadata

import q2_emperor
from q2_types import PCoAResults
from emperor import Emperor
from os.path import join


def plot(output_dir: str, sample_metadata: qiime.Metadata,
         pcoa: skbio.OrdinationResults) -> None:

    mf = sample_metadata.to_dataframe()

    output = join(output_dir, 'emperor-required-resources/')
    viz = Emperor(pcoa, mf, remote='.')

    with open(join(output_dir, 'index.html'), 'w') as f:
        # correct the path
        html = viz.make_emperor(standalone=True)
        viz.copy_support_files(output_dir)
        f.write(html)

    return None


plugin = Plugin(
    name='emperor',
    version=q2_emperor.__version__,
    website='https://emperor.microbio.me',
    package='q2_emperor',
    citation_text=('EMPeror: a tool for visualizing high-'
                   'throughput microbial community data.\nVazquez-Baeza Y, '
                   'Pirrung M, Gonzalez A, Knight R.\nGigascience. '
                   '2013 Nov 26;2(1):16.'),
    user_support_text=('To get help with Emperor, please post to the Emperor '
                       'issue tracker: https://github.com/biocore/emperor'
                       '/issues')
)

plugin.visualizers.register_function(
    function=plot,
    inputs={'pcoa': PCoAResults},
    parameters={'sample_metadata': Metadata},
    name='Visualize and Interact with Principal Coordinates Analysis Plots',
    description='Generate visualization of your ordination.'
)
