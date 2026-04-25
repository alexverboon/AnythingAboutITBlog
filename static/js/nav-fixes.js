document.addEventListener('DOMContentLoaded', function () {
  var navLinks = document.querySelectorAll('.navbar-nav li a');

  for (var i = 0; i < navLinks.length; i++) {
    var link = navLinks[i];
    if ((link.textContent || '').trim() === 'All Posts') {
      link.setAttribute('href', './archive/');
      break;
    }
  }
});
