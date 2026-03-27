(function () {
  const ready = (fn) => {
    if (document.readyState === 'loading') {
      document.addEventListener('DOMContentLoaded', fn);
    } else {
      fn();
    }
  };

  const closeHeaderDropdowns = () => {
    document.querySelectorAll('.nav-right .dropdown').forEach((dropdown) => {
      dropdown.classList.remove('show');
      const menu = dropdown.querySelector('.dropdown-menu');
      if (menu) {
        menu.classList.remove('show');
        menu.style.display = '';
      }
    });
  };

  ready(() => {
    document.addEventListener('click', (event) => {
      const sidebarToggle = event.target.closest('.sidebar .dropdown-toggle');
      if (sidebarToggle) {
        event.preventDefault();
        const parent = sidebarToggle.closest('.dropdown');
        if (!parent) return;
        const menu = parent.querySelector('.dropdown-menu');
        const isOpen = parent.classList.toggle('open');
        if (menu) {
          menu.style.display = isOpen ? 'block' : 'none';
        }
        return;
      }

      const headerToggle = event.target.closest('.nav-right .dropdown-toggle');
      if (headerToggle) {
        event.preventDefault();
        const parent = headerToggle.closest('.dropdown');
        if (!parent) return;
        const menu = parent.querySelector('.dropdown-menu');
        const shouldOpen = !parent.classList.contains('show');
        closeHeaderDropdowns();
        if (shouldOpen) {
          parent.classList.add('show');
          if (menu) {
            menu.classList.add('show');
            menu.style.display = 'block';
          }
        }
        return;
      }

      const searchToggle = event.target.closest('.search-toggle');
      if (searchToggle) {
        event.preventDefault();
        const searchBox = searchToggle.closest('.search-box');
        const searchInput = document.querySelector('.search-input');
        if (searchBox && searchInput) {
          searchBox.classList.toggle('active');
          searchInput.classList.toggle('active');
        }
        return;
      }

      if (!event.target.closest('.nav-right .dropdown')) {
        closeHeaderDropdowns();
      }

      if (!event.target.closest('.search-box') && !event.target.closest('.search-input')) {
        document.querySelector('.search-box')?.classList.remove('active');
        document.querySelector('.search-input')?.classList.remove('active');
      }
    });
  });
})();