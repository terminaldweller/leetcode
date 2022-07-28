package main

func isAnagram_v_1(s string, t string) bool {
	s_map := make(map[rune]int, len(s))
	t_map := make(map[rune]int, len(t))
	for _, character := range s {
		s_map[character]++
	}
	for _, character := range t {
		t_map[character]++
	}

	if len(s_map) != len(t_map) {
		return false
	}
	for k, v := range s_map {
		value, ok := t_map[k]
		if !ok {
			return false
		}
		if value != v {
			return false
		}
	}

	return true
}

func isAnagram(s string, t string) bool {
	s_map := make([]int, 26)
	t_map := make([]int, 26)
	for _, character := range s {
		s_map[int(character-'a')]++
	}
	for _, character := range t {
		t_map[int(character-'a')]++
	}

	if len(s_map) != len(t_map) {
		return false
	}
	for i := 0; i < 26; i++ {
		if s_map[i] != t_map[i] {
			return false
		}
	}

	return true
}

func main() {
	isAnagram("anagram", "nagaram")
}
