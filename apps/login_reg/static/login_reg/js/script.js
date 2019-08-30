$(document).ready(function(){
    console.log("jQuery is ready");
    $("#signup").click(function(){
        console.log("I am running");
        $(this).removeClass("text-secondary");
        $(this).addClass("text-primary");
        $("#signin").removeClass("text-primary")
        $("#signin").addClass("text-secondary");

        // $("#register").css("display", "block");
        // $("#login").css("display", "none");
        $("#login").hide();
        $("#register").fadeIn("slow");
        
    });
    $("#signin").click(function(){
        console.log("I am running");
        $(this).removeClass("text-secondary");
        $(this).addClass("text-primary");
        $("#signup").removeClass("text-primary");
        $("#signup").addClass("text-secondary");

        // $("#register").css("display", "none");
        // $("#login").css("display", "block");
        $("#register").hide();
        $("#login").fadeIn("slow");
    });


    // register client-side validation
    var errors = {
        first_name : false,
        last_name : false,
        email : false,
        password : false,
        confirm_password : false
    };

    $("#email").keyup(function(){
        var data = $("#register").serialize()
        $.ajax({
            method : "POST",
            url : "/check_email_unique",
            data : data
        })
        .done(function(res){
            if (res['found'] == true) {
                $("#err_reg_email").html("This email has already been registered").removeClass("green").addClass("error");
                $("#email").removeClass("is-valid");
                $("#email").addClass("is-invalid");
            } else {
                if ($("#email").val().length < 1) {
                    $("#email").addClass("is-invalid");
                    $("#err_reg_email").html("This field is required").removeClass("green").addClass("error");
                } else {
                    $("#err_reg_email").html("This email is available").removeClass("error").addClass("green");
                    $("#email").removeClass("is-invalid");
                    $("#email").addClass("is-valid");
                    errors.email = true;
                }
            }
            
        })
    });

    
    $("#first_name").keyup(function() {
        var length = $(this).val().length
        if (length < 2) {
            $(this).addClass("is-invalid");
            $("#err_reg_first_name").html("first name should at least have 2 characters");
        } else {
            $(this).removeClass("is-invalid");
            $(this).addClass("is-valid");
            $("#err_reg_first_name").empty();
            errors.first_name = true;
        }
    });

    $("#last_name").keyup(function() {
        var length = $(this).val().length
        if (length < 2) {
            $(this).addClass("is-invalid");
            $("#err_reg_last_name").html("last name should at least have 2 characters");
        } else {
            $(this).removeClass("is-invalid");
            $(this).addClass("is-valid");
            $("#err_reg_last_name").empty();
            errors.last_name = true;
        }
    });


    $("#password").keyup(function() {
        var length = $(this).val().length
        if (length < 8) {
            $(this).addClass("is-invalid");
            $("#err_reg_password").html("password should at least have 8 characters")
        } else {
            $(this).removeClass("is-invalid");
            $(this).addClass("is-valid");
            $("#err_reg_password").empty();
            errors.password = true;
        }
    });

    $("#confirm_password").keyup(function() {
        var length = $(this).val().length
        if ($(this).val() != $("#password").val()){
            $(this).addClass("is-invalid");
            $("#err_reg_confirm_password").html("You password did not match");
        } else {
            $(this).removeClass("is-invalid");
            $(this).addClass("is-valid");
            $("#err_reg_confirm_password").empty();
            errors.confirm_password = true;
        }
    });

    $(document).keyup(function() {
        var validation;
        for (var p in errors) {
            if (errors[p] == true) {
                validation = true;
            } else {
                validation = false;
            }
        }
        if (validation == true) {
            $("#registerSubmit").removeAttr("disabled");
        }
    });

    // login client side validation
    var login_errors = {
        email : false,
        password : false
    };

    $("#login_email").keyup(function() {
        if ($(this).val().length < 1) {
            $(this).addClass("is-invalid");
        } else {
            $(this).removeClass("is-invalid");
            login_errors.email = true;
        }
    });

    $("#login_password").keyup(function() {
        if ($(this).val().length < 1) {
            $(this).addClass("is-invalid");
        } else {
            $(this).removeClass("is-invalid");
            login_errors.password = true;
        }
    });

    $(document).keyup(function() {
        var validation;
        for (var p in login_errors) {
            if (login_errors[p] == true) {
                validation = true;
            } else {
                validation = false;
            }
        }

        if (validation == true) {
            $("#loginSubmit").removeAttr("disabled");
        }
    });

});
