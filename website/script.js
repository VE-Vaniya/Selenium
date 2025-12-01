// Product Data
const products = [
    { id: 1, name: "Selenium T-Shirt", price: 2500, category: "clothing", image: "https://placehold.co/300x200?text=T-Shirt" },
    { id: 2, name: "Automation Hoodie", price: 4500, category: "clothing", image: "https://placehold.co/300x200?text=Hoodie" },
    { id: 3, name: "WebDriver Mug", price: 1200, category: "accessories", image: "https://placehold.co/300x200?text=Mug" },
    { id: 4, name: "Python Bot Sticker", price: 200, category: "accessories", image: "https://placehold.co/300x200?text=Sticker" },
    { id: 5, name: "Java Duke Plush", price: 3000, category: "toys", image: "https://placehold.co/300x200?text=Plush" },
    { id: 6, name: "Test Script Cap", price: 1500, category: "clothing", image: "https://placehold.co/300x200?text=Cap" },
    { id: 7, name: "Bug Hunter Hat", price: 1800, category: "clothing", image: "https://placehold.co/300x200?text=Bug+Hat" },
    { id: 8, name: "QA Engineer Notebook", price: 800, category: "accessories", image: "https://placehold.co/300x200?text=Notebook" },
    { id: 9, name: "Debugging Duck", price: 500, category: "toys", image: "https://placehold.co/300x200?text=Duck" },
    { id: 10, name: "CI/CD Keychain", price: 300, category: "accessories", image: "https://placehold.co/300x200?text=Keychain" },
    { id: 11, name: "Full Stack Backpack", price: 6000, category: "accessories", image: "https://placehold.co/300x200?text=Backpack" },
    { id: 12, name: "Legacy Code Shirt", price: 2200, category: "clothing", image: "https://placehold.co/300x200?text=Legacy" },
];

// State
let cart = [];
let currentUser = null;

// DOM Elements
const loginPage = document.getElementById('login-page');
const mainPage = document.getElementById('main-page');
const productGrid = document.getElementById('product-grid');
const cartModal = document.getElementById('cart-modal');
const cartItemsContainer = document.getElementById('cart-items');
const cartCount = document.getElementById('cart-count');
const cartTotal = document.getElementById('cart-total');
const categoryFilter = document.getElementById('category-filter');

// Initialization
document.addEventListener('DOMContentLoaded', () => {
    if (window.location.pathname.includes('index.html') || window.location.pathname.endsWith('/')) {
        checkLogin();
        renderProducts(products);
        setupEventListeners();
    } else if (window.location.pathname.includes('delivery.html')) {
        setupDeliveryForm();
    }
});

function checkLogin() {
    const user = sessionStorage.getItem('user');
    if (user) {
        currentUser = user;
        showMainPage();
    } else {
        showLoginPage();
    }
}

function showLoginPage() {
    if (loginPage) loginPage.style.display = 'flex';
    if (mainPage) mainPage.style.display = 'none';
}

function showMainPage() {
    if (loginPage) loginPage.style.display = 'none';
    if (mainPage) mainPage.style.display = 'block';
}

// Login Logic
function handleLogin(e) {
    e.preventDefault();
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;

    if (username === 'test' && password === '123') {
        sessionStorage.setItem('user', username);
        currentUser = username;
        showMainPage();
    } else {
        alert('Invalid credentials');
    }
}

// Product Logic
function renderProducts(items) {
    if (!productGrid) return;
    productGrid.innerHTML = items.map(product => {
        const inCart = cart.find(item => item.id === product.id);
        return `
        <div class="product-card" id="product-${product.id}" data-name="${product.name}" data-price="${product.price}" data-category="${product.category}">
            <img src="${product.image}" alt="${product.name}" class="product-image">
            <div class="product-info">
                <h3 class="product-title" id="title-${product.id}">${product.name}</h3>
                <p class="product-price">PKR ${product.price}</p>
                <button 
                    onclick="toggleCart(${product.id})" 
                    class="btn add-to-cart-btn ${inCart ? 'added' : ''}"
                    id="add-to-cart-${product.id}"
                    data-id="${product.id}">
                    ${inCart ? 'Remove' : 'Add to Cart'}
                </button>
            </div>
        </div>
    `}).join('');
}

function filterProducts() {
    const category = categoryFilter.value;
    const filtered = category === 'all'
        ? products
        : products.filter(p => p.category === category);
    renderProducts(filtered);
}

// Cart Logic
window.toggleCart = function (productId) {
    const index = cart.findIndex(item => item.id === productId);
    const btn = document.getElementById(`add-to-cart-${productId}`);

    if (index === -1) {
        const product = products.find(p => p.id === productId);
        cart.push({ ...product, qty: 1 });
        if (btn) {
            btn.textContent = 'Remove';
            btn.classList.add('added');
        }
    } else {
        cart.splice(index, 1);
        if (btn) {
            btn.textContent = 'Add to Cart';
            btn.classList.remove('added');
        }
    }
    updateCartUI();
};

function updateCartUI() {
    if (cartCount) cartCount.textContent = cart.reduce((acc, item) => acc + item.qty, 0);
    renderCartItems();
}

function renderCartItems() {
    if (!cartItemsContainer) return;

    if (cart.length === 0) {
        cartItemsContainer.innerHTML = '<p style="text-align:center; color:var(--text-secondary)">Your cart is empty</p>';
        if (cartTotal) cartTotal.textContent = 'PKR 0';
        return;
    }

    let total = 0;
    cartItemsContainer.innerHTML = cart.map(item => {
        total += item.price * item.qty;
        return `
        <div class="cart-item">
            <div class="cart-item-info">
                <h4>${item.name}</h4>
                <p>PKR ${item.price}</p>
            </div>
            <div class="cart-item-controls">
                <button class="qty-btn" onclick="updateQty(${item.id}, -1)">-</button>
                <span>${item.qty}</span>
                <button class="qty-btn" onclick="updateQty(${item.id}, 1)">+</button>
            </div>
        </div>
    `}).join('');

    if (cartTotal) cartTotal.textContent = `PKR ${total}`;
}

window.updateQty = function (id, change) {
    const item = cart.find(i => i.id === id);
    if (item) {
        item.qty += change;
        if (item.qty <= 0) {
            toggleCart(id); // Remove if qty is 0
        } else {
            updateCartUI();
        }
    }
};

// Event Listeners
function setupEventListeners() {
    const loginForm = document.getElementById('login-form');
    if (loginForm) loginForm.addEventListener('submit', handleLogin);

    const cartBtn = document.getElementById('cart-btn');
    const closeCartBtn = document.getElementById('close-cart');
    const checkoutBtn = document.getElementById('checkout-btn');

    if (cartBtn) cartBtn.addEventListener('click', () => cartModal.classList.add('open'));
    if (closeCartBtn) closeCartBtn.addEventListener('click', () => cartModal.classList.remove('open'));

    if (checkoutBtn) checkoutBtn.addEventListener('click', () => {
        if (cart.length === 0) {
            alert("Your cart is empty! Please add items before checking out.");
            return;
        }
        window.open('checkout.html', '_blank');
    });

    if (categoryFilter) categoryFilter.addEventListener('change', filterProducts);
}

// Delivery Form Logic
function setupDeliveryForm() {
    const form = document.getElementById('delivery-form');
    const confirmation = document.getElementById('confirmation-screen');

    if (!form) return;

    form.addEventListener('submit', (e) => {
        e.preventDefault();

        const promptVal = prompt("Please enter the confirmation code (1100):");

        if (promptVal === '1100') {
            alert("Order has been confirmed");
            form.style.display = 'none';
            if (confirmation) confirmation.style.display = 'block';
        } else {
            alert("Invalid confirmation code!");
        }
    });

    // Coupon Logic
    const couponSelect = document.getElementById('coupons');
    if (couponSelect) {
        couponSelect.addEventListener('change', () => {
            const selected = Array.from(couponSelect.selectedOptions);
            if (selected.length > 5) {
                alert("You can only select up to 5 coupons");
                selected[selected.length - 1].selected = false;
            }
        });
    }
}

window.goHome = function () {
    if (window.top) {
        window.top.location.href = 'index.html';
    } else {
        window.location.href = 'index.html';
    }
};
