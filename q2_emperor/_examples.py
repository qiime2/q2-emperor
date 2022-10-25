# ----------------------------------------------------------------------------
# Copyright (c) 2016-2022, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

from qiime2 import Visualization


pcoa_results_url = 'https://docs.qiime2.org/2022.8/data/tutorials/' \
    'moving-pictures/core-metrics-results/bray_curtis_pcoa_results.qza'

metadata_url = 'https://data.qiime2.org/{epoch}/tutorials/' \
               'moving-pictures/sample_metadata.tsv'

def plot(use):
    pcoa_results = use.init_artifact_from_url('pcoa_result', pcoa_results_url)
    metadata = use.init_metadata_from_url('sample_metadata', metadata_url)

    viz, = use.action(
        use.UsageAction('emperor', 'plot'),
        use.UsageInputs(
            pcoa=pcoa_results,
            metadata=metadata
            ),
        use.UsageOutputNames(
            visualization='plot'
        )
    )

    viz.assert_output_type('Visualization')

