# Implement a function which convert the given boolean value into its string representation.

# Note: Only valid inputs will be given.

#Parameters are if im not given bool(True or False) then return not bool
#Result return the stringified value of boolean
#Example if True as argument "True"
# 2) if False as argument then return "False"

#PseudoCode 


def convertBoolTOStr(bool):
    #1) Take bool & check edge cases 
    if (str(bool)!="True" and str(bool)!="False"):
        return "not bool"
    else:
    # 2) if bool then use str(bool) & return it
        return str(bool)
test1 = convertBoolTOStr(True)
test2 = convertBoolTOStr("true")
test3 = convertBoolTOStr("hjk")
test4 = convertBoolTOStr(False)

print(test1)
print(test2)
print(test3)
print(test4)

#Learnt
# 1) str method to convert bool, num to String 
# 2) Always Use TestCases & consider edgecases 
# 3) Python has True False not true false keywords
# 4) Use Capitalize method by chatgpt
# 5) Use if for lower probability & leave else for all other i did reverse

#Mistakes
# 1) lower doesnt work on bool
