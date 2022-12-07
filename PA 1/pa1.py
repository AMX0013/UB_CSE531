# Python 3 program to count inversions in an array

# Function to Use Inversion Count


# change and refactor maadi maga




def mergeSort(arr, n):
    # A temp_arr is created to store
    # sorted array in merge function
    temp_arr = [0]*n
    return _mergeSort(arr, temp_arr, 0, n-1)

# This Function will use MergeSort to count inversions


def _mergeSort(arr, temp_arr, left, right):

    # A variable count_inversions is used to store
    # inversion counts in each recursive call

    count_inversions = 0

    # We will make a recursive call if and only if
    # we have more than one elements

    if left < right:

        # mid is calculated to divide the array into two subarrays
        # Floor division is must in case of python

        mid = (left + right)//2

        # It will calculate inversion
        # counts in the left subarray

        count_inversions += _mergeSort(arr, temp_arr,left, mid)

        # It will calculate inversion
        # counts in right subarray

        count_inversions += _mergeSort(arr, temp_arr,mid + 1, right)

        # It will merge two subarrays in
        # a sorted subarray

        count_inversions += merge(arr, temp_arr, left, mid, right)
    return count_inversions

# This function will merge two subarrays
# in a single sorted subarray


def merge(arr, temp_arr, left, mid, right):
    i = left	 # Starting index of left subarray
    j = mid + 1  # Starting index of right subarray
    k = left	 # Starting index of to be sorted subarray
    count_inversions = 0

    # Conditions are checked to make sure that
    # i and j don't exceed their
    # subarray limits.

    while i <= mid and j <= right:

        # There will be no inversion if arr[i] <= arr[j]

        if arr[i] <= arr[j]:
            temp_arr[k] = arr[i]
            k += 1
            i += 1
        else:
            # Inversion will occur.
            temp_arr[k] = arr[j]
            count_inversions += (mid-i + 1)
            k += 1
            j += 1

    ## Copy  remaining elements of left
    # subarray into temp
    while i <= mid:
        temp_arr[k] = arr[i]
        k += 1
        i += 1

    ## Copy  remaining elements of right
    # subarray into temp
    while j <= right:
        temp_arr[k] = arr[j]
        k += 1
        j += 1

    # Copy the sorted subarray into the OG
    for loop_var in range(left, right + 1):
        arr[loop_var] = temp_arr[loop_var]

    return count_inversions


# Driver Code

def accept_input():
    lines = []
    n = input()
    arr_index = 0
    while arr_index < int(n):
        user_in = input()

        # break out of read loop
        if user_in == '':
            break
        else:
            lines.append(int(user_in))
        arr_index += 1

    return lines


# input_arr = [1, 20, 6, 4, 5]
input_arr = accept_input()
n = len(input_arr)

result = mergeSort(input_arr, n)
print(result)

