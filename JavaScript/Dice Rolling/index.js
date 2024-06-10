let rollBtn = document.getElementById("roll");
let inputNumber = document.getElementById("inputNumber");
let resultDice = document.getElementById("resultDice");
let resultImage = document.getElementById("image-container");
let values = [];
let images = [];

rollBtn.onclick = function() {
    inputNumber = inputNumber.value;

    // Generate random number for each dice between 1 to 6
    for (i = 0; i < inputNumber; i++) {
        let newRandomDice = Math.floor(Math.random() * 6) + 1;
        values.push(newRandomDice);
        images.push(`<img src = "dice/${newRandomDice}.jpg">`);
    }

    resultDice.textContent = `dice: ${values.join(", ")}`;
    resultImage.innerHTML = images.join("");
}