#!/bin/bash
i=0
while read line
do

    name=$(echo $line | cut -d',' -f3)
    budget=$(echo $line | cut -d',' -f4)
    owner_id=$(echo $line | cut -d',' -f6)
    country_id=$(echo $line | cut -d',' -f5)
 

    echo "<record id='discography$i' model='brodoonx.discography'>"
    echo "<field name='name'>$name</field>"
    echo "<field name='budget'>$budget</field>"
    echo "<field name='owner' ref='brodoonx.player$owner_id'></field>"
    echo "<field name='country' ref='brodoonx.country$country_id'></field>"
    echo "</record>"
    i=$((i+1))
done