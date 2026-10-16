
const WHATSAPP_NUMBER = "918123711079 ";

function openWhatsApp(message) {
    if (!/^\d{10,15}$/.test(WHATSAPP_NUMBER) ||
        WHATSAPP_NUMBER.includes("YOURNUMBER")) {
        alert(
            "Please configure Ravi Pharmacy's WhatsApp number in script.js."
        );
        return;
    }

    const url =
        "https://wa.me/" +
        WHATSAPP_NUMBER +
        "?text=" +
        encodeURIComponent(message);

    window.open(url, "_blank", "noopener,noreferrer");
}

function orderProduct(name, price) {
    const message =
        "Hello Ravi Pharmacy! I would like to enquire about:\n" +
        name +
        "\nListed price: Rs. " +
        Number(price).toFixed(2) +
        "\nPlease confirm availability and final price.";

    openWhatsApp(message);
}

function contactPharmacy() {
    openWhatsApp(
        "Hello Ravi Pharmacy, I would like to enquire about your products and services."
    );
}
