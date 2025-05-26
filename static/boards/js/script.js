	
$('.owl-carousel').owlCarousel({
    loop:true,
    margin:20,
    nav:true,
	// dotsContainer: '#carousel-custom-dots',
    responsive:{
		0 : {
			items:1,
			dots:true,
			stagePadding: 0,
		},
		200: {
			items:1,
			dots:true,
			stagePadding: 0,
		},
		485: {
			items:1,
			dots:true,
			stagePadding: 100,
		},
		728 : {
			items:2,
			dots:true,
			stagePadding: 100,
		},
		960: {
			items:3,
			dots:true,
			stagePadding: 100,
		},
		1200: {
			items:3,
			dots:true,
			stagePadding: 150,
		},
	}
});


