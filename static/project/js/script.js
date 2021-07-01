// $(function () {
//     $("#sortable1, #sortable2").sortable({
//         connectWith: ".connectedSortable"
//     }).disableSelection();
// });


$(function () {
    $.ajaxSetup({
        headers: {"X-CSRFToken": getCookie("csrftoken")}
    });
    $("#sortable1, #sortable2").sortable({
        connectWith: ".connectedSortable",

        start: function (event, ui) {
            item = ui.item;
            newList = oldList = ui.item.parent().parent();
        },
        stop: function (event, ui) {
            var tile_id = ui.item[0].getAttribute('id');
            var column_id = newList.attr('id');

            var op = "move_tile";

            DataToSend = {
                tile_id: tile_id,
                column_id: column_id,
                move_tile: op
            };

            $.ajax({
                url: '',
                type: 'POST',
                data: DataToSend,

                success: function (result) {
                }
            });
        },
        change: function (event, ui) {
            if (ui.sender) newList = ui.placeholder.parent().parent();
        },
    }).disableSelection();

    function getCookie(c_name) {
        if (document.cookie.length > 0) {
            c_start = document.cookie.indexOf(c_name + "=");
            if (c_start != -1) {
                c_start = c_start + c_name.length + 1;
                c_end = document.cookie.indexOf(";", c_start);
                if (c_end == -1) c_end = document.cookie.length;
                return unescape(document.cookie.substring(c_start, c_end));
            }
        }
        return "";
    }

});