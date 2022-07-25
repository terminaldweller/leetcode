package main

import "fmt"

func reverse(x int) int {
	var res int
	var negative bool
	if x < 0 {
		negative = true
		x = x * -1
	}
	for x > 0 {
		digit := x - ((x / 10) * 10)
		res = res*10 + digit
		if res > (0x1 << 31) {
			return 0
		}
		x = x / 10
	}

	if negative {
		return res * -1
	}
	return res
}

func main() {
	fmt.Println(reverse(123))
	fmt.Println(reverse(-123))
	fmt.Println(reverse(120))
	fmt.Println(reverse(1534236469))

}
