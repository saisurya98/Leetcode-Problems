class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        #the idea is to make two arrays fwd arry nd back array for given [1,2,3,4]
        # so  fwd_arry=[1,1,2,6]  &bck_arry=[24,12,4,1] and multiply them to get the required.
        # You can use a running product to get the forwd & backwrd arrays.
        # the reason for the approach is we are not allowed to use a division operator
        #TC, SC-O(N)
        fwd = [1 if i == 0 else 0 for i in range(len(nums))]
        fwd_prod = 1

        for i in range(len(nums) - 1):
            fwd_prod = fwd_prod * nums[i]
            fwd[i + 1] = fwd_prod

        bck = [1 if i == len(nums) - 1 else 0 for i in range(len(nums))]
        bck_prod = 1

        for i in range(len(nums) - 1, 0, -1):
            bck_prod = bck_prod * nums[i]
            bck[i - 1] = bck_prod
        ans = []

        for i in range(len(nums)):
            ans.append(fwd[i] * bck[i])
        return ans







