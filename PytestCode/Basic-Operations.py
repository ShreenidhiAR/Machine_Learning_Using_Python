##Using basic Operations
#File Reading
#use pytest -rs Basic-Operations.py 
import os
import time
def test_read_file_p0():
    file=open(os.getcwd()+"/test.csv")
    print("i am printing this")
    type(file)

def test_time_related_p0():
    print(time.time())
    print("TIME IS "+time.asctime())
