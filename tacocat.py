########Palindrome Checker########

def ObtainInput():
    TestPhrase = input("Please Enter Your Test Word/Phrase: ")
    return TestPhrase

def ConvertInput(TestPhrase):
    TestArray = TestPhrase.lower()
    TestArray = TestArray.replace(" ", "")
    TestList = list(TestArray)
    return TestList

def TestInput(TestList):
    TestRuns = 0
    for Letters in TestList:
#       print(Letters)
#       print(TestList[len(TestList) - (TestRuns + 1)])
#       print(TestRuns)
        if Letters != TestList[len(TestList) - (TestRuns + 1)]:
            Success = False
            break
        if Letters == TestList[len(TestList) - (TestRuns + 1)]:
            TestRuns += 1
            if len(TestList) - TestRuns > TestRuns:
                pass
            else:
                Success = True
        continue
    return Success  

def DisplayResult(Success, TestPhrase):
    if Success == True:
        print(TestPhrase,"is indeed a Palindrome.")
    if Success == False:
        print(TestPhrase,"is NOT a Palindrome.")

def RunCode():
    TestPhrase = ObtainInput()
    TestList = ConvertInput(TestPhrase)
    Success = TestInput(TestList)
    DisplayResult(Success, TestPhrase)

    
##############################################################################################

RunCode()