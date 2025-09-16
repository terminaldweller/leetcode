package main

import "fmt"

func longestCommonPrefix(strs []string) string {
	longestPrefix := strs[0]
	for _, element := range strs {
		for index, char := range element {
			if len(longestPrefix) == 0 {
				break
			}
			if index > len(longestPrefix)-1 {
				// longestPrefix = longestPrefix[0 : index-1]
				// fmt.Println("XXX:", longestPrefix)
				break
			}
			if byte(char) != longestPrefix[index] {
				longestPrefix = longestPrefix[0:index]
			}
		}

		if len(longestPrefix) > len(element) {
			longestPrefix = longestPrefix[0:len(element)]
		}
		// fmt.Println(longestPrefix)
	}

	return longestPrefix
}

func main() {
	strs := []string{"flower", "flow", "flight"}
	fmt.Println(longestCommonPrefix(strs))
	strs2 := []string{"dog", "racecar", "car"}
	fmt.Println(longestCommonPrefix(strs2))
	strs3 := []string{"ab", "a"}
	fmt.Println(longestCommonPrefix(strs3))
	strs4 := []string{"aaa", "aa", "aaa"}
	fmt.Println(longestCommonPrefix(strs4))
}
