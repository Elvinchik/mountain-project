$(document).ready(function () {
   $('.slider').slick({
      arrows: false,
      speed: 1000,
      easing: 'ease',
      autoplay: true,
      autoplaySpeed: 3000,
      pauseOnFocus: false,
      centerMode: true,
      variableWidth: true,
      mobileFirst: true,
      responsive: [
         {
            breakpoint: 1024,
            settings: {
               arrows: true,
            }
         },
         {
            breakpoint: 768,
            settings: {
               slidesToShow: 2,
               centerMode: false,
               variableWidth: false,
            }
         }
      ]
   });

   let header = $("#header");
   let Height = $("#1st-page").innerHeight();
   let scrollOffset = $(window).scrollTop();

   CheckScroll(scrollOffset);

   $(window).on("scroll", function () {
      scrollOffset = $(this).scrollTop();
      CheckScroll(scrollOffset);
   });

   function CheckScroll() {

      if (scrollOffset >= Height) {
         header.addClass("fixed");
      }

      else {
         header.removeClass("fixed");
      }
   }

   $("[data-goto]").on("click", function (event) {
      event.preventDefault();
      let $this = $(this);
      let elementId = $this.data("goto");
      let elementOffset = $(elementId).offset().top;

      $("#nav a").removeClass("active3");
      $this.addClass("active3");

      $("html, body").animate({
         scrollTop: elementOffset
      }, 800)
   });

});
