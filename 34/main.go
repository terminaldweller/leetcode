package main

import "fmt"

func explore(nums []int, index int) []int {
	low := index
	high := index
	for {
		if low-1 >= 0 {
			if nums[low-1] == nums[index] {
				low--
			} else {
				break
			}
		} else {
			break
		}
	}

	for {
		if high+1 < len(nums) {
			if nums[high+1] == nums[index] {
				high++
			} else {
				break
			}
		} else {
			break
		}
	}

	return []int{low, high}
}

func searchRange(nums []int, target int) []int {
	low := 0
	high := len(nums) - 1

	for low <= high {
		median := (high + low) / 2
		fmt.Println(low, high, median)
		if target > nums[median] {
			low = median + 1
		} else {
			high = median - 1
		}
	}

	if low == len(nums) || nums[low] != target {
		return []int{-1, -1}
	}

	return explore(nums, low)
}

func main() {
	nums1 := []int{5, 7, 7, 8, 8, 10}
	nums2 := []int{5, 7, 7, 8, 8, 10}
	nums3 := []int{}
	nums5 := []int{5, 7, 7, 8, 8, 10}
	nums4 := []int{1}
	fmt.Println(searchRange(nums3, 0))
	fmt.Println(searchRange(nums1, 8))
	fmt.Println(searchRange(nums2, 6))
	fmt.Println(searchRange(nums5, 1))
	fmt.Println(searchRange(nums5, 100))
	fmt.Println(searchRange(nums4, 1))
}
