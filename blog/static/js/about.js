$(document).ready(function() {

$('#typed').css('color', 'white')

});

setTimeout((function(){

$('#typed').css('color', 'black')

}), 1300);

setTimeout((function(){

	$("#typed").typed({
		strings: [
			"At this point we're all masters of the office power play - we've had decades of highly informative educational literature on the subject.  Less well known, though, is the art of the social power play.  Generations of prom queens, suck-ass frat boys, and straight-up sociopaths have been honing these secret techniques to establish firm social positioning for decades.  But now Powerful Plays for Powerful People is majorly disrupting the power play space. This site will teach you the moves you need to climb the social ladder and defend your rightful place atop the social pyrmaid.  Of course, lest such powerful knowledge be used for the wrong purposes, such as bullying, undeserved gain, or evil, we also include a counter manuever for each power play.  Stay powerful, people.  "	
		],
		// The lower the faster, the higher the slower
		startDelay: 100,
		typeSpeed: -23, 
		showCursor: false,
		backSpeed: -100,
		backSpeedDelay: 50,
		backDelay: 500,
		loop: false,
		contentType: 'html', // or text
		loopCount: false // defaults to false for infinite loop
	});

}), 1000);






