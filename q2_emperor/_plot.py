# ----------------------------------------------------------------------------
# Copyright (c) 2016-2018, QIIME 2 development team.
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
from emperor import Emperor

TEMPLATES = pkg_resources.resource_filename('q2_emperor', 'assets')


def generic_plot(output_dir: str, master: skbio.OrdinationResults,
                 metadata: qiime2.Metadata,
                 other_pcoa: skbio.OrdinationResults, plot_name,
                 custom_axes: str=None, settings: dict=None):

    mf = metadata.to_dataframe()

    if other_pcoa is None:
        procrustes = None
    else:
        procrustes = [other_pcoa]

    viz = Emperor(master, mf, procrustes=procrustes, remote='.')

    if custom_axes is not None:
        viz.custom_axes = custom_axes

    if other_pcoa:
        viz.procrustes_names = ['reference', 'other']

    vis.settings = settings

    html = viz.make_emperor(standalone=True)
    viz.copy_support_files(output_dir)
    with open(os.path.join(output_dir, 'emperor.html'), 'w') as fh:
        fh.write(html)

    index = os.path.join(TEMPLATES, 'index.html')
    q2templates.render(index, output_dir, context={'plot_name': plot_name})


def plot(output_dir: str, pcoa: skbio.OrdinationResults,
         metadata: qiime2.Metadata, custom_axes: str=None) -> None:
    generic_plot(output_dir, master=pcoa, metadata=metadata, other_pcoa=None,
                 custom_axes=custom_axes, plot_name='plot')


def procrustes_plot(output_dir: str, reference_pcoa: skbio.OrdinationResults,
                    other_pcoa: skbio.OrdinationResults,
                    metadata: qiime2.Metadata, custom_axes: str=None) -> None:
    generic_plot(output_dir, master=reference_pcoa, metadata=metadata,
                 other_pcoa=other_pcoa, custom_axes=custom_axes,
                 plot_name='procrustes_plot')
