import * as Sentry from '@sentry/browser';


Sentry.init({
    dsn: '',
    environment: DJANGO_ENV,
});


window.$ = window.jQuery = require('jquery');

// require('bootstrap');
require('bootstrap/dist/js/bootstrap.min.js')
require('./main.scss');

// djangocms-bootstrap4 icons
require('@fortawesome/fontawesome-free/scss/fontawesome.scss');
require('@fortawesome/fontawesome-free/scss/brands.scss');
require('@fortawesome/fontawesome-free/scss/solid.scss');
require('@fortawesome/fontawesome-free/scss/regular.scss');
// function dropdownOpen() {

//     var $dropdownLi = $('li.dropdown');

//     $dropdownLi.mouseover(function() {
//         $(this).addClass('open');
//     }).mouseout(function() {
//         $(this).removeClass('open');
//     });
// }
// $(document).ready(function () {
//     console.log(99999)
//     $(document).off('click.bs.dropdown.data-api');
//     dropdownOpen();
// })
window.onload = () => {

    // let dom = document.getElementById('services')
    // let dom1 = document.getElementById('wxcontact')
    // if (dom && dom1) {
    //   dom.addEventListener('mouseenter', function () {
    //     this.style.visibility = 'hidden';
    //     dom1.style.visibility = 'visible'
    //   });
    //   dom1.addEventListener('mouseleave', function () {
    //     dom.style.visibility = 'visible';
    //     dom1.style.visibility = 'hidden'
    //   });
    // }
}
