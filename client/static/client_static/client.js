$(document).ready(function() {
    var oldPlateMask = 'AAA-9999';
    var nemPlateMask = 'AAA9A99'

    $('#id_car_plate').inputmask({
        mask: [oldPlateMask, nemPlateMask],
        keepStatic: true
    });

    $('#cellphone').inputmask('(99) 99999-9999');

});
