#!bin/bash

if [ -d "../scripts" ]
then
    cd ..
fi

if [ -d "../tools" ]
then
    cd ..
fi

if [ ! -d "./build" ]
then
    mkdir build
fi
cd build
cmake ..
cmake --build .

ctest -VV
