from ax12 import Ax12
import math
import time
import mido
import sys
import os

def accept_control(port):
    """Only let note_on and note_off messages through."""
    for message in port:
        if message.type in ('control_change'):
            yield message


MIN = 0
MAX = 700


def main(motor: Ax12):
    lastTime = time.time()
    goal = None
    w = 0.0
    if len(sys.argv) > 1:
        ortname = sys.argv[1]
    else:
        portname = None  # Use default port

    try:
        with mido.open_input(portname) as port:
            print(f'Using {port}')

            print("Ignoring everything but 'note_on' and 'note_off'.")
            print('Waiting for notes...')

            for message in accept_control(port):
                    print(f'Received {message}')
                    print('Volume changed to', message.value)
                    goal = message.value/127*MAX
                    print("Moving to", goal)
                    motor.set_goal_position(int(goal))

    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)






           
         


if __name__ == "__main__":
    Ax12.DEVICENAME = 'COM3'
    Ax12.BAUDRATE = 1_000_000

    # sets baudrate and opens com port
    Ax12.connect('COM3')

    my_dxl = Ax12(1)
    my_dxl.set_moving_speed(0)
    my_dxl.set_torque_enable(1)
    my_dxl.set_led(1)
    
    
    main(my_dxl)
