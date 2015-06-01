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
  
  //POST uploadFileForm 進度條
  $(document).on('click', '.uploadFileForm', function(){
  	$(this).ajaxForm({
  	  beforeSend: function(){
  	    $('.progress').show();
  	    //clear everything
  	    $('.progress-bar').width('0%');
  	    $('.sr-only').html('0%');
  	  },
  	  uploadProgress: function(event, position, total, percentComplete){
  	    $('.progress-bar').width(percentComplete+'%');
  	    $('.sr-only').html(percentComplete+'%');
  	  },
  	  success: function(returnData){
  	    $('.progress-bar').width('100%');
  	    $('.sr-only').html('100%');
  	    $('section').html(returnData);
  	    return false;
  	  }
  	});
  });
  
});
