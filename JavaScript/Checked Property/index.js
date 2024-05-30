let subscribeBtn = document.getElementById("subscribeBtn");
let visaBtn = document.getElementById("visaBtn");
let masterCardBtn = document.getElementById("masterCardBtn");
let payPalBtn = document.getElementById("payPalBtn");
let submitBtn = document.getElementById("submitBtn");
let subscribeCheck = document.getElementById("subscribeCheck");
let cardCheck = document.getElementById("cardCheck");

submitBtn.onclick = function(){
    if (subscribeBtn.checked) {
        subscribeCheck.textContent = `You have subscribed!`;
    }
    else {
        subscribeCheck.textContent = `You have NOT subscribed!`;
    }

    if (visaBtn.checked ) {
        cardCheck.textContent = `You have selected Visa`;
    }
    else if (masterCardBtn.checked) {
        cardCheck.textContent = `You have selected MasterCard`;
    }

    else if (payPalBtn.checked) {
        cardCheck.textContent = `You have selected Paypal`;
    }

    else {
        cardCheck.textContent = `NO mode of payment selected!`;
    }

}