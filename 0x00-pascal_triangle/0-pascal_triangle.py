#!/usr/bin/python3
"""pascal triangle """



def pascal_triangle(n):
  """
  Returns:
      A list of lists containing the integers of Pascal's triangle.
      Returns an empty list if n is less than or equal to 0.
  """

  if n <= 0:
    return []

  triangle = [[1]]

  for i in range(1, n):
    prev_row = triangle[i-1]
    cur_row = [1]
    for j in range(1, i):
      cur_row.append(prev_row[j-1] + prev_row[j])
    cur_row.append(1)
    triangle.append(cur_row)

  return triangle
