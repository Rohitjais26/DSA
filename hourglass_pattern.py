
# 2D array
# hourglass pattern
# bounds
# Brute force
# Tracking maximum correctly - 1) inf and -inf, 2) first element of the 2D array
def hourglassSum(arr):
    max_sum = float('-inf')  # handles all-negative cases

    # i and j are top-left positions of the hourglass
    for i in range(4):        # 0 to 3
        for j in range(4):    # 0 to 3
            current = (
                arr[i][j] + arr[i][j+1] + arr[i][j+2]
                + arr[i+1][j+1] +
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            )
            max_sum = max(max_sum, current)

    return max_sum