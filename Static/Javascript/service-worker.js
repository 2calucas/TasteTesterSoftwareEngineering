self.addEventListener("install", event => {
    event.waitUntil(
        caches.open("taste-cache").then(cache => {
            return cache.addAll([
                "/",
                "/static/css/home.css",
                "/static/css/dashboard.css",
                "/static/css/makeareview.css"
            ]);
        })
    );
});

self.addEventListener("fetch", event => {
    event.respondWith(
        caches.match(event.request).then(response => {
            return response || fetch(event.request);
        })
    );
});