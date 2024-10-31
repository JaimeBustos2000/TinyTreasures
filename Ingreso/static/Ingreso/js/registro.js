var checkbox = document.getElementById('flexSwitchCheckDefault')
var type = document.getElementById('typeuser')

checkbox.addEventListener('change', function () {
    if (this.checked) {
        type.innerHTML = 'Empresa/pyme';
    } else {
        type.innerHTML = 'Individual';
    }
});


document.addEventListener('DOMContentLoaded', function () {
    var form = document.getElementById('registroform');
    console.log('Formulario:', form);

    form.addEventListener('submit', function (e) {
        var terms_check = document.getElementById('defaultCheck1');
        console.log('Checkbox:', terms_check);
        if (!terms_check.checked) {
            e.preventDefault();
            alert('Debe aceptar los términos y condiciones');
        }
    });
});