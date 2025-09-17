package main

import "fmt"

// func possibleBipartition(N int, dislikes [][]int) bool {
// 	color := make(map[int]bool, N)
// 	visited := make(map[int]bool, N)
// 	adjList := make(map[int][]int, N)

// 	for _, d := range dislikes {
// 		a := d[0]
// 		b := d[1]
// 		adjList[a] = append(adjList[a], b)
// 		adjList[b] = append(adjList[b], a)
// 	}

// 	for i := 1; i <= N; i++ {
// 		if !visited[i] {
// 			visited[i] = true
// 			res := isBiparitionDfs(i, adjList, visited, color)
// 			if !res {
// 				return false
// 			}
// 		}
// 	}

// 	return true
// }

// func isBiparitionDfs(cur int, adjList map[int][]int, visited map[int]bool, color map[int]bool) bool {
// 	for _, next := range adjList[cur] {
// 		if !visited[next] {
// 			visited[next] = true
// 			color[next] = !color[cur]
// 			res := isBiparitionDfs(next, adjList, visited, color)
// 			if !res {
// 				return false
// 			}
// 		} else if color[cur] == color[next] {
// 			return false
// 		}
// 	}
// 	return true
// }

// red: 1; green: -1
func possibleBipartition(n int, dislikes [][]int) bool {
	edges := make([][]int, n+1)
	for _, dislike := range dislikes {
		u, v := dislike[0], dislike[1]
		edges[u] = append(edges[u], v)
		edges[v] = append(edges[v], u)
	}

	color := make([]int, n+1)

	var dfs func(u, c int) bool
	dfs = func(u, c int) bool {
		if color[u] != 0 {
			return color[u] == c
		}

		fmt.Printf("node: %d will mark color: %d\n", u, c)
		color[u] = c
		for _, v := range edges[u] {
			if !dfs(v, -c) {
				return false
			}
		}

		return true
	}

	for u := 1; u <= n; u++ {
		if color[u] == 0 && !dfs(u, 1) {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(possibleBipartition(4, [][]int{{1, 2}, {1, 3}, {2, 4}}))
	fmt.Println(possibleBipartition(3, [][]int{{1, 2}, {1, 3}, {2, 3}}))
	fmt.Println(possibleBipartition(5, [][]int{{1, 2}, {2, 3}, {3, 4}, {4, 5}, {1, 5}}))
}
