$(document).ready(function() {

$('#typed').css('color', 'white')

$('#thanks').css('color', 'white')


});

setTimeout((function(){

$('#typed').css('color', 'black')

}), 1300);

setTimeout((function(){

	$("#typed").typed({
		strings: [
			"A collection of powerful plays for powerful people"	
		],
		// The lower the faster, the higher the slower
		startDelay: 100,
		typeSpeed: 50, 
		showCursor: false,
		backSpeed: -100,
		backSpeedDelay: 50,
		backDelay: 500,
		loop: false,
		contentType: 'html', // or text
		loopCount: false // defaults to false for infinite loop
	});

	$("#thanks").typed({
		strings: [
			"A collection of NEEERDS"	
		],
		// The lower the faster, the higher the slower
		startDelay: 100,
		typeSpeed: 50, 
		showCursor: false,
		backSpeed: -100,
		backSpeedDelay: 50,
		backDelay: 500,
		loop: false,
		contentType: 'html', // or text
		loopCount: false // defaults to false for infinite loop
	});


}), 1000);


