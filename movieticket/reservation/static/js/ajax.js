$(document).ready(function() {
$("#select-movie").on("changed", function() {
    var movie_id = $this.val()
    $.ajax({
        type: "POST"
        url: "",
        data: {"movie_id": movie_id},
        dataType: "json",
        before: alert(movie_id),
        success: ,
    });
});
});