# Pricesearcher

This project represents my first attempt to build a simple Information Retrieval (IR) system.
It has been written by using [Python3.4](https://www.python.org/download/releases/3.4.0/). 
It comes as a really light, fully unit-tested, quite well documented software.
The system downloads input data source from a user defined URL, unpack and store it into a user defined output path.
To perform ranked query searches, it generates TFIDF indexes for a given number of user defined research keys.
Then it applies cosine similarity for building similarities scores, ranking them and printing research results.

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
