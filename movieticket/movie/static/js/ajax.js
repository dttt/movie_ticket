// Ajax function for select theaters
$(document).on("change", "#select-movie", function() {
    ajax_theaters();
});

function ajax_theaters() {
    reset_selects();
    var container_id = "#theaters";
    var movie_id = $('#select-movie').val();
    $.ajax({
        type: "GET",
        url: "/ajax/theaters/",
        data: {"movie_id": movie_id},
    })
    .done(function(data) {
        replace_content(container_id, data);
    })
    .fail(function() {
        replace_content(container_id, '');
    });
}

// Ajax function for select schedules
$(document).on("change", "input[type=radio][name=select-theater]", function() {
    ajax_schedules();
});

function ajax_schedules() {
    var container_id = "#schedules";
    var theater_id = $("input[type=radio][name=select-theater]:checked").val();
    var movie_id = $('#select-movie').val();
    $.ajax({
        type: "GET",
        url: "/ajax/schedules/",
        data: {"movie_id": movie_id, "theater_id": theater_id},
    })
    .done(function(data) {
        replace_content(container_id, data);
    })
    .fail(function() {
        replace_content(container_id, '')
    });
}


function replace_content(selector, content) {
    $(selector).html(content);
}


function reset_selects() {
    $("#theaters").html('');
    $("#schedules").html('');
}

// Ajax function for select seats
$(document).on("click", "#select-seats", function(){
    ajax_seats();
});

function ajax_seats() {
    var schedule_id = $('#schedule-id').attr('data-id');
    var csrftoken = $.cookie('csrftoken');
    $.ajax({
        type: "POST",
        url: "/ajax/seats/",
        beforeSend: function(xhr, settings) {
            if (!csrfSafeMethod(settings.type) && sameOrigin(settings.url)) {
                xhr.setRequestHeader("X-CSRFToken", csrftoken);
            }
        },
        data: {
            "tickets": JSON.stringify(tickets),
            "schedule_id": schedule_id,
        },
    })
    .done(function(data){
        //alert(data);
        replace_content("#ajax-container", data);
    })
    .fail(function(){
        alert("dafs");
    });
}


// Ajax functions for show theater's information
$(document).on("click", '.show-theater', function(e){
    var href = $(this).attr('href');
    if (supported_api()) {
        window.history.pushState(null, null, href);
        e.preventDefault();

        $.ajax({
            type: "GET",
            url: href,
        })
        .done(function(data){
            replace_content('#theater-info' ,data);
        })
        .fail(function(){
            alert('fail');
        });
    }
});

function supported_api() {
    return !!(window.history && history.pushState);
}

$(document).on("click", ".paginator", function(){
    var href = $(this).attr('data-url');
    var container = $(this).attr('data-container');
    var query = $(this).attr('data-query');

    $.ajax({
        type: "GET",
        url: href,
        data: {
            'query': query,
            'container': container
        },
    })
    .done(function(data){
        //alert(data);
        replace_content(container, data);
    })
    .fail(function(){
        alert('fail');
    });
});
