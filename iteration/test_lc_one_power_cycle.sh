#!/usr/bin/bash
array=( 1 3 7 )
echo "total iteration: $2 for linecard 1 3 7"
for i in `seq 1 $2`;
do
        echo "this is the iteration $i"
        START=$(date +%s)
        for LC in "${array[@]}"
        do
                echo "line card power cycle for $LC"
                f=log/"$i"_lc"$LC"_power_cycle_`date "+%b_%d_%Y_%H.%M.%S"`.log
                expect telnet_lib/fusion23_lc_power_cycle.exp 10.20.98.200 "$1" $LC | tee $f
                sleep 10
        done
        sleep 5
        END=$(date +%s)
        DIFF=$(( $END - $START ))
        echo "It took $DIFF seconds for iteration $i"
done

