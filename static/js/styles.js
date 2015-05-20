/* 
 * 
 * This is The Website's Style Settings.
 * 
 */
$(function(){
  // getContainer
  $(document).on('click', '.getContainer', function() {
	var url = $(this).attr('href');
	var state = {title : 'main' , url1 : url};
	history.pushState(state, 'main', '/');
	$('article').load(url);
	return false;
  });
  
  //admin getContainer
  $(document).on('click', '.adminGetContainer', function(){
	var url = $(this).attr('href');
	var state = {title : 'main' , url1 : url};
	history.pushState(state, 'main', '/');
	$('section').load(url);
	return false;
  });
  
});

$('.dropdown-toggle').dropdown();
