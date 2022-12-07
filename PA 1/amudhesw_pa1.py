class DnC():
    def inversionCounter(self,arr, temp_arr, left, right):

        count_inversions = 0

        if left < right:

            mid = (left + right)//2

            #recurse left half
            count_inversions += self.inversionCounter(arr, temp_arr,left, mid)

            #recurse right half
            count_inversions += self.inversionCounter(arr, temp_arr,mid + 1, right)

            #at the depths of the recursion stack, compute inversions
            count_inversions += self.detectInversions(arr, temp_arr, left, mid, right)
        return count_inversions



    def detectInversions(self,arr, temp_arr, left, mid, right):
        i = left	 # Starting index of left subarray
        j = mid + 1  # Starting index of right subarray
        k = left	 # Starting index of to be sorted subarray
        count_inversions = 0

        #identify inversions
        '''
        Inversions occur when arr[i] > arr[j] but i < j

         In a way it tells us how many steps we are, away from a completely sorted list i.e : 
         arr[i] <= arr[j] and i < j

        '''
        while i <= mid and j <= right:
            if arr[i] <= arr[j]:
                temp_arr[k] = arr[i]
                k += 1
                i += 1
            else:
                temp_arr[k] = arr[j]
                count_inversions += (mid-i + 1)
                k += 1
                j += 1
        ## Copy  remaining elements of left subarray into temp
        while i <= mid:
            temp_arr[k] = arr[i]
            k += 1
            i += 1

        ## Copy  remaining elements of right subarray into temp
        while j <= right:
            temp_arr[k] = arr[j]
            k += 1
            j += 1



        # Copy the sorted subarray into the OG
        for edits in range(left, right + 1):
            arr[edits] = temp_arr[edits]

        return count_inversions


   
constructed_list = []
n = int(input())
arr_index = 0
# read lines of arr inputs
for arr_index in range(n):
    user_in = input()
    if user_in != '':
        constructed_list.append(int(user_in))
    else:
        break
temp = [0]*n
ic = DnC()
print(ic.inversionCounter(constructed_list, temp, 0, n-1) )
