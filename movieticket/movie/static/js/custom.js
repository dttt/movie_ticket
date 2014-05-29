$(document).ready(function() {
    $('.datepicker').datepicker({ dateFormat: "dd/mm/yy" });
    $('.combobox').combobox();
    ajax_theaters();
    ajax_schedules();
});