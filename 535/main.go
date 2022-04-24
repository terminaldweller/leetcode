package main

import (
	"crypto/sha256"
	"fmt"
)

type Codec struct {
	table map[string]string
}

func Constructor() Codec {
	var codec Codec
	table := make(map[string]string)
	codec.table = table
	return codec
}

// Encodes a URL to a shortened URL.
func (this *Codec) encode(longUrl string) string {
	hash := sha256.Sum256([]byte(longUrl))
	hashStr := string(hash[:])
	tinyUrl := "http://tinyurl.com/" + hashStr
	this.table[hashStr] = longUrl
	return tinyUrl
}

// Decodes a shortened URL to its original URL.
func (this *Codec) decode(shortUrl string) string {
	return this.table[shortUrl[19:]]
}

/**
 * Your Codec object will be instantiated and called as such:
 * obj := Constructor();
 * url := obj.encode(longUrl);
 * ans := obj.decode(url);
 */

func main() {
	longUrl := "https://leetcode.com/problems/design-tinyurl"
	obj := Constructor()
	url := obj.encode(longUrl)
	fmt.Println(url)
	ans := obj.decode(url)
	fmt.Println(ans)
}
