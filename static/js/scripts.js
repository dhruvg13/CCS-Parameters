$(document).ready(function() {
    $('#predictForm').submit(function(event) {
        event.preventDefault();

        const cssValue = $('#css').val();

        $.ajax({
            type: 'POST',
            url: '/predict',
            data: { css: cssValue },
            success: function(response) {
                displayResults(response);
            },
            error: function(error) {
                $('#error-message').text('Error: ' + error.responseText);
            }
        });
    });

    function displayResults(data) {
        $('#result-css').text(data.css);
        $('#result-coal').text(data.coal);
        $('#result-bentonite').text(data.bentonite);
        $('#result-furnance_oil').text(data.furnance_oil);
        $('#result-im_speed').text(data.im_speed);
        $('#result-total_bed_height').text(data.total_bed_height);
        $('#result-lime_coal').text(data.lime_coal);
        $('#result-t1').text(data.t1);
        $('#result-t2').text(data.t2);
        $('#result-t3').text(data.t3);
        $('#result-t4').text(data.t4);
        $('#result-t5').text(data.t5);
        $('#result-t6').text(data.t6);
        $('#result-t7').text(data.t7);
        $('#result-t8').text(data.t8);
        $('#result-prod_qty').text(data.prod_qty);
        $('#result-tumble_index').text(data.tumble_index);
        $('#result-abrasion_index').text(data.abrasion_index);
        $('#result-mean_dia').text(data.mean_dia);
        $('#result-porosity_pellet').text(data.porosity_pellet);
        $('#result-input_fe').text(data.input_fe);
        $('#result-output_fe').text(data.output_fe);

        $('#result').slideDown();
    }
});
