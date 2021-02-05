# ----------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import q2_emperor
from ._plot import plot, procrustes_plot, biplot

from qiime2.plugin import (Plugin, Metadata, Str, List, Citations, Range, Int,
                           Bool, Properties)
from q2_types.ordination import PCoAResults

PARAMETERS = {'metadata': Metadata, 'custom_axes': List[Str],
              'ignore_missing_samples': Bool}
PARAMETERS_DESC = {
    'metadata': 'The sample metadata.',
    'custom_axes': ('Numeric sample metadata columns that should be '
                    'included as axes in the Emperor plot.'),
    'ignore_missing_samples': (
        'This will suppress the error raised when the coordinates matrix '
        'contains samples that are not present in the metadata. Samples '
        'without metadata are included by setting all metadata values to: '
        '"This sample has no metadata". This flag is only applied if at '
        'least one sample is present in both the coordinates matrix and the '
        'metadata.'
    )
}

PLOT_PARAMETERS_DESC = {
    **PARAMETERS_DESC,
    'ignore_pcoa_features': 'Biplot arrows cannot be visualized using this '
                            'method. If you want to visualize biplot arrows '
                            'use the `biplot` method. Enabling this setting '
                            'will ignore any PCoA features that are present, '
                            'otherwise, if PCoA features are detected an '
                            'error will be raised.'
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
    parameters={
        'metadata': Metadata,
        'custom_axes': List[Str],
        'ignore_missing_samples': Bool,
        'ignore_pcoa_features': Bool
    },
    input_descriptions={
        'pcoa': 'The principal coordinates matrix to be plotted.'
    },
    parameter_descriptions=PLOT_PARAMETERS_DESC,
    name='Visualize and Interact with Principal Coordinates Analysis Plots',
    description='Generates an interactive ordination plot where the user '
                'can visually integrate sample metadata.'
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

plugin.visualizers.register_function(
    function=biplot,
    inputs={'biplot': PCoAResults % Properties("biplot")},
    parameters={'sample_metadata': Metadata,
                'feature_metadata': Metadata,
                'ignore_missing_samples': Bool,
                'invert': Bool,
                'number_of_features': Int % Range(1, None)},
    input_descriptions={
        'biplot': 'The principal coordinates matrix to be plotted.'
    },
    parameter_descriptions={
        'sample_metadata': 'The sample metadata',
        'feature_metadata': 'The feature metadata (useful to manipulate the '
                            'arrows in the plot).',
        'invert': 'If specified, the point and arrow coordinates '
                  'will be swapped.',
        'ignore_missing_samples': PARAMETERS_DESC['ignore_missing_samples'],
        'number_of_features': 'The number of most important features '
                              '(arrows) to display in the ordination.'
                              ' “Importance” is calculated for each feature '
                              'based on the vector’s magnitude '
                              '(euclidean distance from origin).',
        },
    name='Visualize and Interact with Principal Coordinates Analysis Biplot',
    description='Generates an interactive ordination biplot where the user '
                'can visually integrate sample and feature metadata. '
                'Vectors representing the n most important features '
                'are then plotted in the emperor '
                'visualization (5 largest, by default).'
)
