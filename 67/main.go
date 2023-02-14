package main

import "fmt"

func addBinary(a string, b string) string {
	var long string
	var short string
	var count int
	carry := false

	if len(a) >= len(b) {
		long = a
		short = b
	} else {
		long = b
		short = a
	}

	result := make([]byte, len(long)+1)

	for i := len(long) - 1; i >= 0; i-- {
		if long[i] == '1' {
			count++
		}

		if len(short)-(len(long)-i) >= 0 {
			if short[len(short)-(len(long)-i)] == '1' {
				count++
			}
		}

		if carry {
			count++
		}

		switch count {
		case 0:
			result[i+1] = '0'
			carry = false
		case 1:
			result[i+1] = '1'
			carry = false
		case 2:
			result[i+1] = '0'
			carry = true
		case 3:
			result[i+1] = '1'
			carry = true
		}

		count = 0
	}
	if carry {
		result[0] = '1'
	}

	// fmt.Println(result)
	if result[0] == 0 {
		return string(result[1:])
	} else {
		return string(result)
	}
}

func main() {
	fmt.Println(addBinary("11", "1"))
	fmt.Println(addBinary("1010", "1011"))
	fmt.Println(addBinary("0111", "0111"))
	fmt.Println(addBinary("0", "0"))
	fmt.Println(addBinary("10", "0"))
	fmt.Println(addBinary("10", "1"))
}
