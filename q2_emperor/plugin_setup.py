# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import q2_emperor
from ._plot import plot

from qiime2.plugin import Plugin, Metadata, Str, List, Citations
from q2_types.ordination import PCoAResults

plugin = Plugin(
    name='emperor',
    version=q2_emperor.__version__,
    website='http://emperor.microbio.me',
    package='q2_emperor',
    citations=Citations.load('citations.bib', package='q2_emperor'),
    description=('This QIIME 2 plugin wraps Emperor and '
                 'supports interactive visualization of ordination '
                 'plots.'),
    short_description='Plugin for ordination plotting with Emperor.'
)

plugin.visualizers.register_function(
    function=plot,
    inputs={'pcoa': PCoAResults},
    parameters={'metadata': Metadata, 'custom_axes': List[Str]},
    input_descriptions={
        'pcoa': 'The principal coordinates matrix to be plotted.'
    },
    parameter_descriptions={
        'metadata': 'The sample metadata.',
        'custom_axes': ('Numeric sample metadata columns that should be '
                        'included as axes in the Emperor plot.')
    },
    name='Visualize and Interact with Principal Coordinates Analysis Plots',
    description='Generate visualization of your ordination.'
)
