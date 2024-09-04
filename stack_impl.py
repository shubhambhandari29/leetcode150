'''
Design a stack class that supports the push, pop, top, and getMin operations.

MinStack() initializes the stack object.
void push(int val) pushes the element val onto the stack.
void pop() removes the element on the top of the stack.
int top() gets the top element of the stack.
int getMin() retrieves the minimum element in the stack.
'''
class MinStack:

    def __init__(self):
        stack=[]
        self.stack=stack

    def push(self, val: int) -> None:
        top = len(self.stack)
        print("TOP >>", top)
        if top==0:
            self.stack.append(val)
            return
        else:
            self.stack.insert(top,val)
            return

            


    def pop(self) -> None:
        top = len(self.stack)
        if top ==0:
            print("nothing to pop")
            return
        print("ELE TO BE popped", self.stack[top-1])
        self.stack.pop()

    def top(self) -> int:
        top = len(self.stack)
        print("top element of stack is  " ,self.stack[top-1])

    def getMin(self) -> int:
        self.stack.sort()
        print("minimum of stack is", self.stack[0])

    def print(self):
        print("stack is",self.stack)

obj=MinStack()
obj.push(2)
obj.print()
obj.pop()
obj.print()
obj.push(72)
obj.print()
obj.push(34)
obj.print()
obj.top()
obj.print()
obj.push(32)
obj.print()
obj.push(21)
obj.print()
obj.push(8)
obj.print()
obj.push(43)
obj.print()
obj.getMin()
obj.print()

