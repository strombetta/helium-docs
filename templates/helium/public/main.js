const lastUpdatedManifestUrl = new URL('last-updated.json', import.meta.url);
const lastUpdatedFormatter = new Intl.DateTimeFormat('en-US', {
  year: 'numeric',
  month: 'long',
  day: 'numeric',
  timeZone: 'UTC',
});

function manifestPathname() {
  const assetBasePath = new URL('.', import.meta.url).pathname;
  const pagePath = window.location.pathname;

  if (assetBasePath !== '/' && pagePath.startsWith(assetBasePath)) {
    return `/${pagePath.slice(assetBasePath.length)}`;
  }

  return pagePath;
}

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

async function addLastUpdated() {
  const article = document.querySelector('article');
  const home = document.querySelector('.helium-home');
  const container = article || home;
  if (!container || container.querySelector('.helium-last-updated')) {
    return;
  }

  try {
    const response = await fetch(lastUpdatedManifestUrl, { cache: 'no-cache' });
    if (!response.ok) {
      return;
    }

    const manifest = await response.json();
    const date = manifest[manifestPathname()];
    if (!/^\d{4}-\d{2}-\d{2}$/.test(date || '')) {
      return;
    }

    const updated = document.createElement('p');
    updated.className = 'helium-last-updated';
    updated.append('Last updated: ');

    const time = document.createElement('time');
    time.dateTime = date;
    time.textContent = lastUpdatedFormatter.format(new Date(`${date}T00:00:00Z`));
    updated.append(time);

    if (home) {
      const lead = home.querySelector('.helium-lead');
      if (lead) {
        lead.insertAdjacentElement('afterend', updated);
        return;
      }
    }

    const heading = container.querySelector('h1');
    if (heading) {
      heading.insertAdjacentElement('afterend', updated);
    }
  } catch {
    // Page metadata is supplemental and must not block documentation rendering.
  }
}

function addArticleFeedback() {
  if (document.querySelector('.helium-home')) {
    return;
  }

  const article = document.querySelector('article');
  if (!article || article.querySelector('.helium-feedback')) {
    return;
  }

  const heading = article.querySelector('h1')?.textContent?.trim() || document.title;
  const issueUrl = new URL('https://github.com/strombetta/helium-docs/issues/new');
  issueUrl.searchParams.set('title', `Documentation: ${heading}`);
  issueUrl.searchParams.set(
    'body',
    `Page: ${window.location.href}\n\nDescribe the problem, missing information, or suggested improvement.`,
  );

  const feedback = document.createElement('div');
  feedback.className = 'helium-feedback';

  const prompt = document.createElement('span');
  prompt.textContent = 'Found a problem with this page?';

  const link = document.createElement('a');
  link.href = issueUrl.toString();
  link.target = '_blank';
  link.rel = 'noopener noreferrer';
  link.textContent = 'Report a documentation issue';

  feedback.append(prompt, link);
  article.append(feedback);
}

function start() {
  addLastUpdatedStyles();
  void addLastUpdated();
  addArticleFeedback();
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
