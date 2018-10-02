Python:

def silly(a):
    if a > 0:
        print 'Hi'
    else:
        print 5 + '3'

-------------------------
Golang:

package main

import ("fmt"
)

func silly(a int) {
    if (a > 0) {
        fmt.Println("Hi")
    } else {
        fmt.Println("3" + 5)
    }
}

func main() {
    silly(2)
}
