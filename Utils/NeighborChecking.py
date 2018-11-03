positionIndices = ((1, 2), (0, 2), (0, 1), (0, 0), (1, 0), (2, 0), (2, 1), (2, 2))

def indexToPattern(index):
	grid = [
	[0, 0, 0],
	[0, 0, 0],
	[0, 0, 0]]
	for p in reversed(range(8)):
		if index >= 2**p:
			index -= 2**p
			grid[positionIndices[p][0]][positionIndices[p][1]] = 1
	return(grid)


def patternToIndex(pattern):
	# Turn a 3x3 pattern of tile neighbors (bools or ints 0/1) into an index between 0 and 255
	index = 0
	for p in range(8):
		x, y = positionIndices[p]
		if pattern[x][y]:
			index += 2**p
	return(index)


def multiPatternToIndex(patterns):
	# Generate a list of indices for each pattern in the list and all rotations
	indices = []
	for p in patterns:
		pr1 = tuple(zip(*reversed(p)))
		pr2 = tuple(zip(*reversed(pr1)))
		pr3 = tuple(zip(*reversed(pr2)))
		indices.append(patternToIndex(p))
		indices.append(patternToIndex(pr1))
		indices.append(patternToIndex(pr2))
		indices.append(patternToIndex(pr3))
	return(indices)


if __name__ == "__main__":
	pat = indexToPattern(17)
	for i in pat:
		print(i)