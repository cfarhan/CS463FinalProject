$(document).ready(function(){
    $('#trivia-form').on('submit', function(e){
      e.preventDefault();
      var userResponse = $('#quiz-response').val();
      $('#backend-answer').text('');
      $('#trivia-response').hide();
      $.ajax({
        url: 'https://cfarhan-f9900dc398ab.herokuapp.com/question',
        type: 'POST',
        contentType: 'application/json',
        data: JSON.stringify({ quiz_response: userResponse }),
        success: function(response){
          $('#backend-answer').text(response.answer);
          $('#trivia-response').show();
        },
        error: function(jqXHR, textStatus, errorThrown){
          $('#backend-answer').text("Error: " + textStatus);
          $('#trivia-response').show();
        }
      });
    });
  });