package main

import "fmt"

func strStr(haystack string, needle string) int {
	if len(needle) > len(haystack) {
		return -1
	}

	needle_len := len(needle)
	haystack_len := len(haystack)
	noMatch := false

	for i, _ := range haystack {
		if needle_len <= haystack_len-i {
			for j, _ := range needle {
				if needle[j] != haystack[i+j] {
					noMatch = true
					break
				}
			}
			if noMatch {
				noMatch = false
			} else {
				return i
			}

		} else {
			return -1
		}
		//fmt.Println(i, h)
	}

	return -1
}

func main() {
	// fmt.Println(strStr("sadbutsad", "sad"))
	fmt.Println(strStr("mississipi", "a"))
}
