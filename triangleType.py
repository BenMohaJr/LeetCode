class Solution:
    def triangleType(self, nums: List[int]) -> str:
        triangles = {
            1: 'equilateral',
            2: 'isosceles',
            3: 'scalene'
        }
        nums.sort()
        if nums[0] + nums[1] <= nums[2]:
            return 'none'
        return triangles[len(set(nums))]
