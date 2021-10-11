<?php

class ConnectionManager {

    public function getConnection() {
        $servername = 'localhost';
        $username = 'root';
        $password = '';
        $dbname = 'lms';
        //$port = '3308';
        
        // Create connection
        //$conn = new PDO("mysql:host=$servername;dbname=$dbname;port=$port", $username, $password);     
        $conn = new PDO("mysql:host=$servername;dbname=$dbname", $username, $password);     
        $conn->setAttribute(PDO::ATTR_ERRMODE, PDO::ERRMODE_EXCEPTION); // if fail, exception will be thrown

        // Return connection object
        return $conn;
    }

}