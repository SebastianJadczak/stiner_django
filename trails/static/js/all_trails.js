<!--    Wszystkie trasy-->
let buttonRight = document.getElementById('right');
let buttonLeft = document.getElementById('left');
let amount = document.querySelectorAll('div.all_trails-trail');
let position = 0;
let widthTrail = (amount[0].offsetWidth - 50)

buttonRight.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('trails');
    if (position >= 0 && position <= (widthTrail * amount.length)) {
        position += widthTrail
        list_point_user_add.style.marginLeft = `-${position}px`
    }
});

buttonLeft.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('trails');
    if (position >= widthTrail) {
        position -= widthTrail;
        list_point_user_add.style.marginLeft = `-${position}px`
    }
});
//    Najwyżej oceniane
let buttonLeft_rate = document.getElementById('left-rate');
let buttonRight_rate = document.getElementById('right-rate');
let amount_top_rate = document.querySelectorAll('div.top_rate-trail');
let position_top_rate = 0;
let widthTrailTopRate = (amount_top_rate[0].offsetWidth - 50)

buttonRight_rate.addEventListener('click', function () {
    console.log(widthTrailTopRate)
    console.log(position_top_rate)
    let list_point_user_add = document.getElementById('top_rate-trails');
    if (position_top_rate >= 0 && position_top_rate <= (widthTrailTopRate * amount_top_rate.length)) {
        position_top_rate += widthTrailTopRate;
        list_point_user_add.style.marginLeft = `-${position_top_rate}px`
    }
});
buttonLeft_rate.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('top_rate-trails');
    if (position_top_rate >= widthTrailTopRate) {
        position_top_rate -= widthTrailTopRate;
        list_point_user_add.style.marginLeft = `-${position_top_rate}px`
    }
});

//    Najpopularniejsze
let buttonLeft_popular = document.getElementById('left-popular');
let buttonRight_popular = document.getElementById('right-popular');
let amount_popular_trail = document.querySelectorAll('div.popular-trail');
let position_popular_trail = 0;
let widthTrailPopular = (amount_popular_trail[0].offsetWidth - 50)

buttonRight_popular.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('popular-trails');
    if (position_popular_trail >= 0 && position_popular_trail <=  (widthTrailPopular * amount_popular_trail.length)) {
        position_popular_trail += widthTrailPopular;
        list_point_user_add.style.marginLeft = `-${position_popular_trail}px`
    }
});
buttonLeft_popular.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('popular-trails');
    if (position_popular_trail >= widthTrailPopular) {
        position_popular_trail -= widthTrailPopular;
        list_point_user_add.style.marginLeft = `-${position_popular_trail}px`
    }
});

let hamburger = document.getElementById('hamburger')
let filter_trails = document.querySelector('.filter_trails')
let x_hamburger = document.getElementById('x_hamburger')

if(hamburger){
    hamburger.addEventListener('click', function (){
        filter_trails.classList.toggle('active')
        x_hamburger.style.display = 'block'
    })
}
if(x_hamburger){
    x_hamburger.addEventListener('click', function (){
        filter_trails.classList.toggle('active')
        x_hamburger.style.display = 'none'
    })
}