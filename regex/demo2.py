import re

ON="((((s3.5|s7.4)&(!s4.7))|((s7.4|s4.6)&(s4.5))&(s4.1)&(s4.10))|(kus))&(s3.2)"
ON1="((((s3.5|s7.4)&(!s4.7))|((s7.4|s4.6)&(s4.5))&(s4.1)&(s4.10))|(kus)"
ON2="(((s3.5|s7.4)&(!s4.7))|((s7.4|s4.6)&(s4.5))&(s4.1)&(s4.10)"
ON3="((s3.5|s7.4)&(!s4.7))|((s7.4|s4.6)&(s4.5))&(s4.1)"
ON4="((s3.5|s7.4)&(!s4.7))|((s7.4|s4.6)&(s4.5)"
ON5="((s3.5|s7.4)&(!s4.7))|(s7.4|s4.6)"
ON6="(s3.5|s7.4)&(!s4.7)"
def pipei_function(str):
    pattern="[(](.*)[)][&|\|][(](.*)[)]"
    matchobj = re.search(pattern, str)
    print(matchobj[1])
    print(matchobj[2])

pipei_function(ON)
pipei_function(ON1)
pipei_function(ON2)
pipei_function(ON3)
pipei_function(ON4)
pipei_function(ON5)
pipei_function(ON6)