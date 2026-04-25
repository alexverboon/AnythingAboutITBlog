document.addEventListener('DOMContentLoaded', function () {
  var navLinks = document.querySelectorAll('.navbar-nav li a');
  var brandLink = document.querySelector('.navbar-brand');
  var homeHref = '/';

  if (brandLink && brandLink.getAttribute('href')) {
    homeHref = brandLink.getAttribute('href');
  }

  for (var i = 0; i < navLinks.length; i++) {
    var link = navLinks[i];
    var label = (link.textContent || '').trim();

    if (label === 'All Posts' || label === 'Home') {
      link.textContent = 'Home';
      link.setAttribute('href', homeHref);
      break;
    }
  }
});
