var budget = 100000;

var forwardDetails =
	[
		{ID: "Degoey ", position: "F", price: 10980, projScore: 99},
		{ID: "Christensen ", position: "F", price: 10680, projScore: 74},
		{ID: "McStay ", position: "F", price: 7190, projScore: 51.33},
		{ID: "McCarthy ", position: "F", price: 8250, projScore: 63.33},
		{ID: "Cameron ", position: "F", price: 9370, projScore: 58.33},
		{ID: "Hipwood ", position: "F", price: 8040, projScore: 64},
		{ID: "Varcoe ", position: "F", price: 8010, projScore: 52.67},
		{ID: "Mathieson ", position: "F", price: 8530, projScore: 57.67},
		{ID: "McInerney ", position: "F", price: 7850, projScore: 64.67},
		{ID: "Elliott ", position: "F", price: 8310, projScore: 48.33},
		{ID: "Thomas ", position: "F", price: 8700, projScore: 62.33},
		{ID: "Rayner ", position: "F", price: 8240, projScore: 43},
		{ID: "Stephenson ", position: "F", price: 9770, projScore: 74.67}
	];

var centreDetails =
	[
		{ID: "Lyons ", position: "C", price: 12150, projScore: 69.67},
		{ID: "Adams ", position: "C", price: 15740, projScore: 99},
		{ID: "Pendlebury ", position: "C", price: 13060, projScore: 89.33},
		{ID: "Sidebottom ", position: "C", price: 14260, projScore: 97.67},
		{ID: "Treloar ", position: "C", price: 15340, projScore: 110.67},
		{ID: "Neale ", position: "C", price: 16220, projScore: 140},
		{ID: "Robinson ", position: "C", price: 12250, projScore: 92.33},
		{ID: "Zorko ", position: "C", price: 13410, projScore: 89.67},
		{ID: "Phillips ", position: "C", price: 13300, projScore: 99},
		{ID: "Beams ", position: "C", price: 15830, projScore: 101.33},
		{ID: "Berry ", position: "C", price: 12460, projScore: 91},
		{ID: "McCluggage ", position: "C", price: 11970, projScore: 79.67},
		{ID: "Brown ", position: "C", price: 8200, projScore: 53}
	];

var backDetails =
	[
		{ID: "Crisp ", position: "B", price: 12590, projScore: 85.33},
		{ID: "Langdon ", position: "B", price: 9980, projScore: 71.67},
		{ID: "Maynard ", position: "B", price: 10080, projScore: 83},
        {ID: "Moore ", position: "B", price: 8110, projScore: 63.33},
		{ID: "Andrews ", position: "B", price: 10100, projScore: 63.67},
		{ID: "Gardiner ", position: "B", price: 9350, projScore: 51},
        {ID: "Rich ", position: "B", price: 11190, projScore: 91.67},
		{ID: "Robertson ", position: "B", price: 9210, projScore: 53},
		{ID: "Walker ", position: "B", price: 10660, projScore: 80.33},
		{ID: "Hodge ", position: "B", price: 9760, projScore: 63.67},
        {ID: "Aish ", position: "B", price: 10020, projScore: 72},
        {ID: "Howe ", position: "B", price: 10440, projScore: 81},
        {ID: "Witherden ", position: "B", price: 13850, projScore: 90.33},
        {ID: "Mihocek ", position: "B", price: 9980, projScore: 80.67}
	];

var ruckDetails =
	[
		{ID: "Grundy ", position: "R", price: 16770, projScore: 129},
		{ID: "Roughead ", position: "R", price: 9050, projScore: 67.33},
		{ID: "Martin ", position: "R", price: 12450, projScore: 81.67},
		{ID: "Cox ", position: "R", price: 8530, projScore: 59.67}
	];

//finding all possible combinations of 2 backs
var backNames = [];
var backPrices = [];
var backScores = [];

for (let i = 0; i < backDetails.length - 1; i++) {
  for (let j = i + 1; j < backDetails.length; j++) {
    backNames.push(`${backDetails[i].ID}${backDetails[j].ID}`);
	backPrices.push(`${backDetails[i].price + backDetails[j].price}`);
	backScores.push(`${backDetails[i].projScore + backDetails[j].projScore}`);
  }
}

/*console.log("BACK Options:");
console.log(backNames);
console.log("BACK Prices:");
console.log(backPrices);
console.log("BACK Scores:");
console.log(backScores);*/

//finding all possible combinations of 4 centres
let centreNames = [];
let centrePrices = [];
let centreScores = [];


for (let i = 0; i < centreDetails.length - 1; i++) {
  for (let j = i + 1; j < centreDetails.length; j++) {
	  for (let k = j + 1; k < centreDetails.length; k++) {
		  for (let l = k + 1; l < centreDetails.length; l++) {			  centreNames.push(`${centreDetails[i].ID}${centreDetails[j].ID}${centreDetails[k].ID}${centreDetails[l].ID}`);
			  centrePrices.push(`${centreDetails[i].price + centreDetails[j].price+ centreDetails[k].price+ centreDetails[l].price}`);
	centreScores.push(`${centreDetails[i].projScore + centreDetails[j].projScore+ centreDetails[k].projScore+ centreDetails[l].projScore}`);
		  }
	  }
  }
}

/*console.log(" ");
console.log("CENTRE Options:");
console.log(centreNames);
console.log("centre Prices:");
console.log(centrePrices);
console.log("centre Scores:");
console.log(centreScores);
console.log(" ");*/

//finding all possible combinations of 2 fwds
let forwardNames = [];
let forwardPrices = [];
let forwardScores = [];

for (let i = 0; i < forwardDetails.length - 1; i++) {
  for (let j = i + 1; j < forwardDetails.length; j++) {
    forwardNames.push(`${forwardDetails[i].ID}${forwardDetails[j].ID}`);
	forwardPrices.push(`${forwardDetails[i].price + forwardDetails[j].price}`);
	forwardScores.push(`${forwardDetails[i].projScore + forwardDetails[j].projScore}`);
  }
}
/*console.log("FORWARD Options:");
console.log(forwardNames);
console.log("FORWARD Prices:");
console.log(forwardPrices);
console.log("FORWARD Scores:");
console.log(forwardScores);
console.log(" ");*/

//adding all rucks to their respective arrays (only 1 ruck per team)
let ruckNames = [];
let ruckPrices = [];
let ruckScores = [];

for (let i = 0; i < ruckDetails.length; i++) {
    ruckNames.push(`${ruckDetails[i].ID}`);
	ruckPrices.push(`${ruckDetails[i].price}`);
	ruckScores.push(`${ruckDetails[i].projScore}`);
}

/*console.log("RUCK Options:");
console.log(ruckNames);
console.log("RUCK Prices:");
console.log(ruckPrices);
console.log("RUCK Scores:");
console.log(ruckScores);
console.log("_______________________");
console.log(" ");*/

//finished basic positioning and scores

//optimising team
//Name

// finding all possible combinations of teams (names), and their corresponding prices and scores
var NameCombos = [];
var PriceCombos = [];
var ScoreCombos = [];

for(var i = 0; i < backNames.length; i++) {
     for(var j = 0; j < centreNames.length; j++) {
		 for(var k = 0; k < forwardNames.length; k++) {
			 for(var l = 0; l < ruckNames.length; l++) {
        NameCombos.push(backNames[i] + centreNames[j]+ forwardNames[k]+ ruckNames[l]);
		PriceCombos.push(backPrices[i]*1 + centrePrices[j]*1 + forwardPrices[k]*1 + 	ruckPrices[l]*1);
		ScoreCombos.push(backScores[i]*1 + centreScores[j]*1+ forwardScores[k]*1+ ruckScores[l]*1);
	 		}
     	}
	}
}

// finding price values that exceed the budget and replacing them with a '0'. Also replacing values in the corresponing 'team name' and 'score' arrays with a '0'
for (var i = 0; i < PriceCombos.length; i++){
    if (PriceCombos[i] > budget) {
        PriceCombos.splice(i, 1);
        i--;
    }
}

//printing final arrays
/*
console.log(" ");
console.log(NameCombos);
console.log(PriceCombos);
console.log(ScoreCombos);*/

// function to find the index of the highest value in an array
function indexOfMax(arr) {
    if (arr.length === 0) {
        return -1;
    }

    var max = arr[0];
    var maxIndex = 0;

    for (var i = 1; i < arr.length; i++) {
        if (arr[i] > max) {
            maxIndex = i;
            max = arr[i];
        }
    }

    return maxIndex;
}

// the 'highest' variable is the index of the highest value in the score array.
var highest = indexOfMax(ScoreCombos);

// find the best team name, score and price
var BestTeam = NameCombos[highest];
var BestScore = ScoreCombos[highest];
var BestPrice = PriceCombos[highest];

console.log("___________");
console.log("BEST TEAM");
console.log("Players: " + BestTeam);
console.log("Pred. Score: " + BestScore);
console.log("Team Cost: " + BestPrice);

// removing the highest value so that the second best team can be identified 
var removed = NameCombos.splice(1,highest);
var removed = ScoreCombos.splice(1,highest);
var removed = PriceCombos.splice(1,highest);

// finding the second best team
var highest = indexOfMax(ScoreCombos);
var BestTeam = NameCombos[highest];
var BestScore = ScoreCombos[highest];
var BestPrice = PriceCombos[highest];

console.log("___________");
console.log("SECOND BEST TEAM");
console.log("Players: " + BestTeam);
console.log("Pred. Score: " + BestScore);
console.log("Team Cost: " + BestPrice);

//finding the third best team
var removed = NameCombos.splice(1,highest);
var removed = ScoreCombos.splice(1,highest);
var removed = PriceCombos.splice(1,highest);

var highest = indexOfMax(ScoreCombos);
var BestTeam = NameCombos[highest];
var BestScore = ScoreCombos[highest];
var BestPrice = PriceCombos[highest];

console.log("___________");
console.log("THIRD BEST TEAM");
console.log("Players: " + BestTeam);
console.log("Pred. Score: " + BestScore);
console.log("Team Cost: " + BestPrice);