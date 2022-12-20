package main

import "fmt"

func canVisitAllRooms(rooms [][]int) bool {
	visited := map[int]bool{}
	dfs(rooms, visited, 0)
	return len(visited) == len(rooms)
}

func dfs(rooms [][]int, visited map[int]bool, room int) {
	if _, ok := visited[room]; !ok {
		visited[room] = true
	} else {
		return
	}

	for i := range rooms[room] {
		dfs(rooms, visited, rooms[room][i])
	}
}

func main() {
	fmt.Println(canVisitAllRooms([][]int{{1}, {2}, {3}, {}}))
	fmt.Println(canVisitAllRooms([][]int{{1, 3}, {3, 0, 1}, {2}, {}}))
}
