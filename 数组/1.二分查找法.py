class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #选用闭区间来搜
        # 1.初始化左右指针
        left = 0
        right = len(nums)-1
        # 2.二分搜索
        # 2.1 因为是闭区间搜索，所以left可以=right
        while left<=right:
            # 2.2 取中点地板除
            mid = left + ((right-left)//2)
            # 2.3 判断中点和target的关系
            # 2.3.1 相等情况
            if nums[mid] == target:
                return mid
            # 2.3.2 大于情况,移动右指针到mid-1,因为mid已经搜过了
            if nums[mid] > target:
                right = mid -1
                continue
            # 2.3.3 小于情况,移动左指针到mid+1,因为mid已经搜过了
            elif nums[left] < target:
                left = mid+1
        return -1
