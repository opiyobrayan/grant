console.log('hello world')

const evenBox=document.getElementById('event-box')

const countdownBox=document.getElementById('countdown-box')

const eventDate=Date.parse(evenBox.textContent)

setInterval(()=>{
        const now= new Date().getTime()

        const diff=eventDate-now

        const d=Math.floor(eventDate/(1000*60*60*24) -(now/(1000*60*60*24)))
    
        const h=Math.floor((eventDate/(1000*60*60) -(now/(1000*60*60))) % 24)

        const m=Math.floor((eventDate/(1000*60) -(now/(1000*60))) % 60)
    
        const s=Math.floor((eventDate/(1000) -(now/(1000))) % 60)
        
        if (diff>0){
            countdownBox.innerHTML=d+ " day(s), "  + h + " hours ,  "+ m + "  minutes, " + s + "  seconds "
        }
        else{
            countdownBox.innerHTML='countdown completed'
        }

    },1000
)