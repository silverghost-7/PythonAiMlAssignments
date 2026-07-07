import threading

def Even():
    for i in range(1,11):
        print(f"Even:{i*2}\n",end="")

def Odd():
    for i in range(0,10):
        print(f"Odd:{(i*2)+1}\n",end="")

def main():
    t1 = threading.Thread(target=Even,name="Even")
    t2 = threading.Thread(target=Odd,name="Odd")

    t1.start()
    t2.start()

if (__name__=="__main__"):
    main()