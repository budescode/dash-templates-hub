(function () {
  var mapInstance = null;

  function initVectorMap() {
    var container = document.getElementById('world-map-marker');
    if (!container || typeof jsVectorMap === 'undefined') return;

    // Clean up previous instance
    if (mapInstance) {
      try { mapInstance.destroy(); } catch (e) {}
      mapInstance = null;
    }
    // Remove any leftover vmap div
    var old = document.getElementById('vmap');
    if (old) old.remove();

    // Create inner div
    var mapDiv = document.createElement('div');
    mapDiv.id = 'vmap';
    mapDiv.style.height = '490px';
    container.appendChild(mapDiv);

    mapInstance = new jsVectorMap({
      selector: '#vmap',
      map: 'world',
      backgroundColor: 'transparent',
      zoomOnScroll: false,
      zoomButtons: false,
      regionStyle: {
        initial: { fill: '#e6eaf0', stroke: '#d3d9e3', 'stroke-width': 1, 'stroke-opacity': 0.4 },
        hover:   { fill: '#0f9aee', cursor: 'pointer' },
      },
      markerStyle: {
        initial: { r: 7, fill: '#7774e7', stroke: '#0f9aee', 'stroke-width': 2, 'stroke-opacity': 0.4 },
        hover:   { r: 10, fill: '#0f9aee', 'stroke-opacity': 0.8, cursor: 'pointer' },
      },
      markers: [
        { name: 'India: 350',     coords: [21.00,  78.00] },
        { name: 'Australia: 250', coords: [-33.00, 151.00] },
        { name: 'USA: 250',       coords: [36.77, -119.41] },
        { name: 'UK: 250',        coords: [55.37,   -3.41] },
        { name: 'UAE: 250',       coords: [25.20,   55.27] },
      ],
    });
  }

  // Watch for Dash page-content changes
  var observer = new MutationObserver(function () {
    if (document.getElementById('world-map-marker')) {
      setTimeout(initVectorMap, 100);
    }
  });

  function start() {
    var target = document.getElementById('page-content');
    if (target) {
      observer.observe(target, { childList: true, subtree: false });
    } else {
      setTimeout(start, 100);
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', start);
  } else {
    start();
  }
})();
