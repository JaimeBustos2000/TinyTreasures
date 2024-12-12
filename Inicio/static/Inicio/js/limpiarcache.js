document.addEventListener('DOMContentLoaded', function () {
    limpiarCache();
});

function limpiarCache() {
    let button = document.getElementById('disconnect');
    if (button) {
        button.addEventListener('click', function () {
            localStorage.removeItem('productos');
            console.log('Cache limpiada');
        });
    } else {
        console.error('El botón con ID "disconnect" no existe en el DOM.');
    }
}
