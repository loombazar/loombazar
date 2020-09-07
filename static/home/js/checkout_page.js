$(document).ready(function()
        {
            // Custom Validation Password Check
            $.validator.addMethod("pwcheck", function(value) {
                return /(?=^.{8,}$)((?=.*\d)|(?=.*\W+))(?![.\n])(?=.*[A-Z])(?=.*[a-z]).*$/.test(value);
            }, "Please Enter Password (UpperCase, LowerCase, Number/SpecialChar and min 8 Chars)");

            //// End Custom Validation Password Check
            // Custom Validation Password Check
            $.validator.addMethod("phonecheck", function(value) {
                return /^[6-9]\d{9}$/.test(value);
            }, "Please Enter Mobile Number starts With 9 or 8 or 7 or 6 and  Total 10 Digits ");


            // End Custom Validation Password Check
            // Custom Validation Pincode Check
            jQuery.validator.addMethod("zipcode", function(value, element) {
                return this.optional(element) || /^[1-9][0-9]{5}$/.test(value);
              }, "Please provide a valid pincode.");
           


            // End Custom Validation pincode Check
            

          
            //BackGround Color change Active Accodian
                        $('.collapse').on('shown.bs.collapse', function () {
                    $(this).prev().addClass('active-acc');
                });

                // //End BackGround Color change Active Accodian

                $('.collapse').on('hidden.bs.collapse', function () {
                    $(this).prev().removeClass('active-acc');
                });
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
                     

          // Login form Validation

    var checkoutloginform = $('#checkout-login');

    if (checkoutloginform.length) {
        checkoutloginform.validate({
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



//    Start Register Page Checkout
    var checkoutregisterform = $('#checkout-register');

    if (checkoutregisterform.length) {
        checkoutregisterform.validate({
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
                    number:true,
                    phonecheck: true
                    

                },


                password: {
                    required: true,
                    pwcheck: true
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
                    number:'Only Numberic Allowed'


                },
                password: {
                    required: 'Password is Mandatory!'
                }
                



            }

        });
    }

    //  //    End Register Page Checkout
    //    MobileNumber Verfication Page Checkout
    var checkoutmobileverficationform = $('#mobileverfication-form');

    if (checkoutmobileverficationform.length) {
        checkoutmobileverficationform.validate({
            rules: {
               
                mobile: {
                    required: true,
                    number:true,
                    phonecheck: true
                    


                }


                
                



            },
            messages: {
                
                mobile: {
                    required: 'Mobile is Mandatory!',
                    number:'Only Numeric Allowed'


                }
                



            }

        });
    }

    //  //    // End   MobileNumber Verfication Page Checkout
    //    Otp Verfication Page Checkout
    var checkoutotpficationform = $('#otpverfication-form');

    if (checkoutotpficationform.length) {
        checkoutotpficationform.validate({
            rules: {
               
                otp: {
                    required: true,
                  

                }


                
                



            },
            messages: {
                
                otp: {
                    required: 'OTP is Mandatory!',


                }
                



            }

        });
    }

    //  //    // End   Otp Verfication Page Checkout



     //   Start  Checkout Add New Address
     var checkoutaddnewaddressprofile = $('#checkout-addnewaddress');

     if (checkoutaddnewaddressprofile.length) {
        checkoutaddnewaddressprofile.validate({
             rules: {
                 pin_code: {
                     required: true,
                     number:true,
                     zipcode:true
                    
                 },
                 district: {
                     required: true
                 },
                 state: {
                     required: true
                     
 
                 },
 
 
                 full_name: {
                     required: true,
                     minlength: 3
                 },
                 address: {
                     required: true
                     
                 },
                 landmark: {
                     required: true
                    
                 },
                 mobile_number: {
                     required: true,
                     number:true,
                     
                     phonecheck: true
                    
                 }
                 
 
                 
 
 
 
             },
             messages: {
                 pin_code: {
                     required: 'Pincode is Mandatory!',
                     number:'Only Numeric Allowed'
                 },
                 district: {
                     required: 'District is Mandatory!'
                 },
                 state: {
                     required: 'State is Mandatory!',
 
 
                 },
                 full_name: {
                     required: 'Name is Mandatory!'
                 },
                 address: {
                     required: 'Address is Mandatory!'
                 },
                 landmark: {
                     required: 'LandMark is Mandatory!',
 
 
                 },
                 mobile_number: {
                     required: 'Mobile Number is Mandatory!',
                     number:'Only Numeric Allowed'
                 }
 
 
 
             }
 
         });
     }
 
 
 
 //End Add New Address Profile Checkout
 

   



    //    Edit Profile Checkout
    var checkouteditprofile = $('#checkout-edit-profile');

    if (checkouteditprofile.length) {
        checkouteditprofile.validate({
            rules: {
                pin_code: {
                    required: true,
                    number: true,
                    zipcode:true
                
                   
                },
                district: {
                    required: true
                },
                state: {
                    required: true,
                    

                },


                full_name: {
                    required: true,
                    minlength: 3
                },
                address: {
                    required: true,
                    
                },
                landmark: {
                    required: true,
                   
                },
                mobile_number: {
                    required: true,
                    number:true,
                    phonecheck: true
                    
                   
                }
                

                



            },
            messages: {
                pin_code: {
                    required: 'Pincode is Mandatory!',
                    number:'Only Numeric Allowed'
                },
                district: {
                    required: 'District is Mandatory!'
                },
                state: {
                    required: 'State is Mandatory!',


                },
                full_name: {
                    required: 'Name is Mandatory!'
                },
                address: {
                    required: 'Address is Mandatory!'
                },
                landmark: {
                    required: 'LandMark is Mandatory!',


                },
                mobile_number: {
                    required: 'Mobile Number is Mandatory!',
                    number:'Only Allowed Numeric'
                }



            }

        });
    }



//End Edit Profile Checkout

























       });