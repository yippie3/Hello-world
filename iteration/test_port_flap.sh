#!/usr/bin/bash
for i in `seq 1 $1`;
do
        echo "this is the iteration $i"
        START=$(date +%s)
        echo "disabling"
        f=log/"$i"_port_flap_slot_`date "+%b_%d_%Y_%H.%M.%S"`.log
        expect telnet_lib/fusion23.exp 10.20.98.200 cfg/disble_port_slot.cfg | tee $f     
        expect telnet_lib/fusion23.exp 10.20.98.200 "show/show_ip_int_b show/show_rate_slot_all show/show_cast_slot_all" | tee -a $f
        
        
        echo "enabling"
        expect telnet_lib/fusion23.exp 10.20.98.200 cfg/enable_port_slot.cfg | tee -a $f     
        expect telnet_lib/fusion23.exp 10.20.98.200 "show/show_ip_int_b show/show_rate_slot_all show/show_cast_slot_all" | tee -a $f

        sleep 5
        
        END=$(date +%s)
        DIFF=$(( $END - $START ))
        echo "It took $DIFF seconds for iteration $i"
done
