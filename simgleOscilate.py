from ax12 import Ax12
import math
import time



MOVING_SPEED = 0
FREQ = 1
AMPLITUDE = 500
OFFSET =512


def main(motor: Ax12):
    lastTime = time.time()
    goal = None
    w = 0.0
    while True:
            w = w + (time.time()-lastTime)*math.tau*FREQ
            lastTime =time.time()
            goal = (math.cos(w)*AMPLITUDE)+OFFSET
            goal = int(goal)
            #print(w)
            #print("Moving to", goal)
            motor.set_goal_position(goal)
            #curr_pos = motor.get_present_position()
           
            

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
