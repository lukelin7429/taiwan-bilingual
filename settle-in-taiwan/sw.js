// Offline support: the app, lessons, recordings and stroke data are cached on first visit.
const VERSION = 'sit-v3';
const SHELL = [
  './', 'index.html', 'manifest.webmanifest', 'css/app.css', 'js/app.js',
  'content/content.json', 'audio/index.json', 'vendor/hanzi-writer.min.js',
  'icons/icon-192.png', 'icons/icon-512.png', 'icons/apple-touch-icon.png',
];

self.addEventListener('install', (e) => {
  e.waitUntil(caches.open(VERSION).then((c) => c.addAll(SHELL)).then(() => self.skipWaiting()));
});

self.addEventListener('activate', (e) => {
  e.waitUntil(caches.keys()
    .then((keys) => Promise.all(keys.filter((k) => k !== VERSION && k !== 'sit-media').map((k) => caches.delete(k))))
    .then(() => self.clients.claim())
    .then(() => Promise.all([fetch('audio/index.json').then((r) => r.json()), fetch('content/content.json').then((r) => r.json())]))
    .then(([idx, content]) => {
      // Fetch every recording and stroke file in the background so lessons work offline later.
      const files = new Set();
      Object.values(idx).forEach((v) => Object.values(v).forEach((s) => Object.values(s).forEach((f) => files.add(`audio/${f}`))));
      content.units.forEach((u) => u.write.forEach((ch) => files.add(`vendor/hanzi/${encodeURIComponent(ch)}.json`)));
      return caches.open('sit-media').then((c) => c.addAll([...files]));
    })
    .catch(() => {}));
});

self.addEventListener('fetch', (e) => {
  const url = new URL(e.request.url);
  if (e.request.method !== 'GET' || url.origin !== location.origin) return;
  // Recordings and stroke data never change: cache first.
  if (/\/(audio\/[0-9a-f]+\.mp3|vendor\/hanzi\/)/.test(url.pathname)) {
    e.respondWith(caches.match(e.request).then((hit) => hit || fetch(e.request).then((res) => {
      if (res.ok) { const copy = res.clone(); caches.open('sit-media').then((c) => c.put(e.request, copy)); }
      return res;
    })));
    return;
  }
  // Everything else: network first so updates arrive, cache when offline.
  e.respondWith(
    fetch(e.request)
      .then((res) => {
        if (res.ok) { const copy = res.clone(); caches.open(VERSION).then((c) => c.put(e.request, copy)); }
        return res;
      })
      .catch(() => caches.match(e.request, { ignoreSearch: true }).then((r) => r || caches.match('index.html')))
  );
});
