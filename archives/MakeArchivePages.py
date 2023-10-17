from datetime import datetime as dt
from datetime import timedelta


# 日付条件の設定
strdt = dt.strptime("2023-06-20", '%Y-%m-%d')  # 開始日
enddt = dt.strptime("2023-10-16", '%Y-%m-%d')  # 終了日

# 日付差の日数を算出（リストに最終日も含めたいので、＋１しています）
days_num = (enddt - strdt).days + 1
datelist = []
for i in range(days_num):
    datelist.append(strdt + timedelta(days=i))
    
htmlContent = f"""<!DOCTYPE html>
<html>

<head>
    <meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
    <link rel="stylesheet" type="text/css" href="../style.css" />
    <link rel="icon" type="image/png" href="../images/icon.png">
    <title>大阪大学今日の運勢サークル</title>
    <script src="../script.js"></script>
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

<body onload="resizePadding()" onresize="resizePadding()" id="body">"""
month = 0
datelist.reverse()
for date in datelist:
    if date.month != month:
        month = date.month
        htmlContent += f"""
    <h1>{date.year}年{date.month}月</h1>
    <a class="archiveLink" href="{date.strftime('%Y-%m-%d')}.html">{date.strftime('%Y-%m-%d')}</a><br>"""
    else:
        htmlContent += f"""
    <a class="archiveLink" href="{date.strftime('%Y-%m-%d')}.html">{date.strftime('%Y-%m-%d')}</a><br>"""

htmlContent += """
</body>

</html>
"""

with open("archivePages.html", "w", encoding='utf-8') as f:
    f.write(htmlContent)