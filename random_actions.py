import time
import gym

from gym_rooms.envs import *
env_list = [key for key, _ in gym.envs.registry.env_specs.items()]

environment = 'Rooms-v0'
env = gym.make(environment)
max_steps = 1000
max_episodes = 10
total_steps = 0

for i in range(max_episodes):
	s = env.reset()
	for j in range(max_steps):			
		a = env.action_space.sample()
		sp, r, terminal, step_info = env.step(a)
		env.render()
		total_steps += 1
		s = sp
		time.sleep(0.05)
		
		if terminal:
			print('solved the rooms task!')
			break

env.close()


