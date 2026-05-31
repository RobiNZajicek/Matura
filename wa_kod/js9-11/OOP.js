

class Animal{
    constructor(name){
        this.name = name

    }
    sound(){
        console.log('Neco ')
    }
}
class Pes extends Animal{
    constructor(name,plemeno){
        super(name)
        this.plemeno = plemeno

    }
    sound(){
        console.log(`${this.name} dela haf haf`)
    }
}

let pes = new Pes('Azor','Ohar')
pes.sound()