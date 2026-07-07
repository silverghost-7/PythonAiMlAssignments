import threading
from functools import reduce

def Small(Str):
    Count = 0
    for chr in Str:
        if chr.islower():
            Count = Count + 1
    print(f"Thread id: {threading.get_ident()}  Thread name: {threading.current_thread().name}  Lowercase characters: {Count}")

def Capital(Str):
    Count = 0
    for chr in Str:
        if chr.isupper():
            Count = Count + 1
    print(f"Thread id: {threading.get_ident()}  Thread name: {threading.current_thread().name}  Capital characters: {Count}")

def Digits(Str):
    Count = 0
    for chr in Str:
        if chr.isdigit():
            Count = Count + 1
    print(f"Thread id: {threading.get_ident()}  Thread name: {threading.current_thread().name}  Digits: {Count}")

def main():
    Txt = input("Enter text:")
    t1 = threading.Thread(target=Small,name="Small",args=(Txt,))
    t2 = threading.Thread(target=Capital,name="Capital",args=(Txt,))
    t3 = threading.Thread(target=Digits,name="Digits",args=(Txt,))

    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

    print("Exit from main")

if (__name__=="__main__"):
    main()