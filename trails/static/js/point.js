var coordinateX = document.getElementById('x').innerText
var coordinateY = document.getElementById('y').innerText
let leftArrow = document.getElementById('left-arrow')
let rightArrow = document.getElementById('right-arrow')
let position = 0;
let amount = document.querySelectorAll('img.img');

rightArrow.addEventListener('click', function () {
    let wrapImage = document.getElementById('small');
    if (position >= 0 && position <= (amount.length * 20)) {
        console.log((amount.length * 10))
        position += 240;
        wrapImage.style.transform = `translateX(-${position}px)`
    }

});
leftArrow.addEventListener('click', function () {
        let wrapImage = document.getElementById('small');
        console.log(position)
        if (position>0 ){
            position -= 240;
            wrapImage.style.transform =`translateX(${position}px)`
        }
    });

//Map-mini
var map_1de6ef4f1218487da9d6da057bb8f454 = L.map(
    "map_1de6ef4f1218487da9d6da057bb8f454",
    {
        center: [coordinateX, coordinateY],
        crs: L.CRS.EPSG3857,
        zoom: 16,
        zoomControl: false,
        preferCanvas: false,
        scrollWheelZoom: false
    }
);

var tile_layer_03c10e7010194be69dc37614c4d58514 = L.tileLayer(
    "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
    {
        "attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.",
        "detectRetina": false,
        "maxNativeZoom": 18,
        "maxZoom": 18,
        "minZoom": 0,
        "noWrap": false,
        "opacity": 1,
        "subdomains": "abc",
        "tms": false
    }
).addTo(map_1de6ef4f1218487da9d6da057bb8f454);
var layerGroup = L.layerGroup().addTo(map_1de6ef4f1218487da9d6da057bb8f454);


var punkt = L.marker(
    [coordinateX, coordinateY],
    {}
).addTo(layerGroup);


//------------------------------------------
//Handle scroll on the map.
$("#map_1de6ef4f1218487da9d6da057bb8f454").bind('mousewheel DOMMouseScroll', function (event) {
    event.stopPropagation();
    if (event.ctrlKey === true) {
        event.preventDefault();
        map_1de6ef4f1218487da9d6da057bb8f454.enable();
        $('#map_1de6ef4f1218487da9d6da057bb8f454').removeClass('map-scroll');
        setTimeout(function () {
            map_1de6ef4f1218487da9d6da057bb8f454.disable();
        }, 1000);
    } else {
        map_1de6ef4f1218487da9d6da057bb8f454.disable();
        $('#map_1de6ef4f1218487da9d6da057bb8f454').addClass('map-scroll');
    }

});

$(window).bind('mousewheel DOMMouseScroll', function (event) {
    $('#map_1de6ef4f1218487da9d6da057bb8f454').removeClass('map-scroll');
})