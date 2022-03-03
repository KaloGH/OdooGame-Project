#!/bin/bash
i=000
while read line
do
    
    name=$(echo $line | cut -d';' -f1)
    audience=$(echo $line | cut -d';' -f2)
    echo "<record id='musical_genre$i' model='brodoonx.musical_genre'>"
    echo "<field name='name'>$name</field>"
    echo "<field name='audience'>$audience</field>"
    echo "</record>"
    i=$((i+1))
done