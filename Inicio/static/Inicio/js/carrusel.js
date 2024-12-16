let currentIndex = 0;

function moveCarousel(direction) {
    const items = document.querySelectorAll('.carousel-item');
    const totalItems = items.length;

    // Ocultar la imagen actual
    items[currentIndex].classList.remove('active');

    // Calcular el nuevo índice
    currentIndex = (currentIndex + direction + totalItems) % totalItems;

    // Mostrar la nueva imagen
    items[currentIndex].classList.add('active');
}

// Inicializar el carrusel
document.addEventListener('DOMContentLoaded', () => {
    const items = document.querySelectorAll('.carousel-item');
    items[currentIndex].classList.add('active'); // Asegurarse de que la primera imagen esté activa
});