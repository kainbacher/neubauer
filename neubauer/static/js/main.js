function teamListSwiper() {
    var mySwiper = new Swiper ('.teamlist-swiper', {
        spaceBetween: 16,
        freeMode: false,
        mousewheel: true,
        slidesPerView: 2,
        loop: true,
        centeredSlides : true,
        centeredSlidesBounds: true,
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        breakpoints: {
            // when window width is >= 768px
            768: {
            slidesPerView: 3,
            spaceBetween: 16
            },
            // when window width is >= px
            992: {
            slidesPerView: 3,
            spaceBetween: 16
            }
        }
    });
}

function gallerySwiper() {
    var mySwiper = new Swiper ('.gallery-swiper', {
        spaceBetween: 0,
        freeMode: false,
        mousewheel: true,
        slidesPerView: 1,
        autoplay: {
            delay: 5000,
        },
        pagination: {
            el: '.swiper-pagination',
            type: 'bullets',
            clickable: true,
        },
        navigation: {
            nextEl: '.swiper-button-next',
            prevEl: '.swiper-button-prev',
        },
        effect: 'coverflow',
        coverflowEffect: {
            rotate: 30,
            slideShadows: false,
        },
    });
}

function partnerSwiper() {
    var mySwiper = new Swiper ('.partner-swiper', {
        spaceBetween: 16,
        freeMode: false,
        mousewheel: false,
        slidesPerView: 2,
        loop: true,
        autoplay: {
            delay: 3000,
        },
        breakpoints: {
            // when window width is >= 768px
            768: {
            slidesPerView: 3,
            },
            // when window width is >= px
            992: {
            slidesPerView: 5,
            }
        }
    });
}

document.addEventListener("DOMContentLoaded", function() {
    teamListSwiper();
    gallerySwiper();
    partnerSwiper();
});
