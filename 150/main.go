package main

import (
	"fmt"
	"strconv"

	"github.com/emirpasic/gods/stacks/arraystack"
)

func evalRPN(tokens []string) int {
	st := arraystack.New()
	for _, op := range tokens {
		switch op {
		case "+":
			{
				val1, _ := st.Pop()
				val2, _ := st.Pop()
				res := val1.(int) + val2.(int)
				fmt.Printf("%d + %d = %d\n", val1, val2, res)
				st.Push(res)
			}
		case "-":
			{
				val1, _ := st.Pop()
				val2, _ := st.Pop()
				res := val2.(int) - val1.(int)
				fmt.Printf("%d - %d = %d\n", val2, val1, res)
				st.Push(res)
			}
		case "*":
			{
				val1, _ := st.Pop()
				val2, _ := st.Pop()
				res := val1.(int) * val2.(int)
				fmt.Printf("%d * %d = %d\n", val1, val2, res)
				st.Push(res)
			}
		case "/":
			{
				val1, _ := st.Pop()
				val2, _ := st.Pop()
				res := val2.(int) / val1.(int)
				fmt.Printf("%d / %d = %d\n", val2, val1, res)
				st.Push(res)
			}
		default:
			{
				val1, _ := strconv.Atoi(op)
				st.Push(val1)
			}
		}
	}

	final, _ := st.Pop()

	return final.(int)
}

func main() {
	fmt.Println(evalRPN([]string{"2", "1", "+", "3", "*"}))
	fmt.Println(evalRPN([]string{"4", "13", "5", "/", "+"}))
	fmt.Println(evalRPN([]string{"10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"}))
}
