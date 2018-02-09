# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import q2_emperor
from ._plot import plot

from qiime2.plugin import Plugin, Metadata, Str, List
from q2_types.ordination import PCoAResults


plugin = Plugin(
    name='emperor',
    version=q2_emperor.__version__,
    website='http://emperor.microbio.me',
    package='q2_emperor',
    citation_text=('EMPeror: a tool for visualizing high-'
                   'throughput microbial community data.\nVazquez-Baeza Y, '
                   'Pirrung M, Gonzalez A, Knight R.\nGigascience. '
                   '2013 Nov 26;2(1):16.\n'
                   'Bringing the Dynamic Microbiome to Life with Animations.\n'
                   'Vazquez-Baeza Y, Gonzalez A, Smarr L, McDonald D, Morton '
                   'J, Navas-Molina J, Knight R.\nCell Host & Microbe.'
                   'Volume 21, Issue 1, p7–10, 11 January 2017.'),
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
