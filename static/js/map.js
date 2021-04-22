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



<!--Mapa-->
var x =52.22977
var y =21.01178
//danie inicjujące lokalizje mapy


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
                                <p> ${item.descriptions}</p>
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

    // Obsługa menu Trasy
    if (yours_trails){
     tr.classList.toggle("active");
}
//    Obsługa formularzu filtrowania obiektów na stronie

let city = document.querySelectorAll("select.location option")

function selected(){
    //    Sprawdzenie które miasto jest wybrane
    let value_city
    for(item of city){
        if(item.selected){
            value_city =item.value
        }
    }
    return value_city
}

function select_city(){
    //    Pobranie danych lokalizacji miast i przekirowanie widoku mapy
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

function post_monuments(){
        //Metoda która pobiera elementy z API w zależności które checkboxy są zaznaczone.
        //Jeśli żaden nie jest zaznaczony a użytkownik kliknie seach to nic nie dostanie.
        data=[]

        check_monuments()
        layerGroup.clearLayers();
        for(item of data){
           marker =fetch(`/map/api/points/${item.toString()}`)
                        .then(response => response.json())
                        .then(data=> {

                            data.forEach(addElements);

                            function addElements(item, index) {
                                var punkt = L.marker(
                                    [item.coordinateX, item.coordinateY],
                                    {}
                                ).addTo(layerGroup);
                                var popup = L.popup({"Width": "300px"});
                                var html = $(`<div id="html_96971d4f2da24e9499eaf1295989655a" style="width: 100.0%; height: 100.0%;">
                                <strong>${item.name}</strong>
                                <p> ${item.descriptions}</p>
                                <a href="/trails/point/${item.id}">Więcej</a></div>`)[0];

                                popup.setContent(html);
                                punkt.bindPopup(popup);
                            }
                        })
        }
    }

        //Obsługa scrola na mapie
        $("#map_1de6ef4f1218487da9d6da057bb8f454").bind('mousewheel DOMMouseScroll', function (event) {
        event.stopPropagation();
         if (event.ctrlKey === true) {
                 event.preventDefault();
             map_1de6ef4f1218487da9d6da057bb8f454.scrollWheelZoom.enable();
               $('#map_1de6ef4f1218487da9d6da057bb8f454').removeClass('map-scroll');
             setTimeout(function(){
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