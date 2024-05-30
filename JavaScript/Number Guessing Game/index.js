const minNum = 1;
const maxNum = 100;
const correctNum = 25;
let guessNum;

let isGuessed = false;


while(!isGuessed) {
    guessNum = window.prompt("Guess the number between 1 to 100:");
    guessNum = Number(guessNum);

    if (guessNum === correctNum){
        isGuessed = true;
        console.log(`Congrats! You have correctly guessed the number.`);
        window.alert(`Congrats! You have correctly guessed the number.`);
    }

    else if (guessNum < minNum || guessNum > maxNum) {
        window.alert(`ERROR! Input exceeded 1 to 100.`);
    }

    else if (guessNum > correctNum) {
        window.alert(`LOWER!`);
    }

    else if (guessNum < correctNum) {
        window.alert(`HIGHER!`);
    }

    else {
        console.log(`Numbers only!`);
        window.alert(`Numbers only!`);
    }

}