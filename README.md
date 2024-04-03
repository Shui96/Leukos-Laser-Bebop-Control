# README for BebopControl and Sample Usage

## Overview

This repository contains Python code for controlling the Bebop tunable wavelength filter from Leukos Laser. The primary script, `BebopControl.py`, provides functionalities to load the Bebop API, connect to the Bebop device, manipulate filter positions, and check the device's status. Additionally, `sample.py` demonstrates how to use these functionalities in a practical scenario.

## Requirements

- Python 3.x
- BebopAPI DLL and Initialization file `device.ini` (provided by Leukos Laser, typically installed with the device software)
- .NET runtime compatible with Python (required for the `pythonnet` package to interface with .NET assemblies)

## Installation

1. Ensure Python and the .NET runtime are installed on your system.
2. Place the `BebopControl.py` and `sample.py` in your project directory.
3. Verify that the BebopAPI DLL is installed in the default directory (`C:\Program Files\Leukos\Bebop`). If not, you will need to modify the `dll_path` in `BebopControl.py` to match your installation path.
4. Verify that the Initialization file `device.ini` is in the default directory (`C:\Program Files\Leukos\Bebop\Config\device.ini`). If not, you will need to modify the `source_path` in `BebopControl.py` to match your path.

## Usage

### BebopControl.py

This script includes several functions:

- `load_bebop_api()`: Loads the Bebop API into the Python environment.
- `connect_to_bebop()`: Connects to the Bebop device.
- `disconnect_from_bebop()`: Disconnects from the Bebop device.
- `check_connection()`: Checks the connection status of the Bebop device.
- `get_wavelength_bandwidth()`: Retrieves and prints the max & min wavelength and bandwidth settings of the Bebop device.
- `set_filter_positions()`: Sets the filter positions of the Bebop device.
- `check_filters_position()`: Checks if the filters are in the set positions.

### sample.py

A simple example demonstrating how to use `BebopControl.py` to connect to a Bebop device, check its status, set filter positions, and then disconnect.

## Contributing

Contributions to improve the code or extend its functionalities are welcome. Please feel free to submit pull requests or open issues to discuss potential improvements.

## License

Please ensure you comply with the licensing terms of the BebopAPI and any other dependencies. This project itself is distributed under the MIT license, allowing free use, modification, and distribution of the code.

## Acknowledgments

Thanks to Leukos Laser for providing the corresponding API that made this project possible.
