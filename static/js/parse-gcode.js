$(document).ready(function() {


    // This is the function that is called when the user clicks the "Send GCode" button
    $(".send-gcode").on("click", function() {

        //prevent default form submission
        event.preventDefault();
        // Get the GCode from the text box
        var gcode = document.getElementById("gcode-entry").value;
    
        // Send the GCode to the server
        req  = $.ajax({
            url : '/send_gcode',
            type : 'POST',
            data : { command : gcode },
            success: function(_response) {
                console.log("response: " + _response);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
        });

        //clear the text box
        document.getElementById("gcode-entry").value = "";

        document.getElementById("gcode-response").value += gcode + "\n ";
        $('#gcode-response').scrollTop($('#gcode-response')[0].scrollHeight);

    });


    // var textarea = document.getElementById('gcode-response');
    // textarea.scrollBottom = textarea.scrollHeight;


    $("#home-robot").on("click", function() {
            
            //prevent default form submission
            event.preventDefault();
    
            //send the printer ip to the server 
            req  = $.ajax({
                url : '/home_robot',
                type : 'POST',
                success: function(_response) {
                    console.log("response: " + _response.result);
                },
                error: function(_status, _xhr, _error) {
                    console.log("error");
                }
            });
    
    });

    //stop the robot
    $("#stop-robot").on("click", function() {
            
            //prevent default form submission
            event.preventDefault();
    
            //send the printer ip to the server 
            req  = $.ajax({
                url : '/stop_robot',
                type : 'POST',
                success: function(_response) {
                    console.log("response: " + _response.result);
                },
                error: function(_status, _xhr, _error) {
                    console.log("error");
                }
            });
    
    }); 


    //Handle Connect Button
    $("#connect-btn").on("click", function() {
            console.log("connect");
            //prevent default form submission
            event.preventDefault();
    
            //send the printer ip to the server 
            req  = $.ajax({
                url : '/connect_printer',
                type : 'POST',
                success: function(_response) {
                    console.log("response: " + _response.result);
                },
                error: function(_status, _xhr, _error) {
                    console.log("error");
                }
            });
    
    });

    //Handle Disconnect Button
    $("#disconnect-btn").on("click", function() {
        console.log("disconnect");
        //prevent default form submission
        event.preventDefault();
        req = $.ajax({
            url : '/disconnect_printer',
            type : 'POST',
            success: function(_response) {
                console.log("response: " + _response.result);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
    });
    });
    


    //Handle the X-Axis
    $("#home-x-btn").on("click", function() {
        console.log("home x");
        //prevent default form submission
        event.preventDefault();

        //send the printer ip to the server 
        req  = $.ajax({
            url : '/home_x',
            type : 'POST',
            success: function(_response) {
                console.log("response: " + _response.result);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
        });

    });

    //Handle the Y-Axis
    $("#home-y-btn").on("click", function() {
        console.log("home y");
        //prevent default form submission
        event.preventDefault();

        //send the printer ip to the server 
        req  = $.ajax({
            url : '/home_y',
            type : 'POST',
            success: function(_response) {
                console.log("response: " + _response.result);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
        });

    });

    //Handle the Z-Axis
    $("#home-z-btn").on("click", function() {
        console.log("home z");

        //prevent default form submission
        event.preventDefault();

        //send the printer ip to the server 
        req  = $.ajax({
            url : '/home_z',
            type : 'POST',
            success: function(_response) {
                console.log("response: " + _response.result);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
        });

    });
    
    // Handle Home All
    $("#home-all-btn").on("click", function() {
        console.log("home all");
        //prevent default form submission
        event.preventDefault();

        //send the printer ip to the server 
        req  = $.ajax({
            url : '/home_all',
            type : 'POST',
            success: function(_response) {
                console.log("response: " + _response.result);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
        });

    });

    //Handle Pause
    $("#pause-btn").on("click", function() {
        console.log("pause");
        //prevent default form submission
        event.preventDefault();

        //send the printer ip to the server 
        req  = $.ajax({
            url : '/pause',
            type : 'POST',
            success: function(_response) {
                console.log("response: " + _response.result);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
        });

    });

    //Handle Stop
    $("#stop-btn").on("click", function() {
        console.log("stop");
        //prevent default form submission
        event.preventDefault();

        //send the printer ip to the server 
        req  = $.ajax({
            url : '/stop',
            type : 'POST',
            success: function(_response) {
                console.log("response: " + _response.result);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
            });
        });

    //Handle Print Files Button
    $("#files-btn").on("click", function() {
        console.log("files");
        //prevent default form submission
        event.preventDefault();

        //send the printer ip to the server 
        req  = $.ajax({
            url : '/print_files',
            type : 'POST',
            success: function(_response) {
                console.log("response: " + _response.result);
            },
            error: function(_status, _xhr, _error) {
                console.log("error");
            }
        });

    });

});