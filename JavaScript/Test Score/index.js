let testScore = "PIZZA";
let letterGrade;

switch(true){
    case testScore >= 92:
        letterGrade = "A";
        break;
    
    case testScore >= 85:
        letterGrade = "B";
        break;

    case testScore >= 75:
        letterGrade = "C";
        break;

    case testScore >= 60:
        letterGrade = "D";
        break;

    case testScore < 60:
        letterGrade = "F";
        break;

    default:
        console.log(`Incorrect input!`);
        letterGrade = "No Grade";
        break;
}

console.log(letterGrade);