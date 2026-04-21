// YouTube ლინკის embed-ად გარდაქმნა
function convertToEmbed(url) {
    if (!url) return '';
    url = url.trim();
    let videoId = '';

    if (url.includes('v=')) {
        videoId = url.split('v=')[1].split('&')[0];
    } else if (url.includes('youtu.be/')) {
        videoId = url.split('youtu.be/')[1].split(/[?#]/)[0];
    } else if (url.includes('embed/')) {
        return url.split(/[?#]/)[0];
    }

    return videoId ? `https://www.youtube.com/embed/${videoId}` : url;
}

document.addEventListener('DOMContentLoaded', () => {

    // 🚀 Autoplay Policy workaround
    document.addEventListener('click', initSoundOnce, { once: true });

    function initSoundOnce() {
        const sound = document.getElementById('hoverSound');
        if (!sound) return;
        sound.play().catch(() => {});
        sound.pause();
        sound.currentTime = 0;
    }

    // 🎧 Hover ხმები ყველა ღილაკზე
    const buttons = document.querySelectorAll('.menu button');
    const sound = document.getElementById('hoverSound');

    if (buttons.length > 0 && sound) {
        buttons.forEach(button => {
            button.addEventListener('mouseenter', () => {
                sound.currentTime = 0;
                sound.play().catch(() => {});
            });
        });
    }

    // iframe-ების ავტომატური კონვერტაცია
    document.querySelectorAll('iframe').forEach(iframe => {
        const currentSrc = iframe.getAttribute('src');
        if (currentSrc && !currentSrc.includes('embed/')) {
            iframe.setAttribute('src', convertToEmbed(currentSrc));
        }
    });

    // Upload ფორმა - ლინკის ავტომატური კონვერტაცია
    const uploadForm = document.querySelector('.admin-panel form');
    if (uploadForm) {
        uploadForm.addEventListener('submit', function () {
            const input = document.querySelector('input[name="movie_file"]');
            if (input) {
                input.value = convertToEmbed(input.value);
            }
        });
    }

});