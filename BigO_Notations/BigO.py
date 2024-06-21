# Constant time complexity O(1)
# The operation inside the function takes a constant amount of time regardless of the input values.
def add(a, b):
    c = a + b
    return c

# Linear time complexity O(N)
# The loop runs N times, so the time complexity is directly proportional to the size of the input N.
def printNumbers(N):
    for i in range(N):
        print(i)

# Linear time complexity O(N+M)
# The first loop runs N times and the second loop runs M times, making the total time complexity O(N+M).
def printTables(N, M):
    for i in range(N):
        print(i * N)
    for j in range(M):
        print(j * M)

# Quadratic time complexity O(N^2)
# There are two nested loops, each running N times. Therefore, the time complexity is O(N * N) = O(N^2).
def printQuadratic(N):
    for i in range(N):
        for j in range(N):
            print(i, j)

# Cubic time complexity O(N^3)
# There are three nested loops, each running N times. Therefore, the time complexity is O(N * N * N) = O(N^3).
def printCubic(N):
    for i in range(N):
        for j in range(N):
            for k in range(N):
                print(i, j, k)

# Logarithmic time complexity O(log N)
# The loop runs logarithmically, halving the size of the input each time.
def printLogarithmic(N):
    i = 1
    while i < N:
        print(i)
        i *= 2

# Linearithmic time complexity O(N log N)
# The outer loop runs N times and the inner loop runs logarithmically.
def printLinearithmic(N):
    for i in range(N):
        j = 1
        while j < N:
            print(i, j)
            j *= 2

# Exponential time complexity O(2^N)
# The function calls itself twice for each call, leading to an exponential growth in calls.
def printExponential(N):
    if N == 0:
        return
    print(N)
    printExponential(N-1)
    printExponential(N-1)

# Factorial time complexity O(N!)
# The function generates all permutations of the input, which leads to a factorial number of operations.
def printFactorial(N):
    def permute(nums, l, r):
        if l == r:
            print(nums)
        else:
            for i in range(l, r + 1):
                nums[l], nums[i] = nums[i], nums[l]
                permute(nums, l + 1, r)
                nums[l], nums[i] = nums[i], nums[l]  # backtrack

    nums = list(range(1, N + 1))
    permute(nums, 0, N - 1)
