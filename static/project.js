const dieFaces = ["\u{2680}", "\u{2681}", "\u{2682}", "\u{2683}", "\u{2684}", "\u{2685}"];

const dieImages = ["/static/dice/d1.png", "/static/dice/d2.png", "/static/dice/d3.png", "/static/dice/d4.png", "/static/dice/d5.png", "/static/dice/d6.png"];

const delay = async(ms = 1000) => new Promise(resolve => setTimeout(resolve, ms))

function removeOverlayMenu() {
    document.getElementById("container").innerHTML = "";
    //saveCharacter;
    //displayCharacter();
}

function popoverRollBones() {

    removeOverlayMenu();

    var popoverView = document.createElement("p");
    // popoverView.className = "overlayElement translucent";
    popoverView.id = "overlay";

    var playersRoll = rollNumberAndSides(2, 6);
    var modsTotal = 0;

    var contentDiv = document.createElement("p");
    contentDiv.className = "overlayTextElement";


    //contentDiv.innerHTML = "The applicable skills: <strong>" + JSON.stringify(applicableSkills) + "</strong></br>" + "die roll = " + rollNumberAndSides(2, 6);
    contentDiv.innerHTML = "You have rolled 2d6!</br></br>"

    var rollP = document.createElement("p");
    rollP.innerHTML = "2d6 Total:    " + playersRoll + "</br>" + attToTest + " value:    " + attValueToTest;
    contentDiv.appendChild(rollP);

    if (applicableSkills.length > 0) {
        for (let index = 0; index < applicableSkills.length; index++) {
            const element = applicableSkills[index];
            if (element["bonus"] !== "none") {
                var modP = document.createElement("p");
                modP.innerHTML = element["skill"] + " adds:    " + element["bonus"];
                modsTotal = modsTotal + element["bonus"];
                contentDiv.appendChild(modP);


            }


        }

    } else {

    }

    var finalRollP = document.createElement("p");
    var finalRoll = playersRoll + modsTotal + attValueToTest;
    finalRollP.innerHTML = "<strong>FINAL ROLL:    " + finalRoll + "</strong>";
    contentDiv.appendChild(finalRollP);


    var cancelButton = document.createElement("button");
    cancelButton.className = "skillButton";
    cancelButton.innerHTML = "DISMISS";
    cancelButton.onclick = function() { removeOverlayMenu() };

    popoverView.appendChild(contentDiv);
    popoverView.appendChild(cancelButton);

    document.getElementById("container").appendChild(popoverView);


}


function popoverDice(attStr, myVal) {

    removeOverlayMenu();
    var container = document.getElementById("container");
    //container.style.display = "flex";



    // BUTTONS..............
    var bd6 = document.createElement("button");
    bd6.innerHTML = "1d6<br>disadvantage";
    bd6.className = "diceButton"
    bd6.onclick = function() {
        tumbleDice(1, "dice");
        tumbleDice(1, "dangerDie");
    };

    var b2d6 = document.createElement("button");
    b2d6.innerHTML = "2d6<br>normal";
    b2d6.className = "diceButton"
    b2d6.onclick = function() {
        tumbleDice(2, "dice");
        tumbleDice(1, "dangerDie")
    }

    var b3d6 = document.createElement("button");
    b3d6.innerHTML = "3d6<br>advantage";
    b3d6.className = "diceButton"
    b3d6.onclick = function() {
        tumbleDice(3, "dice");
        tumbleDice(1, "dangerDie")
    };

    var cancelButton = document.createElement("button");
    cancelButton.innerHTML = "Cancel";
    cancelButton.className = "diceButton"
    cancelButton.onclick = function() { removeOverlayMenu() };

    var dangerDieButton = document.createElement("button");
    dangerDieButton.innerHTML = "DANGER DIE";
    dangerDieButton.className = "diceButton"
    dangerDieButton.onclick = function() { tumbleDice(1, "dangerDie") };


    // DIVS.................
    var selectButtonsP = document.createElement("div");
    selectButtonsP.appendChild(bd6);
    selectButtonsP.appendChild(b2d6);
    selectButtonsP.appendChild(b3d6);
    selectButtonsP.appendChild(cancelButton);

    var attDiv = document.createElement("div");
    attDiv.style.fontSize = "large";
    attDiv.style.color = "black";
    attDiv.id = "attDiv";
    attDiv.innerHTML = popoverString(attStr, myVal);

    var diceDiv = document.createElement("div");
    diceDiv.style.fontSize = "50px";
    diceDiv.style.color = "black";
    diceDiv.id = "dice";
    // diceDiv.innerHTML = "\u{2680}" + "  " + "\u{2680}";
    diceDiv.innerHTML = "<img src=\"/static/dice/d1.png\"style=\"width:50px; margin: 10px\"/>" + "<img src=\"/static/dice/d1.png\"style=\"width:50px; margin: 10px\"/>";;

    var dangerDieDiv = document.createElement("div");
    dangerDieDiv.style.fontSize = "50px";
    dangerDieDiv.style.color = "red";
    dangerDieDiv.id = "dangerDie";
    //dangerDieDiv.innerHTML = "\u{2680}";
    dangerDieDiv.innerHTML = "<img src=\"/static/dice/d1.png\"style=\"width:50px; margin: 10px; filter: invert(100%) saturate(1000%);\"/>";


    var dangerButtonDiv = document.createElement("div");
    dangerButtonDiv.style.fontSize = "large";
    dangerButtonDiv.style.color = "red";
    dangerButtonDiv.id = "dangerButtonDiv";
    dangerButtonDiv.innerHTML = "Danger Die"
        // dangerButtonDiv.appendChild(dangerDieButton)


    // POPOVER VIEW.......................................
    var popoverView = document.createElement("div");
    popoverView.className = "overlayElement"
    popoverView.appendChild(selectButtonsP);
    popoverView.appendChild(attDiv);
    popoverView.appendChild(diceDiv);
    popoverView.appendChild(dangerDieDiv);
    popoverView.appendChild(dangerButtonDiv);



    document.getElementById("container").appendChild(popoverView);


}

function popoverString(att, val) {

    var rank = rankOfAttribute(val);

    var successNumString = "";

    if (rank == "LOW") {
        successNumString = "You're " + att + " value is LOW.<br>You succeed if any of the dice show a 6.\n";
    } else if (rank == "AVERAGE") {
        successNumString = "You're " + att + " value is AVERAGE.<br>You succeed if any of the dice show a 5 or a 6.\n";
    } else if (rank == "HIGH") {
        successNumString = "You're " + att + " value is HIGH.<br>You succeed if any of the dice show a 4, 5, or 6.\n";
    } else if (rank == "SUPER") {
        successNumString = "You're " + att + " value is SUPER.<br>You succeed if any of the dice show a 3, 4, 5, or 6.\n";
    } else {
        successNumString = "We can't tell what your " + att + "is.<br>Roll the dice and let the GM decide what to do."
    }

    var myString = "You're rolling an " + att + " check.<br> " + successNumString;

    return myString
}

function rankOfAttribute(attVal) {

    if (attVal == 1 || attVal == 2) {
        return "LOW";
    } else if (attVal == 3 || attVal == 4) {
        return "AVERAGE";
    } else if (attVal == 5 || attVal == 6) {
        return "HIGH";
    } else if (attVal > 6) {
        return "SUPER";
    } else {
        return "UNKNOWN";
    }
}

function rollDice(dnum, myElementID) {
    var diceString = ""
        // UNICODE DICE
        // for (let i = 0; i < dnum; i++) {
        //     diceString = diceString + " " + dieFaces[Math.floor(Math.random() * dieFaces.length)] + " ";
        // }

    // DICE IMAGES
    for (let i = 0; i < dnum; i++) {
        diceString = diceString + "<img src=" + dieImages[Math.floor(Math.random() * dieImages.length)] + " style=\"width:50px; margin: 10px";

        if (myElementID == "dangerDie") {
            // diceString = diceString + "; filter: brightness(0.5) sepia(1) saturate(10000%);"
            diceString = diceString + "; filter: invert(100%) saturate(1000%);"
        }

        diceString = diceString + "\"/>"
    }





    document.getElementById(myElementID).innerHTML = diceString;
}

function tumbleDice(dnum, myElementID) {

    timesRoll = 10;

    rollDice(dnum, myElementID);
    diceLoop(dnum, myElementID)
}

async function diceLoop(dnum, myElementID) {
    for (var i = 0; i < 10; i += 1) {
        rollDice(dnum, myElementID);
        await delay(50);
        console.log("looping in dice");
    }
}

function removeAllChildrenFrom(elementID) {
    //console.log("removeAllChildrenFrom -- element id: " + elementID);
    //to empty an element of all internal elements...
    const myNode = document.getElementById(elementID);
    while (myNode.firstChild) {
        myNode.removeChild(myNode.firstChild);
    }
}

function addElementToPanel(panelID, myElement) {
    document.getElementById(panelID).appendChild(attButton(myElement));
}

function numberToDollarsString(num) {

    return "$" + numToExactitude(num, 2);
}

function numToExactitude(num, decPlaces) {
    return num.toFixed(decPlaces);
}

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