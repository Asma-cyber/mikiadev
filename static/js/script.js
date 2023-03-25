// Récupère l'élément body et crée un compteur de temps
const body = document.querySelector('body');
let timex = 0;
let timey = 0;

// Défini la fonction d'animation pour modifier la position du gradient radial
function animateBackground() {
    const bgImage = `radial-gradient(circle at ${timex}px ${timey}px, rgba(0, 250, 253, 0.2) 0%, #071722 40%)`;
    body.style.backgroundImage = bgImage;
    for (let i = 0; i < window.innerWidth; i++) {
        timex = i;
        for (let j = 0; j < window.innerHeight; j++) {
            timey = j;
            body.style.backgroundImage = bgImage;
            if (timex > window.innerWidth || timey > window.innerHeight) {
                timey = 0;
                timey = 0;
            }
        }
    }


}

// Démarre l'animation à intervalle de 50ms
setInterval(animateBackground, 50);
// Sélectionne tous les liens du menu
const tabLinks = document.querySelectorAll('.tab-link');
// Sélectionne tous les panneaux du contenu
const tabPanes = document.querySelectorAll('.tab-pane');

// Boucle sur chaque lien de menu
tabLinks.forEach((tabLink, index) => {
    // Ajoute un écouteur d'événement au clic
    tabLink.addEventListener('click', (event) => {
        event.preventDefault();
        // Supprime la classe active de tous les liens de menu
        tabLinks.forEach((tabLink) => {
            tabLink.classList.remove('active');
        });
        // Ajoute la classe active au lien de menu cliqué
        tabLink.classList.add('active');
        // Masque tous les panneaux de contenu
        tabPanes.forEach((tabPane) => {
            tabPane.classList.remove('active');
        });
        // Affiche le panneau de contenu correspondant
        tabPanes[index].classList.add('active');
    });
});