"""
This is a setup.py script for the Windows build of nCoda. It uses py2exe to aid in 
installation process.

Usage:
    python setup.py py2exe
"""
import os
from distutils.core import setup
import py2exe

def rec_find_data_files(this_dir):
    """
    Recursively gets all the files contained within the main_directory 
    in the proper format for the py2exe.setup function's "data_files" 
    argument.
    """

    if not os.path.isdir(this_dir):
        print "The argument passed is not a directory."
        return []
    
    all_files = [] # list of tuples [(main_dir, [l_o_files]), (sub_dir, files), etc.]
    dir_files = [] # list of files in this_dir
    
    for name in os.listdir(this_dir):
        full_path = this_dir + name
        if os.path.isfile(full_path):
            dir_files.append(full_path)
        elif os.path.isdir(full_path):
            subtree_files = recursive_find_data_files(full_path)
            all_files.extend(subtree_files)
    
    dir_name = os.path.basename(this_dir) # name of current directory
    dir_tuple = (dir_name, dir_files)
    all_files.append(dir_tuple)
    
    return reversed(all_files)

cwd = os.getcwd()
OPTIONS = {'packages': ['fujian', 'abjad', 'lychee', 'shelfex']}

setup(
    console=['nCoda.py'],
    data_files=rec_find_data_files(cwd),
    options={'py2exe': OPTIONS},
    )
