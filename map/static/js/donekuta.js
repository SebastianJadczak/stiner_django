// for getting the sorting status to be displayed in sorting dropdown placeholder
function get(name) {
    if (name = (new RegExp('[?&]' + encodeURIComponent(name) + '=([^&]*)')).exec(location.search))  //location.search give query sling part
        return decodeURIComponent(name[1]);
}


if (get('sorting'))
    document.getElementById('placeholder-sort').innerText = "Sort: " + document.getElementById(get('sorting')).innerText;
if (get('filtercity'))
    document.getElementById('placeholder-city').innerText = "Filter: " + get('filtercity')
if (get('filtercountry'))
    document.getElementById('placeholder-country').innerText = "Filter: " + get('filtercountry')


// for getting url after applying sorting
function finalurl() {
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('sorting', document.getElementById("sort-list").value);
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url
}

function filteringcity() {
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('filtercity', document.getElementById("filter-city").value);
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url
}

function filteringcountry() {
    var url = new URL(window.location.href);
    var search_params = url.searchParams;
    search_params.set('filtercountry', document.getElementById("filter-country").value);
    url.search = search_params.toString();
    var new_url = url.toString();
    return new_url
}
