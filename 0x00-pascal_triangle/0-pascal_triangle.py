#!/usr/bin/python3
"""
0. Pascal's Triangle
"""


def pascal_triangle(n):
	"""Create a function def pascal_triangle(n): that returns a list of lists
	of integers representing the Pascal’s triangle of n
	"""
	triangle = []
	if n <= 0: return triangle
	prev_row = [1]
	triangle.append(prev_row[:])
	for _ in range(n - 1):
		prev_row.append(0)
		prev_row = [0] + prev_row
		next_row = []
		for i in range(len(prev_row) - 1):
			next_row.append(prev_row[i] + prev_row[i + 1])
		triangle.append(next_row[:])
		prev_row = next_row
	return triangle
