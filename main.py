#!/usr/bin/env python3

import sys
import os
import argparse
import myClass

# Defining & finding prosess function using os module
def find_process(pname):
    process_name = os.popen('ps -ef | grep ' + pname + ' | grep -v grep | grep -v ' + sys.argv[0]).read().splitlines()
    return process_name

# tot_m, used_m, free_m = map(int, os.popen('free -t -m').readlines()[-1].split()[1:])

# main program geting help from rikards parse algorithms
if __name__ == "__main__":

    parser = argparse.ArgumentParser(description="Write something here!")
    parser.add_argument('-i', '--info', help="More information! ", action="store_true")
    parser.add_argument('text', help="Write process id: .")

    arguments = parser.parse_args()
# if funktion to check the argument and finally getting the user_input to kill the running process
    if (len(arguments.text) > 0):
        if (arguments.info):
            print(arguments.text.upper() + "!?")
        else:
            array = []
            output = find_process(arguments.text)
            print(f" Running process list: {arguments.text}")
            for i in range (0,len(output)):
                txt1 = output[i]
                txtlist = txt1.split()
                procObj = myClass.Process(txtlist[0], txtlist[1])
                myClass.Process.show_process(procObj)
                array.append(txtlist[1])
            user_input = input("write process -id to kill: ")
            if user_input in array:
                myClass.Process.kill_process(user_input)
    else:
        print("You have to write something! ")

