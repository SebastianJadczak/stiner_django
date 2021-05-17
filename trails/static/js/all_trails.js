<!--    Wszystkie trasy-->
let buttonRight = document.getElementById('right');
let buttonLeft = document.getElementById('left');
let amount = document.querySelectorAll('div.all_trails-trail');
let position = 0;

buttonRight.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('trails');
    if (position >= 0 && position <= amount.length * 10) {
        position += 350;
        list_point_user_add.style.marginLeft = `-${position}px`
    }
});

buttonLeft.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('trails');
    if (position >= 300) {
        position -= 350;
        list_point_user_add.style.marginLeft = `-${position}px`
    }
});
//    Najwyżej oceniane
let buttonLeft_rate = document.getElementById('left-rate');
let buttonRight_rate = document.getElementById('right-rate');
let amount_top_rate = document.querySelectorAll('div.top_rate-trails');
let position_top_rate = 0;

buttonRight_rate.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('top_rate-trails');
    if (position_top_rate >= 0 && position_top_rate <= amount_top_rate.length * 10) {
        position_top_rate += 350;
        list_point_user_add.style.marginLeft = `-${position_top_rate}px`
    }
});
buttonLeft_rate.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('top_rate-trails');
    if (position_top_rate >= 300) {
        position_top_rate -= 350;
        list_point_user_add.style.marginLeft = `-${position_top_rate}px`
    }
});

//    Najpopularniejsze
let buttonLeft_popular = document.getElementById('left-popular');
let buttonRight_popular = document.getElementById('right-popular');
let amount_popular_trail = document.querySelectorAll('div.popular-trail');
let position_popular_trail = 0;

buttonRight_popular.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('popular-trails');
    if (position_popular_trail >= 0 && position_popular_trail <= amount_popular_trail.length * 10) {
        position_popular_trail += 350;
        list_point_user_add.style.marginLeft = `-${position_popular_trail}px`
    }
});
buttonLeft_popular.addEventListener('click', function () {
    let list_point_user_add = document.getElementById('popular-trails');
    if (position_popular_trail >= 300) {
        position_popular_trail -= 350;
        list_point_user_add.style.marginLeft = `-${position_popular_trail}px`
    }
});
