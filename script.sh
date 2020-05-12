#!/bin/zsh
i=40
while [[ $i -lt 53 ]]
do
    mkdir ex${i}
    cd ex${i}
    touch ex${i}.py
    cd ..
    let 'i=i+1'
done
