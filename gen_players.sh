#!/bin/bash
i=0
while read line
do

    name=$(echo $line | cut -d',' -f3)
    user_email=$(echo $line | cut -d',' -f4)
    user_password=$(echo $line | cut -d',' -f5)
    isPremium=$(echo $line | cut -d',' -f6)

    echo "<record id='player$i' model='brodoonx.player'>"
    echo "<field name='name'>$name</field>"
    echo "<field name='user_email'>$user_email</field>"
    echo "<field name='user_password'>$user_password</field>"
    echo "<field name='isPremium'>$isPremium</field>"
    echo "</record>"
    i=$((i+1))
done