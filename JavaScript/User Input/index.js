let radius;
const PI = 3.14;
let circumference;

document.getElementById("mySubmit").onclick = function(){
    radius = document.getElementById("radius").value;
    radius = Number(radius);
    circumference = 2*PI*radius;
    document.getElementById("circumference").textContent = `The circumference of the circle is ${circumference}`;

}