# xmax_gcode_process
Takes sliced GCODE from Prusa Slicer and removes commands incompatible with the QIDI X-Max

In PrusaSlicer, with advanced settings on, under "Output options/Post-processing scripts", place the following:

"<path/to/python/exe>" "<path/to/xmax_gcode_process>/src/xmax_gcode_process.py";

After pressing "Export Gcode" in the slicer, a Python window should show up denoting the current progress. Currently takes about 60 seconds for 1,000,000 lines of gcode
