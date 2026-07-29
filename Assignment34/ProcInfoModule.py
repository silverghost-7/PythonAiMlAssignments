import psutil

def LogProcessInfo(proc):
    pid = proc.info['pid']
    name = proc.info['name']
    username = proc.info['username']
    info ="PID: "+str(pid)+"\tUsername: "+str(username)+"\tName: "+str(name)
    return info

def GetProcInfo():
    ProcInfoList = list()
    for proc in psutil.process_iter(attrs=['pid', 'name', 'username']):
        try:
            info = LogProcessInfo(proc)
            ProcInfoList.append(info)
        except ex:
            print(ex)
    return ProcInfoList