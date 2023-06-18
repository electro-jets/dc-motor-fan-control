#Credits to How2Electronics.com
#Credits to Elecrow.com
#Developed by Elecrow Developers
#Edited and Modified by Kristian Koev
#https://github.com/electro-jets


from machine import Pin,ADC,PWM
from time import sleep
 
A_1A_pin = 15
Pot_pin = 0
 
def setup():
    global A_1A
    global pot_ADC
    
    A_1A = PWM(Pin(A_1A_pin))
    A_1A.freq(1000)
    pot_ADC = ADC(Pot_pin)
 
def loop():
    while True:
        print ("Най-малка стойност: 64/80")
        print ("Най-голяма стойност: 65535")
        print ('Стойност на потенциометъра:', pot_ADC.read_u16())
        Value = pot_ADC.read_u16()  
        A_1A.duty_u16(Value)
        sleep(0.2)                          
 
if __name__ == '__main__':
     setup()     
     loop()    
