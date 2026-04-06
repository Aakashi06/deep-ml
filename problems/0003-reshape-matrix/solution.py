import numpy as np

def reshape_matrix(a, new_shape):
	r, c = new_shape

	if len(a) * len(a[0]) != r*c:
		return[]

	arr = np.array(a)		
	reshaped_matrix = arr.reshape(r, c)
	return reshaped_matrix.tolist()