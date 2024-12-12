document.addEventListener('DOMContentLoaded', function () {
    var checkbox = document.getElementById('flexSwitchCheckDefault')
    var type = document.getElementById('typeuser')
    checkbox.addEventListener('change', function () {
        if (checkbox) {
            if (this.checked) {
                type.innerHTML = 'Empresa/pyme';
            } else {
                type.innerHTML = 'Individual';
            }
        } else {
            console.log('No se encontró el contenedor form-nombre-empresa');
        }
    });
});

