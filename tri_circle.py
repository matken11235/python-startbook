def sample(a):
	for i in range(36):
		a.forward(10)
		a.right(10)
		for j in range(3):
			a.forward(50)
			a.right(120)