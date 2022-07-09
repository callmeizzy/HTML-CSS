<!DOCTYPE html>
<html>
<head>
    <!-- 제목 만들기 -->
    <title>WEB_Study</title>

    <h1>HTML이란 무엇인가?</h1>

    <!-- UTF-8로 ENCODING해 주어야 웹 상에서 한글이 깨지지 않음 -->
    <meta charset = 'utf-8'> 
    <!-- utf-8로 문서를 읽어와, character set -->
</head>
<body>
    <h1><a href = 'index.html'>WEB</a></h1>

    <!-- 목차를 작성해 봅시다  -->
    <!--<ul> : 부모 // <li> : 자식  -->
    <ul>
        <li><a href = '1.html'>1. HTML</a></li>
        <li><a href = '2.html'>2. CSS</a></li>
        <li><a href = '3.html'>3. JavaScript</a></li>
    </ul>

    <h2>HTML</h2>


   <P><h2>How to make table</h2></P>
    <!-- <ol> : auto number increment  -->
    <ol>
        <li>izzy</li>
        <li>illo</li>
        <li>momo</li>
    </ol>
    <!-- UL : Unordered List / OL : Ordered List -->

    <!-- table 만들기 -->
    <table> 
        <tr> 
            <td>izzy</td>
            <td>29 years old</td>
        </tr>
        <tr>
            <td>illo</td>
            <td>man 29 years old</td>
        </tr>
        <tr>
            <td>momo the cat</td>
            <td>7 years old at catplanet</td>
        </tr>
    </table>

    <!-- link tag : <a href> -->
    <!--  title : 링크에 커서 올리면 툴 팁이 나옴  -->
    <h1><a href = 'https://www.space.com/could-people-breathe-air-on-mars'
        target = '_blank'
        title = 'space.com article'>
        Could people breathe the air on Mars?</a></h1>
    <!-- html parameter tag : <p> -->
    <p>Let's <strong>suppose</strong> 
        you were an astronaut who just landed on the planet Mars.</p>
        What would you need to survive?
    <p style = 'margin-top : 40px;'>
        For starters, here's a short list: 
        Water, food, shelter — and oxygen.</p>
    Oxygen is in the air we breathe here on Earth.

    <!-- <br> : changes line  --> 
    <br>Plants and some kinds of bacteria provide it for us.
    <br>But oxygen is not the only gas in the Earth's atmosphere. 
    <br>It's not even the most abundant.
    <br><u>In fact, only 21% of our air is made up of oxygen.</u>
    <br>Almost all the rest is nitrogen — about 78%.
    <h4><p>Loading image file : yikes.png</p></h4>

    <!-- <img src = '' : loading images  --> 
    <p><img src = 'yikes.png' ></p>
    <h4><p>Loading image file : 최고심 가보자고! </p></h4>
    <p><img src = 'https://pbs.twimg.com/media/E72nzO8UUAIeVjg?format=jpg&name=900x900'
        width="450" ></p>
    <h4><p>Loading image file : 몽글이몽몽 </p></h4>
    <p><img src = 'https://postfiles.pstatic.net/MjAxOTA1MjNfMjIx/MDAxNTU4NTc4NTM4NDMx.QwJlSl1l3b-ArZL56wKxrfR1qeQ3fsJls9ehFtFL3PAg.Kp-v52B4qZwfQsNiA7Mma779EYYuc0rCaQydnqDH8VQg.JPEG.saltapat/KakaoTalk_20190523_112716726.jpg?type=w966'
        width="100%" ></p>


        
    Now you might be wondering: If there's more nitrogen in the air, why do we breathe oxygen?

    Here's how it works: Technically, when you breathe in, you take in everything that's in the atmosphere. 
    But your body uses only the oxygen; you get rid of the rest when you exhale.

    <h2> The air on Mars </h2>
</body>
</html>