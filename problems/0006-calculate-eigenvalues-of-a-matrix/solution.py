import numpy as np

def calculate_eigenvalues(matrix: list[list[float|int]]) -> list[float]:

	eigenvalues = np.linalg.eigvals(matrix)
	eigenvalues = sorted(eigenvalues, reverse=True)
	return eigenvalues