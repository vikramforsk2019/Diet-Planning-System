function report(cat)
{
  alert(cat);
        $.ajax({
            type: 'POST',       // define the type of HTTP verb we want to use (POST for our form)
            url: '{% url "dietapp:homepage" %}',
            dataType: 'json',
            data: JSON.stringify({
            'content': cat
                   }), 
            success: function (data) {
                //alert('ok');
                  window.location.reload();
             //  $('input[name=commentbox]').val(''); // remove the value from the input
            },
            error: function (exception) {
                alert('Exeption:' + exception);
            },
        });
  
  }