# ----------------------------------------------------------------------------
# Copyright (c) 2016-2023, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

bc_pcoa_results_url = ('https://data.qiime2.org/usage-examples/'
                       'moving-pictures/core-metrics-results/'
                       'bray_curtis_pcoa_results.qza')
unweighted_pcoa_results_url = ('https://data.qiime2.org/usage-examples/'
                               'moving-pictures/core-metrics-results/'
                               'unweighted_unifrac_pcoa_results.qza')

metadata_url = ('https://data.qiime2.org/usage-examples/'
                'moving-pictures/sample-metadata.tsv')


def plot(use):
    pcoa_results = use.init_artifact_from_url('pcoa_result',
                                              bc_pcoa_results_url)
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


def procrustes_plot(use):
    bc_pcoa_results = use.init_artifact_from_url('bc_pcoa_result',
                                                 bc_pcoa_results_url)
    unw_pcoa_results = use.init_artifact_from_url('unw_pcoa_result',
                                                  unweighted_pcoa_results_url)
    metadata = use.init_metadata_from_url('sample_metadata', metadata_url)

    viz, = use.action(
        use.UsageAction('emperor', 'procrustes_plot'),
        use.UsageInputs(
            reference_pcoa=bc_pcoa_results,
            other_pcoa=unw_pcoa_results,
            metadata=metadata
            ),
        use.UsageOutputNames(
            visualization='plot'
        )
    )

    viz.assert_output_type('Visualization')
