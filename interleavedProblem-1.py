testCases = input ("Testcases")
strList = []
for i in testCases:
    strList[i] = input()
    
for i in len(strList):
    
    # check if the IO pattern exists
    if "I" in strList[i] and "O" in strList[i]:
        # check if the equi amt of IO
        if strList[i].count("I") == strList[i].count("O")
            
        