#!/bin/bash
i=0
while read line
do
    name=$(echo $line | cut -d',' -f3)
    duration=$(echo $line | cut -d',' -f4)
    views=$(echo $line | cut -d',' -f5)
    declare -i musical_genre_id=$(echo $line | cut -d',' -f6)
    discography_id=$(echo $line | cut -d',' -f7)
    singer_id=$(echo $line | cut -d',' -f8)
    producers_id=$(echo $line | cut -d',' -f9)
    singer2_id=$(echo $line | cut -d',' -f10)
    remix=$(echo $line | cut -d',' -f11)
    musical_genre2_id=$((musical_genre_id+1))

    


    echo "<record id='song$i' model='brodoonx.song'>"
    echo "<field name='name'>$name</field>"
    echo "<field name='duration'>$duration</field>"
    echo "<field name='views'>$views</field>"
    echo "<field name='musical_genre' eval='[(6,0,[ref(\"brodoonx.musical_genre$musical_genre_id\"),ref(\"brodoonx.musical_genre$musical_genre2_id\")])]'></field>"
    echo "<field name='discography' ref='brodoonx.discography$discography_id'></field>"
    echo "<field name='producers' eval='[(6,0,[ref(\"brodoonx.artist$producers_id\")])]'></field>"
    if [[ $remix -eq 1 ]]; then
        echo "<field name='singers' eval='[(6,0,[ref(\"brodoonx.artist$singer_id\"),ref(\"brodoonx.artist$singer2_id\")])]'></field>"
    else 
        echo "<field name='singers' eval='[(6,0,[ref(\"brodoonx.artist$singer_id\")])]'></field>"
    fi
    echo "</record>"
    i=$((i+1))
done