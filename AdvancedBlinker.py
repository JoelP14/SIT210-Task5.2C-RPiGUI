import tkinter as tk 
import RPi.GPIO as GPIO
#pin setup
GPIO.setmode(GPIO.BOARD)
GPIO.setup(7, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(13, GPIO.OUT)

LEDControls = tk.Tk()
LEDControls.title("LED Controls") #set name
LEDControls.geometry("400x200") #set size

def ChangeLight():
    LightVar = Light.get() #get the var
    print(str(LightVar)) #debug
    if LightVar == 1:
        GPIO.output(7, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
    elif LightVar == 2:
        GPIO.output(11, GPIO.HIGH)
        GPIO.output(7, GPIO.LOW)
        GPIO.output(13, GPIO.LOW)
    else:
        GPIO.output(13, GPIO.HIGH)
        GPIO.output(11, GPIO.LOW)
        GPIO.output(7, GPIO.LOW)
#switching var with tk
Light = tk.IntVar()
#radio1
R1 = tk.Radiobutton(LEDControls, text="Red LED", variable=Light, value=1, command=ChangeLight)
R1.grid(row=0, column=0)
#radio2
R2 = tk.Radiobutton(LEDControls, text="Green LED", variable=Light, value=2, command=ChangeLight)
R2.grid(row=1, column=0)
#radio3
R3 = tk.Radiobutton(LEDControls, text="Blue LED", variable=Light, value=3, command=ChangeLight)
R3.grid(row=2, column=0)
#exitbutton
Exitbutton = tk.Button(LEDControls, text="Exit",bg="red", command=LEDControls.destroy)
Exitbutton.grid(row=3, column=0)
LEDControls.mainloop()