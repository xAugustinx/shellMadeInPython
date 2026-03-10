#!/bin/sh

mkdir /usr/local/share/shellMIP/
cp main.py /usr/local/share/shellMIP/

gcc main.c -o shellMIP
mv shellMIP /usr/bin/