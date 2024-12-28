// Función para leer y dibujar el carrito almacenado en localStorage
function drawCartFromLocalStorage() {
    const cartItemsContainer = document.getElementById('dropdown'); // Contenedor del carrito
    const cart = localStorage.getItem('cart'); // Leer carrito desde localStorage

    if (!cart) {
        cartItemsContainer.innerHTML = '<p>Sin productos</p>'; // Mostrar mensaje si no hay carrito
        return;
    }

    const parsedCart = JSON.parse(cart); // Parsear carrito almacenado
    let content = '';

    // Recorrer el carrito y generar el contenido dinámico
    Object.keys(parsedCart).forEach(productId => {
        const product = parsedCart[productId];
        content += `
            <p>
                ${product.name} (x${product.quantity}) 
                <button onclick="decreaseQuantity('${productId}')">-</button>
                <button onclick="increaseQuantity('${productId}')">+</button>
                <button onclick="removeFromCart('${productId}')">Eliminar</button>
            </p>
        `;
    });

    cartItemsContainer.innerHTML = content; // Actualizar el contenido del contenedor
}

document.addEventListener('DOMContentLoaded', () => {
    drawCartFromLocalStorage(); // Dibujar el carrito desde localStorage
});