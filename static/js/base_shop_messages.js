let menu = document.querySelector("button.user_menu");
let icon = document.querySelector("i.fa-angle-down");
let user_menu = document.querySelector("div.user_menu");
let yours_trails = document.querySelector("li.yours_trails");
let tr = document.querySelector("div.tr")
let data = []
let list_checkbox_message = document.querySelectorAll(".checkbox_message")
let login_rwd = document.getElementById('login_rwd')
let login_mapa_menu = document.querySelector('.login_mapa')

//------------------------------------------
// Handle menu users.
if (menu) {
    menu.addEventListener('click', function () {
        user_menu.classList.toggle("active");
        icon.classList.toggle("active");
    });
}
//------------------------------------------
// Handle menu trails.
if (yours_trails) {
    tr.classList.toggle("active");
}

//------------------------------------------
// Add messages to important
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
//------------------------------------------
//    Delete messages.
function delete_message() {
    list_checkbox_message.forEach(check_checked)
    $.ajax({
        type: "POST",
        url: "/shop/user/messages/delete",
        data: {
            csrfmiddlewaretoken: "{{ csrf_token }}",
            data: data
        }
    });
    location.reload()
}
//------------------------------------------
//The method responsible for choosing login / registration at low screen resolution
if (login_rwd) {
    login_rwd.addEventListener('click', function () {
        login_mapa_menu.classList.toggle('mini')
    })
}