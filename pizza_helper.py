import pyautogui as pg
import numpy as np
import math

def sauce_spiral(angle_step=1, distance_step=50, radius=500):
	direction = 0

	# init_pos = np.array(pg.position())
	# pos = init_pos

	width,height = pg.size()

	print("Parameters used:\n\tAngle Step Size: {}\n\tDistance Step Size: {}\n\tRadius: {}".format(angle_step,distance_step,radius))
	# print("\nInitial Conditions:\n\tWidth: {}\n\tHeight: {}\n\tInitial Position: {}".format(width,height,init_pos))

	i = 0
	max_iter = 1**3
	while (True):#np.sum(np.square(init_pos - pos))  <= radius**2):
		step = distance_step * np.array((math.cos(direction), math.sin(direction)))
		step = step.astype(np.int)
		# print("stepping: {}".format(step))

		desired_pos = step + np.array(pg.position());

		# if(desired_pos[0] >= width or desired_pos[0] < 0 or desired_pos[1] >= width or desired_pos[1] < 0 or i >= max_iter):
		# 	print("Stopping due to screen border.")
		# 	break

		pg.move(step[0], step[1], duration=0.1)

		direction += angle_step
		# pos = np.array(pg.position())
		i+=1

sauce_spiral()