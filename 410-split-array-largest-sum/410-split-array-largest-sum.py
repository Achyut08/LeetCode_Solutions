class Solution:
	def splitArray(self, nums: List[int], m: int) -> int:

		def max_sum_required(max_sum_value):

			current_sum = 0
			split_required = 0

			for i in range(len(nums)):

				if current_sum + nums[i] <= max_sum_value:
					current_sum = current_sum + nums[i]
				else:
					current_sum = nums[i]
					split_required = split_required + 1

			return split_required + 1

		result = 0

		low = max(nums)

		high = sum(nums)

		while low <= high:

			max_sum_value = ( low + high ) // 2

			if max_sum_required(max_sum_value) <= m:

				high = max_sum_value - 1

				result = max_sum_value

			else:

				low = max_sum_value + 1

		return result