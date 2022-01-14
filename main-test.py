from ast import Assert
from main import Add

def testAdd():
    Assert(Add(2,3)==5)
    print("Function runs perfectly")

if __name__ == '__main__':  
        testAdd() 