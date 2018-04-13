# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 19:20:27 2018

@author: francesco capponi
@email: capponi.francesco87@gmail.com
"""

import json
import os
import numpy
import pandas
import unittest
from research_engine.engine import ResearchEngine
from scipy.sparse.csr import csr_matrix
from sklearn.feature_extraction.text import TfidfVectorizer

class TestResearchEngine(unittest.TestCase):
    
    def setUp(self):
        
        self.example_list = [{'A':'unbelievably not a','B':'kung fu','C':'pandas'},{'A':'tRoubles','B':'liTTle Chinatown','C':'Town'}]
           
        self.json_descriptor = 'descriptor.json'
        self.expected_frame = pandas.DataFrame.from_records(self.example_list)
        with open(self.json_descriptor, 'w') as fp:
            json.dump(self.example_list, fp)

    def tearDown(self):
        os.remove(self.json_descriptor)

    def test_init(self):
        engine = ResearchEngine('Pluto')
        self.assertEqual(engine.json_descriptor, 'Pluto')
        self.assertEqual(None, engine.vectorizers)
        self.assertEqual(None, engine.inverse_indexes)
        
    def test_populate_data_frame(self):
        engine = ResearchEngine(self.json_descriptor)
        engine.populate_data_frame()
        pandas.testing.assert_frame_equal(self.expected_frame, engine.dataframe)
        
    def test_preprocess_corpus(self):
        engine = ResearchEngine(self.json_descriptor)
        engine.populate_data_frame()
        
        test_series=engine._preprocess_corpus('A')
        pandas.testing.assert_series_equal(pandas.Series(['unbeliev', 'troubl'], name='A'), test_series)
        
        test_series=engine._preprocess_corpus('C')
        pandas.testing.assert_series_equal(pandas.Series(['panda', 'town'], name='C'), test_series)

    def test_preprocess_query(self):
        engine = ResearchEngine(self.json_descriptor)
        engine.populate_data_frame()
        
        query = 'I am a magical cat!'
        preprocessed_query = engine._preprocess_query(query)
        self.assertEqual(preprocessed_query, 'magic cat')

    def test_create_TFIDF_indexes(self):
        engine = ResearchEngine(self.json_descriptor)
        engine.populate_data_frame()
                
        keys=['A', 'C']
        engine.create_TFIDF_indexes(keys)
        test_arrays = [numpy.array([[0., 1.],[1., 0.]]), numpy.array([[1., 0.],[0., 1.]])]        
        
        for index in range(len(keys)):
            self.assertTrue(isinstance(engine.vectorizers[index], TfidfVectorizer))
            self.assertTrue(isinstance(engine.inverse_indexes[index], csr_matrix))
            numpy.testing.assert_array_equal(engine.inverse_indexes[index].todense(), test_arrays[index])

    def test_research_and_rank(self):    
        engine = ResearchEngine(self.json_descriptor)
        engine.populate_data_frame()
        keys=['A', 'C']
        engine.create_TFIDF_indexes(keys)
        result = engine.research_and_rank('panda', 1)
        pandas.testing.assert_series_equal(self.expected_frame.iloc[[0]].iloc[0], result.iloc[0])
        
        keys=['B']
        engine.create_TFIDF_indexes(keys)
        result = engine.research_and_rank('little', 1)
        pandas.testing.assert_series_equal(self.expected_frame.iloc[[1]].iloc[0], result.iloc[0])

    def test_sanity_check(self):
        engine = ResearchEngine(self.json_descriptor)
        engine.populate_data_frame()
        self.assertCountEqual(engine._sanity_check(['B']),['B'])
        self.assertCountEqual(engine._sanity_check(['A', 'B']),['A', 'B'])
        self.assertCountEqual(engine._sanity_check(['B', 'A', 'C']), ['B', 'A', 'C'])
        self.assertCountEqual(engine._sanity_check(['A', 'B', 'D']), ['A', 'B'])
        self.assertCountEqual(engine._sanity_check([]), ['A', 'B', 'C'])