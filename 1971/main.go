package main

import "fmt"

func validPath(n int, edges [][]int, source int, destination int) bool {
	seen := make([][]int, n)

	for _, edge := range edges {
		seen[edge[0]] = append(seen[edge[0]], edge[1])
		seen[edge[1]] = append(seen[edge[1]], edge[0])
	}

	visited := map[int]struct{}{}
	none := struct{}{}

	q := []int{source}

	for len(q) > 0 {
		sz := len(q)

		for i := 0; i < sz; i++ {
			item := q[0]
			if item == destination {
				return true
			}

			if _, ok := visited[item]; !ok {
				q = append(q, seen[item]...)
				visited[item] = none
			}
		}

		q = q[1:]
	}

	return false
}

func main() {
	fmt.Println("vim-go")
}
