# -*- coding: utf-8 -*-
"""
Created on Tue Apr 10 18:06:05 2018

@author: francesco capponi
@email: capponi.francesco87@gmail.com
"""

import os
import unittest
from research_engine.downloader import PackageDownloader

URL='https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/software-engineer/products.json.gz'

class TestPackageDownloader(unittest.TestCase):
    
    def setUp(self):
        self.url=URL
        self.wrongurl='qufkwebkuwedsbn'
        self.outpath = os.getcwd()
        self.expected_gz_file = os.path.join(self.outpath, 'products.json.gz')
        self.expected_json_file = os.path.join(self.outpath, 'products.json')
             
    def test_init(self):
        
        loader = PackageDownloader(self.wrongurl)
        self.assertEqual(loader.url, self.wrongurl)
        
    def test_download_and_unpack(self):

        # check it raises exception if wrong url is given        
        loader = PackageDownloader(self.wrongurl)
        self.assertRaises(ValueError, loader.download_and_unpack,self.outpath)
        
        # now load from correct url
        loader = PackageDownloader(self.url)

        loader.download_and_unpack(self.outpath)                
        self.assertTrue(os.path.isfile(self.expected_gz_file))

        descriptor_name = loader.download_and_unpack(self.outpath, unpack=True)
        self.assertTrue(os.path.isfile(self.expected_json_file))
        self.assertEqual(descriptor_name, self.expected_json_file)
        
        os.remove(self.expected_json_file)
