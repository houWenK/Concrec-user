#!/bin/sh

if [ -z "${DATASET_PATH}" ]; then
    export DATASET_PATH='../data/anime'
fi

python -m bin.train
