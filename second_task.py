# Works for every hex digit
def find_largest_hex(possible):
	answers = []
	for ok in possible:
		for digit in range(16):
			t = ok.copy()
			t.append(digit)
			if (sum(t[i] * 16 ** t[len(t) - i - 1] for i in range(len(t))) + 1) % len(t) == 0: # Condition
				answers.append(t)
	return answers

k = [[i] for i in range(1, 16)]
d = {i: [] for i in range(16)}
for n in range(2, 38):
	k = find_largest_hex(k) 
	if n % 2 == 1: # Odd len
		for p in k:
			d[p[len(p) // 2]] = p # Update with largest value

for key in d:
	print ('0123456789ABCDEF'[key], '->', ''.join('0123456789ABCDEF'[d[key][i]] for i in range(len(d[key]))))
