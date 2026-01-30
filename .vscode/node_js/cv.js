const length = 5;
const width = 3;
var chuvi = (length,width) => console.log("chu vi: " + ((length + width) * 2))
var dientich = (length,width) => console.log("dien tich: " + (length * width))
var main = () => {
    chuvi(length,width); 
    dientich(length,width);
}
main();