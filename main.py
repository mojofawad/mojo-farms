from __builtins__ import *
from farmer import farm
import prioritizer

while True:
	pumpkin_needed = 0
	
	priority_item = prioritizer.get_priority()
	unlockable = priority_item[0]
	item_needed = priority_item[1]
	while num_unlocked(unlockable) == 0:
		if not (unlock(unlockable)):			
			for i in item_needed:
				while num_items(i) < item_needed[i]:
					print("farming for: ", i)
					list_to_farm = [i]
					farm(list_to_farm)
				farm()