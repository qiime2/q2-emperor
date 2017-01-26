# ----------------------------------------------------------------------------
# Copyright (c) 2016-2017, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------


import q2_emperor
from ._plot import plot

from qiime2.plugin import Plugin, Metadata, Str
from q2_types.ordination import PCoAResults


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
    parameters={'metadata': Metadata, 'custom_axis': Str},
    input_descriptions={
        'pcoa': 'The principal coordinates matrix to be plotted.'
    },
    parameter_descriptions={
        'metadata': 'The sample metadata.',
        'custom_axis': ('A sample metadata category containing continuous '
                        'values that should be included as an axis in the '
                        'Emperor plot.')
    },
    name='Visualize and Interact with Principal Coordinates Analysis Plots',
    description='Generate visualization of your ordination.'
)
