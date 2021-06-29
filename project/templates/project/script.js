$(document).ready(function() {
    $('input[type="radio"]').click(function() {
        if($(this).attr('id') == 'text-radio') {
             $('#radio-text').show();
        }

        else {
             $('#radio-text').hide();
        }
    });
 });

 $(document).ready(function() {
    $('input[type="radio"]').click(function() {
        if($(this).attr('id') == 'image-radio') {
             $('#radio-image').show();
        }

        else {
             $('#radio-image').hide();
        }
    });
 });
