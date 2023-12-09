import pya
from pya import *
import SiEPIC
from SiEPIC.verification import layout_check
from SiEPIC.scripts import zoom_out
from SiEPIC.utils import get_technology_by_name
import siepic_ebeam_pdk
import os
import sys
"""
Script to load .gds file passed in through commmand line and run verification using layout_check().
Ouput lyrdb file is saved to path specified by 'file_lyrdb' variable in the script.

Jasmina Brar 12/08/23

"""

# gds file to run verification on
gds_file = sys.argv[1]

# load into layout
layout = pya.Layout()
layout.read(gds_file)

# get top cell from layout
top_cell = layout.top_cell()


# set layout technology because the technology seems to be empty, and we cannot load the technology using TECHNOLOGY = get_technology() because this isn't GUI mode
# refer to line 103 in layout_check()
# tech = layout.technology()
# print("Tech:", tech.name)
layout.TECHNOLOGY = get_technology_by_name('EBeam')


# run verification
zoom_out(top_cell)

# get file path, filename, path for output lyrdb file
path = os.path.dirname(os.path.realpath(__file__))
filename = gds_file.split(".")[0]
file_lyrdb = os.path.join(path,filename+'.lyrdb')

# run verification
num_errors = layout_check(cell = top_cell, verbose=True, GUI=True, file_rdb=file_lyrdb)

# Print the result value to standard output
print(num_errors)

