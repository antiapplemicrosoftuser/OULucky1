/*
Array.prototype.shuffle = function () {
    this.sort(() => Math.random() - 0.5);
}
*/

// const constellation = [["牡羊座", "Aries"], ["牡牛座", "Taurus"], ["双子座", "Gemini"], ["蟹座", "Cancer"], ["獅子座", "Leo"], ["乙女座", "Virgo"], ["天秤座", "Libra"], ["蠍座", "Scorpio"], ["射手座", "Sagittarius"], ["山羊座", "Capricorn"], ["水瓶座", "Aquarius"], ["魚座", "Pisces"]];
// constellation.shuffle();

let constellation, luckyItem, data, id, objP;

const orderString = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"];
const JE = ["J", "E"];
const className = ["jpn", "eng"];

function setupPage() {
    today = new Date();
    id = "Title";
    objP = document.getElementById(id);
    objP.innerText = today.getFullYear() + "年" + (today.getMonth() + 1) + "月" + today.getDate() + "日の運勢はこちら!";
    if (today.getMonth() + 1 < 10){
        filename = today.getFullYear() + "-0" + (today.getMonth() + 1) + "-" + today.getDate() + ".json";
    } else {
        filename = today.getFullYear() + "-" + (today.getMonth() + 1) + "-" + today.getDate() + ".json";
    }
    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", filename);
    xmlhttp.setRequestHeader( 'content-type', 'application/json;charset=UTF-8' );
    // xmlhttp.responseType = "json";
    xmlhttp.send();
    xmlhttp.onreadystatechange = () => {
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200) {
                data = JSON.parse(xmlhttp.responseText);
                constellation = data.constellation;
                luckyItem = data.luckyItem;
                viewConstellation();
            } else {
                alert("status = " + xmlhttp.status);
            } 
        }
    };
}
function viewConstellation(){
    for (var i = 0; i < 12; i++){
        for (var j = 0; j < 2; j++){
            id = orderString[i] + JE[j];
            objP = document.getElementById(id);
            objP.innerText = constellation[i][j];
            objP.className = className[j];
        }
        id = orderString[i] + "LI";
        objP = document.getElementById(id);
        objP.innerText = "Lucky Item: " + luckyItem[i];
        objP.className = "LuckyItem";
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