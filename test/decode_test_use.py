
#this line just executes the code in the file test_file.py
f = "test_file.py";import secure_python.secure_python as spy;m = spy.lm(f);dc = spy.dfts(f, m);exec(dc)

import os; import time
os.remove("test_file.py")  # delete the file
time.sleep(3)

# this line saves the encrypted code to a file again
spy.df(f)