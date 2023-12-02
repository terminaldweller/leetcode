package main

func countCharacters(words []string, chars string) int {
	var cnt int
	charMap := make(map[rune]int)
	for _, v := range chars {
		charMap[v]++
	}
	for _, v := range words {
		tmpMap := make(map[rune]int)
		for _, vv := range v {
			tmpMap[vv]++
		}
		var flag bool
		for k, v := range tmpMap {
			if charMap[k] < v {
				flag = true
				break
			}
		}
		if !flag {
			cnt += len(v)
		}
	}
	return cnt
}
