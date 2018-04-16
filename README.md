# Pricesearcher

## Introduction

This project represents my first attempt to build a simple Information Retrieval (IR) system. It comes as a really light, fully unit-tested, quite well documented software.
It has been written by using [Python3.4](https://www.python.org/download/releases/3.4.0/). To run the system, the following libraries

  1. [Numpy](http://www.numpy.org), version 1.14.2 or higher;
  2. [Pandas](https://pandas.pydata.org), version 0.22.0 or higher; 
  3. [Scikit-learn](http://scikit-learn.org/stable/) , version 0.19.1 or higher;  
  4. [NLTK](https://www.nltk.org) , version 3.0.4 or higher.

along with the [nltk.corpus.stopwords](https://pythonspot.com/nltk-stop-words/), module are needed.
The latter can be easily obtained by typing
```
$ python -m nltk.downloader stopwords
```
from command line once before running the system.


## System overview

The system downloads input data source from a user defined URL, unpack and store it into a user defined output path.
To perform ranked query searches, it generates TFIDF indexes for a given number of user defined research keys.
Then it applies cosine similarity for building similarities scores, ranking them and printing research results.
For this projects I have decided to use [**Vector Space Model**](https://en.wikipedia.org/wiki/Vector_space_model) representation for documents and queries.

## Software Installation Guide

To install the software, just follows the following instructions

```
$ mkdir ${HOME}/Project_directory
$ cd ${HOME}/Project_directory
$ git clone https://github.com/Fracappo87/Pricesearcher
```

then add the following line to your ```.bashrc``` file (or ```.profile``` if you are a Mac user)

```
export PYTHONPATH="$PYTHONPATH:$HOME/Project_directory/Pricesearcher"
```

Before starting to use the system, open a new terminal, move into the code directory and run all the tests:

```
$ cd $HOME/Project_directory/Pricesearcher
$ python3.4 -m unittest discover
```

if everything runs smoothly, then you are ready to use the software!
In this case, build the software documentation

```
$ cd $HOME/Project_directory/Pricesearcher/doc
$ ls
  Makefile source
$ make html
$ ls
  Makefile build source
```

the documentation in HTML format can be found inside the ```build``` directory

## Running the system

To run the system, just type

```
$ python3.4 -m research_engine.pricesearcher -h
```

and follow the instructions. For more details about running the system, you can have a look at the documentation.
