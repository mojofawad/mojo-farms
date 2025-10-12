from __builtins__ import *
import accountant

def get_locked_items():
	locked_items = dict()
	# for item in Unlocks:
		# if num_unlocked(item) == 0:
		# 	locked_items[item] = accountant.get_costs_of_item(item)
	for unlock in Unlocks:
		cost = get_cost(unlock)
		for i in cost:
			if cost[i] != None and cost[i] != 0:
				locked_items[unlock] = accountant.get_costs_of_item(unlock)
				break
	return locked_items		