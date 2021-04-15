#!/usr/bin/python
"""
Generate Markov chains to be cached in the filesystem; this saves us the effort
of generating new chains every time we want to make poetry.
"""
from __future__ import print_function

from argparse import ArgumentParser
import Markov
import os


def makeChain(name, sourceDir, cacheDir):
    """Parse the source text to generate new Markov chains."""
    sourceFile = sourceDir + name + ".txt"

    fwd = Markov.MarkovChain(cacheDir + name + "-fwd", 1, True)

    try:
        for line in open(sourceFile):
            words = line.split()
            if len(words) > 0:
                fwd.add(words)
    except IOError:
        print("The source named '%s' does not exist" % (name,))
    finally:
        fwd.close()


def deleteChainCache(name, cacheDir):
    """Delete the old cached versions of the chains, so we start fresh rather
    than adding to the previous chain files."""
    try:
        os.remove(cacheDir + name + "-fwd")
    except OSError:
        # if they don't exist, we don't care
        pass


if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument(
        "chainName", help="chainName is a specific source text to parse and cache"
    )
    args = parser.parse_args()
    print("Deleting old cache files")
    deleteChainCache(args.chainName, "cache/")

    print("Creating new cache files")
    makeChain(args.chainName, "sources/", "cache/")

    print("Chain(s) created successfully.")
