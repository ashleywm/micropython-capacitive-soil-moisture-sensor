import machine
from src.CSMS import CSMS

adc = machine.ADC(machine.Pin(36))

csms = CSMS(adc, min_value=3494, max_value=1868)

print(csms.read(25), '% Soil Moisture')
