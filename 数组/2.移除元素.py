class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # 初始化快慢指针,和计数器k
        slow = 0
        fast = 0
        k = 0
        # 判断快指针是否指向的是删除目标值
        while fast < len(nums):
            # 如果不是，则赋值,k+1
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow += 1
                k += 1
            # 无论是不是fast都判断下一个数
            fast += 1
        return k


