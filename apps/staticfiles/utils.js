/* global $, fetch */

function ajaxDownload(url, name, done, fail) {
    fetch(url)
        .then(res => res.blob())
        .then(blob => {
            const url = window.URL.createObjectURL(blob);
            const a = document.createElement('a');
            a.style.display = 'none';
            a.href = url;
            a.download = name;
            document.body.appendChild(a);
            a.click();
            window.URL.revokeObjectURL(url);
            done();
        })
        .catch(() => fail());
}

function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = $.trim(cookies[i]);
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}

function csrfSafeMethod(method) {
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}

function nameInPath(path) {
    var isName = false, startIdx = 0;
    for (var idx = path.length-1; idx >= 0; idx -= 1) {
        isName = isName || path.charAt(idx) == '.';
        if (path.charAt(idx) == '/') {
            startIdx = idx + 1;
            break;
        }
    }
    return isName ? path.substring(startIdx, path.length) : null;
}
    
$(function() {
    $('.message .close').on('click', function() {
        $(this).closest('.message').transition('fade');
    });
    
    $.ajaxSetup({
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
                xhr.setRequestHeader("X-CSRFToken", getCookie('csrftoken'));
            }
        }
    });
});