let submitBtn = document.getElementById("submit");
let inputTemp = document.getElementById("inputTemp");
let CtoFBtn = document.getElementById("CtoF");
let FtoCBtn = document.getElementById("FtoC");
let convertedTemp = document.getElementById("convertedTemp");

submitBtn.onclick = function() {
    // Get user input
    let tempValue = inputTemp.value;
    tempValue = Number(tempValue);

    let convertedValue;

    // Check if C to F or F to C button was selected
    if (CtoFBtn.checked) {
        convertedValue = (tempValue * 9/5) + 32;
        convertedValue = convertedValue.toFixed(2);

        // Show converted temperature
        convertedTemp.textContent = `Converted Temperature: ${convertedValue} \u00B0F`;
        document.querySelector("h3").textContent = ``;
    }

    else if (FtoCBtn.checked) {
        convertedValue = (tempValue - 32) * 5/9;
        convertedValue = convertedValue.toFixed(2);

        // Show converted temperature
        convertedTemp.textContent = `Converted Temperature: ${convertedValue} \u00B0C`;
        document.querySelector("h3").textContent = ``;
    }

    else {
        document.querySelector("h3").textContent = `Select a Conversion Factor!`;
    }
}