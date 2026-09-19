/**
 * KOFFIE ART — Central Configuration Object (Single Source of Truth)
 * Edit all business info, URLs, contacts, opening hours, preview products,
 * gallery photos, and full menu items here.
 */
const CAFE_CONFIG = {
    // ── Business Details ──
    name: "KOFFIE ART",
    tagline: "House-roasted specialty coffee and desserts, crafted with care in the heart of Mansoura.",
    shortDescription: "Specialty coffee shop & roastery in Mansoura, Egypt.",
    eyebrow: "SPECIALTY COFFEE · MANSOURA",
    sinceYear: "2021",
    rating: "4.9 ★",
    ratingReviews: "500+ reviews",

    // ── Contact & Social (TODO: update with official credentials) ──
    phone: "+20 100 000 0000", // TODO: Replace with shop direct phone
    phoneDisplay: "+20 100 000 0000",
    
    // WhatsApp (TODO: replace with official WhatsApp number; '351XXXXXXXXX' retained for QA test suite)
    whatsappNumber: "351XXXXXXXXX",
    whatsappDefaultMessage: "Hi KOFFIE ART, I'd like to ask about...",
    
    instagramHandle: "@koffieart",
    instagramUrl: "https://instagram.com/koffieart", // TODO: Replace with official Instagram profile link
    facebookUrl: "https://facebook.com/", // TODO
    tiktokUrl: "https://tiktok.com/", // TODO
    
    // ── Location & Maps (TODO: update with exact Google Maps listing) ──
    address: "El-Geish St., Mansoura, Dakahlia Governorate, Egypt",
    addressShort: "Mansoura, Egypt",
    mapsUrl: "https://maps.google.com/?q=Mansoura+Dakahlia+Egypt",
    mapsEmbedUrl: "https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d109477.56061327178!2d31.312959827055747!3d31.037933107024887!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x14f79db7a9053547%3A0xf69c7308cfd0ee6e!2sMansoura%2C%20Mansoura%20Qism%202%2C%20El%20Mansoura%2C%20Dakahlia%20Governorate!5e0!3m2!1sen!2seg!4v1700000000000!5m2!1sen!2seg",

    // ── Weekly Opening Hours (Africa/Cairo timezone) ──
    // 24-hour decimal notation: 10 = 10 AM, 24 = 12 AM midnight, 25 = 1 AM next day
    weeklyHours: [
        { day: "Saturday", dayKey: "Sat", open: 10, close: 24, openDisplay: "10:00 AM", closeDisplay: "12:00 AM", display: "10:00 AM – 12:00 AM" },
        { day: "Sunday", dayKey: "Sun", open: 10, close: 24, openDisplay: "10:00 AM", closeDisplay: "12:00 AM", display: "10:00 AM – 12:00 AM" },
        { day: "Monday", dayKey: "Mon", open: 10, close: 24, openDisplay: "10:00 AM", closeDisplay: "12:00 AM", display: "10:00 AM – 12:00 AM" },
        { day: "Tuesday", dayKey: "Tue", open: 10, close: 24, openDisplay: "10:00 AM", closeDisplay: "12:00 AM", display: "10:00 AM – 12:00 AM" },
        { day: "Wednesday", dayKey: "Wed", open: 10, close: 24, openDisplay: "10:00 AM", closeDisplay: "12:00 AM", display: "10:00 AM – 12:00 AM" },
        { day: "Thursday", dayKey: "Thu", open: 10, close: 24, openDisplay: "10:00 AM", closeDisplay: "12:00 AM", display: "10:00 AM – 12:00 AM" },
        { day: "Friday", dayKey: "Fri", open: 13, close: 24, openDisplay: "1:00 PM", closeDisplay: "12:00 AM", display: "1:00 PM – 12:00 AM" }
    ],

    // ── Menu Preview (Featured 3 items for Landing Page) ──
    // Cards 1 & 2 in 2-column grid, Card 3 full width landscape below
    menuPreview: [
        {
            id: "spanish-latte",
            name: "Signature Spanish Latte",
            description: "Silky textured milk, artisan espresso, and lightly spiced sweet cream.",
            price: "85 EGP",
            imageWebp: "assets/products/spanish_latte.webp",
            imageJpg: "assets/products/spanish_latte.jpg",
            alt: "Artisan Spanish Latte in a modern ribbed glass"
        },
        {
            id: "v60-pourover",
            name: "V60 Specialty Pour-Over",
            description: "Single-origin Ethiopian Guji with bright jasmine notes and citrus finish.",
            price: "95 EGP",
            imageWebp: "assets/products/v60_pourover.webp",
            imageJpg: "assets/products/v60_pourover.jpg",
            alt: "V60 manual pour-over specialty coffee"
        },
        {
            id: "basque-cheesecake",
            name: "Basque Burnt Cheesecake",
            description: "Caramelized deeply scorched crust with a melting custard center, baked fresh in-house daily.",
            price: "110 EGP",
            imageWebp: "assets/products/basque_cheesecake.webp",
            imageJpg: "assets/products/basque_cheesecake.jpg",
            alt: "Creamy slice of Basque burnt cheesecake on artisan plate"
        }
    ],

    // ── Gallery Images (6 images for Gallery & Lightbox) ──
    galleryImages: [
        {
            src: "assets/gallery/latte_art.webp",
            fallback: "assets/gallery/latte_art.jpg",
            alt: "Artisan tulip latte art poured in a handcrafted stoneware cup",
            title: "Artisan Pour",
            caption: "Freshly steamed micro-foam and single-origin espresso."
        },
        {
            src: "assets/gallery/interior.webp",
            fallback: "assets/gallery/interior.jpg",
            alt: "Warm minimalist specialty coffee space in Mansoura with light oak and ambient light",
            title: "The Mansoura Space",
            caption: "Designed for calm conversation, deep focus, and specialty craft."
        },
        {
            src: "assets/gallery/barista.webp",
            fallback: "assets/gallery/barista.jpg",
            alt: "Barista dialing in espresso recipe on commercial group head",
            title: "Barista Precision",
            caption: "Every cup is weighed to within 0.1g for flawless extraction."
        },
        {
            src: "assets/gallery/coffee_craft.webp",
            fallback: "assets/hero-coffee.jpg",
            alt: "Barista crafting specialty coffee with rich crema",
            title: "House Roasting",
            caption: "Small-batch specialty beans sourced with ethical provenance."
        },
        {
            src: "assets/gallery/cold_brew.webp",
            fallback: "assets/menu_images/page_1.webp",
            alt: "Refreshing artisan iced cold brew extraction",
            title: "Slow-Drip Cold Brew",
            caption: "18-hour cold steeped immersion for an ultra-smooth profile."
        },
        {
            src: "assets/gallery/desserts.webp",
            fallback: "assets/products/basque_cheesecake.jpg",
            alt: "Freshly baked artisan pastries and Basque cheesecake",
            title: "Daily Bakery",
            caption: "Handcrafted pairing desserts baked from scratch each morning."
        }
    ],

    // ── Full Menu Categories & Items (for /menu page) ──
    menuCategories: [
        {
            id: "specialty-brews",
            name: "Specialty Brews",
            description: "Manual filter methods highlighting single-origin nuances.",
            items: [
                { name: "V60 Pour-Over", desc: "Ethiopian Guji / Colombian Supremo, hand brewed", price: "95 EGP", badge: "Signature" },
                { name: "Chemex", desc: "Clean, ultra-bright body brewed for sharing (2 cups)", price: "140 EGP" },
                { name: "Aeropress", desc: "Immersion & pressure extraction with rich clarity", price: "90 EGP" },
                { name: "Cold Drip Brew", desc: "18-hour slow drip extraction served over clear ice", price: "95 EGP", badge: "Chilled" }
            ]
        },
        {
            id: "hot-coffee",
            name: "Hot Classics",
            description: "Dialed-in double-shot espresso beverages.",
            items: [
                { name: "Espresso (Doppio)", desc: "Double shot of our house seasonal specialty blend", price: "55 EGP" },
                { name: "Cortado", desc: "Equal parts velvety steamed milk and rich espresso", price: "70 EGP" },
                { name: "Flat White", desc: "Velvety micro-foam over a concentrated double ristretto", price: "75 EGP", badge: "Popular" },
                { name: "Cappuccino", desc: "Classic proportion of espresso, steamed milk, and silky foam", price: "75 EGP" },
                { name: "Caffe Latte", desc: "Smooth textured milk layered over double espresso", price: "80 EGP" },
                { name: "Spanish Latte", desc: "House condensed milk infusion with espresso & cinnamon touch", price: "85 EGP", badge: "Favorite" },
                { name: "Americano", desc: "Double espresso pulled over hot mountain spring water", price: "60 EGP" }
            ]
        },
        {
            id: "cold-coffee",
            name: "Iced & Refreshers",
            description: "Chilled specialty coffees for Mansoura sunny days.",
            items: [
                { name: "Iced Spanish Latte", desc: "Signature chilled sweet latte over artisan ice cubes", price: "90 EGP", badge: "Best Seller" },
                { name: "Iced Caffe Latte", desc: "Double shot espresso chilled with cold organic milk", price: "85 EGP" },
                { name: "Espresso Tonic", desc: "Double espresso float over premium tonic with fresh rosemary", price: "85 EGP" },
                { name: "Iced Salted Caramel Latte", desc: "Artisan caramel sauce with sea salt and espresso", price: "95 EGP" },
                { name: "Iced Shaken Americano", desc: "Aerated cold espresso shaken over ice with thick golden crema", price: "65 EGP" }
            ]
        },
        {
            id: "desserts-bakery",
            name: "Desserts & Bakery",
            description: "Baked daily in-house to pair perfectly with your brew.",
            items: [
                { name: "Basque Burnt Cheesecake", desc: "Creamy caramelized custard center baked to perfection", price: "110 EGP", badge: "Must Try" },
                { name: "San Sebastian Cheesecake", desc: "Served with warm Belgian milk chocolate pour", price: "125 EGP" },
                { name: "Chocolate Babka", desc: "Rich braided brioche loaded with dark chocolate ribbons", price: "85 EGP" },
                { name: "Almond Croissant", desc: "Twice-baked French butter croissant with almond frangipane", price: "80 EGP" },
                { name: "Tiramisu Pot", desc: "Savoiardi soaked in KOFFIE ART espresso & mascarpone", price: "95 EGP" }
            ]
        }
    ]
};

// Expose on window for vanilla script compatibility
if (typeof window !== 'undefined') {
    window.CAFE_CONFIG = CAFE_CONFIG;
}
