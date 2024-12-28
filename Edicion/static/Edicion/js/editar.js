document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('form-new-product');
    form.addEventListener('submit', function(event) {
        localStorage.removeItem('apiproducts')
        localStorage.removeItem('products')
        console.log('Cache del navegador borrada');
    });
});