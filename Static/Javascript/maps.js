function initMap() {
    const bathurst = { lat: -33.419, lng: 149.577 }; // Bathurst coordinates
    const map = new google.maps.Map(document.getElementById("map"), {
        zoom: 13,
        center: bathurst,
    });

    // Example marker
    new google.maps.Marker({
        position: bathurst,
        map: map,
        title: "Bathurst Central",
    });
}