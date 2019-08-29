def findMin(rotateArray):
    """
    :type nums: List[int]
    :rtype: int
    """
    # def minNumberInRotateArray(self, rotateArray):
    left = 0
    right = len(rotateArray)-1
    while left < right:
        mid = int((left+right)/2)
        if rotateArray[mid] > rotateArray[right]: # 当mid位置大于right，说明最小值mid右边
            left = mid + 1                        # 且最小不可能是mid，故令left=mid+1
        elif rotateArray[mid] < rotateArray[right]: # 当mid位置小于right，说明最小值mid左边
            right = mid                             # 且有可能最小就是mid，故令right=mid
        else:   # 当right=mid时，如[1,0,1,1,1]，将right往前移一格
            right -= 1
    return rotateArray[left]

a = [1,0,1,1,1]
print(findMin(a))