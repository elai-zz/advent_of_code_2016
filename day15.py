def is_at_zero(time, disc, offset, positions):
	return (time + disc + offset) % (positions) == 0

def run(is_part_2):
	t = 0
	while True:
		d1 = is_at_zero(t, 1, 15, 17)
		d2 = is_at_zero(t, 2, 2, 3)
		d3 = is_at_zero(t, 3, 4, 19)
		d4 = is_at_zero(t, 4, 2, 13)
		d5 = is_at_zero(t, 5, 2, 7)
		d6 = is_at_zero(t, 6, 0, 5)
		d7 = is_at_zero(t, 7, 0, 11)
		if is_part_2:
			if d1 and d2 and d3 and d4 and d5 and d6 and d7:
				return t
		else:
			if d1 and d2 and d3 and d4 and d5 and d6:
				return t
		t += 1

print run(True)
