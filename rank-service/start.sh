#!/bin/sh

if [ -z "${RECALL_PORT}" ]; then
    export RECALL_PORT=5001
fi
if [ -z "${RANK_PORT}" ]; then
    export RANK_PORT=5002
fi


export RECALL_ENDPOINT="http://localhost:${RECALL_PORT}"

export FLASK_APP=app

flask run -p $RANK_PORT
