# -*- coding: utf-8 -*-
"""
Created on Mon Apr  9 18:20:03 2018

@author: Francesco Capponi
@email: capponi.francesco87@gmail.com
"""

import os
import requests

# To DO:
# General methods for filtering data
# General methods for researching fields and ranking them

class PackageDownloader(object):
    """Base class describing a research engine"""
    
    def __init__(self, url):
        
        self.url = url
        
    def download_and_unpack(self, outpath, unpack=False):
        """Download source data file from a given url, unpack"""   
        
        r = requests.get(self.url)
        r.raise_for_status()

        filename = os.path.join(outpath, self.url.split("/")[-1])
        with open(filename, "wb") as f:            
             f.write(r.content)
        
        if unpack:
            return self.unpack(filename)
     
    @staticmethod       
    def unpack(filename):
        """Unpack compressed data file, returns json object """
      
        os.system("gunzip  {}".format(filename))   
        descriptor_name = os.path.splitext(filename)[0]
            
        return  descriptor_name
        
        

