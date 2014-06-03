var tickets = {};

$(document).ready(function() {
    $('.datepicker').datepicker({ dateFormat: "dd/mm/yy" });
    $('.combobox').combobox();
    ajax_theaters();
    ajax_schedules();
    quantity = $('select[class="quantity"]').val();
});

// Event for select tickets
$(document).on('change', 'select[class="quantity"]', function() {
    get_tickets();
});

function get_tickets() {
    var element = $('select[class="quantity"]');
    var quantity = element.val();
    var type_id = element.attr('id');
    tickets.type_id = {"id": element.attr('data-id'), "quantity": quantity};
    alert(tickets);
}
