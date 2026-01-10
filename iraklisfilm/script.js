// ფუნქციები Register/Login
function showRegister() {
    document.getElementById("register").style.display = "block";
    const firstDiv = document.querySelector(".first");
    if (firstDiv) firstDiv.style.display = "none"; // first დივის დამალვა
}

function showlogin() {
    document.getElementById("login").style.display = "block";
    const firstDiv = document.querySelector(".first");
    if (firstDiv) firstDiv.style.display = "none"; // first დივის დამალვა
}

// 🚀 Autoplay Policy workaround
document.addEventListener('click', initSoundOnce, { once: true });

function initSoundOnce() {
    const sound = document.getElementById('hoverSound');
    if (!sound) return;
    // ერთი “ცარიელი” დაკვრა ბრაუზერის ავტოპლეისთვის
    sound.play().catch(() => {});
    sound.pause();
    sound.currentTime = 0;
}

// 🎧 Hover ხმები ყველა ღილაკზე
const buttons = document.querySelectorAll('.menu button');
const sound = document.getElementById('hoverSound');

buttons.forEach(button => {
    button.addEventListener('mouseenter', () => {
        if (!sound) return;
        sound.currentTime = 0; // თავიდან დაიწყოს ყოველი hover-ზე
        sound.play().catch(() => {}); // დაუკრავს მხოლოდ თუ autoplay policy საშუალებას აძლევს
    });
});
document.getElementById("register").addEventListener("click", () => {
    fetch("register.html")
        .then(response => response.text())
        .then(data => {
            const temp = document.createElement("div");
            temp.innerHTML = data;

            // წამოვიღოთ კონკრეტული Div register.html-დან
            const newDiv = temp.querySelector("#registerDiv");

            if (newDiv) {
                const target = document.getElementById("targetDiv");
                target.innerHTML = "";  // ძველი კონტენტის წაშლა
                target.appendChild(newDiv);

                // ანდა, თუ გინდა თავიდან დამალული იყო, შემდეგ გამოჩენა
                newDiv.style.display = "block";
            }
        })
        .catch(error => console.error("Error loading register.html:", error));
});

