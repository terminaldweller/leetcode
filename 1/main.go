package main

import "fmt"

func twoSum(nums []int, target int) []int {
	dict := make(map[int][]int, len(nums))
	for i := 0; i < len(nums); i++ {
		dict[nums[i]] = append(dict[nums[i]], i)
	}
	// fmt.Println(dict)

	if target%2 == 0 {
		if _, ok := dict[target/2]; ok {
			// fmt.Println(len(dict[target/2]))
			if len(dict[target/2]) >= 2 {
				// fmt.Println("one")
				return []int{dict[target/2][0], dict[target/2][1]}
			}
		}
	}
	for key, val := range dict {
		if _, ok := dict[target-key]; ok {
			if val[0] != dict[target-key][0] {
				return []int{val[0], dict[target-key][0]}
			}
		}
	}

	return []int{100, 100}
}

func main() {
	fmt.Println(twoSum([]int{2, 7, 11, 15}, 9))
	fmt.Println(twoSum([]int{3, 2, 4}, 6))
	fmt.Println(twoSum([]int{3, 3}, 6))
}
