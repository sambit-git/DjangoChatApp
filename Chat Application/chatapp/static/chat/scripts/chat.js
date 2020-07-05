function fixStyling(){
    if(window.innerWidth <= 950){
        fixSmallScreenStyling()
    }
    else{
        fixBigScreenStyling()
    }
}

function fixSmallScreenStyling(){
    availableHeight= window.innerHeight - $("#main-nav").outerHeight();
    availableWidth= window.innerWidth;
    $("#chat-window").css("minHeight", availableHeight);
    $("#chat-window").css("maxHeight", availableHeight);
    $("#chat-window").css("width", availableWidth);
    $(".chat-form").css("width", $(".right").outerWidth());
    if(!window.location.href.endsWith('chat/')){
        $(".right").css("height", $("#chat-window").outerHeight());
        var left = document.getElementById("left")
        if (left){
            left.remove();
        }
        $("#msg").css("width", 0.9*($(".chat-form").width()));
    }
}

function fixBigScreenStyling(){
    availableHeight= window.innerHeight - $("#main-nav").outerHeight();
    availableWidth= window.innerWidth;
    $(".chat-wrapper").css("height", availableHeight)
    $(".chat-wrapper").css("width", availableWidth)
    $(".chat-form").css("width", $(".right").outerWidth())

    scrollUserBlockHeight = $("#chat-window").outerHeight() - $(".my-info").outerHeight() - $(".searchbar").outerHeight();
    scrollChatSpaceHeight = $("#chat-window").outerHeight() - $(".user-info").outerHeight() - $(".chat-form").outerHeight();
    $(".other-users").css("maxHeight", scrollUserBlockHeight );
    $(".chat-space").css("maxHeight", scrollChatSpaceHeight );
    $(".chat-form").css("width", $(".right").width());
}

$("document").ready(fixStyling);
$(window).resize(fixStyling);


let loc = window.location

let wsStart = "ws://"
if(loc.protocol == "https://"){
    wsStart = "wss://"
}


var chatSpace = $("#chat-space");

let endpoint = wsStart + loc.host + loc.pathname;
let socket = new WebSocket(endpoint);

socket.onmessage = function(e){
    // console.log("message",e);
    $("#chat-space").scrollTop($("#chat-space")[0].scrollHeight);
    let response = JSON.parse(e.data);
    let msg = response.message;
    let username = response.user, div;

    if(username == myUsername){
        div = `
            <div class="sent">
                <div class="text">${msg}</div>
                <div class="photo">
                    <img src="${loc.origin}${myPhoto}" >
                </div>
            </div>
        `
    }
    else{
        div = `
            <div class="received">
                <div class="photo">
                    <img src="${loc.origin}${otherUserPhoto}" >
                </div>
                <div class="text">${msg}</div>
            </div>
        `
    }
    chatSpace.append(div)
    
}
socket.onopen = function(e){
    console.log("open",e)
    var formData = $("#msg-form");
    var msg = $("#msg");
    formData.submit(function(e){
        e.preventDefault();
        var msgText = msg.val()
        var finalData = {
            'message' : msgText
        }
        $("#chat-space").scrollTop($("#chat-space")[0].scrollHeight);
        socket.send(JSON.stringify(finalData));
        formData[0].reset();
    })
}
socket.onerror = function(e){
    console.log("erroer",e)
}
socket.onclose = function(e){
    console.log("close",e)
}
