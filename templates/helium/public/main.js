function addLastUpdatedStyles() {
  if (document.querySelector('style[data-helium-last-updated]')) {
    return;
  }

  const stylesheet = document.createElement('style');
  stylesheet.dataset.heliumLastUpdated = '';
  stylesheet.textContent = `
    .helium-last-updated {
      margin: -0.5rem 0 1.5rem;
      color: var(--helium-muted);
      font-size: 0.875rem;
      line-height: 1.5;
    }

    .helium-hero .helium-last-updated {
      margin: 0.75rem 0 0;
    }
  `;
  document.head.append(stylesheet);
}

function start() {
  addLastUpdatedStyles();
}

export default {
  iconLinks: [
    {
      icon: 'github',
      href: 'https://github.com/strombetta/helium',
      title: 'Helium framework on GitHub',
    },
  ],
  start,
};
