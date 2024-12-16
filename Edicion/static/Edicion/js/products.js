let datos;

function fetch_data() {
    // Intenta obtener los datos de localStorage
    localStorage.clear()
    let storedData = localStorage.getItem('productos');
    if (storedData) {
        // Si los datos ya están guardados, los carga desde localStorage
        datos = JSON.parse(storedData);
        console.log('Datos cargados de localStorage:', datos);
        render_products();
    }

    // En cualquier caso, hace la llamada a la API para obtener los datos más recientes
    fetch('http://127.0.0.1:8000/api/products')
        .then(response => {
            if (!response.ok) {
                throw new Error('Error en la respuesta de la API');
            }
            return response.json();
        })
        .then(data => {
            datos = data.productos;
            console.log('Datos cargados de la API:', datos);

            // Limpia el localStorage y guarda los datos más recientes
            localStorage.clear();
            localStorage.setItem('productos', JSON.stringify(datos));
            render_products();
        })
        .catch(error => {
            console.error('Error al cargar los productos:', error);
        });
}

function render_products() {
    let container = document.getElementById('card-container');
    if (!container) {
        console.error('No se encontró el contenedor con id "container"');
        return;
    }

    if (datos && datos.length > 0) {
        let html = '';

        datos.forEach(product => {
            let productUrl = 'http://127.0.0.1:8000/' + product.url;
            const productUrlParts = product.url.split('/');
            const productCode = productUrlParts[2];

            
            const destinationUrl = `/Mis-Productos/edit/${productCode}`; 

            html += `
            <a href="${destinationUrl}" class="card-link" title="Ver mas">
                <div class="card">
                    <div class="card-body">
                        <div class="image-container">
                            <img src="${productUrl}" class="card-img-top" alt="${product.nombre}">
                        </div>
                        <h5 class="card-title">${product.nombre}</h5>
                        <p class="card-text">Precio: ${product.precio}</p>
                        <p class="card-text">Stock: ${product.stock}</p>
                        <p class="card-text">Categoría: ${product.categoria}</p>
                    </div>
                </div>
            </a>
            `;
        });
        container.innerHTML = html;
    } else {
        container.innerHTML = `
        <h1 class="no-products">No hay productos disponibles, añada un nuevo producto</h1>
        `;
    }
}


document.addEventListener('DOMContentLoaded', fetch_data);
