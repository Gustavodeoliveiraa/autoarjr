$(document).ready(function() {
    var oldPlateMask = 'AAA-9999';
    var nemPlateMask = 'AAA9A99';

    $('#id_car_plate').inputmask({
        mask: [oldPlateMask, nemPlateMask],
        keepStatic: true
    });

    $('#cellphone').inputmask('(99) 99999-9999');

    var cpfMask = '999.999.999-99';
    var cnpjMask = '99.999.999/9999-99';

    $('#cpf').inputmask({
        mask: [cpfMask, cnpjMask],
        keepStatic: true,
        placeholder: '_',
        clearMaskOnLostFocus: true,
        autoUnmask: true
    });

});

