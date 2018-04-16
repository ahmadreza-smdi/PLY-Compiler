from copy import deepcopy

class evaluation:
    def __init__(self,ttype,value):
        self.ttype = ttype
        self.value = value


def seprate(character):
    w = ['+','-','\\','**','*']
    a = []
    c = []
    a = list(character)
    for i in range(len(a)):
        if a[i] in w :
            b = 0
            b = a[j:i]

            if a[i] == '+': ttype = 'Plus'
            if a[i] == '-': ttype = 'minus'
            if a[i] == '\\': ttype = 'devide'
            if a[i] == '*': ttype = 'multiple'
            if a[i] == '**': ttype = 'power'
            
            c.append(deepcopy(evaluation(ttype,'0')))
            c.append(deepcopy(evaluation('ID',b)))
            j = i
            return c

c = seprate('123\\125+2')
print (c[2].ttype)
