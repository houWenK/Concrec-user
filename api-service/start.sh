#!/bin/sh

if [ -z "${RANK_PORT}" ]; then
    export RANK_PORT=5002
fi
if [ -z "${RECALL_PORT}" ]; then
    export RECALL_PORT=5001
fi
if [ -z "${API_PORT}" ]; then
    export API_PORT=5003
fi
if [ -z "${DATASET_PATH}" ]; then
    export DATASET_PATH='../data/anime'
fi
if [ -z "${RANK_ENDPOINT}" ]; then
  export RANK_ENDPOINT="http://localhost:${RANK_PORT}"
fi
if [ -z "${RECALL_ENDPOINT}" ]; then
  export RECALL_ENDPOINT="http://localhost:${RECALL_PORT}"
fi


export FLASK_APP=app

flask run -p $API_PORT
