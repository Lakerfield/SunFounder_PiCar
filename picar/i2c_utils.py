#!/usr/bin/env python
'''
**********************************************************************
* Filename    : i2c_utils.py
* Description : Shared I2C utility functions
* Brand       : SunFounder
* E-mail      : service@sunfounder.com
* Website     : www.sunfounder.com
**********************************************************************
'''
import os


def get_i2c_bus_number():
    '''Auto-detect the I2C bus number by scanning /dev/ for i2c-* devices.
    Prefers bus 1 (the standard Raspberry Pi user I2C bus on GPIO2/GPIO3),
    then returns the lowest numeric bus number found, or 1 as a fallback.
    Non-numeric device names (e.g. i2c-vc) are silently skipped.'''
    try:
        bus_numbers = []
        for device in os.listdir('/dev/'):
            if device.startswith('i2c-'):
                try:
                    bus_numbers.append(int(device.split('-')[1]))
                except (ValueError, IndexError):
                    pass  # skip non-numeric i2c devices such as i2c-vc
        if bus_numbers:
            if 1 in bus_numbers:
                return 1  # prefer bus 1 (standard Raspberry Pi user I2C)
            return sorted(bus_numbers)[0]
    except OSError:
        pass
    return 1
