function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", csrftoken);
        }
    }
});
var csrftoken = jQuery("[name=csrfmiddlewaretoken]").val();
let len_trail = document.getElementById('len_trail')

function addAudioCountUser() {
    $.post({
        url: "audioCount/",
        headers: {
            'csrfmiddlewaretoken': csrftoken
        }

    })

}

let audioTrail = document.getElementById('audioTrail')
let closeAudioTrail = document.getElementById('closeAudioTrail')

function openAudioTrailUser() {
    audioTrail.style.display = 'block'
    addAudioCountUser()
}

if (closeAudioTrail) {
    closeAudioTrail.addEventListener('click', function () {
        audioTrail.style.display = 'none'
    })
}