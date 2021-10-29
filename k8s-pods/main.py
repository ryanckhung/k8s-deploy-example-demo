import time
import os
import sys

# create ./data folder if not exist
os.system("mkdir -p ./data")

# ENVIRONMENT VARIABLE
# the TEST_TOKEN should be stored in the linux env
# in Linux set the environment variable 
# > export TEST_TOKEN="HELLO WORLD"
print(os.environ.get('TEST_TOKEN'))
cmd = "echo {} >> ./data/env.txt".format(os.environ.get('TEST_TOKEN'))
os.system(cmd)

# COMMAND AND ARGUMENT
if len(sys.argv) != 2:
    print("This command need one text argument")
else:
    while True:
        curTime = int(time.time())
        msg = "{}: {}".format(sys.argv[1],curTime)
        cmd = "echo {} >> ./data/log.txt".format(msg)
        os.system(cmd)
        print(msg)
        time.sleep(10)