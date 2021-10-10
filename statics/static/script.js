function showPassword(){
    let passShowCheck = document.getElementById('showPasswordCheck');
    let passInput = document.getElementById('password');

    if (passShowCheck.checked == true) {
        passInput.type = "text";
        if (document.getElementById('repassword')){
            document.getElementById('repassword').type = "text";
        }
    }
    else {
        passInput.type = "password"
    }
}