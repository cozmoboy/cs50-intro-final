function randomNumberBetween(min, max) {
    return Math.floor(Math.random() * (max - min + 1) + min);
}

function rollDie(sides) {
    return randomNumberBetween(1, sides);
}

function roll3d6() {
    return rollDie(6) + rollDie(6) + rollDie(6);
}

function attGenRollMCU() {
    // var rollsArray = [rollDie(6), rollDie(6), rollDie(6), rollDie(6)];
    // var fivesNsixes = 0;
    // for(var i=0; i<rollsArray.length; i++ ){	
    // 	var roll = rollsArray[i];
    // 	if(roll==5 || roll == 6){
    // 		fivesNsixes++;
    // 	}
    // }
    fivesNsixes = rollFor5sAnd6s(4);
    console.log("Fives and Sixes: " + fivesNsixes);
    console.log("Returning: " + (fivesNsixes - 1));
    return fivesNsixes - 1;
}

function rollFor5sAnd6s(numberOFDice) {
    var rollsArray = [];
    for (let i = 1; i <= numberOFDice; i++) {
        rollsArray.push(rollDie(6));
    }

    var fivesNsixes = 0;
    for (var i = 0; i < rollsArray.length; i++) {
        var roll = rollsArray[i];
        if (roll == 5 || roll == 6) {
            fivesNsixes++;
        }
    }
    return fivesNsixes;

}

function attCheckRollMCU() {
    return rollDie(6) + rollDie(6);
}

function rollNumberAndSides(dNumber, dSides) {
    var total = 0;
    for (let index = 1; index <= dNumber; index++) {
        total = total + rollDie(dSides);
    }
    return total;
}

function randomElementFromArray(myArray) {
    return myArray[randomNumberBetween(0, myArray.length - 1)];
}