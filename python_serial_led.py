import serial
import tkinter
from tkinter import *
from tkinter import font
import time,sys,os
import tkinter.messagebox   #this is a dialog message



#make a tkinter Windows
top = tkinter.Tk()
top.title("On/Off Led by Python2.7.10, pySerial2.7 and tkinter8.5 ,Revised by joeGTEC")
top.geometry("%dx%d" %(650,550))
top.bind("<Escape>",lambda e: top.destroy())  #when escape key pressed then quit.
top.bind("<F7>",lambda e:requestState())  #F7 key call requestState func.


try:
             top.iconbitmap('joegtec.ico') # the program icon has to in the same path of this program.
except tkinter.TclError:

             tkinter.messagebox.showerror("Error" , 'bitmap "joegtec.ico" not defined.\nDue to the program icon not found "joegtec.ico" in the same path of program.')
             
else:
             print ("iconbitmap('joegtec.ico') ok ")
             
#default vaule if config file is not found.
serialPort = "com79"
baudRate = 9600


def ReadConfigFile(filename):
             #read  comport and baudRate  from a config file and save to variables as serialPort,baudRate.
             if os.path.isfile(filename):
                          global serialPort
                          global baudRate
                          f=open(filename,'r')
                          data=f.readline()       # read only one line.                                
                          f.close()
                          serialPort,baudRate=data.split(',')    #split with comma and save to variables respectively.
                          
             else:
                          print('file not found : ' + filename + '\nIn same path of program\n ,Use default : port:com79,buadrate:9600')
                          tkinter.messagebox.showerror("Error" , 'file not found : ' + filename + '\nIn same path of program\nUse default : port:com79,buadrate:9600')
                         
             return



             

#open serial and check exception error.
# Open a file get comport and baudrate.
ReadConfigFile('config.txt')
time.sleep(0.5)
try:
             ser = serial.Serial(serialPort , baudRate, timeout=0, writeTimeout=0) #ensure non-block
             #This problem can be avoided with the timeout=0 option when enitializing the Serial object
             #, which will cause it to return nothing unless something is already waiting in the Serial object's buffer.
except serial.SerialException:
             tkinter.messagebox.showerror("Error" , "could not open port : " + serialPort)
             top.destroy()
             sys.exit()
except IOError:
             tkinter.messagebox.showerror("Error" , "can't find file or read data")
             top.destroy()
             sys.exit()
else:
             print ("open serial successfully : " + serialPort)
             
             
#define function              
def led1():
             #command to arduino for on/off led1
             if button1["fg"] == 'green':
                          ser.write(b'c0')  #send to arduino with the converted string to byte before.
                          button1["fg"] == 'red'
                          button1["text"] = 'LED1 OFF'
                          time.sleep(1)     #delay 1 s
                          
             else:
                          ser.write(b'c1')
                          button1["fg"] == 'green'
                          button1["text"] = 'LED1 ON'
                          time.sleep(1)
                          
             return
                                    
def led2():
             #command to arduino for on/off led2
             if button2["fg"] == 'green':
                          ser.write(b'd0')
                          button2["fg"] == 'red'
                          button2["text"] = 'LED2 OFF'
                          time.sleep(1)                                      
             else:
                          ser.write(b'd1')
                          button2["fg"] == 'green'
                          button2["text"] = 'LED2 ON'
                          time.sleep(1)
             return
def requestState():
             # function runs once for check state on/off of LEDs  when start program.
             print ('e1 \'inti program start\',request state on/off')
             ser.write(b'e1')
             time.sleep(0.5) #delay 500us
             return
     
                         
#begin design widget into a form windows
row1=Frame(top)

#set font size
helv36 = tkFont.Font(family='Helvetica' , size=25, weight='bold')
button1=tkinter.Button(row1,bd=4,width=10,height=5,text="...",font=helv36,command=led1)
button1.pack(side=LEFT,padx=70,pady=10)
button2=tkinter.Button(row1,bd=4,width=10,height=5,text="...",font=helv36,command=led2)
button2.pack(side=LEFT,padx=5,pady=10)
row1.pack(side=TOP,fill=X)

var1 = 'How does it work.' + ' (port: ' + serialPort + ', baudRate: ' + str(baudRate) + ')\n'
var2 ='''
1. Program will read a Comport and Buadrate from  a filename named \'config.txt\' where in same path of Program\n
2. When the program run in the first time,it will request the state of LEDs(on/off). Which  button text and color  will  change according to the received data(state of LEDs).\n
3. Both buttons, when clicked, it will command an Arduino in order to turn on and off  the LEDs (led1,led2).\n
4. When pressing the switch from the side of Arduino. Button text and color changes in the status of switch on(led on) and off(led off).\n
** This project use  Python2.7.10, pySerial2.7 and tkinter8.5
 P.S. -Make exe file using py2exe and create icons for this program.
      -Press Escape key for quit, F7 key for request state(on/off)
      -Protect arduino reset,use Electrolyte Cap10-100uf((+)->reset,(-)-> gnd))'''
text = Text(top,bg="blue",fg="white")
text.insert(INSERT,var1 + var2)
text.pack(side=BOTTOM,expand=YES)
text.tag_add("How", "1.0","1.17")
text.tag_config("How", background="yellow", foreground="blue")


serBuffer = ""
def readSerial():
    while True:
        try:
                     # a Serial.readline() won't print anything until there is a whole line to return
                     c = ser.read()
                                         
        except serial.SerialException:
                     print ("call to ClearCommError failed")
                     tkinter.messagebox.showerror("Error" , "call to ClearCommError failed\nSerial connection lost\nPlease start program again.")
                     
                           
        #was anything read?
        if len(c) == 0:
            break
        
        # get the buffer from outside of this function
        global serBuffer
        
        # check if character is a delimeter
        if c == '\r':
            c = '' # don't want returns. chuck it
            
        if c == '\n':
            #serBuffer += "\n" # add the newline to the buffer
            
             print (serBuffer)
             state=serBuffer
             if (state == 'c1' ):
                          button1["fg"] = 'green'
                          button1["text"] = 'LED1 ON'
                          
             elif(state == 'c0' ):
                          button1["fg"] = 'red'
                          button1["text"] = 'LED1 OFF'
                          
             if (state == 'd1' ):
                          button2["fg"] = 'green'
                          button2["text"] = 'LED2 ON'
                          
             elif(state == 'd0' ):
                          button2["fg"] = 'red'
                          button2["text"] = 'LED2 OFF'                          
                          
             serBuffer = "" # empty the buffer
        else:
             serBuffer += c # add to the buffer
             


             
    # It needs the things in there to run every now and then in order to make the interface respond to interactions  
    top.after(2, readSerial) # check serial again soon ,a function to be called after the time delay after(delay_ms, callback=None, *args)


top.after(50,readSerial)  # to run a non-blocking version of read in the tkinter main loop
requestState()  # function runs once for check state on/off of LEDs  when start program
top.mainloop()
