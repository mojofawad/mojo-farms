from __builtins__ import *
from farmer import farm
import mazeRunner
import prioritizer
import cactusMaker

while True:
	priority_item = prioritizer.get_priority()
	unlockable = priority_item[0]
	item_needed = priority_item[1]

	if not (unlock(unlockable)):
		for i in item_needed:
			while num_items(i) < item_needed[i]:
				print("unlocking: ", unlockable)
				print("farming for: ", i)
				if i == Items.Gold:
					mazeRunner.run_maze()
				elif i == Items.Cactus:
					cactusMaker.do_cacti()
					harvest()
				else:
					list_to_farm = [i]
					farm(list_to_farm)
			#farm()