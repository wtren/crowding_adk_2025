#!/bin/sh

conc_atp="0.1 0.5 2.0 4.0 6.0 10.0 14.0 18.0 24.0 32.0"
for elem in $conc_atp; do
    for i in `seq 40`; do
	if [ -f data-${elem}_${i} ]; then
	    python ../../../scripts/cata_pathway.py -i data-${elem}_${i} -o cata-${elem}_${i}
	else
	    echo "Warn: data-${elem}_${i} does not exist!!!"
	fi
    done
done
