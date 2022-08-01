eel.expose(photo_name)
function photo_name(name) {
    console.log(name)
    document.getElementById('qr_img').src = document.getElementById('qr_img').src + name;
}