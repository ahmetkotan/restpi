from RPi.GPIO import *

PINS = [
    {"physical": 1, "name": "3.3v", "mode": None, "value": None, "BCM": None},
    {"physical": 2, "name": "5v", "mode": None, "value": None, "BCM": None},
    {"physical": 3, "name": "SDA.1", "mode": None, "value": None, "BCM": 2},
    {"physical": 4, "name": "5v", "mode": None, "value": None, "BCM": None},
    {"physical": 5, "name": "SCL.1", "mode": None, "value": None, "BCM": 3},
    {"physical": 6, "name": "0v", "mode": None, "value": None, "BCM": None},
    {"physical": 7, "name": "GPIO.7", "mode": None, "value": None, "BCM": 4},
    {"physical": 8, "name": "TxD", "mode": "ALT0", "value": None, "BCM": 14},
    {"physical": 9, "name": "0v", "mode": None, "value": None, "BCM": None},
    {"physical": 10, "name": "RxD", "mode": "ALT0", "value": None, "BCM": 15},
    {"physical": 11, "name": "GPIO.0", "mode": None, "value": None, "BCM": 17},
    {"physical": 12, "name": "GPIO.1", "mode": None, "value": None, "BCM": 18},
    {"physical": 13, "name": "GPIO.2", "mode": None, "value": None, "BCM": 27},
    {"physical": 14, "name": "0v", "mode": None, "value": None, "BCM": None},
    {"physical": 15, "name": "GPIO.3", "mode": None, "value": None, "BCM": 22},
    {"physical": 16, "name": "GPIO.4", "mode": None, "value": None, "BCM": 23},
    {"physical": 17, "name": "3.3v", "mode": None, "value": None, "BCM": None},
    {"physical": 18, "name": "GPIO.5", "mode": None, "value": None, "BCM": 24},
    {"physical": 19, "name": "MOSI", "mode": None, "value": None, "BCM": 10},
    {"physical": 20, "name": "0v", "mode": None, "value": None, "BCM": None},
    {"physical": 21, "name": "MISO", "mode": None, "value": None, "BCM": 9},
    {"physical": 22, "name": "GPIO.6", "mode": None, "value": None, "BCM": 25},
    {"physical": 23, "name": "SCLK", "mode": None, "value": None, "BCM": 11},
    {"physical": 24, "name": "CE0", "mode": None, "value": None, "BCM": 8},
    {"physical": 25, "name": "0v", "mode": None, "value": None, "BCM": None},
    {"physical": 26, "name": "CE1", "mode": None, "value": None, "BCM": 7},
    {"physical": 27, "name": "SDA.0", "mode": None, "value": None, "BCM": 0},
    {"physical": 28, "name": "SCL.0", "mode": None, "value": None, "BCM": 1},
    {"physical": 29, "name": "GPIO.21", "mode": None, "value": None, "BCM": 5},
    {"physical": 30, "name": "0v", "mode": None, "value": None, "BCM": None},
    {"physical": 31, "name": "GPIO.22", "mode": None, "value": None, "BCM": 6},
    {"physical": 32, "name": "GPIO.26", "mode": None, "value": None, "BCM": 12},
    {"physical": 33, "name": "GPIO.23", "mode": None, "value": None, "BCM": 13},
    {"physical": 34, "name": "0v", "mode": None, "value": None, "BCM": None},
    {"physical": 35, "name": "GPIO.24", "mode": None, "value": None, "BCM": 19},
    {"physical": 36, "name": "GPIO.27", "mode": None, "value": None, "BCM": 16},
    {"physical": 37, "name": "GPIO.25", "mode": None, "value": None, "BCM": 26},
    {"physical": 38, "name": "GPIO.28", "mode": None, "value": None, "BCM": 20},
    {"physical": 39, "name": "0v", "mode": None, "value": None, "BCM": None},
    {"physical": 40, "name": "GPIO.29", "mode": None, "value": None, "BCM": 21},
]

BOARD_PORTS = [3, 5, 7, 8, 10, 11, 12, 13, 15, 16, 18, 19, 21, 22, 23, 24, 26, 29, 31, 32, 33, 35, 36, 37, 38, 40]
PORT_MODES = {
    OUT: "OUT",
    IN: "IN",
    SERIAL: "SERIAL(ALT0)",
    SPI: "SPI",
    I2C: "I2C",
    HARD_PWM: "HARD_PWM",
    UNKNOWN: "UNKNOWN",
    None: None,
}

PORT_VALUES = {
    HIGH: "HIGH",
    LOW: "LOW",
    None: None,
}

setmode(BOARD)
setwarnings(False)