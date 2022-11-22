const dieFaces = ["\u{2680}", "\u{2681}", "\u{2682}", "\u{2683}", "\u{2684}", "\u{2685}"]

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
    console.log(".......... ATTRIBUTE AND VALUE.............");
    // console.log(attStr);
    // log(myVal);
    var container = document.getElementById("container");
    container.style.display = "flex";
    ///container.style.backgroundColor = "pink";
    //container.style.backgroundColor = "pink";

    var popoverView = document.createElement("div");
    popoverView.className = "overlayElement translucent"

    // var nameInput = document.createElement("input");
    // nameInput.type = "text";
    // nameInput.value = myPC.name;
    // nameInput.id = "nameText";
    // nameInput.className = "bsButtonBasic bs-theme-light"; //"skillButton";
    // nameInput.style.textAlign = "center";
    // nameInput.style.width = "50%";
    // nameInput.style.padding = "5px";
    // nameInput.style.fontSize = "18px";
    // nameInput.onkeydown = function() { if (event.key == "Enter") { myPC.name = nameInput.value;
    //         removeOverlayMenu() } };
    // popoverView.appendChild(nameInput);

    var bd6 = document.createElement("button");
    // randomNameButton.className = "bsButtonBasic bsPaddingBasic"; //"skillButton";
    bd6.innerHTML = "1d6";
    bd6.onclick = function() { rollDice(1) };

    var b2d6 = document.createElement("button");
    b2d6.innerHTML = "2d6";
    b2d6.onclick = function() { rollDice(2) }

    var b3d6 = document.createElement("button");
    b3d6.innerHTML = "3d6";
    b3d6.onclick = function() { rollDice(3) };

    var diceDiv = document.createElement("div");
    diceDiv.style.fontSize = "xx-large";
    diceDiv.style.color = "black";
    diceDiv.id = "dice";
    diceDiv.innerHTML = popoverString(attStr, myVal);

    // randomNameButton.onclick = function() { nameInput.value = randomCharacterName(); };

    // var saveButton = document.createElement("button");
    // saveButton.className = "bsButtonBasic bsPaddingBasic"; //"skillButton";
    // saveButton.innerHTML = "Save New Name";
    // saveButton.id = "saveName";
    // saveButton.onclick = function() { myPC.name = nameInput.value;
    //     saveCharacter();
    //     displayCharacter();
    //     removeOverlayMenu() };

    var cancelButton = document.createElement("button");
    //cancelButton.className = "bsButtonBasic bsPaddingBasic"; //"skillButton";
    cancelButton.innerHTML = "Cancel";
    cancelButton.onclick = function() { removeOverlayMenu() };


    var selectButtonsP = document.createElement("div");
    selectButtonsP.appendChild(bd6);
    selectButtonsP.appendChild(b2d6);
    selectButtonsP.appendChild(b3d6);
    // selectButtonsP.appendChild(saveButton);
    selectButtonsP.appendChild(cancelButton);
    popoverView.appendChild(selectButtonsP);
    // popoverView.appendChild(document.createElement("/br"));
    // popoverView.appendChild(document.createElement("/br"));
    popoverView.appendChild(diceDiv);


    document.getElementById("container").appendChild(popoverView);


}

function popoverString(att, val) {

    var successNumString = "";
    if (val == 1 || val == 2) {
        successNumString = "You're " + att + "value is LOW. You succeed if any of the dice show a 6.\n";
    } else if (val == 3 || val == 4) {
        successNumString = "You're " + att + "value is AVERAGE. You succeed if any of the dice show a 5 or a 6.\n";
    } else {
        successNumString = "You're " + att + "value is HIGH. You succeed if any of the dice show a 4, 5, or 6.\n";
    }

    var myString = "You're rolling an " + att + " check.\n " + successNumString;

    return myString
}

function rollDice(dnum) {
    var diceString = ""
    for (let i = 0; i < dnum; i++) {
        diceString = diceString + " " + dieFaces[Math.floor(Math.random() * dieFaces.length)] + " ";
    }
    document.getElementById("dice").innerHTML = diceString;
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