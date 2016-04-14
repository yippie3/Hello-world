f=analyze/run_config_verbose
expect telnet_lib/fusion23.exp 10.20.98.200 show/show_run > $f 
echo ""
if grep "refused" $f
then 
    rm $f
else
    grep --color "Error" $f
fi


