$(document).ready(function() {

  $('#submit').on('click', function(event) {

    event.preventDefault();

    var formData = new FormData($('form')[0]);

    $.ajax({
      xhr : function() {
        var xhr = new window.XMLHttpRequest();

        xhr.upload.addEventListener('progress', function(e) {

              $('#status').text('');
              
            if (e.lengthComputable) {
              console.log('Bytes Loaded: ' + e.loaded);
              console.log('Total Size: ' + e.total);
              console.log('Percentage Uploaded: ' + (e.loaded / e.total));

              var percent = Math.round((e.loaded / e.total) * 100)

              if (percent == 100) {
                $('#status').text('Please wait...');
              }

              $('#progressBar').attr('aria-valuenow', percent).css('width', percent + '%').text(percent + '%');
            }
        });

        return xhr;
      },
      type : 'POST',
      url : '/dashboard/upload',
      data : formData,
      processData : false,
      contentType : false,
      success : function() {
        $('#status').text('Upload Successful!');
      }
    });
  });
});
