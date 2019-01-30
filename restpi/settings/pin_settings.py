from RPi.GPIO import *

PINS = [
    {"physical": 1, "name": "3.3v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 2, "name": "5v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 3, "name": "SDA.1", "mode": None, "value": None, "BCM": 2, "is_gpio": False},
    {"physical": 4, "name": "5v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 5, "name": "SCL.1", "mode": None, "value": None, "BCM": 3, "is_gpio": False},
    {"physical": 6, "name": "0v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 7, "name": "GPIO.7", "mode": None, "value": None, "BCM": 4, "is_gpio": True},
    {"physical": 8, "name": "TxD", "mode": "ALT0", "value": None, "BCM": 14, "is_gpio": False},
    {"physical": 9, "name": "0v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 10, "name": "RxD", "mode": "ALT0", "value": None, "BCM": 15, "is_gpio": False},
    {"physical": 11, "name": "GPIO.0", "mode": None, "value": None, "BCM": 17, "is_gpio": True},
    {"physical": 12, "name": "GPIO.1", "mode": None, "value": None, "BCM": 18, "is_gpio": True},
    {"physical": 13, "name": "GPIO.2", "mode": None, "value": None, "BCM": 27, "is_gpio": True},
    {"physical": 14, "name": "0v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 15, "name": "GPIO.3", "mode": None, "value": None, "BCM": 22, "is_gpio": True},
    {"physical": 16, "name": "GPIO.4", "mode": None, "value": None, "BCM": 23, "is_gpio": True},
    {"physical": 17, "name": "3.3v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 18, "name": "GPIO.5", "mode": None, "value": None, "BCM": 24, "is_gpio": True},
    {"physical": 19, "name": "MOSI", "mode": None, "value": None, "BCM": 10, "is_gpio": False},
    {"physical": 20, "name": "0v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 21, "name": "MISO", "mode": None, "value": None, "BCM": 9, "is_gpio": False},
    {"physical": 22, "name": "GPIO.6", "mode": None, "value": None, "BCM": 25, "is_gpio": True},
    {"physical": 23, "name": "SCLK", "mode": None, "value": None, "BCM": 11, "is_gpio": False},
    {"physical": 24, "name": "CE0", "mode": None, "value": None, "BCM": 8, "is_gpio": False},
    {"physical": 25, "name": "0v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 26, "name": "CE1", "mode": None, "value": None, "BCM": 7, "is_gpio": False},
    {"physical": 27, "name": "SDA.0", "mode": None, "value": None, "BCM": 0, "is_gpio": False},
    {"physical": 28, "name": "SCL.0", "mode": None, "value": None, "BCM": 1, "is_gpio": False},
    {"physical": 29, "name": "GPIO.21", "mode": None, "value": None, "BCM": 5, "is_gpio": True},
    {"physical": 30, "name": "0v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 31, "name": "GPIO.22", "mode": None, "value": None, "BCM": 6, "is_gpio": True},
    {"physical": 32, "name": "GPIO.26", "mode": None, "value": None, "BCM": 12, "is_gpio": True},
    {"physical": 33, "name": "GPIO.23", "mode": None, "value": None, "BCM": 13, "is_gpio": True},
    {"physical": 34, "name": "0v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 35, "name": "GPIO.24", "mode": None, "value": None, "BCM": 19, "is_gpio": True},
    {"physical": 36, "name": "GPIO.27", "mode": None, "value": None, "BCM": 16, "is_gpio": True},
    {"physical": 37, "name": "GPIO.25", "mode": None, "value": None, "BCM": 26, "is_gpio": True},
    {"physical": 38, "name": "GPIO.28", "mode": None, "value": None, "BCM": 20, "is_gpio": True},
    {"physical": 39, "name": "0v", "mode": None, "value": None, "BCM": None, "is_gpio": False},
    {"physical": 40, "name": "GPIO.29", "mode": None, "value": None, "BCM": 21, "is_gpio": True},
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