/* ============================================================
   Chiayi County Interactive Township Map (Leaflet + TopoJSON)
   Polygons from g0v/twgeojson, filtered for 嘉義縣
   ============================================================ */

const TOWNSHIP_META = {
  taibao:    { zh:'太保市',  en:'Taibao City',       emoji:'🏛️' },
  puzi:      { zh:'朴子市',  en:'Puzi City',          emoji:'🏙️' },
  budai:     { zh:'布袋鎮',  en:'Budai Township',     emoji:'🦐' },
  dalin:     { zh:'大林鎮',  en:'Dalin Township',     emoji:'🚉' },
  minxiong:  { zh:'民雄鄉',  en:'Minxiong Township',  emoji:'🍍' },
  xikou:     { zh:'溪口鄉',  en:'Xikou Township',     emoji:'🌾' },
  xingang:   { zh:'新港鄉',  en:'Xingang Township',   emoji:'🏮' },
  liujiao:   { zh:'六腳鄉',  en:'Liujiao Township',   emoji:'🌻' },
  dongshi:   { zh:'東石鄉',  en:'Dongshi Township',   emoji:'🦪' },
  yizhu:     { zh:'義竹鄉',  en:'Yizhu Township',     emoji:'🍉' },
  lucao:     { zh:'鹿草鄉',  en:'Lucao Township',     emoji:'🦌' },
  shuishang: { zh:'水上鄉',  en:'Shuishang Township', emoji:'✈️' },
  zhongpu:   { zh:'中埔鄉',  en:'Zhongpu Township',   emoji:'🦋' },
  zhuqi:     { zh:'竹崎鄉',  en:'Zhuqi Township',     emoji:'🚂' },
  meishan:   { zh:'梅山鄉',  en:'Meishan Township',   emoji:'🍵' },
  fanlu:     { zh:'番路鄉',  en:'Fanlu Township',     emoji:'🌲' },
  dapu:      { zh:'大埔鄉',  en:'Dapu Township',      emoji:'🏞️' },
  alishan:   { zh:'阿里山鄉',en:'Alishan Township',   emoji:'🌸' }
};

/* Chinese name → slug map */
const ZH_TO_SLUG = {};
Object.entries(TOWNSHIP_META).forEach(([slug, m]) => { ZH_TO_SLUG[m.zh] = slug; });

window.initChiayiMap = function() {
  const mapEl = document.getElementById('chiayi-map');
  if (!mapEl || typeof L === 'undefined') return;

  const map = L.map('chiayi-map', {
    center: [23.48, 120.40],
    zoom: 10,
    zoomControl: true,
    scrollWheelZoom: false
  });

  /* Clean base tile */
  L.tileLayer('https://{s}.basemaps.cartocdn.com/light_nolabels/{z}/{x}/{y}{r}.png', {
    attribution: '© <a href="https://www.openstreetmap.org/copyright">OpenStreetMap</a> © <a href="https://carto.com/attributions">CARTO</a>',
    subdomains: 'abcd',
    maxZoom: 15
  }).addTo(map);

  let activeLayer = null;

  function getStyle(highlighted) {
    return {
      fillColor:   highlighted ? '#c4a055' : '#2d6032',
      fillOpacity: highlighted ? 0.65 : 0.38,
      color:       highlighted ? '#8a5a00' : '#1e4220',
      weight:      highlighted ? 2.5 : 1.5,
      opacity:     1
    };
  }

  /* Determine base path for township links */
  const pathParts = window.location.pathname.split('/');
  const eercIdx = pathParts.indexOf('eerc');
  const basePath = eercIdx >= 0
    ? pathParts.slice(0, eercIdx + 1).join('/')
    : '/chiayi/eerc';

  /* Load TopoJSON (199 KB vs 20 MB for full GeoJSON) */
  const TOPO_URL = 'https://raw.githubusercontent.com/g0v/twgeojson/master/json/twTown1982.topo.json';

  fetch(TOPO_URL)
    .then(r => r.json())
    .then(topo => {
      /* Find the object key */
      const objKey = Object.keys(topo.objects)[0];
      /* topojson-client converts to GeoJSON */
      const geojson = topojson.feature(topo, topo.objects[objKey]);
      /* Filter for Chiayi County only */
      geojson.features = geojson.features.filter(
        f => f.properties.COUNTYNAME === '嘉義縣'
      );

      L.geoJSON(geojson, {
        style: () => getStyle(false),
        onEachFeature: function(feature, layer) {
          const townName = feature.properties.TOWNNAME;
          const slug = ZH_TO_SLUG[townName];
          const meta = slug ? TOWNSHIP_META[slug] : null;

          layer.on('mouseover', function() {
            if (layer !== activeLayer) layer.setStyle(getStyle(true));
            layer.bringToFront();
          });
          layer.on('mouseout', function() {
            if (layer !== activeLayer) layer.setStyle(getStyle(false));
          });
          layer.on('click', function() {
            if (activeLayer) activeLayer.setStyle(getStyle(false));
            layer.setStyle(getStyle(true));
            activeLayer = layer;

            const en   = meta ? meta.en   : townName;
            const zh   = meta ? meta.zh   : townName;
            const emoj = meta ? meta.emoji : '📍';
            const href = slug ? `${basePath}/townships/${slug}/` : '#';

            layer.bindPopup(`
              <div class="map-popup">
                <div class="mp-emoji">${emoj}</div>
                <div class="mp-en">${en}</div>
                <div class="mp-zh">${zh}</div>
                <a class="mp-link" href="${href}">Explore →</a>
              </div>`, { maxWidth: 230, className: 'eerc-popup' }
            ).openPopup();
          });

          if (meta) {
            layer.bindTooltip(
              `<span style="font-weight:700;color:#1e4220">${meta.en}</span><br><span style="color:#c4a055;font-size:13px">${meta.zh}</span>`,
              { sticky: true, opacity: 0.95, className: 'eerc-tooltip' }
            );
          }
        }
      }).addTo(map);

      /* Fit to Chiayi County bounds */
      const tempLayer = L.geoJSON(geojson);
      map.fitBounds(tempLayer.getBounds().pad(0.06));
    })
    .catch(() => {
      /* Fallback: simple markers if TopoJSON load fails */
      const fallbackTowns = [
        { zh:'太保市', lat:23.4587, lng:120.3322 }, { zh:'朴子市', lat:23.4683, lng:120.2406 },
        { zh:'布袋鎮', lat:23.3761, lng:120.1605 }, { zh:'大林鎮', lat:23.5929, lng:120.4713 },
        { zh:'民雄鄉', lat:23.5508, lng:120.4367 }, { zh:'溪口鄉', lat:23.5848, lng:120.3970 },
        { zh:'新港鄉', lat:23.5605, lng:120.3480 }, { zh:'六腳鄉', lat:23.5009, lng:120.2835 },
        { zh:'東石鄉', lat:23.4578, lng:120.1498 }, { zh:'義竹鄉', lat:23.3857, lng:120.2483 },
        { zh:'鹿草鄉', lat:23.4462, lng:120.3295 }, { zh:'水上鄉', lat:23.4624, lng:120.3877 },
        { zh:'中埔鄉', lat:23.4338, lng:120.4887 }, { zh:'竹崎鄉', lat:23.5152, lng:120.5379 },
        { zh:'梅山鄉', lat:23.5838, lng:120.5735 }, { zh:'番路鄉', lat:23.4824, lng:120.5487 },
        { zh:'大埔鄉', lat:23.2807, lng:120.5826 }, { zh:'阿里山鄉', lat:23.5117, lng:120.6743 }
      ];
      fallbackTowns.forEach(t => {
        const slug = ZH_TO_SLUG[t.zh];
        const meta = slug ? TOWNSHIP_META[slug] : null;
        if (!meta) return;
        L.circleMarker([t.lat, t.lng], {
          radius: 10, fillColor: '#2d6032', fillOpacity: 0.7,
          color: '#1e4220', weight: 2
        }).addTo(map)
          .bindPopup(`<div class="map-popup">
            <div class="mp-emoji">${meta.emoji}</div>
            <div class="mp-en">${meta.en}</div>
            <div class="mp-zh">${meta.zh}</div>
            <a class="mp-link" href="${basePath}/townships/${slug}/">Explore →</a>
          </div>`, { className: 'eerc-popup' });
      });
      map.fitBounds([[22.9, 119.9],[23.9, 121.0]]);
    });
};

/* Inject popup + tooltip styles */
(function(){
  const s = document.createElement('style');
  s.textContent = `
    .eerc-popup .leaflet-popup-content-wrapper {
      border-radius: 12px;
      box-shadow: 0 8px 28px rgba(0,0,0,.2);
      border: 1px solid #d0e4cc;
      padding: 0; overflow: hidden;
    }
    .eerc-popup .leaflet-popup-content { margin: 0; }
    .map-popup { padding: 18px 22px; text-align: center; font-family: 'Inter', sans-serif; }
    .mp-emoji  { font-size: 30px; margin-bottom: 6px; }
    .mp-en     { font-family: 'Playfair Display', serif; font-size: 17px; font-weight: 700; color: #1e4220; margin-bottom: 2px; }
    .mp-zh     { font-size: 13px; color: #c4a055; font-weight: 600; margin-bottom: 12px; }
    .mp-link   { display: inline-block; background: #1e4220; color: #fff; border-radius: 999px;
                 padding: 6px 18px; font-size: 14px; font-weight: 600; text-decoration: none; }
    .mp-link:hover { background: #2d6032; }
    .eerc-tooltip { background: rgba(255,255,255,.97); border: 1px solid #d0e4cc;
                    border-radius: 8px; padding: 7px 12px; font-family: 'Inter', sans-serif;
                    box-shadow: 0 4px 14px rgba(0,0,0,.12); font-size: 14px; }
    .eerc-tooltip::before { display: none; }
  `;
  document.head.appendChild(s);
})();
