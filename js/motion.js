$OBJ = {
	'doc' : $(document),
	'html' : $('html')
}




$OBJ.win.on('load',function(){
	AOS.init({
		duration:1000,
		offset: 20
	});
});