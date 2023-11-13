G0         ; Rapid positioning
G1         ; Linear interpolation
G4 P5000   ; Wait for 5000 Milliseconds
G28        ; returns to the reference position
G92        ; Coordinate system setting
M0         ; Pause printing(When continuing to print, start with the next line of code, for Gcode)
M24        ; To continue printing
M25        ; Pause to print(Continue printing from the top line of code for the control panel)
M84        ; Stop printing
M104       ; Set the nozzle temperature
M106       ; Open the fan
M107       ; Close the fan
M109       ; Wait until the nozzle is heated or lowered to the appropriate temperature
M140       ; Set the hot bed temperature
M190       ; Wait until the hot bed is heated or lowered to the appropriate temperature
M141       ; Set the chamber temperature
M221       ; Adjust flow
M4000      ; Read the current state of the device
M4010      ; displays schematic diagram on an panel
M300 I3000 ; Buzzer alarm 3s
M4003      ; Turn off the printer
