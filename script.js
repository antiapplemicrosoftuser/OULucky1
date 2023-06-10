Array.prototype.shuffle = function () {
    this.sort(() => Math.random() - 0.5);
}

const constellation = [["牡羊座", "Aries"], ["牡牛座", "Taurus"], ["双子座", "Gemini"], ["蟹座", "Cancer"], ["獅子座", "Leo"], ["乙女座", "Virgo"], ["天秤座", "Libra"], ["蠍座", "Scorpio"], ["射手座", "Sagittarius"], ["山羊座", "Capricorn"], ["水瓶座", "Aquarius"], ["魚座", "Pisces"]];

constellation.shuffle();

const orderString = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"];
const JE = ["J", "E"];
const className = ["jpn", "eng"];

function viewConstellation() {
    for (var i = 0; i < 12; i++){
        for (var j = 0; j < 2; j++){
            var id = orderString[i] + JE[j];
            var objP = document.getElementById(id);
            objP.innerText = constellation[i][j];
            objP.className = className[j];
        }
        var objB = document.getElementById("rank_" + String(i + 1));
        if (i%2 === 0){
            objB.style["background-image"] = "linear-gradient(rgba(25, 25, 87, 0.9), rgba(25, 25, 87, 0.9)), url(images/" + constellation[i][1] + ".png)";
            objB.style["background-position"] = "50% 50%";
        } else{
            objB.style["background-image"] = "linear-gradient(rgba(38, 51, 117, 0.9), rgba(38, 51, 117, 0.9)), url(images/" + constellation[i][1] + ".png)";
            objB.style["background-position"] = "50% 50%";
        }
    }
}