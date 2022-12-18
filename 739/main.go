package main

import "fmt"

func dailyTemperaturesDummy(temperatures []int) []int {
	l := len(temperatures)
	res := make([]int, l)
	for i := 0; i < l; i++ {
		for j := i + 1; j < l; j++ {
			if temperatures[j] > temperatures[i] {
				res[i] = j - i
				break
			}
		}
	}

	return res
}

func dailyTemperatures(temperatures []int) []int {
	l := len(temperatures)
	ret := make([]int, l)
	stack := make([]int, 0)

	for i := 0; i < l; i++ {
		for len(stack) > 0 && temperatures[stack[len(stack)-1]] < temperatures[i] {
			ret[stack[len(stack)-1]] = (i - stack[len(stack)-1])
			stack = stack[:len(stack)-1]
		}

		stack = append(stack, i)
	}

	return ret
}

func main() {
	fmt.Println(dailyTemperatures([]int{73, 74, 75, 71, 69, 72, 76, 73}))
	fmt.Println(dailyTemperatures([]int{30, 40, 50, 60}))
	fmt.Println(dailyTemperatures([]int{30, 60, 90}))
	fmt.Println(dailyTemperatures([]int{90, 60, 90}))
}
