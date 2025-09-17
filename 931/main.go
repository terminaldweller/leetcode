package main

import "fmt"

func min(a, b int) int {
	if a < b {
		return a
	}
	return b
}

func min3(a, b, c int) int {
	min := a
	if b < min {
		min = b
	}
	if c < min {
		min = c
	}

	return min
}

func max(a, b int) int {
	if a > b {
		return a
	}
	return b
}

func getRowMin(row []int) int {
	min := row[0]
	for i := 1; i < len(row); i++ {
		if row[i] < min {
			min = row[i]
		}
	}

	return min
}

func dumpMatrix(matrix [][]int) {
	for i := 0; i < len(matrix[0]); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			fmt.Print(matrix[i][j], " ")
		}
		fmt.Println()
	}
}

func minFallingPathSum(matrix [][]int) int {
	for i := 1; i < len(matrix[0]); i++ {
		for j := 0; j < len(matrix[0]); j++ {
			matrix[i][j] += min3(matrix[i-1][j], matrix[i-1][max(0, j-1)], matrix[i-1][min(len(matrix[0])-1, j+1)])
		}
	}

	dumpMatrix(matrix)

	return getRowMin(matrix[len(matrix[0])-1])
}

func main() {
	fmt.Println(minFallingPathSum([][]int{{1, 2, 3}, {4, 5, 6}, {7, 8, 9}}))
	fmt.Println(minFallingPathSum([][]int{{2, 1, 3}, {6, 5, 4}, {7, 8, 9}}))
}
