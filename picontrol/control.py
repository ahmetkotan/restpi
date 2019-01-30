from django.conf import settings
from rest_framework.exceptions import ValidationError

import RPi.GPIO as gpio


def pin_physical_control(physical):
    if type(physical) != int:
        raise ValidationError({"physical": "Wrong pin number."})

    if physical > 40 and physical < 1:
        raise ValidationError({"physical": "Wrong pin number."})

    if physical not in settings.BOARD_PORTS:
        raise ValidationError({"physical": "This pin isn't a board pin."})

def get_pin(physical):
    pins = settings.PINS

    for pin in pins:
        if pin["physical"] == physical:
            return pin

def read_pin(physical):
    physical = int(physical)

    pin_physical_control(physical)
    pin = get_pin(physical)

    pin_mode = gpio.gpio_function(physical)
    if pin_mode == 1:
        pin_setup = gpio.IN
    elif pin_mode == 0:
        pin_setup = gpio.OUT


    gpio.setup(physical, pin_setup)
    pin_value = gpio.input(physical)
    pin["value"] = pin_value
    pin["mode"] = pin_mode
    pin["hr_mode"] = settings.PORT_MODES[pin_mode]
    pin["hr_value"] = settings.PORT_VALUES[pin_value]

    return pin

def read_all_pin():
    ports = settings.BOARD_PORTS

    for port in ports:
        read_pin(port)

    return settings.PINS

def write_pin_mode(physical, mode):
    physical = int(physical)
    pin_physical_control(physical)

    if mode == gpio.OUT:
        new_mode = gpio.OUT
    elif mode == gpio.IN:
        new_mode = gpio.IN
    else:
        raise ValidationError({"mode": "Wrong mode."})

    gpio.setup(physical, new_mode)
    pin = read_pin(physical)
    if mode == gpio.IN:
        pin["value"] = 0
        pin["hr_value"] = settings.PORT_VALUES[0]
    return pin


def write_pin_value(physical, value):
    physical = int(physical)
    pin_physical_control(physical)

    if value == 1:
        new_value = gpio.HIGH
    elif value == 0:
        new_value = gpio.LOW
    else:
        raise ValidationError({"value": "Wrong value."})

    pin = read_pin(physical)
    if pin["mode"] == gpio.OUT:
        gpio.setup(physical, gpio.OUT)
        gpio.output(physical, new_value)
        return read_pin(physical)
    else:
        raise ValidationError({"mode": "Pin's mode is not OUT."})
