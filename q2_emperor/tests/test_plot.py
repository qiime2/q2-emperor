# ----------------------------------------------------------------------------
# Copyright (c) 2016-2021, QIIME 2 development team.
#
# Distributed under the terms of the Modified BSD License.
#
# The full license is in the file LICENSE, distributed with this software.
# ----------------------------------------------------------------------------

import os
import tempfile
import unittest

import pandas as pd
import numpy as np
import qiime2
import skbio

from q2_emperor import plot, procrustes_plot, biplot, generic_plot


class PlotTests(unittest.TestCase):
    def setUp(self):
        eigvals = pd.Series(np.array([0.50, 0.25, 0.25]),
                            index=['PC1', 'PC2', 'PC3'])
        samples = np.array([[0.1, 0.2, 0.3],
                            [0.2, 0.3, 0.4],
                            [0.3, 0.4, 0.5],
                            [0.4, 0.5, 0.6]])
        proportion_explained = pd.Series([15.5, 12.2, 8.8],
                                         index=['PC1', 'PC2', 'PC3'])
        samples_df = pd.DataFrame(samples,
                                  index=['A', 'B', 'C', 'D'],
                                  columns=['PC1', 'PC2', 'PC3'])
        self.pcoa = skbio.OrdinationResults(
                'PCoA',
                'Principal Coordinate Analysis',
                eigvals,
                samples_df,
                proportion_explained=proportion_explained)

        samples_df = pd.DataFrame(samples + 1.01,
                                  index=['A', 'B', 'C', 'D'],
                                  columns=['PC1', 'PC2', 'PC3'])
        self.other = skbio.OrdinationResults(
                'PCoA',
                'Principal Coordinate Analysis',
                eigvals.copy(),
                samples_df,
                proportion_explained=proportion_explained.copy())

        features = pd.DataFrame(index=['x', 'y', 'z'],
                                columns=['PC1', 'PC2', 'PC3'],
                                data=[[1, 2, 3], [1, 1, -1], [0, -2, 0.1]])
        self.biplot = skbio.OrdinationResults(
                'PCoA',
                'Principal Coordinate Analysis',
                eigvals.copy(),
                samples_df,
                features=features,
                proportion_explained=proportion_explained.copy())

        self.metadata = qiime2.Metadata(
            pd.DataFrame({'val1': ['1.0', '2.0', '3.0', '4.0'],
                          'val2': ['3.3', '3.5', '3.6', '3.9']},
                         index=pd.Index(['A', 'B', 'C', 'D'], name='id')))

    def test_plot(self):
        with tempfile.TemporaryDirectory() as output_dir:
            plot(output_dir, self.pcoa, self.metadata)
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())

    def test_plot_custom_axis(self):
        with tempfile.TemporaryDirectory() as output_dir:
            plot(output_dir, self.pcoa, self.metadata, custom_axes=['val1'])
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())

    def test_plot_custom_axes(self):
        with tempfile.TemporaryDirectory() as output_dir:
            plot(output_dir, self.pcoa, self.metadata,
                 custom_axes=['val1', 'val2'])
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())

    def test_plot_with_pcoa_features_strategy_ignore(self):
        # using the biplot test data, since it has features
        with tempfile.TemporaryDirectory() as output_dir:
            plot(output_dir, self.biplot, self.metadata,
                 ignore_pcoa_features=True)
            self.assertTrue(True)  # checkpoint, everything should be good

    def test_plot_with_pcoa_features_strategy_error(self):
        # using the biplot test data, since it has features
        with tempfile.TemporaryDirectory() as output_dir, \
                self.assertRaisesRegex(ValueError,
                                       'Arrows cannot be visualized'):
            plot(output_dir, self.biplot, self.metadata,
                 ignore_pcoa_features=False)

    def test_plot_procrustes(self):
        with tempfile.TemporaryDirectory() as output_dir:
            procrustes_plot(output_dir, self.pcoa, other_pcoa=self.other,
                            metadata=self.metadata)
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())

    def test_plot_procrustes_custom_axis(self):
        with tempfile.TemporaryDirectory() as output_dir:
            procrustes_plot(output_dir, self.pcoa, other_pcoa=self.other,
                            metadata=self.metadata, custom_axes=['val1'])
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())

    def test_generic_plot_with_settings(self):
        settings = {'shape': {'category': 'val1', 'data': {}}}
        with tempfile.TemporaryDirectory() as output_dir:
            generic_plot(output_dir, self.pcoa, self.metadata, other_pcoa=None,
                         plot_name='plot', settings=settings)
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())

    def test_biplot(self):
        with tempfile.TemporaryDirectory() as output_dir:
            biplot(output_dir, self.biplot,
                   sample_metadata=self.metadata)
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())

    def test_biplot_with_feature_metadata(self):
        feat_md = qiime2.Metadata(
            pd.DataFrame(index=pd.Index(['x', 'y', 'z'], name='feature id'),
                         columns=['k', 'p'],
                         data=[['Bacteria', 'Firmicutes'],
                               ['Bacteria', 'Firmicutes'],
                               ['Bacteria', 'Bacteroidetes']]))

        with tempfile.TemporaryDirectory() as output_dir:
            biplot(output_dir, self.biplot,
                   sample_metadata=self.metadata, feature_metadata=feat_md)
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())

    def test_biplot_invert(self):
        feat_md = qiime2.Metadata(
            pd.DataFrame(index=pd.Index(['x', 'y', 'z'], name='feature id'),
                         columns=['k', 'p'],
                         data=[['Bacteria', 'Firmicutes'],
                               ['Bacteria', 'Firmicutes'],
                               ['Bacteria', 'Bacteroidetes']]))

        with tempfile.TemporaryDirectory() as output_dir:
            biplot(output_dir, self.biplot,
                   sample_metadata=self.metadata, feature_metadata=feat_md,
                   invert=True)
            index_fp = os.path.join(output_dir, 'index.html')
            self.assertTrue(os.path.exists(index_fp))
            self.assertTrue('src="./emperor.html"' in open(index_fp).read())
