# MCP23017
![picture](https://cdn-shop.adafruit.com/970x728/732-02.jpg)

Python driver for MCP23017, I2C controlled GPIO expander with 16 GPIOs and 2 interrupt pins.

Primarily written for use on a Raspberry Pi as the smbus module is used. I wanted the functions to look as similar to RPi.GPIO, as that is what I am used to. Written as a proof of concept before I start using the part with a MCU (using a different C library). My favorite feature of the MCP23017 is that the I2C can be at 3.3V and the GPIO can run at 5V. Be sure to tie the A0, A1, A2 (and Reset) to static voltages before using as these pins do not have weak pull-ups or pull-downs. If you are using the DIP package, the datasheet incorrectly shows the reset pin as an output. Drive it high if you don't want to reset the part.

I use read-modify-write when setting register values. "& ( 0xFF - (1 << int(pin[1])))" is used to clear a single bit and "| (1 << int(pin[1]))" is used to set a single bit. They are used frequently. 
