"""
Given an array arr[], find the maximum j – i such that arr[j] > arr[i]
Given an array arr[], find the maximum j – i such that arr[j] > arr[i].

Examples:

  Input: {34, 8, 10, 3, 2, 80, 30, 33, 1}
  Output: 6  (j = 7, i = 1)

  Input: {9, 2, 3, 4, 5, 6, 7, 8, 18, 0}
  Output: 8 ( j = 8, i = 0)

  Input:  {1, 2, 3, 4, 5, 6}
  Output: 5  (j = 5, i = 0)

  Input:  {6, 5, 4, 3, 2, 1}
  Output: -1
  """

  #Version 1: Brute Force

  #Version 2:
  def solution(a):
      n = len(a)
      lmin = [i for i in a] # min val in a[:i+1]
      rmax = [i for i in a] # max val in a[i:]
      for i in range(1, n):
          lmin = min(a[i], lmin(i-1))
      for i in range(n-2, -1, -1):
          rmax = max(a[i], rmax[i+1])

      i = j = 0
      maxDiff = 0
      while i < n and j < n:
          if lmin[i] < rmax[j]:
              maxDiff = max(maxDiff, j-i)
              j += 1
          else:
              i += 1
      return maxDiff
