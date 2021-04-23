<!--    "Przycisk rozwijania menu"-->
let menu = document.querySelector("button.user_menu");
let icon = document.querySelector("i.fa-angle-down");
let user_menu = document.querySelector("div.user_menu");
let yours_trails = document.querySelector("li.yours_trails");
let tr = document.querySelector("div.tr")
let login_rwd = document.getElementById('login_rwd')
let login_mapa_menu = document.querySelector('.login_mapa')

if (menu) {
    menu.addEventListener('click', function () {
        user_menu.classList.toggle("active");
        icon.classList.toggle("active");
    });
}
// Handle menu trails
    if (yours_trails) {
        tr.classList.toggle("active");
    }
//------------------------------------------
//The method responsible for choosing login / registration at low screen resolution
if(login_rwd){
    login_rwd.addEventListener('click',function(){
        login_mapa_menu.classList.toggle('mini')
    })
}