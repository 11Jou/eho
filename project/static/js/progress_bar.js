$(document).ready(function() {
    var fileInput = $('#id_video');
    var form = fileInput.closest('form');

    form.on('submit', function(e) {
        e.preventDefault();
        var formData = new FormData(this);
        var progressBar = $('<div class="progress-bar"><div class="progress"></div></div>');
        $('body').append(progressBar);

        console.log("Start Upload")

        $.ajax({
            url: form.attr('action'),
            type: form.attr('method'),
            data: formData,
            processData: false,
            contentType: false,
            xhr: function() {
                var xhr = new window.XMLHttpRequest();
                xhr.upload.addEventListener('progress', function(evt) {
                    if (evt.lengthComputable) {
                        var percentComplete = evt.loaded / evt.total;
                        percentComplete = parseInt(percentComplete * 100);
                        $('.progress').css('width', percentComplete + '%');
                        if (percentComplete === 100) {
                            progressBar.fadeOut();
                        }
                    }
                }, false);
                return xhr;
            },
            success: function(response) {
                console.log("Uploaded file")
            },
            error: function(response) {
                alert('An error occurred while uploading the file.');
                progressBar.remove();
            }
        });
    });
});
