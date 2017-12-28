from tkinter import *

class Calculator:
    def __init__(self):
        # Create the main window
        self.window = Tk()
        
        # Assign a title for this window
        self.window.title('Simple Calculator')
        
        # Place an Entry widget in the window to accept input
        self.display = StringVar()
        entrybox = Entry(self.window, relief=SUNKEN, textvariable = self.display)
        entrybox.pack(side=TOP, expand=YES, fill=BOTH)
        
        frameA = Frame(self.window)
        frameA.pack(side=TOP, expand=YES, fill=BOTH)
        
        self.firstbutton = Button(frameA, text='1', command=self.func1)   # command tells which method is executed
        self.firstbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.secondbutton = Button(frameA, text='2', command=self.func2)   # command tells which method is executed
        self.secondbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.thirdbutton = Button(frameA, text='3', command=self.func3)   # command tells which method is executed
        self.thirdbutton.pack(side=LEFT, expand=YES, fill=BOTH)        
        
        # Create a Frame in which to place the Buttons
        frameB = Frame(self.window)
        frameB.pack(side=TOP, expand=YES, fill=BOTH)
        
        self.fourthbutton = Button(frameB, text='4', command=self.func4)   # command tells which method is executed
        self.fourthbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.fifthbutton = Button(frameB, text='5', command=self.func5)   # command tells which method is executed
        self.fifthbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.sixthbutton = Button(frameB, text='6', command=self.func6)   # command tells which method is executed
        self.sixthbutton.pack(side=LEFT, expand=YES, fill=BOTH)        
        
        # Create a Frame in which to place the Buttons
        frameC = Frame(self.window)
        frameC.pack(side=TOP, expand=YES, fill=BOTH)
        
        self.seventhbutton = Button(frameC, text='7', command=self.func7)   # command tells which method is executed
        self.seventhbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.eighthbutton = Button(frameC, text='8', command=self.func8)   # command tells which method is executed
        self.eighthbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.ninthbutton = Button(frameC, text='9', command=self.func9)   # command tells which method is executed
        self.ninthbutton.pack(side=LEFT, expand=YES, fill=BOTH)     
        
        
        # Create a Frame in which to place the Buttons
        frameD = Frame(self.window)
        frameD.pack(side=TOP, expand=YES, fill=BOTH)
        
        self.negativebutton = Button(frameD, text='-', command=self.funcNegate)   # command tells which method is executed
        self.negativebutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.zerobutton = Button(frameD, text='0', command=self.func0)   # command tells which method is executed
        self.zerobutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.dotbutton = Button(frameD, text='.', command=self.funcDot)   # command tells which method is executed
        self.dotbutton.pack(side=LEFT, expand=YES, fill=BOTH)     
        
        
        # Create a Frame in which to place the Buttons
        frameE = Frame(self.window)
        frameE.pack(side=TOP, expand=YES, fill=BOTH)
        
        self.plusbutton = Button(frameE, text='+', command=self.funcPlus)   # command tells which method is executed
        self.plusbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.minusbutton = Button(frameE, text='-', command=self.funcMinus)   # command tells which method is executed
        self.minusbutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.timesbutton = Button(frameE, text='*', command=self.funcTimes)   # command tells which method is executed
        self.timesbutton.pack(side=LEFT, expand=YES, fill=BOTH)  
        
        self.dividebutton = Button(frameE, text='/', command=self.funcDivide)   # command tells which method is executed
        self.dividebutton.pack(side=LEFT, expand=YES, fill=BOTH)
        
        self.equalsbutton = Button(frameE, text='=', command=self.funcEquals)   # command tells which method is executed
        self.equalsbutton.pack(side=LEFT, expand=YES, fill=BOTH)          
        
        # Create a Frame in which to place the Buttons
        frameF = Frame(self.window)
        frameF.pack(side=TOP, expand=YES, fill=BOTH)     
        
        self.clearbutton = Button(frameF, text='Clear', command=self.funcClear)   # command tells which method is executed
        self.clearbutton.pack(side=LEFT, expand=YES, fill=BOTH)         
        
        
        
        
        # Enter tkinter main loop
        mainloop()        
        
    def func1(self): 
        self.display.set(self.display.get() + '1')        
        
    def func2(self): 
        self.display.set(self.display.get() + '2')
    
    def func3(self): 
        self.display.set(self.display.get() + '3')
        
    def func4(self): 
        self.display.set(self.display.get() + '4')        
        
    def func5(self): 
        self.display.set(self.display.get() + '5')
    
    def func6(self): 
        self.display.set(self.display.get() + '6') 
        
    def func7(self): 
        self.display.set(self.display.get() + '7')        
        
    def func8(self): 
        self.display.set(self.display.get() + '8')
    
    def func9(self): 
        self.display.set(self.display.get() + '9')
        
    def funcNegate(self):
        self.display.set("-" + self.display.get())
        
    def func0(self):
        self.display.set(self.display.get() + '0')
        
    def funcDot(self):
        self.display.set(self.display.get() + '.')
        
    def funcPlus(self):
        self.display.set(self.display.get() + '+')
        
    def funcMinus(self):
        self.display.set(self.display.get() + '-')
        
    def funcTimes(self):
        self.display.set(self.display.get() + '*')
    
    def funcDivide(self):
        self.display.set(self.display.get() + '/')  
        
    def funcEquals(self):
            try:
                self.display.set(eval(self.display.get()))
            except:
                self.display.set("ERROR")        
    
    def funcClear(self):
        self.display.set('')
        


def main():        
    gui = Calculator()
    
    
main()