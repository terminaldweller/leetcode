package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func abs(a int) int {
	if a > 0 {
		return a
	}
	return -a
}

func minTimeToVisitAllPoints(points [][]int) int {
	sum := 0
	for index, item := range points {
		if index+1 < len(points) {
			min_dist_x := abs(item[0] - points[index+1][0])
			min_dist_y := abs(item[1] - points[index+1][1])
			sum += min(min_dist_x, min_dist_y) + abs(min_dist_x-min_dist_y)
		}
	}

	return sum
}

func main() {
	points2 := [][]int{{3, 2}, {-2, 2}}
	fmt.Println(minTimeToVisitAllPoints(points2))
	points := [][]int{{1, 1}, {3, 4}, {-1, 0}}
	fmt.Println(minTimeToVisitAllPoints(points))
}
