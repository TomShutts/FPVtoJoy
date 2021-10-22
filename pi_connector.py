"""
Connects to the raspberry Pi GPIO pins
"""

from gpiozero.pins.pigpio import PiGPIOFactory
from gpiozero import DigitalInputDevice
from time import perf_counter_ns


def setup_callbacks(ip_address: str, pins: list):
    # Setups a link with the IP address and creates callbacks for the pins
    factory = PiGPIOFactory(host=ip_address)
    for pin in pins:
        device = DigitalInputDevice(pin, pin_factory=factory)
        PPMDevice(device)


class PPMDevice:
    def __init__(self, device):
        self.device = device
        # Setting the callbaks
        self.device.when_activated = self.callback_high
        self.device.when_deactivated = self.callback_low
        
        self.pulse_start = perf_counter_ns()
        self.pulse_end = perf_counter_ns()

        self.pulses = []
        self.frames = []

    def callback_high(self):
        self.frames.append(perf_counter_ns() - self.pulse_start)
        self.pulse_start = perf_counter_ns()

    def callback_low(self):
        self.pulse_end = perf_counter_ns()
        self.pulses.append(self.pulse_end - self.pulse_start)