const timers = [];  // set timer for duplicate
const jqueryDom = createDanmaku('hihihi');
addInterval(jqueryDom);

const ws = new WebSocket('ws://localhost:8765');
ws.onmessage = function (data) {
    const rec_danmuku = createDanmaku(data.data);
    addInterval(rec_danmuku);
}

$(".send").on("click", function () {
    const v = document.getElementById("danmakutext").value;
    ws.send(v)
});

function createDanmaku(text) {
    const jqueryDom = $("<div class='bullet'>" + text + "</div>");
    const fontColor = "rgb(255,255,255)";
    const fontSize = "20px";
    let top = Math.floor(Math.random() * 400) + "px";
    const left = $(".screen_container").width() + "px";
    jqueryDom.css({
        "position": 'absolute',
        "color": fontColor,
        "font-size": fontSize,
        "left": left,
        "top": top,
    });
    $(".screen_container").append(jqueryDom);
    return jqueryDom;
}

function addInterval(jqueryDom) {
    let left = jqueryDom.offset().left - $(".screen_container").offset().left;
    const timer = setInterval(function () {
        left--;
        jqueryDom.css("left", left + "px");
        if (jqueryDom.offset().left + jqueryDom.width() < $(".screen_container").offset().left) {
            jqueryDom.remove();
            clearInterval(timer);
        }
    }, 5);
    timers.push(timer);
}