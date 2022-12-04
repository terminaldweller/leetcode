package main

import (
	"fmt"
)

func minimumAverageDifference(nums []int) int {
	ave_l := 0
	num_count := len(nums)
	if num_count == 1 {
		return 0
	}
	ave_r := func(nums []int) int {
		sum := 0
		for i := 1; i < num_count; i++ {
			sum += nums[i]
		}
		return sum
	}(nums)
	ave_l = nums[0]
	// averageDifferences := make(map[int]int, num_count)
	averageDifferences := make([]int, num_count, num_count)
	averageDifferences[0] = ave_l - (ave_r / (num_count - 1))
	if averageDifferences[0] < 0 {
		averageDifferences[0] = -averageDifferences[0]
	}
	for i := 1; i < num_count-1; i++ {
		ave_l = (ave_l + nums[i])
		ave_r = (ave_r - nums[i])
		averageDifferences[i] = (ave_l / (i + 1)) - (ave_r / (num_count - i - 1))
		if averageDifferences[i] < 0 {
			averageDifferences[i] = -averageDifferences[i]
		}
		// fmt.Println(ave_l, ave_r, averageDifferences[i])
	}
	ave_l = ave_l + nums[num_count-1]
	averageDifferences[num_count-1] = ave_l / num_count
	if averageDifferences[num_count-1] < 0 {
		averageDifferences[num_count-1] = -averageDifferences[num_count-1]
	}

	min := averageDifferences[0]
	min_k := 0
	for k, v := range averageDifferences {
		if v < min {
			min = v
			min_k = k
		}
	}

	// fmt.Println(averageDifferences)
	return min_k
}

func main() {
	fmt.Println(minimumAverageDifference([]int{2, 5, 3, 9, 5, 3}))
	fmt.Println(minimumAverageDifference([]int{0}))
	fmt.Println(minimumAverageDifference([]int{1, 2, 3, 4, 5}))
	fmt.Println(minimumAverageDifference([]int{5, 4, 3, 2, 1}))
	fmt.Println(minimumAverageDifference(GetBig()))
	fmt.Println(minimumAverageDifference([]int{2, 5, 3, 9, 5, 3}))
}
