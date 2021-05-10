<!--    "Przycisk rozwijania menu"-->
let menu = document.querySelector("button.user_menu");
let icon = document.querySelector("i.fa-angle-down");
let user_menu = document.querySelector("div.user_menu");
let yours_trails = document.querySelector("li.yours_trails");
let tr = document.querySelector("div.tr")
let login_rwd = document.getElementById('login_rwd')
let login_mapa_menu = document.querySelector('.login_mapa')
let data = []
let list_checkbox_message = document.querySelectorAll(".checkbox_message")
let search_icon = document.getElementById('search-icon')
let search_modal = document.getElementById('search-product')
let search_x = document.getElementById('search_x')
let hamburger_shop = document.getElementById('hamburger-shop')
let left_column = document.getElementsByClassName('left')
let left_column_x = document.getElementById('hamburger-shop_x')
let menuDetail = document.getElementById('menu-detail-trail')

//Top Menu
function menuDetailTrail() {
    menuDetail.classList.toggle('active')
}

if (menu) {
    menu.addEventListener('click', function () {
        user_menu.classList.toggle("active");
        icon.classList.toggle("active");
    });
}
// Obsługa menu Trasy
if (yours_trails) {
    tr.classList.toggle("active");
}

//    Usuwanie wiadomości
function delete_message() {
    console.log("delete")
}

// Dodawanie wiadomości do ważne
function check_checked(element) {
    if (element.checked) {
        data.push(element.id)
    }
}

function add_to_important() {
    list_checkbox_message.forEach(check_checked)
    $.ajax({
        type: "POST",
        url: "/shop/user/messages/important",
        data: {
            csrfmiddlewaretoken: "{{ csrf_token }}",
            data: data
        }
    });
    location.reload()
}

//----------------------------------------
//Handle icon and modal search.
if (search_icon) {
    search_icon.addEventListener('click', function () {
        search_modal.classList.toggle("rwd");
    });
    search_x.addEventListener('click', function () {
        search_modal.classList.toggle("rwd");
    });
}
//----------------------------------------
//    Handle Hamburger menu.
if (hamburger_shop) {
    hamburger_shop.addEventListener('click', function () {
        left_column[0].classList.toggle("rwd")
    })
    left_column_x.addEventListener('click', function () {
        left_column[0].classList.toggle("rwd")
    })
}
//------------------------------------------
//The method responsible for choosing login / registration at low screen resolution
if (login_rwd) {
    login_rwd.addEventListener('click', function () {
        login_mapa_menu.classList.toggle('mini')
    })
}