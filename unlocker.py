from __builtins__ import *
import accountant

def get_locked_items():
	locked_items = dict()
	for item in Unlocks:
		if num_unlocked(item) == 0:
			locked_items[item] = accountant.get_costs_of_item(item)
	return locked_items		