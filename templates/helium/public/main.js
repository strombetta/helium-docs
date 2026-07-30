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

export default {
  iconLinks: [
    {
      icon: 'github',
      href: 'https://github.com/strombetta/helium',
      title: 'Helium framework on GitHub',
    },
  ],
  start: addArticleFeedback,
};
