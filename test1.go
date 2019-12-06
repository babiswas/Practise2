package main
import "fmt"

func main(){
  var arr[3] string
  arr[0]="Hello"
  arr[1]="bello"
  arr[2]="mello"
  for i:=0;i<len(arr);i++{
  fmt.Println(arr[i])
  }
}