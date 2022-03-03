#!/bin/bash
i=1
while read line
do
    
    m_range=$((22+1))
    f_range=$((38+1))
    name=$(echo $line | cut -d',' -f4)
    artist_genre=$(echo $line | cut -d',' -f5)
    country_id=$(echo $line | cut -d',' -f6)
    song_id=$(echo $line | cut -d',' -f7)
    musical_genre_id=$(echo $line | cut -d',' -f8)
    type_artist=$(echo $line | cut -d',' -f9)
    discography_id=$(echo $line | cut -d',' -f10)
    img_name_male=$(($RANDOM%$m_range))
    img_name_female=$(($RANDOM%$f_range))
    image=""
    artist_age=$(echo $line | cut -d',' -f11)

    if [[ $img_name_male -eq 0 ]]; then
        img_name_male=$(($img_name_male+1))
    fi

    if [[ $img_name_female -eq 0 ]]; then
        img_name_female=$(($img_name_female+1))
    fi

    if [[ $artist_genre = m ]]; then
        image=$(base64 brodoonx/images/artist/male$img_name_male.png)
    else 
        image=$(base64 brodoonx/images/artist/female$img_name_female.png)
    fi

    echo "<record id='artist$i' model='brodoonx.artist'>"
    echo "<field name='name'>$name</field>"
    echo "<field name='genre'>$artist_genre</field>"
    echo "<field name='country' ref='brodoonx.country$country_id'></field>"
    echo "<field name='age'>$artist_age</field>"
    echo "<field name='type_artist'>$type_artist</field>"
    echo "<field name='discography' ref='brodoonx.discography$discography_id'></field>"

    if [[ $type_artist = prod ]]; then
        echo "<field name='musical_genre_as_prod' eval='[(6,0,[ref(\"brodoonx.musical_genre$musical_genre_id\"),ref(\"brodoonx.musical_genre$(($musical_genre_id+1))\")])]'></field>"
    else 
        echo "<field name='musical_genre_as_sing' eval='[(6,0,[ref(\"brodoonx.musical_genre$musical_genre_id\"),ref(\"brodoonx.musical_genre$(($musical_genre_id+1))\")])]'></field>"
    fi
    echo "<field name='image'>$image</field>"
    echo "</record>"
    i=$((i+1))
done