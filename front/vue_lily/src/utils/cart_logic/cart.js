let cart = JSON.parse(localStorage.getItem('cart_storage')) || [];

function SaveLocalData(object) {
    localStorage.setItem('cart_storage', JSON.stringify(object));
}

function AddToCart(product) {
    let product_is_exist = false;
    console.log("funtion started successful", product);
    cart.forEach(element => {
        if(element.id === product.id){
            product_is_exist = true;
            element.quantity +=1;
        }
    });

    if(!product_is_exist){
        cart.push({
            id: product.id,
            quantity: 1,
            name: product.name,
            price: product.price,
            category: product.category,
            image: product.image,
            slug_url: product.slug_url
        });
        
    };

    SaveLocalData(cart);
    RedirectToCart();
    console.log('cart:', cart);
};

function RedirectToCart() {
    window.location.href = '/cart';
}

function DeleteItemFromCart(id_product) {
    const indexToDelete = cart.findIndex((item) => item.id === id_product);
    cart.splice(indexToDelete, 1);
    SaveLocalData(cart);
    location.reload();
};

export { AddToCart, RedirectToCart,SaveLocalData, DeleteItemFromCart };