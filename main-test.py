from ast import Assert
from main import Add

def testAdd():
    assert Add(5,5)==10 
    print("Function runs perfectly")

if __name__ == '__main__':  
        testAdd() 