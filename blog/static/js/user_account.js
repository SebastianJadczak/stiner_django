let edit_info_user = document.getElementById('edit_info_user')
let edit_Preference = document.getElementById('editPreference')
editUserAccount = ()=>{
   edit_info_user.classList.toggle('active')
}
closeEditProfile = () =>{
    edit_info_user.classList.toggle('active')
}
editPreference=()=>{
    edit_Preference.classList.toggle('active')
}
closeEditPreference=()=>{
    edit_Preference.classList.toggle('active')
}