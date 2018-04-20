# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import q2_emperor
from ._plot import plot, procrustes_plot

from qiime2.plugin import Plugin, Metadata, Str, List
from q2_types.ordination import PCoAResults

PARAMETERS = {'metadata': Metadata, 'custom_axes': List[Str]}
PARAMETERS_DESC = {
    'metadata': 'The sample metadata.',
    'custom_axes': ('Numeric sample metadata columns that should be '
                    'included as axes in the Emperor plot.')
}

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
    parameter_descriptions=PARAMETERS_DESC,
    name='Visualize and Interact with Principal Coordinates Analysis Plots',
    description='Visualize and ordination'
)

plugin.visualizers.register_function(
    function=procrustes_plot,
    inputs={'reference_pcoa': PCoAResults, 'other_pcoa': PCoAResults},
    parameters=PARAMETERS,
    input_descriptions={
        'reference_pcoa': 'The reference ordination matrix to be plotted.',
        'other_pcoa': 'The "other" ordination matrix to be plotted (the one '
                      'that was fitted to the reference).'
    },
    parameter_descriptions=PARAMETERS_DESC,
    name='Visualize and Interact with a procrustes plot',
    description='Plot two procrustes-fitted matrices'
)
