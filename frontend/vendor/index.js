import * as Sentry from '@sentry/browser';
Sentry.init({
    dsn: '',
    environment: DJANGO_ENV,
});
import Swiper from 'swiper/bundle';
import 'swiper/css/bundle';

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
    let dom = document.getElementsByClassName('custom-link');
    if (dom) {
        for (var i = 0; i < dom.length; i++) {
            // 为每个元素添加事件监听器
            dom[i].addEventListener('click', function (event) {
                if (/products\/\d/.test(location.href)) {
                    event.preventDefault();
                } else {
                    location.href = location.origin + '/' + $(this).attr('languagecode') + '/products/' + $(this).attr('customdata')
                }
            });
        }

    }
    if (document.getElementsByClassName('mySwiper')) {
        var swiper = new Swiper(".mySwiper", {
            direction: 'vertical', // 垂直切换选项
            loop: true, // 循环模式选项
            slidesPerView: 1,
            spaceBetween: 10,
            autoplay: {
                delay: 2500,
                disableOnInteraction: false,
            },
            breakpoints: {
                640: {
                    slidesPerView: 2,
                    spaceBetween: 20,
                },
                768: {
                    slidesPerView: 4,
                    spaceBetween: 40,
                },
                1024: {
                    slidesPerView: 5,
                    spaceBetween: 50,
                },
            },
        });
    }
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
