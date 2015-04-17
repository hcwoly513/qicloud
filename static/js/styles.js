

$('.dropdown-toggle').dropdown();

i18n.init(function(t) {
  // translate nav
  $('nav').i18n();

  // programatical access
  var appName = t('system.name');
});