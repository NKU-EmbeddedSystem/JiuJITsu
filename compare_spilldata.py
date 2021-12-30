#!/usr/bin/env python
# coding=utf-8
import os
spill_baseline=[]
spill_restricted=[]
for _, _, files in os.walk("/home/jz/v8-new/v8/spilldata_baseline/sunspider"):
    for file in files:
        count=0
        with open('/home/jz/v8-new/v8/spilldata_baseline/sunspider/'+file,'r') as f:
            lines=f.readlines()
            for line in lines:
                if 'spill count' in line:
                    count=count + int(line.split(':')[1].strip())
            spill_baseline.append(count)

for _, _, files in os.walk("/home/jz/v8-new/v8/spilldata_restricted/sunspider"):
    for file in files:
        count=0
        with open('/home/jz/v8-new/v8/spilldata_restricted/sunspider/'+file,'r') as f:
            lines=f.readlines()
            for line in lines:
                if 'spill count' in line:
                    count=count + int(line.split(':')[1].strip())
            spill_restricted.append(count)

import numpy as np
print('sunspider baseline mean spill:'+str(np.mean(spill_baseline)))
print('sunspider restricted mean spill:'+str(np.mean(spill_restricted)))

spill_baseline=[]
spill_restricted=[]
for _, _, files in os.walk("/home/jz/v8-new/v8/spilldata_baseline/kraken"):
    for file in files:
        count=0
        with open('/home/jz/v8-new/v8/spilldata_baseline/kraken/'+file,'r') as f:
            lines=f.readlines()
            for line in lines:
                if 'spill count' in line:
                    count=count + int(line.split(':')[1].strip())
            spill_baseline.append(count)

for _, _, files in os.walk("/home/jz/v8-new/v8/spilldata_restricted/kraken"):
    for file in files:
        count=0
        with open('/home/jz/v8-new/v8/spilldata_restricted/kraken/'+file,'r') as f:
            lines=f.readlines()
            for line in lines:
                if 'spill count' in line:
                    count=count + int(line.split(':')[1].strip())
            spill_restricted.append(count)


import numpy as np
print('kraken baseline mean spill:'+str(np.mean(spill_baseline)))
print('kraken restricted mean spill:'+str(np.mean(spill_restricted)))

