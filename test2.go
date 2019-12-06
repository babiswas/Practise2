package main
import "fmt"

func main(){
  myarr:= [3]string{"test1","test2","test3"}
  for i:=0;i<len(myarr);i++{
   fmt.Println(myarr[i])
  }
}