/* global jQuery */

jQuery(function($) {
    "use strict";

    var DONATION_AMTS = [
        ["platinum", 1000],
        ["gold", 500],
        ["silver", 250],
        ["bronze", 100],
        ["individual", 50],
        ["other", 0]
    ];

    var DONATION_AMTS_DICT = {
        platinum: 1000,
        gold: 500,
        silver: 250,
        bronze: 100,
        individual: 50,
        other: 25
    };

    // DONATION TEXTBOX VALUE CHANGE
    var handle_donation_change = function() {
        var donation = parseFloat($("#donationAmt").val());

        var i;

        for (i = 0; i < DONATION_AMTS.length; i++) {
            $("." + DONATION_AMTS[i][0]).removeClass("active");
        }

        for (i = 0; i < DONATION_AMTS.length; i++) {
            if (donation >= DONATION_AMTS[i][1]) {
                $("." + DONATION_AMTS[i][0]).addClass("active");
                break;
            }
        }
        $("#id_donation").val(donation);
    };

    $("#donationAmt").change(handle_donation_change).keyup(handle_donation_change);

    // LEVEL CLICKS
    var handle_donor_lvl_click = function(e) {
        var donation = DONATION_AMTS_DICT[$(e.currentTarget).attr("class").split(" ")[1]];

        $("#donationAmt").val(donation);
        handle_donation_change();
    };

    $(".donor_lvl").click(handle_donor_lvl_click);

    // DONATION SOURCE CHANGE
    var handle_donation_source_change = function(e) {
        var donation_source = $(e.target).val();

        $(".payment-form").addClass("hidden");
        $("#form-" + donation_source).removeClass("hidden");
        $("#id_donation_type").val(donation_source);
    };

    $("#donate_source").change(handle_donation_source_change);
});