from collections import ChainMap
from tkinter import *
from tkinter import ttk
from tkinter.ttk import Notebook
import obd
import time


root = Tk()  # สร้าง หน้าจอ GUI (Create GUI)
root.geometry('1000x625+400+40')  # กำหนดขนาดจอ
root.title('PHATTHARAPHON DASHBOARD')
# กำหนดรูปภาพขึ้นมา
dog = PhotoImage(file='D:\\Python project\\Python\\FONTHINBURG.png')
picture1 = ttk.Label(root, image=dog).place(x=0, y=0, relwidth=1, relheight=1)


# เชื่อมต่อobd (Connect obd2 with serial port of your computer)
connection = obd.OBD()


def on_click():
    global SPEEDstring
    cmd = obd.commands.INTAKE_PRESSURE  # select an OBD command (sensor)
    response_MAP = connection.query(cmd)
    MAPvalue = response_MAP
    print(response_MAP)
    MAPstring = str(MAPvalue)
    MAPstring = MAPstring.replace('revolutions_per_minute', '')
    showMAPvalue.set(MAPstring)

    cmd = obd.commands.SPEED  # select an OBD command (sensor)
    response_SPEED = connection.query(cmd)
    SPEEDvalue = response_SPEED
    print(response_SPEED)
    SPEEDstring = str(SPEEDvalue)
    SPEEDstring = SPEEDstring.replace('kph', '')
    showSPEEDvalue.set(SPEEDstring)

    cmd = obd.commands.RPM  # select an OBD command (sensor)
    response_RPM = connection.query(cmd)
    RPMvalue = response_RPM
    print(response_RPM)
    RPMstring = str(RPMvalue)
    RPMstring = RPMstring.replace(' revolutions_per_minute', '')
    showRPMvalue.set(RPMstring)

    cmd = obd.commands.COOLANT_TEMP  # select an OBD command (sensor)
    response_COOLANT_TEMP = connection.query(cmd)
    ECTvalue = response_COOLANT_TEMP
    print(response_COOLANT_TEMP)
    ECTstring = str(ECTvalue)
    ECTstring = ECTstring.replace('degC', '')
    showECTvalue.set(ECTstring)  # ตั้งค่าให้ showECTvalue เท่ากับ ECT ในfunc

    cmd = obd.commands.MAF  # select an OBD command (sensor)
    response_MAF = connection.query(cmd)
    MAFvalue = response_MAF
    print(response_MAF)
    MAFstring = str(MAFvalue)
    MAFstring = MAFstring.replace('gps', '')
    showMAFvalue.set(MAFstring)

    cmd = obd.commands.ELM_VOLTAGE  # select an OBD command (sensor)
    response_ELM_VOLTAGE = connection.query(cmd)
    CTMVvalue = response_ELM_VOLTAGE
    print(response_ELM_VOLTAGE)
    CTMVstring = str(CTMVvalue)
    CTMVstring = CTMVstring.replace('volt', '')
    showCTMVvalue.set(CTMVstring)

    cmd = obd.commands.ELM_VOLTAGE  # select an OBD command (sensor)
    response_AMBIANT_AIR_TEMP = connection.query(cmd)
    AIRTvalue = response_AMBIANT_AIR_TEMP
    print(response_AMBIANT_AIR_TEMP)
    AIRTstring = str(AIRTvalue)
    showAIRTvalue.set(AIRTstring)

    cmd = obd.commands.THROTTLE_POS  # select an OBD command (sensor)
    response_THROTTLE_POS = connection.query(cmd)
    TPSvalue = response_THROTTLE_POS
    print(response_THROTTLE_POS)
    TPSstring = str(TPSvalue)
    TPSstring1 = TPSstring.replace("percent", "")
    showTPSvalue.set(TPSstring1)

    cmd = obd.commands.TIMING_ADVANCE  # select an OBD command (sensor)
    response_TIMING_ADVANCE = connection.query(cmd)
    IGTvalue = response_TIMING_ADVANCE
    print(response_TIMING_ADVANCE)
    IGTstring = str(IGTvalue)
    showIGTvalue.set(IGTstring)

    cmd = obd.commands.INTAKE_TEMP  # select an OBD command (sensor)
    response_INTAKE_TEMP = connection.query(cmd)
    IATvalue = response_INTAKE_TEMP
    print(response_INTAKE_TEMP)
    IATstring = str(IATvalue)
    showIATvalue.set(IATstring)

    cmd = obd.commands.COMMANDED_EQUIV_RATIO  # select an OBD command (sensor)
    response_COMMANDED_EQUIV_RATIO = connection.query(cmd)
    LAMDAvalue = response_COMMANDED_EQUIV_RATIO
    print(response_COMMANDED_EQUIV_RATIO)
    LAMDAstring = str(LAMDAvalue)
    LAMDAstring1 = LAMDAstring.replace("ratio", "")
    LAMDAstring2 = float(LAMDAstring1)
    LAMDAstring3 = float(14.7)/float(LAMDAstring2)
    LAMDAstring4 = round(LAMDAstring3, 2)
    showAFRvalue.set(LAMDAstring4)

    root.after(1, on_click)  # Loop send/request


root.after(1, on_click)  # Value send together
RPMprogressbar = IntVar()
showMAPvalue = StringVar()
showRPMvalue = StringVar()
showSPEEDvalue = StringVar()
showECTvalue = StringVar()  # ค่าที่setจากfunc (Value when you set on func)
showMAFvalue = StringVar()
showCTMVvalue = StringVar()
showAIRTvalue = StringVar()
showIATvalue = StringVar()
showTPSvalue = StringVar()
showIGTvalue = StringVar()
showAFRvalue = StringVar()

# สั่งทำงาน

button1 = Button(root, text=" = ", command=on_click)

# Print DATA ALL.

BOOSTlabel = Label(root, textvariable=showMAPvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=750, y=25)
SPEEDlabel = Label(root, textvariable=showSPEEDvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=750, y=94)
RPMlabel = Label(root, textvariable=showRPMvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=150, y=76)
ECTlabel = Label(root, textvariable=showECTvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=150, y=200)
ENGINELOADlabel = Label(root, textvariable=showMAFvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=150, y=340)
CTMVlabel = Label(root, textvariable=showCTMVvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=150, y=480)
AIRTlabel = Label(root, textvariable=showAIRTvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=450, y=200)
TPSlabel = Label(root, textvariable=showTPSvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=450, y=340)

IGTlabel = Label(root, textvariable=showIGTvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=760, y=200)
IATlabel = Label(root, textvariable=showIATvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=760, y=340)
AFRlabel = Label(root, textvariable=showAFRvalue, font=(
    'hindenburg', 26), fg='yellow', bg='black').place(x=760, y=480)


root.mainloop()
