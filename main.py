from farmer import farm

while True:
	while num_items(Items.Pumpkin) < 5000:
		list_to_farm = [Entities.Pumpkin]
		farm(list_to_farm)
	farm()