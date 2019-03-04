var text = document.getElementById("h-text");
var timer = setInterval(changeColor, 1000);
var change1 = true;
function changeColor(){
    if(change1){
        text.style.color = "#620041";
    }
    else{
        text.style.color = "#eed1d1";
    }
    change1 = !change1;
}