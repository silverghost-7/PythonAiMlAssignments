import psutil,sys,os,datetime,ProcInfoModule,EmailUtil

def GetEmailBody():
    global ScanStartTime, ScanEndTime, CntDuplicatesDeleted, CntDuplicatesFound, CntFilesScanned
    mailBody = ("Jay Ganesh,\n\n")
    mailBody = mailBody + ("PFA list of processing running.\n\n")
    mailBody = mailBody + ("Regards,\n")
    mailBody = mailBody + ("Marvellous Automation System")
    return mailBody

def main():
    if (len(sys.argv) > 3):
        print("Error: Invalid number of arguments")
        return
    elif (len(sys.argv)==2 and not os.path.exists(sys.argv[1]) or not os.path.isdir(sys.argv[1])):
        os.mkdir(sys.argv[1])
    logFileName = sys.argv[1]+"/LogProcInfo.log"
    fLogObj = open(logFileName,"a")
    fLogObj.write("Processes running at "+str(datetime.datetime.now().replace(microsecond=0))+"\n")
    for procInfo in ProcInfoModule.GetProcInfo():
        fLogObj.write(procInfo+"\n")
    fLogObj.write("\n\n")
    fLogObj.close()
    if (len(sys.argv)==3):
        subject = "System Notification : Running processes"
        EmailUtil.send_notification(subject,GetEmailBody(),sys.argv[2],logFileName)

if (__name__=="__main__"):
    main()