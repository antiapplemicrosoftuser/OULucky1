"""
10/5にアーカイブページ自動作成を実装開始しましたが、
それまでに作成されたアーカイブファイル(json)のアーカイブページを作るためのスクリプトがこちらになります。
ページ構成など変更になった場合にアーカイブページに一括で適用できます。

Actionsによる動作は行っていません。

参考: https://qiita.com/YuukiMiyoshi/items/42a890a95af6ab7a5348
"""
from datetime import datetime as dt
from datetime import timedelta


# 日付条件の設定
strdt = dt.strptime("2023-06-22", '%Y-%m-%d')  # 開始日
enddt = dt.strptime("2023-10-16", '%Y-%m-%d')  # 終了日

# 日付差の日数を算出（リストに最終日も含めたいので、＋１しています）
days_num = (enddt - strdt).days + 1
datelist = []
for i in range(days_num):
    datelist.append(strdt + timedelta(days=i))

for date in datelist:
    htmlName = f"{date.strftime('%Y-%m-%d')}.html"
    jsName = f"{date.strftime('%Y-%m-%d')}.js"
    jsonName = f"{date.strftime('%Y-%m-%d')}.json"
    with open(htmlName, "w", encoding='utf-8') as f:
        htmlContent = f"""<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link rel="stylesheet" type="text/css" href="../style.css" />
    <link rel="icon" type="image/png" href="../images/icon.png">
    <title>大阪大学今日の運勢サークル</title>
    <script src="""+f'"{jsName}"' + """></script>
</head>
<p>
<nav id="g_navi">
    <ul id="menuBar">
        <h1><a id="citeName" href="../index.html">大阪大学今日の運勢サークル</a></h1>
        <li><a href="">Twitter</a></li>
        <li><a href="archivePages.html">アーカイブ</a></li>
        <li><a href="">アクセス</a></li>
        <li><a href="">お問い合わせ</a></li>
    </ul>
</nav>
</p>

<body onload="setupPage()" onresize="resizePadding()" id="body">
    <h1 id="Title"></h1>
    <nav id="rank_navi">
        <table>
            <tbody>
                <tr id="rank_1">
                    <th>
                        <div class="Gold">1st</div>
                    </th>
                    <td id="1stJ"></td>
                    <td id="1stE"></td>
                    <td>おめでとうございます!</td>
                    <td id="1stLI"></td>
                </tr>
                <tr id="rank_2">
                    <th>
                        <div class="Silver">2nd</div>
                    </th>
                    <td id="2ndJ"></td>
                    <td id="2ndE"></td>
                    <td>おめでとう!</td>
                    <td id="2ndLI"></td>
                </tr>
                <tr id="rank_3">
                    <th>
                        <div class="Bronze">3rd</div>
                    </th>
                    <td id="3rdJ"></td>
                    <td id="3rdE"></td>
                    <td>おめでとう</td>
                    <td id="3rdLI"></td>
                </tr>
                <tr id="rank_4">
                    <th>
                        <div class="White">4th</div>
                    </th>
                    <td id="4thJ"></td>
                    <td id="4thE"></td>
                    <td>いいね</td>
                    <td id="4thLI"></td>
                </tr>
                <tr  id="rank_5">
                    <th>
                        <div class="White">5th</div>
                    </th>
                    <td id="5thJ"></td>
                    <td id="5thE"></td>
                    <td>やるやん</td>
                    <td id="5thLI"></td>
                </tr>
                <tr id="rank_6">
                    <th>
                        <div class="White">6th</div>
                    </th>
                    <td id="6thJ"></td>
                    <td id="6thE"></td>
                    <td>凡</td>
                    <td id="6thLI"></td>
                </tr>
                <tr id="rank_7">
                    <th>
                        <div class="White">7th</div>
                    </th>
                    <td id="7thJ"></td>
                    <td id="7thE"></td>
                    <td>このへんの順位のやつに何も言うことない</td>
                    <td id="7thLI"></td>
                </tr>
                <tr id="rank_8">
                    <th>
                        <div class="White">8th</div>
                    </th>
                    <td id="8thJ"></td>
                    <td id="8thE"></td>
                    <td>このへんの順位のやつに何も言うことない</td>
                    <td id="8thLI"></td>
                </tr>
                <tr id="rank_9">
                    <th>
                        <div class="White">9th</div>
                    </th>
                    <td id="9thJ"></td>
                    <td id="9thE"></td>
                    <td>このへんの順位のやつに何も言うことない</td>
                    <td id="9thLI"></td>
                </tr>
                <tr id="rank_10">
                    <th>
                        <div class="White">10th</div>
                    </th>
                    <td id="10thJ"></td>
                    <td id="10thE"></td>
                    <td>このへんの順位のやつに何も言うことない</td>
                    <td id="10thLI"></td>
                </tr>
                <tr id="rank_11">
                    <th>
                        <div class="White">11th</div>
                    </th>
                    <td id="11thJ"></td>
                    <td id="11thE"></td>
                    <td>今までの人生の反省をしましょう。</td>
                    <td id="11thLI"></td>
                </tr>
                <tr id="rank_12">
                    <th>
                        <div class="Worst">12th</div>
                    </th>
                    <td id="12thJ"></td>
                    <td id="12thE"></td>
                    <td>ごめんなさ～い(笑)</td>
                    <td id="12thLI"></td>
                </tr>

            </tbody>
        </table>
    </nav>
</body>

</html>
"""
        f.write(htmlContent)
    
    with open(jsName, "w", encoding='utf-8') as f:
        jsContent = """let constellation, luckyItem, data, id, objP, year, month, day;

const orderString = ["1st", "2nd", "3rd", "4th", "5th", "6th", "7th", "8th", "9th", "10th", "11th", "12th"];
const JE = ["J", "E"];
const className = ["jpn", "eng"];

// ランキングページの表示
function setupPage() {
    
    let menuBarheight = Math.trunc(document.getElementById("menuBar").clientHeight * 0.9);
    let objBody = document.body;
    objBody.style.paddingTop = menuBarheight + "px";
    

    var xmlhttp = new XMLHttpRequest();
    xmlhttp.open("GET", """ + f'"{jsonName}"' + """);
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

"""
        f.write(jsContent)
    print(htmlName)