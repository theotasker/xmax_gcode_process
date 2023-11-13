# for post-processing the temp gcode file exported from Prusa Slicer
# accepts the input file name as an argument
# outputs the processed file to the same directory as the input file
# removes all gcode commands that are not supported by the X-Max, 
# supported commands are listed in xmax_supported_commands.gcode
# in the root directory of this project

import sys
import os
import shutil
import logging
import datetime
from progress.bar import Bar

##############################################################################
# init
##############################################################################

# change cwd to the directory of this file
os.chdir(os.path.dirname(os.path.realpath(__file__)))


LOG_FILE = datetime.datetime.now().strftime('%Y-%m-%d.log')
LOG_PATH = os.path.join('../logs', LOG_FILE)
if not os.path.exists('../logs'):
    os.makedirs('../logs')

logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s',
                        handlers=[
                            logging.FileHandler(LOG_PATH),
                            logging.StreamHandler()
                        ]
                    )

##############################################################################
# functions
##############################################################################

def read_file_to_list(filename, just_gcode=False):
    with open(filename, 'r') as file:
        line_list = file.readlines()
    line_list = [line.strip() for line in line_list]

    if just_gcode:
        line_list = [line.split(' ')[0] for line in line_list 
                        if (line.startswith('G') or line.startswith('M'))]

    return line_list


def remove_unsupported_commands(gcode_file, temp_filename, supported_commands): 
    removed_count = 0

    with open(gcode_file, 'r') as file:
        line_count = len(file.readlines())

    bar = Bar('Processing', max=line_count)

    with open(gcode_file, 'r') as file, open(temp_filename, 'w') as temp_file:
        for line in file:
            if line.startswith(';') or (line == ''):
                temp_file.write(line)
                bar.next()
                continue

            elif line.startswith('G1 '):
                temp_file.write(line)
                bar.next()
                continue

            command = line.split(' ')[0]
            if command not in supported_commands:
                removed_count += 1
                bar.next()
                continue

            else:
                temp_file.write(line)
                bar.next()
                continue

    return removed_count


##############################################################################
# main
##############################################################################

def main():
    logging.debug('Starting xmax_gcode_process.py')

    gcode_file = sys.argv[1]
    logging.debug(f'Retrieved {gcode_file} as the gcode file to process')

    supported_commands = read_file_to_list('../xmax_supported_commands.gcode', just_gcode=True)
    logging.debug(f'Read {len(supported_commands)} supported commands from xmax_supported_commands.gcode')

    temp_filename = '../temp/temp.tmp'
    removed_count = remove_unsupported_commands(gcode_file, temp_filename, supported_commands)
    logging.debug(f'Processed {gcode_file} to {temp_filename}')
    
    shutil.move(temp_filename, gcode_file)
    logging.info(f'Processed {gcode_file}, removed {removed_count} unsupported commands')

    return


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        logging.critical(e)
        raise e