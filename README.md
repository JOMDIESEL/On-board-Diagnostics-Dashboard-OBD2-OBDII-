# OBD2 Dashboard using ELM327 Bluetooth and Tkinter

## Overview

This Python application creates a dashboard using the Tkinter library to display real-time OBD2 data obtained through an ELM327 Bluetooth adapter. The dashboard showcases various vehicle parameters, such as speed, RPM, coolant temperature, intake pressure, engine load, and more.

## Requirements

- Python 3.x
- Tkinter
- obd library
- ELM327 Bluetooth adapter

## Installation

1. Install the required Python libraries:

   ```bash
   pip install obd
```
## Usage
Launch the application, and the dashboard will display real-time OBD2 data.
The dashboard includes parameters such as speed, RPM, coolant temperature, intake pressure, engine load, and more.
The values are updated continuously through the ELM327 Bluetooth connection.
Customization
You can customize the appearance of the dashboard by modifying the Tkinter elements and styles in the Python script (obd2_dashboard.py).
Adjust the layout, font, and colors according to your preferences.

## OBD2 Parameters
The following OBD2 parameters are displayed on the dashboard:
Speed: Vehicle speed in kilometers per hour (kph).
RPM: Engine revolutions per minute.
Coolant Temperature: Engine coolant temperature in degrees Celsius (degC).
Intake Pressure: Intake pressure in revolutions per minute (rpm).
Engine Load: Engine load as a percentage.
ELM Voltage: Voltage of the ELM327 adapter in volts.
Ambient Air Temperature: Ambient air temperature in degrees Celsius (degC).
Throttle Position: Throttle position as a percentage.
Timing Advance: Timing advance in degrees.
Intake Temperature: Intake air temperature in degrees Celsius (degC).
Commanded Equiv Ratio: Commanded equivalence ratio.
Air-Fuel Ratio (AFR): Calculated air-fuel ratio.

## Notes
Ensure that your ELM327 Bluetooth adapter is properly paired and connected to your computer before running the script.
The obd library is used to communicate with the OBD2 adapter and query various parameters.

## Customization Tips
You can further customize the dashboard appearance and behavior by exploring the Tkinter documentation: Tkinter Documentation.
