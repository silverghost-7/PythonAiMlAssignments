import smtplib,sys,os,hashlib,datetime,schedule,time
from email.message import EmailMessage

logFileName = None
ScanStartTime = None
ScanEndTime = None
CntFilesScanned = 0
CntDuplicatesFound = 0
CntDuplicatesDeleted = 0


def send_notification(subject, body, to_email):
    # Define your configuration variables
    sender_email = "emptymindd99@gmail.com"
    app_password = "kshr bmxk xtds ciqz"  # Spaces are ignored automatically
    
    # Structure the email data
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = sender_email
    msg['To'] = to_email
    msg.set_content(body)
    with open(logFileName, 'rb') as f:
        msg.add_attachment(
            f.read(),
            maintype="text",
            subtype="plain",
            filename=os.path.basename(logFileName)
        )
    try:
        # Establish connection with Gmail's SMTP server
        with smtplib.SMTP('smtp.gmail.com', 587) as server:
            server.starttls()  # Secure the traffic connection with TLS encryption
            server.login(sender_email, app_password)
            server.send_message(msg)
            print("Notification sent successfully!")
            
    except Exception as e:
        print(f"Failed to send email. Error: {e}")

def CalculateChecksum(filePath):
    fObj = open(filePath,"rb")
    hObj = hashlib.md5()
    buffer = fObj.read(1024)
    while(len(buffer) > 0):
        hObj.update(buffer)
        buffer = fObj.read(1024)
    chkSum = hObj.hexdigest()
    return chkSum

def RemoveDuplicateFiles(dirPath):
    global logFileName
    global ScanStartTime, ScanEndTime, CntDuplicatesDeleted, CntDuplicatesFound, CntFilesScanned
    ScanStartTime = datetime.datetime.now().replace(microsecond=0)
    timeNow = datetime.datetime.now()
    logFileName = "DuplicateRemovalLog_"+str(timeNow.replace(microsecond=0).strftime("%d_%m_%Y_%H_%M_%S")+".log")
    fLogObj = open(logFileName,"a")
    fLogObj.write("Directory: "+dirPath+"\n")
    fLogObj.write("Scan started: "+str(timeNow)+"\n")
    DeletedFiles = dict()
    Errors = list()
    if (not os.path.exists(sys.argv[1]) or not os.path.isdir(sys.argv[1])):
        fLogObj.write("Error: Invalid directory path\n")
        return
    ChecksumList = list()
    for FolderName,SubFolders,FileNames in os.walk(dirPath):
        for fName in FileNames:
            filePath = os.path.join(FolderName,fName)
            CntFilesScanned = CntFilesScanned + 1
            chkSum = CalculateChecksum(filePath)
            if (chkSum in ChecksumList):
                CntDuplicatesFound = CntDuplicatesFound + 1
                try:
                    os.remove(filePath)
                    CntDuplicatesDeleted = CntDuplicatesDeleted + 1
                    DeletedFiles[filePath] = chkSum
                except:
                    Errors.append("Error deleting file: "+filePath)
            else:
                ChecksumList.append(chkSum)
    ScanEndTime = datetime.datetime.now().replace(microsecond=0)
    fLogObj.write("Scan complete: "+str(datetime.datetime.now())+"\n")
    fLogObj.write("Total number of files scanned: "+str(CntFilesScanned)+"\n")
    fLogObj.write("Total number of duplicate files found: "+str(CntDuplicatesFound)+"\n")
    fLogObj.write("Total number of duplicate files deleted: "+str(CntDuplicatesDeleted)+"\n")
    fLogObj.write("Deleted files: \n")
    for key,value in DeletedFiles.items():
        fLogObj.write(key+" : "+value+"\n")
    fLogObj.write("Error: \n")
    for error in Errors:
        fLogObj.write(error+"\n")
    fLogObj.close()

    send_notification(
        subject="System Alert: Task Completed",
        body=GetEmailBody(sys.argv[1]),
        to_email=sys.argv[3]
    )


def GetEmailBody(dirPath):
    global ScanStartTime, ScanEndTime, CntDuplicatesDeleted, CntDuplicatesFound, CntFilesScanned
    mailBody = ("Jay Ganesh,\n\n")
    mailBody = mailBody + ("The duplicate file removal operation has been completed successfully.\n\n")
    mailBody = mailBody + ("Operation Statistics:\n")
    mailBody = mailBody + ("Starting time of scanning: "+str(ScanStartTime)+"\n")
    mailBody = mailBody + ("Total number of files scanned: "+str(CntFilesScanned)+"\n")
    mailBody = mailBody + ("Total number of duplicate files found: "+str(CntDuplicatesFound)+"\n")
    mailBody = mailBody + ("Total number of duplicate files deleted: "+str(CntDuplicatesDeleted)+"\n")
    mailBody = mailBody + ("Completion time of scanning: "+str(ScanEndTime)+"\n")
    mailBody = mailBody + ("Name of scanned directory: "+dirPath+"\n\n")
    mailBody = mailBody + ("Please find the detailed log file attached to this email.\n\n")
    mailBody = mailBody + ("Regards,\n")
    mailBody = mailBody + ("Marvellous Automation System")
    return mailBody


def main():
    if (len(sys.argv) != 4):
        print("Error: Incorrect number of arguments")
        return
    elif (not os.path.exists(sys.argv[1]) or not os.path.isdir(sys.argv[1])):
        print("Error: Invalid directory path")
    elif (int(sys.argv[2])<=0):
        print("Error: Enter valid time interval(in minutes)")
    elif (sys.argv[3]==""):
        print("Error: Enter valid email address")
    elif(sys.argv[1]=="-u" or sys.argv[1]=="--usage" or sys.argv[1]=="-U"):
        print("Usage:")
        print("python DuplicateFileRemoval.py <Directory to scan> <Interval in minutes> <Receiver email>")
    elif(sys.argv[1]=="-h" or sys.argv[1]=="--help" or sys.argv[1]=="-H"):
        print("Duplicate file removal job\n")
        print("This script will scan the given directory and identify duplicates based on checksums.")
        print("After scanning, the duplicate files will be deleted.  The status of the job will available in the log file.")
        print("The log file will also be mailed to the intended recipient.")
    else:
        schedule.every(int(sys.argv[2])).minutes.do(RemoveDuplicateFiles, sys.argv[1])
        while(True):
            schedule.run_pending()
            time.sleep(10)

# Example execution trigger
if __name__ == "__main__":
    main()