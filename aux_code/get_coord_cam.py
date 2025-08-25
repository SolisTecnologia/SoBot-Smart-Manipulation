import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from aux_functions import get_arm_coord_from_camera, Connect_Dobot


Connect_Dobot()

get_arm_coord_from_camera()

while True:
    pass