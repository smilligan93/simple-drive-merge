#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join, abspath, islink, isdir, isfile
import sys
import getopt

def symlink(src, dest, dir_only, file_only):
    """Will add all files in src to dest through 
    symlinks. If the item src exists as dest, it
    will drop into the directories and recursively
    call again.
    """
    if islink(dest):
        print(dest + " is symlink, returning...")
        return
    for t in os.listdir(src):
        if isdir(join(src, t)) and not file_only:
            d_src  = abspath(join(src, t))
            d_dest = abspath(join(dest, t))
            if isdir(d_dest):
                print(d_dest + " already exists, going in...")
                symlink(d_src, d_dest, dir_only, file_only)
            else:
                print(d_dest + " does not exist, making symlink")
                os.symlink(d_src, d_dest)
        if isfile(join(src, t)) and not dir_only:
            f_src  = abspath(join(src, t))
            f_dest = abspath(join(dest, t))
            if isfile(f_dest):
                print(f_dest + " already exists, skipping...")
                pass
            else:
                print(f_dest + " does not exist, making symlink")
                os.symlink(f_src, f_dest)


if __name__ == "__main__":

    dir_only = False
    file_only = False
    try:
        # Short option syntax: "hv:"
        # Long option syntax: "help" or "verbose="
        opts, args = getopt.getopt(sys.argv[1:], "hs:d:", ["src=","dest=","dir","file"])
    
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
        elif opt in ["--dir"]:
            dir_only = True
        elif opt in ["--file"]:
            file_only = True

    symlink(src, dest, dir_only, file_only)
