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

You can use the pre-filled values or create your own instance of Google Programmable Search Engine and obtain an API key. For more information, see [Google custom search documentation](https://developers.google.com/custom-search/v1/introduction).

## Usage

### Installing dependencies
The application dependencies are listed in ``requirements.txt``.

It is recommended to install dependencies by using a virtual environment.
For information on creating and activating virtual environments, refer to the [Python documentation](https://packaging.python.org/en/latest/guides/installing-using-pip-and-virtual-environments/).

Once you have created and activated the virtual environment in the application directory, run the following command to install the dependencies:

    $ python -m pip install -r requirements.txt

### Launching the application
To launch the application, run the following command in the application directory:

    $ python googler.py [--port <port_number>] [--login <user_name>] [--password <password>]

where:
* ``port_number`` is the localhost port number to be used for the application server.
  
  This parameter is optional and defaults to *5000*.
* ``user_name`` is the user name to be provided when making requests to the application.

  This parameter is optional and defaults to *admin*.
* ``password`` is the password to be provided when making requests to the application.

  This parameter is optional and defaults to *System1!*.

### Getting text search results

``GET``**/text**

This method returns the first 10 text search results from Google.

#### Query string parameters

#### Request example

#### Response example

### Getting image search results

``GET``**/image**

This method returns the first 10 image search results from Google.

#### Query string parameters

#### Request example

#### Response example



