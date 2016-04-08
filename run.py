#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join
import sys
import getopt

def symlink(src, dest):
    """Will add all files in src to dest through 
    symlinks. If the item src exists as dest, it
    will drop into the directories and recursively
    call again.

    :src: TODO
    :dest: TODO
    :returns: TODO

    """
    for s_path, s_dirs, s_files in os.walk(src):
        for d_path, d_dirs, d_files in os.walk(dest):
            for s_dir in s_dirs:
                if s_dir in d_dirs:
                    symlink(join(s_path,s_dir),join(d_path,s_dir))
                else:
                    print("would symlink " + join(s_path,s_dir) + " to " \
                            join(d_path,s_dir))
        pass
    print(src + " " + dest)
    pass


if __name__ == "__main__":
    try:
        # Short option syntax: "hv:"
        # Long option syntax: "help" or "verbose="
        opts, args = getopt.getopt(sys.argv[1:], "hs:d:", ["src","dest"])
    
    except(getopt.GetoptError, err):
        # Print debug info
        print(str(err))
        sys.exit(2)
    
    for opt, arg in opts:
        if opt in ["-h", "--help"]:
            print("Usage: run.py -h -s <source> -d <destination>")
        elif opt in ["-v", "--verbose"]:
            verbose = arg
        elif opt in ["-s", "--src"]:
            src = arg
        elif opt in ["-d", "--dest"]:
            dest = arg

    symlink(src, dest)
