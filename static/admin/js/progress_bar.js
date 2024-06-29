console.log('Hello World')
$(document).ready(function() {
    $('#id_video_file').on('change', function() {
        var fileInput = $(this)[0];
        if (fileInput.files.length > 0) {
            var formData = new FormData();
            formData.append('file', fileInput.files[0]);

            $.ajax({
                url: "{% url 'admin:upload_video_progress' %}",
                type: 'POST',
                data: formData,
                processData: false,
                contentType: false,
                xhr: function() {
                    var xhr = new window.XMLHttpRequest();
                    xhr.upload.addEventListener('progress', function(evt) {
                        if (evt.lengthComputable) {
                            var percentComplete = evt.loaded / evt.total * 100;
                            $('#progress-bar').css('width', percentComplete + '%');
                            $('#progress-bar').text(percentComplete.toFixed(2) + '%');
                        }
                    }, false);
                    return xhr;
                },
                success: function(data) {
                    // Handle success if needed
                },
                error: function(xhr, status, error) {
                    // Handle errors if needed
                }
            });
        }
    });
});