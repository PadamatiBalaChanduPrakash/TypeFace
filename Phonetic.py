def Phonetic(string):
    s= string.upper()
    ph = ""
    ph += s[0]
    stand_Phonetics = {"BFPV": "1", "CGJKQSXZ":"2", "DT":"3", "L":"4", "MN":"5", "R":"6", "AEIOUHWY":"."}

    for i in s[1:]:
        for j in stand_Phonetics.keys():
            if i in j:
                c = stand_Phonetics[j]
                if c != ph[-1]:
                    ph+= c
    ph = ph.replace(".", "")

    ph = ph[:4].ljust(4, "0")
        
    return ph


str1=str(input())
str2=list(map(str,input().split()))
match=[]
for i in str2:
    if Phonetic(str(i))==Phonetic(str1):
        match.append(i)
for str in match:
    print(str+" ")
