# ----------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import pkg_resources

import qiime2
import skbio
import q2templates
import numpy as np
from emperor import Emperor
from scipy.spatial.distance import euclidean

TEMPLATES = pkg_resources.resource_filename('q2_emperor', 'assets')


def generic_plot(output_dir: str, master: skbio.OrdinationResults,
                 metadata: qiime2.Metadata,
                 other_pcoa: skbio.OrdinationResults,
                 plot_name: str,
                 custom_axes: str = None, settings: dict = None,
                 ignore_missing_samples: bool = False,
                 feature_metadata: qiime2.Metadata = None):

    mf = metadata.to_dataframe()
    if feature_metadata is not None:
        feature_metadata = feature_metadata.to_dataframe()

    if other_pcoa is None:
        procrustes = None
    else:
        procrustes = [other_pcoa]

    viz = Emperor(master, mf, feature_mapping_file=feature_metadata,
                  ignore_missing_samples=ignore_missing_samples,
                  procrustes=procrustes, remote='.')

    if custom_axes is not None:
        viz.custom_axes = custom_axes

    if other_pcoa:
        viz.procrustes_names = ['reference', 'other']

    viz.settings = settings

    html = viz.make_emperor(standalone=True)
    viz.copy_support_files(output_dir)
    with open(os.path.join(output_dir, 'emperor.html'), 'w') as fh:
        fh.write(html)

    index = os.path.join(TEMPLATES, 'index.html')
    q2templates.render(index, output_dir, context={'plot_name': plot_name})


def plot(output_dir: str, pcoa: skbio.OrdinationResults,
         metadata: qiime2.Metadata, custom_axes: str = None,
         ignore_missing_samples: bool = False,
         ignore_pcoa_features: bool = False) -> None:

    if ignore_pcoa_features:
        pcoa.features = None
    if pcoa.features is not None:
        raise ValueError("Arrows cannot be visualized with the 'plot' method, "
                         "use 'biplot' instead, or enable "
                         "`ignore_pcoa_features`.")

    generic_plot(output_dir, master=pcoa, metadata=metadata, other_pcoa=None,
                 ignore_missing_samples=ignore_missing_samples,
                 custom_axes=custom_axes, plot_name='plot')


def procrustes_plot(output_dir: str, reference_pcoa: skbio.OrdinationResults,
                    other_pcoa: skbio.OrdinationResults,
                    metadata: qiime2.Metadata, custom_axes: str = None,
                    ignore_missing_samples: bool = False) -> None:
    generic_plot(output_dir, master=reference_pcoa, metadata=metadata,
                 other_pcoa=other_pcoa, custom_axes=custom_axes,
                 ignore_missing_samples=ignore_missing_samples,
                 plot_name='procrustes_plot')


def biplot(output_dir: str, biplot: skbio.OrdinationResults,
           sample_metadata: qiime2.Metadata, feature_metadata:
           qiime2.Metadata = None,
           ignore_missing_samples: bool = False,
           invert: bool = False,
           number_of_features: int = 5) -> None:

    if invert:
        biplot.samples, biplot.features = biplot.features, biplot.samples
        sample_metadata, feature_metadata = feature_metadata, sample_metadata

    # select the top N most important features based on the vector's magnitude
    feats = biplot.features.copy()
    origin = np.zeros_like(feats.columns)
    feats['importance'] = feats.apply(euclidean, axis=1, args=(origin,))
    feats.sort_values('importance', inplace=True, ascending=False)
    feats.drop(['importance'], inplace=True, axis=1)
    biplot.features = feats[:number_of_features].copy()

    generic_plot(output_dir, master=biplot, other_pcoa=None,
                 ignore_missing_samples=ignore_missing_samples,
                 metadata=sample_metadata, feature_metadata=feature_metadata,
                 plot_name='biplot')
