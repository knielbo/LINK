import glob, os
from natsort import natsorted
from dat_parsers import striprtf, xml2txt

path_dat = os.path.join("..","dat")
subdirs = natsorted(os.listdir(path_dat))
print(subdirs)

# rtf parser
from extract_rtf import striprtf
i = 3
fnames = natsorted(glob.glob(os.path.join(path_dat,subdirs[i],"*.rtf")))
ii = 0
with open(fnames[ii],"r") as f:
    content = f.read()
with open(os.path.basename(fnames[ii])+".txt","w") as f:
    f.write(striprtf(content))

# xml parser
i = 2
fnames = natsorted(glob.glob(os.path.join(path_dat,subdirs[i],"*.xml")))
with open(fnames[ii],"r") as f:
    content = f.read()
xml2txt(fnames[ii],out=os.path.basename(fnames[ii])+".txt")
