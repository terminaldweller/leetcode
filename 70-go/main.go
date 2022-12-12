package main

import "fmt"

func climbStairs(n int) int {
	var fact func(n int, memo map[int]int) int

	memo := make(map[int]int, n)
	fact = func(n int, memo map[int]int) int {
		if _, ok := memo[n]; ok {
			return memo[n]
		}
		if n < 2 {
			return 1
		}

		memo[n] = fact(n-1, memo) + fact(n-2, memo)
		return memo[n]
	}

	return fact(n, memo)
}

func main() {
	fmt.Println(climbStairs(2))
	fmt.Println(climbStairs(3))
	fmt.Println(climbStairs(4))
	fmt.Println(climbStairs(5))
	fmt.Println(climbStairs(44))
}
