# w is operators
w = ['+','-','\\','**','*']

def seprate(character):
    a = []
    b = []
    a = list(character)
    for i in range(len(a)):
        if a[i] in w :
            b.append("ID")
            b.append(a[i])
        if i == len(a)-1:
            b.append("ID")

    for i in range(len(b)):
        print (b[i])

seprate("1245+525")

'''
output:

ID
+
ID
'''
