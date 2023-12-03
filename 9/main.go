package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	var y int
	for i := x; i > 0; i /= 10 {
		y = y*10 + i%10
		fmt.Println(y)
	}
	return x == y
}

func main() {
	fmt.Println(isPalindrome(12345678))
	fmt.Println(isPalindrome(1234321))
	fmt.Println(isPalindrome(121))
	fmt.Println(isPalindrome(-121))
	fmt.Println(isPalindrome(10))
}
