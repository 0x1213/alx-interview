#!/usr/bin/env python3
def pascal_triangle(n):
    if n <= 0: return []
    for i in range(n):
        print([i + 1 for i in range(i + 1)])

pascal_triangle(5)
