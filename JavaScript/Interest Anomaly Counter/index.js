let interestAccrued = [5, 7, 25, 5, 4, 8, 50, 100000, 15, 3, 12.5, 10000000];
let sumAccrued = 0;
let averageAccrued = 0;
let monthsChecked = 0;
let anomalyCounter = 0;
let firstCheck = 0;

for (let i = 0; i < interestAccrued.length; i++){
    if(monthsChecked >= 3 && firstCheck > 0) {
        averageAccrued += sumAccrued / 3;
        if (interestAccrued[i] > 2*averageAccrued) {
            anomalyCounter++;
            sumAccrued = 0;
            averageAccrued = 0;
        }
        firstCheck = 0;
        averageAccrued = 0;
    }

    else if (monthsChecked >= 3){
        sumAccrued += (interestAccrued[i-1] + interestAccrued[i-2] + interestAccrued[i-3]);
        averageAccrued += sumAccrued / 3;
        if (interestAccrued[i] > 2*averageAccrued) {
            anomalyCounter++;
            sumAccrued = 0;
            averageAccrued = 0;
        }
        averageAccrued = 0;
    }

    else {
        sumAccrued += interestAccrued[i];
        firstCheck++;
    }
    monthsChecked++;
}
console.log(`The number of anomalies is ${anomalyCounter}`);