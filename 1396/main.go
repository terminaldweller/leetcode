package main

import "fmt"

type Trip struct {
	station string
	t       int
}

type Info struct {
	count int
	sum   int
}

type UndergroundSystem struct {
	checkInTable map[int]Trip
	timeTable    map[string]Info
}

func Constructor() UndergroundSystem {
	var us UndergroundSystem
	us.checkInTable = make(map[int]Trip)
	us.timeTable = make(map[string]Info)
	return us
}

func (this *UndergroundSystem) CheckIn(id int, stationName string, t int) {
	this.checkInTable[id] = Trip{station: stationName, t: t}
}

func (this *UndergroundSystem) CheckOut(id int, stationName string, t int) {
	begin := this.checkInTable[id].station
	key := begin + ":" + stationName
	time := t - this.checkInTable[id].t
	entry, _ := this.timeTable[key]
	entry.count++
	entry.sum += time
	this.timeTable[key] = entry
}

func (this *UndergroundSystem) GetAverageTime(startStation string, endStation string) float64 {
	key := startStation + ":" + endStation
	return float64(this.timeTable[key].sum) / float64(this.timeTable[key].count)

}

/**
 * Your UndergroundSystem object will be instantiated and called as such:
 * obj := Constructor();
 * obj.CheckIn(id,stationName,t);
 * obj.CheckOut(id,stationName,t);
 * param_3 := obj.GetAverageTime(startStation,endStation);
 */

func main() {
	undergroundSystem := Constructor()
	undergroundSystem.CheckIn(10, "Leyton", 3)
	undergroundSystem.CheckOut(10, "Paradise", 8)                       // Customer 10 "Leyton" -> "Paradise" in 8-3 = 5
	fmt.Println(undergroundSystem.GetAverageTime("Leyton", "Paradise")) // return 5.00000, (5) / 1 = 5
	undergroundSystem.CheckIn(5, "Leyton", 10)
	undergroundSystem.CheckOut(5, "Paradise", 16)                       // Customer 5 "Leyton" -> "Paradise" in 16-10 = 6
	fmt.Println(undergroundSystem.GetAverageTime("Leyton", "Paradise")) // return 5.50000, (5 + 6) / 2 = 5.5
	undergroundSystem.CheckIn(2, "Leyton", 21)
	undergroundSystem.CheckOut(2, "Paradise", 30)                       // Customer 2 "Leyton" -> "Paradise" in 30-21 = 9
	fmt.Println(undergroundSystem.GetAverageTime("Leyton", "Paradise")) // return 6.66667, (5 + 6 + 9) / 3 = 6.66667
}
