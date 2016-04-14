#!/usr/bin/bash
array=( 2 3 4 5 )
echo "total iteration $2 for sfmcard 2 3 4 5"
for i in `seq 1 $2`;
do
        echo "this is the iteration $i"
        START=$(date +%s)
        for LC in "${array[@]}"
        do
                echo "sfm card power cycle for $LC"
                f=log/"$i"_sfm"$LC"_power_cycle_`date "+%b_%d_%Y_%H.%M.%S"`.log
                expect telnet_lib/fusion23_sfm_power_cycle.exp 10.20.98.200 "$1" $LC | tee $f
                sleep 10
        done
        sleep 5
        END=$(date +%s)
        DIFF=$(( $END - $START ))
        echo "It took $DIFF seconds for iteration $i"
done

