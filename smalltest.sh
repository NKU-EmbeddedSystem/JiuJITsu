#!/bin/bash
# test/benchmarks/csuite/csuite.py -r 10 sunspider baseline baseline/d8
test/benchmarks/csuite/csuite.py -r 3 sunspider compare ./out/x64.release/d8 > sunspider.txt
