package main

import "fmt"

func dumpDict(dict map[int]int) {
	for key, val := range dict {
		fmt.Println(key, val)
	}
}

func getWordDict(word string) map[int]int {
	dict := make(map[int]int)

	for i := 0; i < len(word); i++ {
		if _, ok := dict[int(word[i])]; ok {
			dict[int(word[i])]++
		} else {
			dict[int(word[i])] = 1
		}
	}

	return dict
}

func closeStrings(word1 string, word2 string) bool {

	if len(word1) != len(word2) {
		return false
	}

	dict1 := getWordDict(word1)
	dict2 := getWordDict(word2)

	// dumpDict(dict1)
	// fmt.Println()
	// dumpDict(dict2)

	if len(dict1) != len(dict2) {
		return false
	}

	for key, _ := range dict1 {
		if _, ok := dict2[key]; ok {
			continue
		} else {
			return false
		}
	}

	delete_key := 0
	matched := false
	for _, val := range dict1 {
		for key2, val2 := range dict2 {
			if val == val2 {
				delete(dict2, key2)
				matched = true
				delete_key = key2
				break
			}
		}

		if matched == true {
			matched = false
			delete(dict2, delete_key)
		} else {
			return false
		}
	}

	return true
}

func main() {
	word1 := "abbzzca"
	word2 := "babzzcz"
	fmt.Println(closeStrings(word1, word2))
}
