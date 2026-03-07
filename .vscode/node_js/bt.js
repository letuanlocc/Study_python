class shape{
    constructor(height,width){
        this.height = height;
        this.width = width
    }
    showInfo(){
        console.log("this is class father")
    }
}
class square extends shape{
    constructor(height,width){
        super(height,width)
    }
    dientich(){
         return this.height * this.width;
    }
    showInfo(){
        console.log("this is a class child")
        console.log("dientich: ", this.dientich())
    }
}
class tamgiac extends shape{
    constructor(height,width){
        super(height,width)
    }
    dientich(){
        return (this.height + this.width)/2
    }
    showInfo(){
        console.log("this is a class child")
        console.log("dientich: ", this.dientich())
    }
}
const sq1 = new square(7,7);
sq1.showInfo()