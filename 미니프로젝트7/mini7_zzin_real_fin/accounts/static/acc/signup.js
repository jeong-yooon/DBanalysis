function check(){
    if(document.getElementById("username").value==""){
        alert("이름을 입력하세요");
        return;
    }
    if(document.getElementById("username").value==""){
        alert("이름을 입력하세요");
        return;
    }
    if(document.getElementById("password1").value==""){
        alert("비밀번호를 입력하세요");
        return;
    }
    if(document.getElementById("password2").value==""){
        alert("비밀번호를 확인하세요");
        return;
    }
    if(document.getElementById("email").value==""){
        alert("E-mail을 입력하세요");
        return;
    }
    frm.submit(); //직접 submit()이라는 메소드를 호출. 액션을 들고 가줌
}