#!/bin/sh

if [ -z "${DATASET_PATH}" ]; then
    export DATASET_PATH='../data/anime'
fi

export FLASK_APP=app

flask run -p 5001