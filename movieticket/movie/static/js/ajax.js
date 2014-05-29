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
        url: "/ajax/schedules",
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