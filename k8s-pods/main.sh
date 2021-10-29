#!/bin/bash
export TEST_TOKEN="token-token-token"
> "./data/log.txt"
source "./venv/bin/activate"
python main.py "hello world"
