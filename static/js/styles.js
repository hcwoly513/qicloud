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
	$('article section').load(url);
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
//POST 含進度條
/*  $(document).on('click', '.uploadFileForm', function(){
    $(this).ajaxForm ({ 
	  beforeSend: function() 
	  {
	    $('#progress').show();
	    //clear everything
	    $('#bar').width('0%');
	    $('#message').html('');
	    $('#percent').html('0%');
	  },
	  uploadProgress: function(event, position, total, percentComplete) 
	  {
   	    $('#bar').width(percentComplete+'%');
   	    $('#percent').html(percentComplete+'%');
	  },
      success: function(returnData) {
        $('#bar').width('100%');
        $('#percent').html('100%');
        $('#container').html(returnData);
        return false;
      }
    });
  });*/
  
//check for unwanted characters
  $.validator.addMethod('validChars', function (value) {
    var result = true;
    // unwanted characters
    var iChars = "!@#$%^&*()+=-[]\\\';,./{}|\":<>?";
    for (var i = 0; i < value.length; i++) {
      if (iChars.indexOf(value.charAt(i)) != -1) {
        return false;
      }
    }
    return result;
  }, '');

  // check for space
  $.validator.addMethod('noSpace', function (value) {
    return value.indexOf(" ") < 0;
  }, '');
  
  
  // Check if account exists
  $.validator.addMethod('checkAccount', function(account) {
    $.ajax({
      cache:false,
      async:false,
      type: "GET",
      data: "account=" + account,
      url: "/signin?arg1=checkAccount",
      success: function(msg) {
        result = (msg=='FALSE') ? true : false;
      }
    });
    return result;
  }, '');

  // Check if account contains letters and numbers
  $.validator.addMethod('alphaNumeric', function(account) {
    if (/^[a-z0-9]+$/i.test(account))
      return true;
    return false;
  }, '');
  
  // Check if email exists
  $.validator.addMethod('checkEmail', function(email) {
    $.ajax({
      cache:false,
      async:false,
      type: "GET",
      data: "email=" + email,
      url: "/signin?arg1=checkEmail",
      success: function(msg) {
        result = (msg=='FALSE') ? true : false;
      }
    });
    return result;
  }, '');
});
