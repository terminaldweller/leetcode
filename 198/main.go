package main

import "fmt"

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func rob(nums []int) int {
	nlen := len(nums)

	switch nlen {
	case 0:
		return 0
	case 1:
		return nums[0]
	case 2:
		return max(nums[0], nums[1])
	case 3:
		return max(nums[1], nums[0]+nums[2])
	}

	dp := make([]int, nlen)

	dp[0] = nums[0]
	dp[1] = nums[1]
	dp[2] = nums[0] + nums[2]

	for i := 3; i < nlen; i++ {
		dp[i] = max(dp[i-2]+nums[i], dp[i-3]+nums[i])
	}

	return max(dp[len(dp)-1], dp[len(dp)-2])
}

func main() {
	fmt.Println(rob([]int{1, 100, 5, 4, 100, 1}))
	fmt.Println(rob([]int{1, 2, 3, 1}))
	fmt.Println(rob([]int{2, 7, 9, 3, 1}))
	fmt.Println(rob([]int{2, 3, 2}))
	fmt.Println(rob([]int{1, 1, 1, 2}))
}
