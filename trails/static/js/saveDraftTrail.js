const saveDraftTrail = '/user_trails/save_draft_trail/'
let content_trail = document.querySelector('.content_trail')

if(window.location.pathname ===saveDraftTrail){
    content_trail.style.margin = '0'
    content_trail.style.width = '100vw'
    content_trail.style.backgroundImage = "url(../../static/img/beach.jpg)"
    content_trail.style.backgroundSize = "cover"
}