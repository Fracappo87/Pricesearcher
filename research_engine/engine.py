# -*- coding: utf-8 -*-
"""
Created on Wed Apr 11 18:01:39 2018

@author: Francesco Capponi
@email: capponi.francesco87@gmail.com
""" 

import numpy 
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
import pandas
import re
from sklearn.feature_extraction.text import TfidfVectorizer
#nltk.download('stopwords')

STOPWORDS=stopwords.words('english')

class ResearchEngine(object):
    """A research engine for performing information retrieval"""
    
    def __init__(self, json_descriptor):
        self.json_descriptor = json_descriptor
        self.vectorizers = None
        self.inverse_indexes = None
        
    def populate_data_frame(self):
        """Populate a relational dataframe by using data contained inside json descriptor"""
        
        self.dataframe = pandas.read_json(self.json_descriptor)
    
    def create_TFIDF_indexes(self, keys, log=False):
        """Create inverse document frequency indexes for a given number of research fields. Apply preprocessing by removing stopwords, stemming, converting all characters to lowercase."""
        
        keys = self._sanity_check(keys)
        print("\nIndexes produced by using the following fields: ",keys)
        
        self.vectorizers = [TfidfVectorizer(sublinear_tf=True, 
                                     strip_accents='unicode',
                                     stop_words='english') for instance in range(len(keys))]
                                     
        self.inverse_indexes = [self.vectorizers[index].fit_transform(self._preprocess_corpus(key)) for index, key in enumerate(keys)]
                     
    def research_and_rank(self, query, first_results=20):
        """Perform information retrieval on a given set of indexes. It applies then ranking by taking the averaged ranking score along the indexes."""             
        
        preprocessed_query = [self._preprocess_query(query)]
        query_vectors = [vectorizer.transform(preprocessed_query) for vectorizer in self.vectorizers]
        ranking = numpy.zeros([self.dataframe.shape[0], 1])
        for index, vector in enumerate(query_vectors):
            ranking += numpy.dot(self.inverse_indexes[index],vector.T)
       
        ranking = ranking/len(self.inverse_indexes)
        
        rank_indices = numpy.argsort(-ranking, axis=0)
        rank_indices = numpy.squeeze(numpy.asarray(rank_indices))[:first_results]

        return self.dataframe.iloc[rank_indices]
    
    def _preprocess_corpus(self, key):
        """Apply preprocessing operations (stemming, lowering, stopwords removal) to a corpus of documents"""

        sliced_frame=self.dataframe[key].str.lower()        
        sliced_frame=sliced_frame.str.split()
        sliced_frame=sliced_frame.apply(lambda words: [PorterStemmer().stem(word) for word in words if not word in set(STOPWORDS)])
        sliced_frame=sliced_frame.str.join(' ')
        
        return sliced_frame
        
    def _preprocess_query(self, query):
        """Apply preprocessing operations (stemming, lowering, stopwords removal) to a given query"""
        
        query = re.sub('[^a-zA-Z]', ' ',query)
        query = query.lower()
        query = query.split()
        query=[PorterStemmer().stem(word) for word in query if not word in set(STOPWORDS)]
        return ' '.join([word for word in query])
        
        
    def _sanity_check(self, keys):
        """Check that the research keys adopted by users are actually existing"""
        
        comprehension = [key for key in keys if key in self.dataframe.columns]
        if len(comprehension):
            return comprehension
        else:
            return self.dataframe.columns