#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
from os.path import join, abspath, islink
import sys
import getopt

def symlink(src, dest, dir_only, file_only):
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
            if not file_only:
                for s_dir in s_dirs:
                    if islink(join(d_path,s_dir)):
                        break
                    if s_dir in d_dirs:
                        symlink(join(s_path,s_dir),
                                join(d_path,s_dir),
                                dir_only,
                                file_only)
                    else:
                        abs_src_path  = abspath(join(s_path,s_dir))
                        abs_dest_path = abspath(join(d_path,s_dir))
                        if islink(abs_dest_path):
                            break
                        print("would symlink "
                                + str(abs_src_path)
                                + " to "
                                + str(abs_dest_path))
                        os.symlink(abs_src_path, abs_dest_path)
                        #return True
            break
            if not dir_only:
                for s_file in s_files:
                    if islink(join(s_path,s_file)):
                        pass
                    elif s_file in d_files:
                        pass
                    else:
                        abs_src_path  = abspath(join(s_path,s_file))
                        abs_dest_path = abspath(join(d_path,s_file))
                        print("would symlink "
                                + str(abs_src_path)
                                + " to "
                                + str(abs_dest_path))
                        #os.symlink(abs_src_path, abs_dest_path)


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
