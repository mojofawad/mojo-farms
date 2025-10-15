from __builtins__ import *
import unlocker

unlocked_items = set()

def unlock_item(item):
	unlock(item)

def get_priority():
	items = unlocker.get_locked_items()
	
	priority = get_easiest_priority(items)

	return priority

def get_easiest_priority(items):
	for item in items: # wtf?
		priority_item = get_cheapest(items)
	
	return priority_item

def get_cheapest(items):
	unlocked_items = get_items()
	priority_item = (None, 0)
	for i in items:
		item = items[i]
		for key in item:
			if priority_item[0] == None and key in unlocked_items:
				priority_item = i, items[i]
			#elif len(item) > 1 and key in unlocked_items:
				#get_cheapest(item)
				#do_a_flip()
			elif len(item) == 1 and key in unlocked_items:
				priority = priority_item[1]
				priority_quantity = priority_item[1]
				for this_key in priority_quantity:
					if item[key] < priority_quantity[this_key]:
						priority_item = i, item
							
	return priority_item
	
def get_items():
	items = set()
	items_to_skip = [Items.Gold, Items.Water, Items.Fertilizer, Items.Bone]
	for item in Items:
		if num_unlocked(item) != 0 and item not in items_to_skip:
			items.add(item)
	# if len(items) == 0:
	# 	for item in Unlocks:
	# 		if num_unlocked(item) != 0:
	# 			items.add(item)
	return items
			
