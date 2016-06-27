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

from q2_types import PCoAResults
from emperor import Emperor


def plot_emperor(output_dir: str, sample_metadata: qiime.Metadata,
                 pcoa: skbio.OrdinationResults) -> None:



    return None


plugin = Plugin(
    name='emperor',
    version=q2_emperor.__version__,
    website='https://emperor.microbio.me',
    package='q2_emperor'
)

plugin.visualizers.register_function(
    function=plot_emperor,
    inputs={'pcoa': PCoAResults},
    parameters={'sample_metadata': Metadata},
    name='Visualize and Interact with Principal Coordinates Analysis Plots',
    description='Generate visualization of your ordination.'
)
