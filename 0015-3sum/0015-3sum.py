class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        result = []
        n = len(nums)

        for i in range(n):
            if i > 0 and nums[i] == nums[i - 1]:
                continue

            leftu = i + 1
            right = n - 1

            while leftu < right:
                total = nums[i] + nums[leftu] + nums[right]

                if total == 0:
                    result.append([nums[i], nums[leftu], nums[right]])
                    leftu += 1
                    right -= 1

                    while leftu < right and nums[leftu] == nums[leftu - 1]:
                        leftu += 1
                    while leftu < right and nums[right] == nums[right + 1]:
                        right -= 1

                elif total < 0:
                    leftu += 1

                else:
                    right -= 1

        return result
        