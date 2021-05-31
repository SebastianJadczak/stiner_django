let menu = document.querySelector("button.user_menu");
let icon = document.querySelector("i.fa-angle-down");
let user_menu = document.querySelector("div.user_menu");
let yours_trails = document.querySelector("li.yours_trails");
let tr = document.querySelector("div.tr")
let newsletter = document.getElementById('newsletter-wrap')
let menuDetail = document.getElementById('menu-detail-trail')

//Top Menu
function menuDetailTrail() {
    menuDetail.classList.toggle('active')
}

//Newsletter
if(newsletter){
    setTimeout(function () {
    newsletter.classList.toggle("active")
}, 3000)
}

closeNewsletter = () => {
    newsletter.classList.toggle("active")
}

//starting geographic coordinates of the map
var x = 52.22977
var y = 21.01178

if (menu) {
    menu.addEventListener('click', function () {
        user_menu.classList.toggle("active");
        icon.classList.toggle("active");
    });
}
//----------------------------------------
//A dish that initiates the location of the map.

var map_1de6ef4f1218487da9d6da057bb8f454 = L.map(
    "map_1de6ef4f1218487da9d6da057bb8f454",
    {
        center: [x, y],
        crs: L.CRS.EPSG3857,
        zoom: 12,
        zoomControl: true,
        preferCanvas: false,
        scrollWheelZoom: false
    }
);

            var tile_layer_03c10e7010194be69dc37614c4d58514 = L.tileLayer(
                "https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png",
                {"attribution": "Data by \u0026copy; \u003ca href=\"http://openstreetmap.org\"\u003eOpenStreetMap\u003c/a\u003e, under \u003ca href=\"http://www.openstreetmap.org/copyright\"\u003eODbL\u003c/a\u003e.", "detectRetina": false, "maxNativeZoom": 18, "maxZoom": 18, "minZoom": 0, "noWrap": false, "opacity": 1, "subdomains": "abc", "tms": false}
            ).addTo(map_1de6ef4f1218487da9d6da057bb8f454);
            var layerGroup = L.layerGroup().addTo(map_1de6ef4f1218487da9d6da057bb8f454);

            function zz(){
                layerGroup.clearLayers();
                marker =fetch('/map/api/points/')
                        .then(response => response.json())
                        .then(data=> {

                            data.forEach(addElements);

                            function addElements(item, index) {
                                var punkt = L.marker(
                                    [item.coordinateX, item.coordinateY],
                                    {}
                                ).addTo(layerGroup);
                                var popup = L.popup({"Width": "300px"});
                                var html = $(`<div id="html_96971d4f2da24e9499eaf1295989655a" style="width: 100.0%; height: 100.0%; font-family: Arial, sans-serif; letter-spacing: 1.1px">
                                <strong style="font-size: 14px;">${item.name}</strong>
                                <p> ${item.descriptions.substring(0, 300)}...</p>
                                <div class="img-map" style="width:300px; height:200px;">
                                    <img src="${item.image}" alt="" style="width: 100%; height: 100%;">
                                </div>
                                <div style="text-align: right; padding-top:10px;">
                                <a href="/trails/point/${item.id}" style="color: green; font-weight: bold; letter-spacing: 1.3px; font-size: 14px;">Więcej</a></div></div>`)[0];

                                popup.setContent(html);
                                punkt.bindPopup(popup);
                            }
                        })
            }
            zz()

// Handle menu trail.
    if (yours_trails){
     tr.classList.toggle("active");
}
//    Handle filter object on site.

let city = document.querySelectorAll("select.location option")

function selected(){
    //    Check select city
    let value_city
    for(item of city){
        if(item.selected){
            value_city =item.value
        }
    }
    return value_city
}

function select_city(){
    //    Downloading city location data and redirecting the map view.
    city_selected = selected()

     fetch(`/map/api/mapCenter/${city_selected}`)
                        .then(response => response.json())
                        .then(data=> {

                        for(item of data){
                           lat=item.coordinateX
                           lon =item.coordinateY
                        }
                        map_1de6ef4f1218487da9d6da057bb8f454.setView(new L.LatLng(lat,lon))
                        })
}

let data = []
let list_checkbox_monuments= document.querySelectorAll(".monuments")

function  check_monuments(){
            for(item of list_checkbox_monuments){
                if(item.checked){
                    data.push(item.id)
                }
            }
    }

function post_monuments() {
    // The method that gets the items from the API depending on which checkboxes are selected.
    // If neither is selected and the user clicks seach, he will get nothing.
    data = []

    check_monuments()
    layerGroup.clearLayers();
    for (item of data) {
        marker = fetch(`/map/api/points/${item.toString()}`)
            .then(response => response.json())
            .then(data => {

                data.forEach(addElements);

                function addElements(item, index) {
                    var punkt = L.marker(
                        [item.coordinateX, item.coordinateY],
                        {}
                    ).addTo(layerGroup);
                    var popup = L.popup({"Width": "300px"});
                    var html = $(`<div id="html_96971d4f2da24e9499eaf1295989655a" style="width: 100.0%; height: 100.0%;">
                                <strong>${item.name}</strong>
                                <p> ${item.descriptions.substring(0, 100)}...</p>
                                <a href="/trails/point/${item.id}">Więcej</a></div>`)[0];

                    popup.setContent(html);
                    punkt.bindPopup(popup);
                }
            })
    }
}

//------------------------------------------
//Handle scroll on the map.
$("#map_1de6ef4f1218487da9d6da057bb8f454").bind('mousewheel DOMMouseScroll', function (event) {
    event.stopPropagation();
    if (event.ctrlKey === true) {
        event.preventDefault();
        map_1de6ef4f1218487da9d6da057bb8f454.scrollWheelZoom.enable();
        $('#map_1de6ef4f1218487da9d6da057bb8f454').removeClass('map-scroll');
        setTimeout(function () {
            map_1de6ef4f1218487da9d6da057bb8f454.scrollWheelZoom.disable();
        }, 1000);
    } else {
             map_1de6ef4f1218487da9d6da057bb8f454.scrollWheelZoom.disable();
             $('#map_1de6ef4f1218487da9d6da057bb8f454').addClass('map-scroll');
         }

     });

      $(window).bind('mousewheel DOMMouseScroll', function (event) {
           $('#map_1de6ef4f1218487da9d6da057bb8f454').removeClass('map-scroll');
      })
//------------------------------------------
//The method responsible for choosing login / registration at low screen resolution
let login_rwd = document.getElementById('login_rwd')
let login_mapa_menu = document.querySelector('.login_mapa')
if(login_rwd){
    login_rwd.addEventListener('click',function(){
        login_mapa_menu.classList.toggle('mini')
    })
}
