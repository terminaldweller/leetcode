package main

import (
	"fmt"
	"math"
)

func getNthDigit(num, k int) int {
	result := num
	if k-1 > 0 {
		result -= num - (num/int(math.Pow10(k-1)))*int(math.Pow10(k-1))
	}

	if math.Pow10(k) <= float64(num) {
		result -= (num / int(math.Pow10(k))) * int(math.Pow10(k))
	}
	// result := num - (num/int(math.Pow10(k)))*int(math.Pow10(k)) - (num/int(math.Pow10(k-2)))*int(math.Pow10(k-2))

	result /= int(math.Pow10(k - 1))
	// fmt.Println(num, k, result)
	return result
}

func addToArrayForm(num []int, k int) []int {
	length := int(math.Max(float64(len(num))+1., 5.))
	result := make([]int, length)
	carry := false
	num_index := len(num) - 1

	var sum int

	for i := length - 1; i >= 0; i-- {
		if num_index >= 0 {
			sum = num[num_index] + getNthDigit(k, (length-i))
		} else {
			sum = getNthDigit(k, (length - i))
		}
		if carry {
			sum++
		}
		if sum >= 10 {
			carry = true
		} else {
			carry = false
		}
		result[i] = sum % 10
		num_index--
	}

	if carry {
		result[0] = 1
	}

	for j := 0; j < length; j++ {
		if result[j] != 0 {
			return result[j:]
		}
	}
	return result
}

func main() {
	fmt.Println(addToArrayForm([]int{1, 2, 0, 0}, 34))
	fmt.Println(addToArrayForm([]int{2, 7, 4}, 181))
	fmt.Println(addToArrayForm([]int{2, 1, 5}, 806))
	fmt.Println(addToArrayForm([]int{0}, 806))
}
