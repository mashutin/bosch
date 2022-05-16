# Googler
Googler is an absolutely useless application made for test purpose.

## Prerequisites
* Python 3 with pip

## Configuration
The ``conf.py`` file contains the following configuration parameters:

* **api_key**

  The Google API key.

* **cse_id**

  The identifier of the Programmable Search Engine.

You can use the pre-filled values or create your own instance of Google Programmable Search Engine and obtain an API key. For more information, see https://developers.google.com/custom-search/v1/introduction.

## Usage

### Installing dependencies

### Launching the application
To launch the application, run the following command:

    googler.py [--port <port_number>] [--login <user_name>] [--password <password>]

where:
* ``port_number`` is the localhost port number to be used for the application server.
  
  This parameter is optional and defaults to *5000*.
* ``user_name`` is the user name to be provided when making requests to the application.

  This parameter is optional and defaults to *admin*.
* ``password`` is the password to be provided when making requests to the application.

  This parameter is optional and defaults to *System1!*.

### Getting text search results
<mark>GET&nbsp</mark><span style="background-color:black;color:white">&nbsp/text&nbsp</span>

### Getting image search results


