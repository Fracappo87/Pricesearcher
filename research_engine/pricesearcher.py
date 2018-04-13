# -*- coding: utf-8 -*-
"""
Created on Fri Apr 13 16:21:58 2018

@author: Francesco Capponi
@email: capponi.francesco87@gmail.com
""" 

import argparse
import pandas
from research_engine.downloader import PackageDownloader
from research_engine.engine import ResearchEngine
from time import time

pandas.set_option('expand_frame_repr', False)
pandas.set_option('display.max_columns', 999)

URL='https://s3-eu-west-1.amazonaws.com/pricesearcher-code-tests/software-engineer/products.json.gz'

def main():
    parser = argparse.ArgumentParser(description='Download and unpack data files, build inverse indexes, search and rank queries')
    parser.add_argument('--outpath',default='./',help='Outputpath for source data')
    parser.add_argument('--fields', default=[],nargs='+', help='Fields users can use for searching. If fields do not match then are removed. When all provided fields are wrong, then default fields are used')
    parser.add_argument('--to_show', default=10,help='Number of results to be shown. Default is 20')
  
    args = parser.parse_args()
    print("#############################################################")
    print("# WELCOME TO PRICESEARCHER, A REALLY SIMPLE RESEARCH ENGINE #")
    print("#############################################################")
    
    loader = PackageDownloader(URL)
    unpacked_filename = loader.download_and_unpack(args.outpath, True)
    print("\nDownloading source zipped file from the following URL :\n")
    print(URL)

    engine = ResearchEngine(unpacked_filename)
    engine.populate_data_frame()
    print("\nCreating inverse indexes\n")
    t0 = time()
    engine.create_TFIDF_indexes(args.fields, log=True)
    print("\nInverse indexes created in "+str(time()-t0)+" seconds\n")
    print("\n Ready to search: please type EXIT to terminate the application, or type anything else to continue\n\n")

    query = input("What do you want to search?")    
    while query != "EXIT":
            result = engine.research_and_rank(query, args.to_show)
            print(result.reset_index(drop=True))
            query = input("What do you want to search?")        
    return 0
        
if __name__ == "__main__":
    # execute only if run as a script
    main()