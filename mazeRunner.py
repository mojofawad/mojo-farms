from __builtins__ import *
import mover

def prepare_plot():
	if can_harvest():
		harvest()
	plant(Entities.Bush)

	while not can_harvest():
		do_a_flip()


def make_maze():
	quantity = get_quantity()
	use_item(Items.Weird_Substance, quantity)

def get_quantity():
	return get_world_size() * 2 ** (num_unlocked(Unlocks.Mazes) - 1)

def solve_maze():
	ix, directions = 0, [North, East, South, West]
	index = 0

	while True:
		if (get_entity_type() == Entities.Treasure):
			harvest()
			break
		else:
			ix += 1 - move(directions[ix % 4])*2

def run_maze():
	mover.go_home()
	prepare_plot()
	make_maze()
	solve_maze()