#!/usr/bin/python3
"""
What does the program do:

- import texts
- remove tags (if necessary)
- write to json file

"""
import os
import glob
import re
import json

# file path to data
data_path = os.path.join("..", "data")
fnames = sorted(glob.glob(os.path.join(data_path, "*.txt")))

# result variable
db = dict()
# delete patterns
tag_file = re.compile(r".txt")
# loop over filenames
for fname in fnames:
    # do something to filenames
    # start by opening files for reading
    with open(fname, "r") as fobj:
        # read content
        content = fobj.read()
        # create meaningful and useful name for content
        content_name = tag_file.sub("", os.path.basename(fname))
        # put content in dictionary (our database)
        db[content_name] = content


# export dictionary (our database) as json file
# filename for json file
outname = "fulltext_hca.json"
# where to put json file
target = os.path.join(data_path, outname)
# export dictionary to json file on target path with outname
with open(target, "w") as fobj:
    json.dump(db, fobj)
