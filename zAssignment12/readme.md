# I made this code with 2 different programming languages for server -> server.js and server.py
# I tried both and the image was uploaded to the firebase but i when i tried to upload a more big image it did't work as needed so i used  
        " const express = require('express'); "
        " const bodyParser = require('body-parser'); "
            // Middleware to parse JSON requests with an increased payload size limit
        " app.use(bodyParser.json({ limit: '10mb' })); "