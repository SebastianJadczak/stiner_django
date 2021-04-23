let menu = document.querySelector("button.user_menu");
let icon = document.querySelector("i.fa-angle-down");
let user_menu = document.querySelector("div.user_menu");
let yours_trails = document.querySelector("li.yours_trails");
let tr = document.querySelector("div.tr")

if (menu) {
    menu.addEventListener('click', function () {
        user_menu.classList.toggle("active");
        icon.classList.toggle("active");
    });
}
if (yours_trails) {
    tr.classList.toggle("active");
}