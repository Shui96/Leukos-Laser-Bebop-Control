# -*- coding: utf-8 -*-
"""
BebopControl.py
=====================
Author: SHUI Yuyang
Date: 2024/MAR/21
Python Version: 3.10.13
"""
import clr
import sys
import os
import shutil


# Function to add the DLL path to the system path and load the BebopAPI assembly
def load_bebop_api(dll_path=r"C:\Program Files\Leukos\Bebop"):
    sys.path.append(dll_path)
    clr.AddReference("BebopAPI")
    from Leukos.BebopAPI import BebopDevice, Devices

    return Devices


# Function to initialize and connect to the first Bebop device found
def connect_to_bebop(Devices):
    if not os.path.exists(Devices.IniFileName):
        print("Device information file does not exist. Copying the default file.")
        source_path = r"C:\Program Files\Leukos\Bebop\Config\device.ini"
        target_path = Devices.IniFileName
        os.makedirs(os.path.dirname(target_path), exist_ok=True)
        shutil.copy(source_path, target_path)
        print(f"Default device information file copied to {Devices.IniFileName}.")
    else:
        print(f"Device information file exists at {Devices.IniFileName}.")
    print(f'Get device information from "{Devices.IniFileName}".')
    Devices.init()
    bebop = Devices.Bebop
    if bebop is not None and bebop.Connect():
        print("Bebop device is connected.")
        return bebop
    else:
        print("Failed to connect to Bebop device or no device found.")
        return None


def disconnect_from_bebop(bebop):
    if bebop is not None and bebop.Disconnect():
        print("Bebop device is disconnected.")
        return True
    else:
        print("Failed to disconnect from Bebop device.")
        return False


# Function to check the connection status of the Bebop device
def check_connection(bebop):
    if bebop is not None and bebop.IsOnline:
        print("Bebop device is online.")
        return True
    else:
        print("Bebop device is offline or not connected.")
        return False


# Function to get and print Bebop device wavelength and bandwidth properties
def get_wavelength_bandwidth(bebop):
    if bebop is not None:
        print(
            f"Minimum wavelength: {bebop.WavelengthMin} nm, Maximum wavelength: {bebop.WavelengthMax} nm"
        )
        print(
            f"Minimum bandwidth: {bebop.DeltaMin} nm, Maximum bandwidth: {bebop.DeltaMax} nm"
        )
    else:
        print("Bebop device is not available.")


# Function to set the filter positions of the Bebop device
def set_filter_positions(bebop, low_pass, high_pass):
    if bebop is not None and bebop.SetFilterPosition(low_pass, high_pass):
        print(f"Filter positions set to {low_pass}nm to {high_pass}nm.")
        return True
    else:
        print("Failed to set filter positions.")
        return False


# Function to check if the filters are in the set positions
def check_filters_position(bebop):
    if bebop is not None and bebop.IsOnActivPosition:
        print("Filters are in the set position.")
        return True
    else:
        print("Filters are not in the set position.")
        return False
