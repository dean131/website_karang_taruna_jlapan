const multipleItemCarousel = document.querySelector('#multipleItemCarousel');
const carouselInner = $('.carousel-inner');
const carousel = new bootstrap.Carousel(multipleItemCarousel, {
    keyboard: false, // Sesuaikan dengan kebutuhan Anda
});

let scrollPosition = 0;
let carouselWidth, cardWidth;

const handleNextClick = function () {
    if (scrollPosition < (carouselWidth - (cardWidth * 3))) {
        console.log('next');
        scrollPosition += cardWidth;
    } else {
        // Jika sudah mencapai batas akhir, kembali ke awal
        scrollPosition = 0;
    }
    carouselInner.animate({ scrollLeft: scrollPosition }, 600);
};

const handlePrevClick = function () {
    if (scrollPosition > 0) {
        console.log('prev');
        scrollPosition -= cardWidth;
    } else {
        // Jika sudah di awal, pindah ke akhir
        scrollPosition = carouselWidth - (cardWidth * 3);
    }
    carouselInner.animate({ scrollLeft: scrollPosition }, 600);
};

const initCarousel = function () {
    const carousel = new bootstrap.Carousel(multipleItemCarousel, {
        interval: false
    });

    carouselWidth = carouselInner[0].scrollWidth;
    cardWidth = $('.carousel-item').width();

    $('.carousel-control-next').on('click', handleNextClick);
    $('.carousel-control-prev').on('click', handlePrevClick);
};

const destroyCarousel = function () {
    $('.carousel-control-next, .carousel-control-prev').off('click');
};

// Inisialisasi carousel saat halaman pertama kali dimuat
initCarousel();

// Pantau perubahan ukuran layar
$(window).on('resize', function () {
    const isLargeScreen = window.matchMedia("(min-width:576px)").matches;

    if (isLargeScreen) {
        // Ubah ke mode carousel saat layar lebih dari 576px
        destroyCarousel();
        initCarousel();
    } else {
        // Hancurkan carousel saat layar kurang dari 576px
        destroyCarousel();
        $(multipleItemCarousel).addClass('slide');
    }
});

