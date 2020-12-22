var evObj = document.createEvent('Events');
evObj.initEvent("click", true, false);
var a = setInterval(function(){
    if(document.querySelector("div[jscontroller='GFartf']") === null){
        document.querySelector("div[jsname='Qx7uuf']").dispatchEvent(evObj);
        clearInterval(a);
        b = setInterval(function(){
            if(document.querySelector("div[data-id='EBS5u']") !== null){
                console.log(document.querySelector("div[data-id='EBS5u']"));
                clearInterval(b);
                setTimeout(function(){
                    document.querySelector("div[data-id='EBS5u'] .CwaK9 span").dispatchEvent(evObj);
                },1000);
            }
        },500);
        c = setInterval(function(){
            let nbr = parseInt(document.querySelector("span[jscontroller='FTBAv']").textContent);
            if( nbr > 5 && nbr < 10){
                document.querySelector("div[jsname='CQylAd']").dispatchEvent(evObj);
                clearInterval(c);
            }
        },1000);
    }
},500);