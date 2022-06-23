#!/bin/bash

for f in ./source/*; do
    base=`basename $f .json` 
    jsonld format -q $f >  ./sink/$base.nq
done
