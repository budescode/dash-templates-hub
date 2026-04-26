(function () {
  function initBootstrapComponents() {
    if (typeof bootstrap === 'undefined') return;

    // Tooltips
    document.querySelectorAll('[data-bs-toggle="tooltip"]').forEach(function (el) {
      if (!el._bsTooltip) {
        el._bsTooltip = new bootstrap.Tooltip(el);
      }
    });

    // Popovers
    document.querySelectorAll('[data-bs-toggle="popover"]').forEach(function (el) {
      if (!el._bsPopover) {
        el._bsPopover = new bootstrap.Popover(el);
      }
    });
  }

  var observer = new MutationObserver(function () {
    setTimeout(initBootstrapComponents, 100);
  });

  function start() {
    var target = document.getElementById('page-content');
    if (target) {
      observer.observe(target, { childList: true, subtree: false });
      initBootstrapComponents();
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
