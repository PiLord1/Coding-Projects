const min = 1;
const max = 6;
let money = 0;

document.getElementById("randomize").onclick = function(){
    let number = Math.floor(Math.random() * (max)) + min;
    document.getElementById("myNumber").textContent = number;

    if (number === 6){
        money += 300;
        document.getElementById("money").textContent = `Money: $ ${money}`

    }
}