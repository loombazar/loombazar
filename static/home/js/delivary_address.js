$(document).ready(function()
{

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

    
 //   Start   newAddress ProfilePage
 var addnewaddressprofile = $('#profileaddnewaddress');

 if ( addnewaddressprofile.length) {
    addnewaddressprofile.validate({
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



//End new Address ProfilePage 
//   Start   EditAddress ProfilePage
var editnewaddressprofile = $('#editDelivaryAddress');

if (editnewaddressprofile.length) {
    editnewaddressprofile.validate({
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



//End Edit Address ProfilePage 






});