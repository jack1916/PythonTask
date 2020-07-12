#!/usr/bin/env python3
#Script to take directory via args and count all .json files inside
import argparse
import os
import sys

def countJsonFiles(path):
    if(not os.path.isdir(path)):
        print('The supplied path is not a directory')
        sys.exit()
    list_json = [x for x in os.listdir(path) if x.endswith(".json")]
    return len(list_json)
        
   #Count Json files in the directory passed to the method
def parseArgs(args):
    parser = argparse.ArgumentParser(description ='Count .json files in a directory')
    parser.add_argument('directory', help="the directory you would like to search")
    return parser.parse_args(args)
def main():
    args = parseArgs(sys.argv[1:])
    print(countJsonFiles(args.directory))

if __name__ == "__main__":
    main()
