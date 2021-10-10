$(document).ready(function () {
   $('.burger').click(function () {
      $('.burger, nav').toggleClass('active2');
      $('body').toggleClass('lock');
   });
});
