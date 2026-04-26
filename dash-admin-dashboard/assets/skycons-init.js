/* Initialize Skycons animated weather icons for Dash */
(function() {
  var icons = null;

  function initSkycons() {
    if (typeof Skycons === 'undefined') return;

    var skyconsColor = getComputedStyle(document.documentElement)
      .getPropertyValue('--skycons-color').trim() || '#ff6849';

    if (icons) {
      try { icons.pause(); icons.remove('all'); } catch(e) {}
    }

    icons = new Skycons({ color: skyconsColor });

    var weatherTypes = [
      'clear-day', 'clear-night',
      'partly-cloudy-day', 'partly-cloudy-night',
      'cloudy', 'rain', 'sleet', 'snow', 'wind', 'fog'
    ];

    weatherTypes.forEach(function(type) {
      var elements = document.getElementsByClassName(type);
      for (var i = 0; i < elements.length; i++) {
        icons.set(elements[i], type);
      }
    });

    icons.play();
  }

  /* Run after Skycons script is ready */
  function waitAndInit() {
    if (typeof Skycons !== 'undefined') {
      initSkycons();
    } else {
      setTimeout(waitAndInit, 50);
    }
  }

  /* Re-run when Dash updates page content */
  document.addEventListener('DOMContentLoaded', function() {
    waitAndInit();

    var pageContent = document.getElementById('page-content');
    if (pageContent) {
      new MutationObserver(function() {
        setTimeout(initSkycons, 50);
      }).observe(pageContent, { childList: true });
    }
  });
}());
