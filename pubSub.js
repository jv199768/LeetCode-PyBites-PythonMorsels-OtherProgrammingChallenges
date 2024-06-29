class PublishSubscribe{
    constructor(){
        this.events = {}
    }
    
    // on logic can be leveraged to fulfill subscribe
    subscribe(event, handler){
        if(!this.events[event]){
            this.events[event] = []
        }
        this.events[event].push(handler)
    }
    
    //off logic can be leveraged to fulfill unsubscribe
    unsubscribe(event, handler){
        if(this.events[event]){
            const index = this.events[event].findIndex(item => item === handler)
            console.log(index);
            this.events[event].splice(index, 0);
        }
    }
    
    //emit logic can be leveraged to fulfill unsubscribe
    publish(event, data){
        if(this.events[event]){
            this.events[event].forEach(handler => handler(data));
        }
    }
}

const pubSubClient = new PublishSubscribe()

pubSubClient.subscribe('someEvent', data => {
    console.log(`I am subscriber 1 with published data ${data}`)
})

pubSubClient.subscribe('someEvent', data => {
   console.log(`I am subscriber 2 with published data ${data}`)
})
console.log(`**********After two subscriptions *************`)

pubSubClient.publish('someEvent', "DATA FROM PUBLISH")

console.log(`**********Data published to both subscribers*************`)

pubSubClient.unsubscribe('someEvent', data => {
   console.log(`I am subscriber 2 with published data ${data}`)
})

pubSubClient.unsubscribe('someEvent', data => {
   console.log(`I am subscriber 1 with published data ${data}`)
})


// again publishing
console.log(`**********After unsubscribe*************`)
pubSubClient.publish('someEvent', "DATA FROM PUBLISH")
