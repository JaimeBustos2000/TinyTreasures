let cart = JSON.parse(localStorage.getItem('cart')) || {}; // Recuperar carrito desde localStorage o inicializar vacío

// Función para agregar producto al carrito
function addToCart(productId, productName) {
    const quantity = parseInt(document.querySelector('.form-select').value) || 1;

    if (cart[productId]) {
        cart[productId].quantity += quantity; // Incrementar cantidad si ya existe
    } else {
        cart[productId] = { name: productName, quantity: quantity }; // Agregar nuevo producto
    }

    localStorage.setItem('cart', JSON.stringify(cart)); // Sobrescribir el carrito en localStorage
    updateCartUI();
}

// Función para actualizar la interfaz del carrito
function updateCartUI() {
    const cartItemsContainer = document.getElementById('dropdown');

    if (Object.keys(cart).length === 0) {
        cartItemsContainer.textContent = 'Sin productos'; // Mostrar mensaje si está vacío
        localStorage.removeItem('cart'); // Vaciar carrito en localStorage
        return;
    }

    let content = '';
    Object.keys(cart).forEach(productId => {
        const product = cart[productId];
        content += `
            ${product.name} (x${product.quantity}) 
            <button onclick="decreaseQuantity('${productId}')">-</button>
            <button onclick="increaseQuantity('${productId}')">+</button>
            <button onclick="removeFromCart('${productId}')">Eliminar</button>
            <br>
        `;
    });

    cartItemsContainer.innerHTML = content; // Actualizar contenido del carrito
}

// Función para guardar el carrito en localStorage
function saveCartToLocalStorage() {
    localStorage.setItem('cart', JSON.stringify(cart));
}

// Función para eliminar producto del carrito
function removeFromCart(productId) {
    delete cart[productId];
    saveCartToLocalStorage();
    updateCartUI();
}

// Función para disminuir cantidad
function decreaseQuantity(productId) {
    if (cart[productId]) {
        cart[productId].quantity--;
        if (cart[productId].quantity <= 0) {
            delete cart[productId];
        }
    }
    saveCartToLocalStorage();
    updateCartUI();
}

// Función para aumentar cantidad
function increaseQuantity(productId) {
    if (cart[productId]) {
        cart[productId].quantity++;
    }
    saveCartToLocalStorage();
    updateCartUI();
}

// Evento para el botón "Agregar al carrito"
document.getElementById('add-to-cart').addEventListener('click', () => {
    const productId = document.getElementById('product-id').value;
    const productName = document.querySelector('.card-title').innerText.replace('Nombre: ', '');
    addToCart(productId, productName);
});

// Inicializar el carrito en la interfaz al cargar la página
updateCartUI();

