import psutil,sys

def DisplayProcessInfo(proc):
    pid = proc.info['pid']
    name = proc.info['name']
    username = proc.info['username']
    print(f"PID: {pid} \tUsername: {username} \tName: {name}")
    

def main():
    if (len(sys.argv)>2):
        print("Error: Invalid number of arguments")
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            if (len(sys.argv)>1):
                if (proc.info['name'] == sys.argv[1]):
                    DisplayProcessInfo(proc)
            else:
                DisplayProcessInfo(proc)
        except:
            pass

if (__name__=="__main__"):
    main()