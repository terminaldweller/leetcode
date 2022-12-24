package main

import "fmt"

func countFib(n int64) int64 {
	f := make([]int64, n+1)

	f[0] = 0
	f[1] = 1
	f[2] = 2
	f[3] = 5

	for i := int64(4); i <= n; i++ {
		f[i] = (2*f[i-1] + f[i-3]) % 1000000007
	}

	return f[n]
}

func numTilings(n int) int {

	if n <= 2 {
		return n
	}

	return int(countFib(int64(n)))
}

func main() {
	// fmt.Println(numTilings(10))
	// fmt.Println(numTilings(1))
	fmt.Println(numTilings(2))
}
