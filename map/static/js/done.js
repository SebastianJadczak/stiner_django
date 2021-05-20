var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();

function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
$.ajaxSetup({
    beforeSend: function(xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});


function sort(type){
    $.post({
            url: "../map/sort/",
            success: function(){
                console.log('ok')
                      },
            dataType: 'json',
            error: function (response, error) {
                console.log('nie ok')
            },
            data: {'type': type},
            headers: {
                'csrfmiddlewaretoken': csrftoken

            }

        })

}