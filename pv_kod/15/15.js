class Animal{
    constructor(name){
        self.name = name
    }
    greate(){
        console.log(`ahoj ${this.name}`);
        
    }
}
class Pes extends Animal{
    constructor(name){

    }
    greate(){
        console.log(`ahoj ${this.name}`);
        
    }
}
ani = Animal('Azor')
pes = Pes('Azor2')