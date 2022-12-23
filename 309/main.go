package main

import "fmt"

func maxProfit(prices []int) int {
	l := len(prices)
	if l < 2 {
		return 0
	}

	has1_doNothing := -prices[0]
	has1_Sell := 0
	has0_DoNothing := 0
	has0_Buy := -prices[0]

	for i := range prices {
		if has1_doNothing > has0_Buy {
			has1_doNothing = +has1_doNothing
		} else {
			has1_doNothing = +has0_Buy
		}
		// has1_doNothing = has1_doNothing > has0_Buy ? has1_doNothing : has0_Buy
		has0_Buy = -prices[i] + has0_DoNothing
		if has0_DoNothing > has1_Sell {
			has0_DoNothing = +has0_DoNothing
		} else {
			has0_DoNothing = +has1_Sell
		}
		// has0_DoNothing = has0_DoNothing > has1_Sell ? has0_DoNothing : has1_Sell
		has1_Sell = prices[i] + has1_doNothing
	}

	if has1_Sell > has0_DoNothing {
		return has1_Sell
	} else {
		return has0_DoNothing
	}
}

func main() {
	fmt.Println(maxProfit([]int{1, 2, 3, 0, 2}))
	fmt.Println(maxProfit([]int{1}))
}
