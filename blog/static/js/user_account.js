let edit_info_user = document.getElementById('edit_info_user')
let edit_Preference = document.getElementById('editPreference')
//------------------------------------------
//The method responsible for choosing login / registration at low screen resolution
let login_rwd = document.getElementById('login_rwd')
let login_mapa_menu = document.querySelector('.login_mapa')
let menuDetail = document.getElementById('menu-detail-trail')

//Top Menu
function menuDetailTrail() {
    menuDetail.classList.toggle('active')
}


if (login_rwd) {
    login_rwd.addEventListener('click', function () {
        login_mapa_menu.classList.toggle('mini')
    })
}
editUserAccount = () => {
    edit_info_user.classList.toggle('active')
}
closeEditProfile = () => {
    edit_info_user.classList.toggle('active')
}
editPreference = () => {
    edit_Preference.classList.toggle('active')
}
closeEditPreference = () => {
    edit_Preference.classList.toggle('active')
}