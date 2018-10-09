def testMethod():
    filePath = "C:\KiaMotors\preprod-configs\KME-obj - Copy.conf"
    fileObject = open(filePath, 'r+').read()
    searchtext = "######### Automated Entries Starts Here ##########"
    print("file object is ---- ", fileObject)
    for line in fileObject:
        print("line is ---- ", line)
        if searchtext in line:
            print(line + "----" + searchtext)
            return "match found"
        else:
            return "no match found"
