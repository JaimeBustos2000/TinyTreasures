
async function getCompanies() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/companies/', {
            method: 'GET',
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
        return null;
    }
}
/* PRODUCTS */
async function fetchProducts() {
    try {
        const response = await fetch('http://127.0.0.1:8000/api/all_products', {
            method: 'GET',
        });
        const data = await response.json();
        return data;
    } catch (error) {
        console.error('Error:', error);
    }
}

async function fetchData() {
    const cachedData = sessionStorage.getItem('apiData');

    console.log('Cached data:', cachedData);
    if (cachedData) {
        var jsondata = JSON.parse(cachedData);
        var marca_select = document.getElementById('marca');
        var data_length = jsondata.length;

        console.log('Data from cache:', jsondata);

        for (var i = 0; i < data_length; i++) {
            let option = document.createElement('option');
            option.text = jsondata[i];
            option.value = jsondata[i];
            marca_select.add(option);
        }
    } else {
        console.log('No data in cache. Fetching from API');
        const response = await getCompanies();

        if (response && response.companies) {
            const companies = response.companies;
            sessionStorage.setItem('apiData', JSON.stringify(companies));
            console.log('Data from API:', companies);

            var marca_select = document.getElementById('marca');
            companies.forEach(company => {
                let option = document.createElement('option');
                option.text = company;
                option.value = company;
                marca_select.add(option);
            });
        } else {
            console.error('No companies data in API response');
        }
    }
}

async function Products() {
    const cachedData = sessionStorage.getItem('apiproducts');
    if (cachedData) {
        console.log('Data from cache:', cachedData);
        return JSON.parse(cachedData);
    } else {
        console.log('No data in cache. Fetching from API');

        const response = await fetchProducts();
        if (response && response.products) {
            const products = response.products;
            sessionStorage.setItem('apiproducts', JSON.stringify(products));
            console.log('Data from API in Products:', products);
            return products;
        } else {
            console.error('No products data in API response');
            return null;
        }
    }
}

document.addEventListener('DOMContentLoaded',async () => {
    await fetchData();
    await Products();
});




