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
    Returns the lowest bus number found, or 1 as a fallback.'''
    try:
        devices = [f for f in os.listdir('/dev/') if f.startswith('i2c-')]
        if devices:
            return sorted([int(d.split('-')[1]) for d in devices])[0]
    except (OSError, ValueError):
        pass
    return 1
