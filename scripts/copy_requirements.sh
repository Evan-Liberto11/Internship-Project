#!/bin/bash

# Copy the requirements.txt file to the VS Code Devcontainer
REPO_NAME=ia-labor-rates-redacted
SOURCE_PATH=/code
DEST_PATH=/workspaces/${REPO_NAME}/requirements
REQ_FILE=requirements.txt
cp ${SOURCE_PATH}/${REQ_FILE} ${DEST_PATH}/${REQ_FILE}
