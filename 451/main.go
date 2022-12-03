package main

import (
	"fmt"
	"sort"
)

func frequencySort(s string) string {
	dict := func(s string) map[int]int {
		dict := make(map[int]int)

		for i := 0; i < len(s); i++ {
			if _, ok := dict[int(s[i])]; ok {
				dict[int(s[i])]++
			} else {
				dict[int(s[i])] = 1
			}
		}

		return dict
	}(s)

	type kv struct {
		key int
		val int
	}

	var ss []kv

	for k, v := range dict {
		ss = append(ss, kv{k, v})
	}

	sort.Slice(ss, func(i, j int) bool {
		return ss[i].val > ss[j].val
	})

	bytes := make([]byte, len(s), len(s))
	counter := 0
	for _, kv := range ss {
		for i := 0; i < kv.val; i++ {
			bytes[counter] = byte(kv.key)
			counter++
		}
	}

	return string(bytes)
}

func main() {
	fmt.Println(frequencySort("tree"))
	fmt.Println(frequencySort("cccaaa"))
	fmt.Println(frequencySort("Aabb"))
}
