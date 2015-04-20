$(function(){
  $(document).on('click', '.getContainer', function() {
	var url = $(this).attr('href');
	var state = {title : 'main' , url1 : url};
	history.pushState(state, 'main', '/');
	$('article').load(url);
	return false;
  });
  
  $(document).on('click', '.adminGetContainer', function(){
	    var url = $(this).attr('href');
	    var state = {title : 'main' , url1 : url};
		history.pushState(state, 'main', '/');
	 	$('article section').load(url);
	 	return false;
  });
});