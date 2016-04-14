#!/usr/bin/bash
usage ()
{ # This is about as simple as functions get.
    echo ""
    echo "usage instruction:"
    echo "sh runtest23.sh -h help message 
                -l enter fusion #
                -u upgrade
                -f print file
                -c configure    -m command  via cmd    (please use \" \" if more than one) N/A 
                                -f file     via file   (please use \" \" if more than one) 
                                -g log      via file and log the file 
                -s show         -m command  via cmd    (please use \" \" if more than one) N/A
                                -f file     via file   (please use \" \" if more than one)
                                -g log      via file and log the file 
                -a analyze      -d | --show_run               check show run  
                                -c | --show_cast              check cast 
                                -r | --show_rate              check rate
                                -f | --show_sfm_link_fe       check sfm fe reachebility
                                -s | --show_sfm_sta           check inout cell, drop cell
                                -e | --show_sfm_link_crc      check sfm linke crc
                -i iteration    -p | --powercycle   -l|--lc  #iteration
                                                    -s|--sfm #iteration
                                -t portflap #iteration   
                -k teamtrack    -l teamtrack login            default page 
                                                    -s        subimit new defect
                                                    -t        track defect 
                -r rqm          -l rqm login #Owner's name      
                ?  help message"
                
            
}

da () 
{ #this is downarrow
    echo '-----------------------------------------'
    echo "content of $1"
    echo '       ||
      \  /
       \/'
    cat $1                 
    echo '-----------------------------------------'
    echo ""
}

#main 
while [ "$1" != "" ]; do
    case $1 in
        -l | --login )          shift 
                                echo "log in to fusion"
                                until expect telnet_lib/fusion_telnet_interact.exp; do sleep 10; done
                                exit
                                ;;
        -u | --upgrade )        shift 
                                echo "upgrade fusion software version"
                                expect telnet_lib/fusion23_upgrade.exp 10.20.98.200
                                exit
                                ;;
        -f | --file )           shift 
			        if [ -n "$1" ]; then
                                    for str in $1; do
                                            if [ -f $str ]; then
                                                da $str
                                            else
                                                read -p "are you sure you want to see all files under folder $str (y/n)?" choice
                                                case "$choice" in 
                                                      y|Y ) echo "yes"
                                                            for i in $str/*; do
                                                                if [ -f $i ]; then
                                                                    da $i
                                                                fi
                                                            done
                                                            ;;
                                                      n|N ) echo "no";;
                                                      * ) echo "invalid";;
                                                esac
                                            fi
                                        done
				else
	                    		echo 'no file selected to print\n' >&2
				fi
				;;
        -c | --configure )      shift
                                case $1 in 
                                    -f | --file )           shift
                                                            if [[ $1 == cfg* ]]; then
                                                                echo "fusion is displaying: $1"
                                                                expect telnet_lib/fusion23.exp 10.20.98.200 "$1"
                                                                exit 0 
                                                            else
                                                                exit 1
                                                            fi
                                                            ;;
                                    -g | --log )            shift
                                                            f=log/$2_`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                            expect telnet_lib/fusion23.exp 10.20.98.200 "$1" | tee $f
                                                            exit
                                                            ;;
                                    -m | --command )        shift
                                                            echo "configure cmd mode"
                                                            echo $1
                                                            ;;
                                esac
                                ;;
        -s | --show )           shift
                                case $1 in 
                                    -f | --file )           shift
                                                            if [[ $1 == show* ]]; then
                                                                echo "fusion is displaying: $1"
                                                                expect telnet_lib/fusion23.exp 10.20.98.200 "$1"
                                                                exit 0 
                                                            else
                                                                exit 1
                                                            fi
                                                            ;;
                                    -g | --log )            shift
                                                            f=log/$2_`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                            expect telnet_lib/fusion23.exp 10.20.98.200 "$1" | tee $f
                                                            exit
                                                            ;;
                                    -m | --command )        shift
                                                            echo "show cmd mode"
                                                            echo $1
                                                            ;;
                                esac
                                ;;
        -h | ? | --help )     usage
                                ;;
        -a | --analyze )        shift
                                case $1 in 
                                    -d | --show_run )       shift
                                                            echo "printing the difference from default show run file"
                                                            python analyze/cmp_run.py
                                                            ;;
                                    -c | --show_cast )      shift
                                                            echo "printing cast that does not equal to zero"
                                                            f=`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                            if expect telnet_lib/fusion23.exp 10.20.98.200 show/show_cast_slot_all > log/analyze_$f ; then
                                                                python analyze/analyze.py log/analyze_$f 'MMVM#' | tee log/analyze2_$f
                                                            else
                                                                "logging failed, no log to analyze"
                                                            fi
                                                            ;;
                                    -r | --show_rate )      shift
                                                            echo "printing rate that does not equal to zero"
                                                            f=`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                            if expect telnet_lib/fusion23.exp 10.20.98.200 show/show_rate_slot_all > log/analyze_$f ; then
                                                                python analyze/analyze.py log/analyze_$f 'MMVM#' | tee log/analyze2_$f
                                                            else
                                                                "logging failed, no log to analyze"
                                                            fi
                                                            ;;
                                    -f | --show_sfm_link_conn )
                                                            shift
                                                            echo "printing sfm link to check fe connected"
                                                            f=`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                            if expect telnet_lib/fusion23.exp 10.20.98.200 show/show_sfm_link_conn > log/analyze_$f ; then
                                                                python analyze/analyze.py log/analyze_$f 'MMVM#' | tee log/analyze2_$f
                                                            else
                                                                "logging failed, no log to analyze"
                                                            fi
                                                            ;;
                                    -s | --show_sfm_sta )
                                                            shift
                                                            echo "printing sfm sta to check cells counter"
                                                            f=`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                            if expect telnet_lib/fusion23.exp 10.20.98.200 show/show_sfm_sta > log/analyze_$f ; then
                                                                python analyze/analyze.py log/analyze_$f 'MMVM#' | tee log/analyze2_$f
                                                            else
                                                                "logging failed, no log to analyze"
                                                            fi
                                                            ;;
                                    -e | --show_sfm_link_crc )
                                                            shift
                                                            echo "printing sfm to check crc error"
                                                            f=`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                            if expect telnet_lib/fusion23.exp 10.20.98.200 show/show_sfm_link > log/analyze_$f ; then
                                                                python analyze/analyze.py log/analyze_$f 'MMVM#' | tee log/analyze2_$f
                                                            else
                                                                "logging failed, no log to analyze"
                                                            fi
                                                            ;;
                                esac
                                ;;
        -i | --iteration )      shift
                                case $1 in 
                                -p | --powercycle )         shift
                                                            case $1 in 
                                                                -l | --linecard )       shift
                                                                                        echo "power cycle lc"
                                                                                        r1="show/show_rate_slot_all show/show_cast_slot_all"
                                                                                        sh iteration/test_lc_one_power_cycle.sh "$r1" $1 | tee log/plc_`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                                                        ;;
                                                                -s | --sfmcard )        shift
                                                                                        echo "power cycle sfm"
                                                                                        r2="show/show_rate_slot_all show/show_cast_slot_all"
                                                                                        sh iteration/test_sfm_one_power_cycle.sh "$r2" $1 | tee log/psfm_`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                                                        ;;
                                                                -c | --lc_sfm )         shift
                                                                                        echo "power cycle both lc and sfm"
                                                                                        r1="show/show_rate_slot_all show/show_cast_slot_all"
                                                                                        sh iteration/test_lc_one_power_cycle.sh "$r1" $1 | tee log/plc_`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                                                        r2="show/show_rate_slot_all show/show_cast_slot_all"
                                                                                        sh iteration/test_sfm_one_power_cycle.sh "$r2" $1 | tee log/psfm_`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                                                        ;;
                                -t | --portflap )           shift 
                                                            sh iteration/test_port_flap.sh $1 | tee log/port_flap_`date "+%b_%d_%Y_%H.%M.%S"`.log
                                                            ;;
                                                            esac
                                                            ;;
                                esac
                                ;;
        -k | --teamtrack )      shift
                                case $1 in 
                                    -l | --login )          shift
                                                            echo "go to teamtrack default page"
                                                            python ticket/teamtrack_login.py
                                                            ;;
                                    -s | --submit )         shift
                                                            echo "go to submit"
                                                            python ticket/teamtrack_submit.py
                                                            ;;
                                    -t | --defec_tracking ) shift
                                                            echo "go to defect tracking"
                                                            python ticket/teamtrack_track.py
                                                            ;;
                                esac
                                ;;
        -r | --rqm )            shift
                                case $1 in 
                                    -l | --login )          shift
                                                            echo "go to rqm for testing"
                                                            python rqm/rqm.py "$1"
                                                            ;;
                                esac
                                ;;

        -- )                    # End of all options.
                                shift
                                break
                                ;;

        * )                     #check the usage
                                exit 1
    esac
    shift
done

