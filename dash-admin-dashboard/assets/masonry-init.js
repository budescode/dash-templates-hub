(function () {
  function initMasonry() {
    var grid = document.querySelector('.masonry');
    if (!grid || typeof Masonry === 'undefined') return;
    new Masonry(grid, {
      itemSelector: '.masonry-item',
      columnWidth: '.masonry-sizer',
      percentPosition: true
    });
  }

  // Watch for Dash page-content changes
  var observer = new MutationObserver(function () {
    setTimeout(initMasonry, 50);
  });

  function start() {
    var target = document.getElementById('page-content');
    if (target) {
      observer.observe(target, { childList: true, subtree: false });
      initMasonry();
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
