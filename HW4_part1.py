# Jhenna-Rae Foronda-Caldetera, 11423409
# Unix/Linux Environment 
# HW 4 - Python Postscript Interpreter Part 1

import re
# global variables
opStack = []
dictStack = []

# ---------- operand stack ---------- #

# pop value from opStack
def opPop():
    if len(opStack) > 0:
        x = opStack[len(opStack) - 1]
        opStack.pop(len(opStack) - 1)
        return x
    else:
        print("Error opPop() - opStack is empty")

# push value to opStack
def opPush(value):
    opStack.append(value)


# ---------- dictionary stack ---------- #

# pop value from dictStack
def dictPop():
    if len(dictStack) > 0: 
        dictStack.pop(len(dictStack) - 1)
    else:
        print("Error dictpop() - dictStack is empty")

# pop the empty dictionary off the operand stack
# push it on the dictStack
def dictPush():
    tempDict = opPop()
    if isinstance(tempDict,dict):
        dictStack.append(tempDict)
    else:
        opPush(tempDict)
        print("Error dictPush() - Expecting a dictionary on the top of the operand stack")

# add variable definition to top of stack
# add new dictionary if  stack is empty
def define(name, value):
    if len(dictStack) > 0:
        dictStack[len(dictStack) - 1][name] = value
    else:
        newDict = {}
        newDict[name]= value
        dictStack.append(newDict)

# search dictStack for variable or function 
# start searhing at the top of the stack
def lookup(name):
    for d in reversed(dictStack): 
        if(d.get("/" + name, 0)): # append '/' to name
            return d["/" + name]
    return None


# ---------- arithmetic operators ---------- #
def add():
    if len(opStack) > 1:
        # pop two values 
        op1 = opPop()
        op2 = opPop()
        # check if values are int or float 
        if((isinstance(op1, int) or isinstance(op1, float))
           and (isinstance(op2, int) or isinstance(op2, float))):
            opPush(op1 + op2) # push addition of values
        else:
            print("Error add() - value not numerical")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error - add expects 2 operands")

def sub():
    if len(opStack) > 1:
        # pop 2 values 
        op1 = opPop()
        op2 = opPop()
        # check if int or float
        if((isinstance(op1, int) or isinstance(op1, float))
           and (isinstance(op2, int) or isinstance(op2, float))):
            opPush(op2 - op1) # push subtraction of values
        else:
            print("Error sub() - value not numerival")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error - sub expects 2 operands")

def mul():
    if len(opStack) > 1:
        # pop 2 values
        op1 = opPop()
        op2 = opPop()
        # check if int or float
        if((isinstance(op1, int) or isinstance(op1, float))
           and (isinstance(op2, int) or isinstance(op2, float))):
            opPush(op1 * op2) # push product of values
        else:
            print("Error mul() - value not numerical")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error - mul expects 2 operands")

def div():
    if len(opStack) > 1:
        # pop 2 values
        op1 = opPop()
        op2 = opPop()
        #check if int or float
        if((isinstance(op1, int) or isinstance(op1, float))
           and (isinstance(op2, int) or isinstance(op2, float))):
            opPush(op2/op1) # push result to stack
        else:
            print("Error div() - value not numerical")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error - div expects 2 operands")

def mod():
    if len(opStack) > 1:
        # pop 2 values
        op1 = opPop()
        op2 = opPop()
        #check if int or float
        if((isinstance(op1, int) or isinstance(op1, float))
           and (isinstance(op2, int) or isinstance(op2, float))):
            opPush(op2 % op1) # push result to stack
        else:
            print("Error div() - value not numerical")
            opPush(op1)
            opPush(op2)             
    else:
        print("Error - div expects 2 operands")

# ---------- array operators ---------- #

def length():
    if len(opStack) > 0:
        # pop value from opStack
        stringInput = opPop()
        # check if list value
        if(isinstance(stringInput, list)):
            opPush(len(stringInput)) # calculate length and push to stack
        else:
           print("Error length() - expecting a string argument")
           opPush(stringInput)
    else:
        print("Error length() - not enough arguments")

def get():
    if len(opStack) > 1:
        # pop index and string value from opStack
        index = opPop()
        stringInput = opPop()
        # check if string is list value and if index is int
        if(isinstance(stringInput, list) and isinstance(index, int)):
            opPush(stringInput[index]) # calculate ascii value and push
        else:
            print("Error get() - expecting string and  integer argument")
            opPush(stringInput)
            opPush(index)
    else:
        print("Error get() - not enough arguments")

# ---------- stack manipulation and print operators ---------- #

#copies top element in opStack
def dup():
    if len(opStack) > 0:
        op1 = opPop()
        opPush(op1)
        opPush(op1)
    else:
        print("Error dup() - not enough arguments")

# swaps top two elements in opStack
def exch():
    if len(opStack) > 1:
        # pop elements
        op1 = opPop()
        op2 = opPop()
        # push them in swapped order
        opPush(op1)
        opPush(op2)
    else:
        print("Error exch() - not enough arguments")

def pop():  
    if len(opStack) > 0:
        x = opStack[len(opStack) - 1]
        opStack.pop(len(opStack) - 1)
    else:
        print("Error pop() - opStack is empty")

# Pops 2 integer values m and n from stack, 
# rolls the top m values n times 
# (if n is positive roll clockwise, otherwise roll countercloackwise)
def roll():
    if len(opStack) > 1:
        n = opPop()
        m = opPop()
        copyList = []
        for x in range(0, m):
            copyList.append(opPop())
        if (n > 0): 
            copyList[len(copyList):] = copyList[0:n]
            copyList[0:n]=[]
        else:
            copyList[:0]=copyList[n:]
            copyList[n:]=[]
       
        for x in reversed(copyList[0:]):
            opPush(x)
        del copyList[:]
          
    else:
       print("Error roll() - not enough arguments")

    
# clears the stack
def clear():
    del opStack[:]

# prints the stack
def stack():
    print(opStack)


# ---------- dictionary manipulation ---------- #

# creates a new empty dictionary  
# pushes it on opStack
def psDict():
    if len(opStack) > 0:
        size = opPop() # size = initial size of the dictionary ; discard      
        opPush({})
    else:
        print("Error psDict() - not enough arguments")

def begin():
    dictPush()

def end():
    dictPop()

# pops a name and value from stack
# adds definition to dictStack
def psDef():
    if len(opStack) > 1:
        value = opPop()
        name = opPop()
        if(isinstance(name, str)):
            define(name, value)
        else:
            print("Error psDef() - invalid name argument")
    else:
        print("Error psDef() - not enough arguments")

#------- Loop Operators --------------

def For():
    forBody = opPop()
    end = opPop()
    step = opPop()
    begin = opPop()
    
    for x in range(begin, end ,step):
        opPush(x) # push loop index onto stack
        interpret(forBody)


#------- Part 1 TEST CASES--------------
def testDefine():
    define("/n1", 4)
    if lookup("n1") != 4:
        return False
    return True

def testLookup():
    opPush("/n1")
    opPush(3)
    psDef()
    if lookup("n1") != 3:
        return False
    return True

#Arithmatic operator tests
def testAdd():
    opPush(1)
    opPush(2)
    add()
    if opPop() != 3:
        return False
    return True

def testSub():
    opPush(10)
    opPush(4.5)
    sub()
    if opPop() != 5.5:
        return False
    return True

def testMul():
    opPush(2)
    opPush(4.5)
    mul()
    if opPop() != 9:
        return False
    return True

def testDiv():
    opPush(10)
    opPush(4)
    div()
    if opPop() != 2.5:
        return False
    return True

def testMod():
    opPush(10)
    opPush(3)
    mod()
    if opPop() != 1:
        return False
    return True

#Array operator tests
def testLength():
    opPush([1,2,3,4,5])
    length()
    if opPop() != 5:
        return False
    return True

def testGet():
    opPush([1,2,3,4,5])
    opPush(4)
    get()
    if opPop() != 5:
        return False
    return True

#stack manipulation functions
def testDup():
    opPush(10)
    dup()
    if opPop()!=opPop():
        return False
    return True

def testExch():
    opPush(10)
    opPush("/x")
    exch()
    if opPop()!=10 and opPop()!="/x":
        return False
    return True

def testPop():
    l1 = len(opStack)
    opPush(10)
    pop()
    l2= len(opStack)
    if l1!=l2:
        return False
    return True

def testRoll():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(4)
    opPush(-2)
    roll()
    if opPop()!=3 and opPop()!=2 and opPop()!=5 and opPop()!=4 and opPop()!=1:
        return False
    return True

def testCopy():
    opPush(1)
    opPush(2)
    opPush(3)
    opPush(4)
    opPush(5)
    opPush(2)
    copy()
    if opPop()!=5 and opPop()!=4 and opPop()!=5 and opPop()!=4 and opPop()!=3 and opPop()!=2:
        return False
    return True

def testClear():
    opPush(10)
    opPush("/x")
    clear()
    if len(opStack)!=0:
        return False
    return True

#dictionary stack operators
def testDict():
    opPush(1)
    psDict()
    if opPop()!={}:
        return False
    return True

def testBeginEnd():
    opPush("/x")
    opPush(3)
    psDef()
    opPush({})
    begin()
    opPush("/x")
    opPush(4)
    psDef()
    end()
    if lookup("x")!=3:
        return False
    return True

def testpsDef():
    opPush("/x")
    opPush(10)
    psDef()
    if lookup("x")!=10:
        return False
    return True

def testpsDef2():
    opPush("/x")
    opPush(10)
    psDef()
    opPush(1)
    psDict()
    begin()
    if lookup("x")!=10:
        end()
        return False
    end()
    return True

def isInt(s):
    try:
        int(s)
        return True
    except ValueError:
        return False

def tokenize(s):
    retValue = re.findall("/?[a-zA-Z][a-zA-Z0-9_]*|[[][a-zA-Z0-9_\s!][a-zA-Z0-9_\s!]*[]]|[-]?[0-9]+|[}{]+|%.*|[^ \t\n]", s)
    return retValue


def groupMatching(it):
    res = []
    for c in it:
        if c == ')':
            return res
        else:
            res.append(groupMatching(it))
    return False

def group(s):
    if s[0] == '(':
        return groupMatching(iter(s[1:]))
    else: return False

def parseMatching(it):
    res = []
    for c in it:
        if c == '}' or c == ']':
            return res
        elif c == '{' or c == '[': 
            res.append(parseMatching(it)) 
        elif isInt(c) or c[0] == '-': 
            res.append(int(c))
        elif c[0] == "[":
            temp = []
            for item in c:
                if isInt(item):
                    temp.append(int(item))
            res.append(temp)
        else:
            res.append(c)
    return False

def parse(tokens):
    if tokens[0] == '{':
        return parseMatching(iter(tokens[1:]))
    else: return False 


def interpret(tokenList):
    builtinFunctions = { "add":add, "sub":sub, "mul":mul, "div":div, "mod":mod, "length":length, "get":get,
        "dup":dup, "exch":exch, "pop":pop, "roll":roll, "clear":clear, "stack":stack, "dict":psDict,
        "begin":begin, "end":end, "def":psDef, "for":For}
    
    for token in tokenList:
        if isinstance(token, int): # case of integer
            opPush(token)
        elif isinstance(token, list):
            opPush(token)
        elif isinstance(token, str): # case of string 
            if token[0] == '(':    
                opPush(token[1:-1])
            
            elif token[0] == '/' : # case of name
                opPush(token)
            else:
                func = builtinFunctions.get(token,None)  # case of built-in function
                if func != None:
                    func()
                else:       # case of variable lookup
                    val = lookup(token)
                    if isinstance(val,list):   # case of code array 
                        interpret(val)   # interpret code array body
                    elif val != None:           
                        opPush(val)
                    else:       # can't find variable/function
                        print("Error: Couldn't find " + token + "in the dictStack!")
        else:      
            print("Error: Undefined token in input!")

def interpreter(s):
	interpret(parse(tokenize(s)))


def main():
    # ---------- testing parsing --------- #
    print(parse(tokenize(
        """
        { /square {dup mul} def 1 square 2 square 3 square add add }
        """
        )))
        
    print("\n")
    
    print(parse(tokenize(
        """
        { /n 5 def 1 n -1 1 {mul} for }
        """
        )))
        
    print("\n")
    
    print(parse(tokenize(
    """
        { /sum { -1 0 {add} for} def
        0
        [1 2 3 4] length
        sum
        2 mul
        [1 2 3 4] 2 get
        add add add
        stack }
    """)))
    
    print("\n")
    
    # ------- testing tokenizing ------ #
    print (tokenize(
    """
        { /fact{
        0 dict
            begin
                /n exch def
                 1
                n -1 1 {mul} for
            end
        }def
        [1 2 3 4 5] dup 4 get pop
        length
        fact
        stack }
        """))
        
    print("\n")
    
    # ------ testing interpretor ------ #
    interpreter("{6 4 add 10 5 sub 8 3 mul 100 25 div 42 7 mod}")
    if opStack != [10, 5, 24, 4, 0]:
        print("test 1 failed")
    else:
        print ("test 1 pass")
    clear()
    
    interpreter("{1 2 3 4 5 6 4 2 roll}")
    if opStack != [1, 2, 5, 6, 3, 4]:
        print("test 2 failed")
    else:
        print ("test 2 pass")
    clear()
    
    interpreter("{/x 4 def x x add}")
    if opPop() != 8:
        print("test 3 failed")
    else:
        print ("test 3 pass")
    clear()
    
    interpreter("{ [1 2 3 4 5] length dup [1 2 3 4 5] 3 get }")
    if opStack != [5, 5, 4]:
        print("test 4 failed")
    else:
        print ("test 4 pass")
    clear()
    
    interpreter("{ /fact { 0 dict begin /n exch def 1 n -1 1 {mul} for end } def [1 2 3 4 5] dup 4 get pop length fact stack }")
    if (opPop() != 120):
        print("test 5 failed")
    else:
        print ("test 5 pass")
    clear()

main()