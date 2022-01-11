
class Stack:
    def __init__(self):
        self.values=list()
    def push(self,element):
        self.values.append(element)   
    def isempty(self):
        return len(self.values)==0
    def pop(self):
        if(not(self.isempty())):
            return self.values.pop()
        else:
            print('Stack Underflow') 
            return None
    def top(self):
        if(not(self.isempty())):
            return self.values[-1]
        else:
            print('Stack Empyty')
            return None
    def size(self):
        return len(self.values)
    def __str__(self):
        stringRepr=''
        for i in reversed(self.values):
            stringRepr += str(i) +'\t'
        return stringRepr
