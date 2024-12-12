// Funcion para obtener la extension del archivo subido
function obtain_extension(file) {
    return file.name.split('.').pop().toLowerCase();
}

// Obtener el csfrtoken de django
function getCSRFToken() {
    let csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    return csrfToken;
}

// Intercepta el evento submit del formulario antes de que se envíe
document.getElementById('form-new-product').addEventListener('submit', function (event) { 
    event.preventDefault();
    console.log('Formulario enviado');

    // Obtener el archivo subido
    let file_input = document.getElementById('image');
    let file = file_input.files[0];

    if (!file) {
        alert('Debe seleccionar un archivo');
        return;
    } else {
        let file_extension = obtain_extension(file);
        if (['jpg', 'jpeg', 'png', 'webp'].indexOf(file_extension) === -1) {
            alert('El archivo seleccionado no es una imagen');
            return;
        } else {
            let formData = new FormData(document.getElementById('form-new-product'));
            fetch('http://127.0.0.1:8000/Mis-Productos/addproduct/', {
                method: 'POST',
                body: formData,
                headers: {
                    'X-CSRFToken': getCSRFToken()
                }
            }).then(response => response.json())
                .then(data => {
                    if (data.status === 'OK') {
                        alert('Producto añadido correctamente');
                        window.location.href = '/Mis-Productos';
                    } else {
                        alert('Error al añadir el producto');
                    }
                })
                .catch(error => {
                    console.error('Error al añadir el producto:', error);
                });
        }
    }
} );