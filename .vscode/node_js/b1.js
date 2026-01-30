var arr = new Array(1,2,3,4,5)
var min = arr[0];
var min_arr = (arr) => {
    for(let i = 0; i < 5; i++){
        if(arr[i] < arr[0]){
            min = arr[i];
        }
    }
}
var main = () =>{
    min_arr(arr)
    console.log(min)
}
main();