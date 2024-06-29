console.log('Hello Worlddd')
$(document).ready(function() {
    $('#eventvideo_form').on('change', function() {
        var fileInput = $("#id_video")[0].files[0];
        console.log(fileInput)
        if (fileInput) {
            var formData = new FormData();
            formData.append('video', fileInput);

            $.ajax({
                url: "{% url 'admin:upload_video_progress' %}",
                type: 'POST',
                headers: {'X-CSRFToken': '{{ csrf_token }}' },
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
                    console.log("Success")
                    // Handle success if needed
                },
                error: function(xhr, status, error) {
                    console.log("Faild")

                    // Handle errors if needed
                }
            });
        }
    });
});