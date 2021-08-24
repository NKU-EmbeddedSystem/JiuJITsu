test/benchmarks/csuite/csuite.py -r 1000 sunspider baseline baseline_d8/x64.release/d8
test/benchmarks/csuite/csuite.py -r 1000 sunspider compare random_d8/x64.release/d8 >> sunspider.txt
test/benchmarks/csuite/csuite.py -r 1000 kraken baseline baseline_d8/x64.release/d8
test/benchmarks/csuite/csuite.py -r 1000 kraken compare random_d8/x64.release/d8 >> kraken.txt
