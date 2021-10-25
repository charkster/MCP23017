from __future__ import print_function
from MCP23017   import MCP23017
import time

# GPB7 has a voltmeter attached (reading only)
# GPB6 has INTB connected to it
# GPB5 has INTA connected to it
# GPB4 is connected to GPA0

GPIO = MCP23017(address=0x20, debug=False) # all address pins are tied low, reset is tied high
GPIO.setup(pin='b7', direction=GPIO.OUT, out_val=GPIO.HIGH)
GPIO.setup(pin='b4', direction=GPIO.OUT, out_val=GPIO.LOW)
GPIO.setup(pin='a0', direction=GPIO.IN,  int_en=True, int_defval=GPIO.LOW)
print("--> Pin a0 value is {:d}".format(GPIO.input('a0')))
time.sleep(3)
print("--> INTA and INTB are by default active-low")
print("--> Pin INTA value is {:d}".format(GPIO.input('b5')))
print("--> Pin INTB value is {:d}".format(GPIO.input('b6')))
print("--> Drive b4 high, this should cause an interrupt on INTA")
GPIO.output('b4', GPIO.HIGH)
time.sleep(1)
# Need to read the GPIO pin first, as read_intcap() will clear the interrupt and the pin
print("--> Pin INTA value is {:d}".format(GPIO.input('b5')))
print("--> Pin INTB value is {:d}".format(GPIO.input('b6')))
print("--> Pin a0 value is {:d}".format(GPIO.input('a0')))
GPIO.read_intcap()
GPIO.write_regs_por()
