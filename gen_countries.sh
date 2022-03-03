#!/bin/bash
i=000
while read line
do
    
    name=$(echo $line | cut -d',' -f1)
    population=$(echo $line | cut -d',' -f2)
    echo "<record id='country$i' model='brodoonx.country'>"
    echo "<field name='name'>$name</field>"
    echo "<field name='population'>$population</field>"
    echo "</record>"
    i=$((i+1))
done