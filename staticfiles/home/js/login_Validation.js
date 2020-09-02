$(function() {
    $.validator.addMethod("pwcheck", function(value) {
        return /(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/.test(value);
    }, "Please Enter Password (UpperCase, LowerCase, Number/SpecialChar and min 8 Chars)");
    $.validator.addMethod("pwcheck1", function(value) {
        return /(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/.test(value);
    }, "Please Enter Password (UpperCase, LowerCase, Number/SpecialChar and min 8 Chars)");


    $.validator.addMethod("phonecheck", function(value) {
        return /^[6-9]\d{9}$/.test(value);
    }, "Please Enter Mobile Number starts With 9 or 8 or 7 or 6 and  Total 10 Digits ");




    // Login form Validation

    var loginform = $('#loginform');

    if (loginform.length) {
        loginform.validate({
            rules: {
                email: {
                    required: true

                },
                password: {
                    required: true,
                    pwcheck: true
                }

            },
            messages: {
                email: {
                    required: 'Email Id is Mandatory!'
                },
                password: {
                    required: 'Password is Mandatory!'
                }


            }



        });
    }
    // End Login Form Validation
    // Forgot Password Validation
    var forgotform = $('#Forgot-Password-Form');

    if (forgotform.length) {
        forgotform.validate({
            rules: {
                email: {
                    required: true

                }


            },
            messages: {
                email: {
                    required: 'Email Id is Mandatory!'
                }
            }



        });
    }

    // End Forgot Password Validation
    // OTP submit Validation
    var otpform = $('#Forgot-Password-Otp');

    if (otpform.length) {
        otpform.validate({
            rules: {
                otp: {
                    required: true

                }


            },
            messages: {
                otp: {
                    required: 'OTP is Mandatory!'
                }
            }



        });
    }



    //End Otp Submit Validation

    //Update Password Validation
    var updatepasswordform = $('#Forgot-Password-Update');

    if (updatepasswordform.length) {
        updatepasswordform.validate({
            rules: {


                password: {
                    required: true,
                    pwcheck1: true
                },
                confirmpassword: {
                    required: true,
                    equalTo: '#password1'
                }



            },
            messages: {

                password: {
                    required: 'Password is Mandatory!'
                },
                confirmpassword: {
                    required: 'Confirmpassword is Mandatory!'
                }



            }

        });
    }



    //Update Password Validation


    //Register Page Validation

    var registerform = $('#registerform');

    if (registerform.length) {
        registerform.validate({
            rules: {
                username: {
                    required: true,
                    minlength: 3
                },
                email: {
                    required: true
                },
                mobile: {
                    required: true,
                    phonecheck: true

                },


                password: {
                    required: true,
                    pwcheck: true
                },
                confirmpassword: {
                    required: true,
                    equalTo: "#password"
                }



            },
            messages: {
                username: {
                    required: 'Name is Mandatory!'
                },
                email: {
                    required: 'Email is Mandatory!'
                },
                mobile: {
                    required: 'Mobile is Mandatory!',


                },
                password: {
                    required: 'Password is Mandatory!'
                },
                confirmpassword: {
                    required: 'Confirmpassword is Mandatory!'
                }



            }

        });
    }
    //end Register Form Validation
    //Password Show
    $(".toggle-password").click(function() {

        $(this).toggleClass("fa-eye fa-eye-slash");
        var input = $($(this).attr("toggle"));
        if (input.attr("type") == "password") {
            input.attr("type", "text");
        } else {
            input.attr("type", "password");
        }
    });
    //Password Not show

});