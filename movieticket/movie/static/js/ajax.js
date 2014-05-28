$(document).on("change", "#select-movie", function() {
    var movie_id = $(this).val();
    $.ajax({
        type: "GET",
        url: "/ajax/theaters/",
        data: {"movie_id": movie_id},
        dataType: "json",
        success: done1,
    });
});

function done1(data) {
    alert(data);
}