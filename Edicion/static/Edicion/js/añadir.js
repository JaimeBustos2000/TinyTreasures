// Funcion para obtener la extension del archivo subido
function obtain_extension(file) {
    return file.name.split('.').pop().toLowerCase();
}

// Función para obtener el nombre del archivo sin la extensión
function obtain_filename_without_extension(file) {
    let filename = file.name.split('.').slice(0, -1).join('.');
    return filename;
}

// Obtener el csrf token de django
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
            // Verificar que el nombre del archivo no tenga más de 15 caracteres
            let filename = obtain_filename_without_extension(file);
            if (filename.length > 15) {
                alert('El nombre del archivo no puede tener más de 15 caracteres');
                return;
            }

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
                        console.log('Borrar cache del navegador');
                        localStorage.removeItem('productos');
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
});
