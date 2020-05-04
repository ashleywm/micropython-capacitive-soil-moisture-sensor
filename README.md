# MicroPython Capacitive Soil Moisture Sensor

A MicroPython implementation to read a capacitive soil moisture sensor

## Capacitive Soil Moisture Sensor

Unlike resistive soil moisture sensors the capacitive soil moisture sensor is corrosion resistant.

The module is cheap can be commonly found on eBay, Banggood and Alliexpress etc.

### Specification

- Operating Voltage: 3.3 ~ 5.5 VDC
- Output Voltage: 0 ~ 3.0VDC
- Operating Current: 5mA

![Capacitive Soil Moisture Sensor - banggood.com](https://img.staticbg.com/thumb/large/oaupload/banggood/images/DC/36/8f82ca99-5261-41bf-bf73-17038f0eaef0.JPG)

## Usage

**Important before using the sensor you must check the input voltage rating of the ADC on your Microcontroller, failure to do so may damage the IC!**

### Calibration

To use this module, you must first run the calibration. The calibration must be ran in the minimum and maximum environments your sensor is going to run in. For example to get the calibrated minimum value run the sensor in air and then in a cup of water for the maximum.

The calibration function gives you 10 seconds to insert your sensor into the min then max environments.

See calibration_example.py

```python
import machine
from src.CSMS import CSMS

adc = machine.ADC(machine.Pin(36))

csms = CSMS(adc)
csms.calibrate()
```

Serial output should look like the following:

```
Calibration complete! Modify your programs variables with the following results:
min_value =  3494
max_value =  1868
```

### Normal Operation

Once the calibration above is complete, you can then use the calibrated values.

```python
import machine
from src.CSMS import CSMS

adc = machine.ADC(machine.Pin(36))

csms = CSMS(adc, min_value=3494, max_value=1868)

print(csms.read(25), '% Soil Moisture')
```

## Contributing

1. Fork it!
2. Create your feature branch: `git checkout -b my-new-feature`
3. Commit your changes: `git commit -am 'Add some feature'`
4. Push to the branch: `git push origin my-new-feature`
5. Submit a pull request

## License

[MIT](LICENSE.md)
