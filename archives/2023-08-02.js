let constellation, luckyItem, data, id, objP, year, month, day;

const orderString = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"];
const JE = ["J", "E"];
const className = ["jpn", "eng"];

// ランキングページの表示
function setupPage() {
    
    let menuBarheight = Math.trunc(document.getElementById("menuBar").clientHeight * 0.9);
    let objBody = document.body;
    objBody.style.paddingTop = menuBarheight + "px";
    

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", "2023-08-02.json");
    xmlhttp.setRequestHeader( 'content-type', 'application/json;charset=UTF-8' );
    // xmlhttp.responseType = "json";
    xmlhttp.send();
    xmlhttp.onreadystatechange = () => {
        if (xmlhttp.readyState == 4) {
            if (xmlhttp.status == 200) {
                data = JSON.parse(xmlhttp.responseText);
                constellation = data.constellation;
                luckyItem = data.luckyItem;
                year = data.year
                month = data.month
                day = data.day
                viewConstellation();
            } else {
                alert("status = " + xmlhttp.status);
            }
        }
    };
}
function viewConstellation(){
    id = "Title";
    objP = document.getElementById(id);
    objP.innerText = year + "年" + month + "月" + day + "日の運勢はこちら!";
    // objP.innerText = "今日の運勢はこちら!";
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
            objB.style["background-image"] = "linear-gradient(rgba(25, 25, 87, 0.9), rgba(25, 25, 87, 0.9)), url(../images/" + constellation[i][1] + ".png)";
            objB.style["background-position"] = "50% 50%";
        } else{
            objB.style["background-image"] = "linear-gradient(rgba(38, 51, 117, 0.9), rgba(38, 51, 117, 0.9)), url(../images/" + constellation[i][1] + ".png)";
            objB.style["background-position"] = "50% 50%";
        }
    }
}

// メニューバーのサイズ変更による上部の空白サイズの調整
function resizePadding(){
    let menuBarheight = Math.trunc(document.getElementById("menuBar").clientHeight * 0.9);
    let objBody = document.body;
    objBody.style.paddingTop = menuBarheight + "px";
}

