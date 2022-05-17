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

Once you have created and activated a virtual environment in the application directory, run the following command to install the dependencies:

    $ python -m pip install -r requirements.txt

### Launching application
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

#### Request example

    curl -u admin:System1! -v http://127.0.0.1:5000/googler/api/text/jobs%20at%20bosch

> **ATTENTION**:
> Don't forget to replace spaces with '%20' in the search request.

#### Response schema

* ``results`` *array*
  
  Search results
  * ``info`` *string*

    Search result description.
  * ``link`` *string*
  
    Link to the webpage.
  * ``title`` *string*
  
    Webpage title.

#### Response example

```json
{
   "results": [
      {
         "info": "Which site do you prefer for finding jobs at Bosch? Indeed. Bosch career site. Other.",
         "link": "https://www.indeed.com/q-Bosch-jobs.html",
         "title": "Bosch Jobs, Employment | Indeed.com"
      },
      {
         "info": "Jobs at Bosch Group. Employees can work remotely. Browse by: Location. -, Slovakia (Slovak Republic). 1 job. Business Developer - priemyseln\u00e9 kotly Bosch.",
         "link": "https://careers.smartrecruiters.com/BoschGroup",
         "title": "Careers at Bosch Group"
      },
      {
         "info": "Bosch jobs in Illinois. Page 1 of 56 jobs at Bosch.",
         "link": "https://www.indeed.com/q-Bosch-l-Illinois-jobs.html",
         "title": "Bosch Jobs, Employment in Illinois | Indeed.com"
      },
      {
         "info": "Jobs at Bosch Group. Employees can work remotely. Browse by: Location. Akron, OH. 1 job. Software Engineer - Research. Full-time. Albion, IN. 1 job\u00a0...",
         "link": "https://careers.smartrecruiters.com/BoschGroup?search=intern%20Research",
         "title": "Careers at Bosch Group"
      },
      {
         "info": "Bosch jobs in Michigan. Page 1 of 223 jobs at Bosch. Did you mean jobs with \"Bosch\" in the job posting? Operators Needed (Machining and Assembly).",
         "link": "https://www.indeed.com/q-Bosch-l-Michigan-jobs.html",
         "title": "Bosch Jobs, Employment in Michigan | Indeed.com"
      },
      {
         "info": "There are currently no open jobs at Bosch Rexroth in Charlotte listed on Glassdoor. Sign up to get notified as soon as new Bosch Rexroth jobs in Charlotte\u00a0...",
         "link": "https://www.glassdoor.com/Jobs/Bosch-Rexroth-Charlotte-Jobs-EI_IE18586.0,13_IL.14,23_IC1138644.htm",
         "title": "No Jobs at Bosch Rexroth in Charlotte | Glassdoor"
      },
      {
         "info": "Jan 8, 2019 ... Around 50,000 jobs at Bosch worldwide depend on diesel products, 15,000 of them in Germany, according to the report.",
         "link": "https://www.cleanenergywire.org/news/germanys-diesel-crisis-causes-staff-layoffs-bosch",
         "title": "Germany's diesel crisis causes staff layoffs at Bosch | Clean Energy ..."
      },
      {
         "info": "There are currently no open jobs at Bosch in Hong Kong listed on Glassdoor. Sign up to get notified as soon as new Bosch jobs in Hong Kong are posted.",
         "link": "https://www.glassdoor.com/Jobs/Bosch-Hong-Kong-Jobs-EI_IE4293.0,5_IL.6,15_IN106.htm",
         "title": "No Jobs at Bosch in Hong Kong | Glassdoor"
      },
      {
         "info": "Jobs at Bosch USA \u00b7 Software Engineer \u00b7 Sales Support Operations Specialist \u00b7 Project Manager - Passive Safety Programs \u00b7 Motorsport Customer Application Engineer.",
         "link": "https://www.linkedin.com/company/boschusa/jobs",
         "title": "Bosch USA: Jobs | LinkedIn"
      },
      {
         "info": "Dec 1, 2017 ... Arthrex is a a global orthopedic medical device company headquartered in Florida,. People interested in applying for jobs at Bosch should go\u00a0...",
         "link": "https://www.independentmail.com/story/news/local/2017/12/01/bosch-adding-125-jobs-major-expansion-its-anderson-county-plant/912769001/",
         "title": "Bosch adding 130 jobs in major expansion of its Anderson County ..."
      }
   ]
}
```

### Getting image search results
``GET``**/image**

This method returns the first 10 image search results from Google.

#### Request example

    curl -u admin:System1! -v http://127.0.0.1:5000/googler/api/image/bavarian%20alps

> **ATTENTION**:
> Don't forget to replace spaces with '%20' in the search request.

#### Response schema

* ``results`` *array*
  
  Search results
  * ``context`` *string*

    Link to the webpage where the image is located.
  * ``link`` *string*
  
    Link to the image.
  * ``size`` *object*

    Image dimensions.
    * ``height`` *integer*
    
      Image height.
    * ``width`` *integer*

      Image width.
  * ``source`` *string*

    Name of the website where the image is located.

#### Response example
```json
{
   "results": [
      {
         "context": "https://www.macsadventure.com/holiday-2547/bavarian-alps-hiking-the-salt-trail/",
         "link": "https://d1hirb55zrpywb.cloudfront.net/macs-adventure-tours/routes/WGSAS/routeimagegallery/1-rsz-08102019151224733.jpg",
         "size": {
            "height": 825,
            "width": 1182
         },
         "source": "www.macsadventure.com"
      },
      {
         "context": "https://www.getyourguide.com/bavarian-alps-l35352/bus-minivan-tours-tc4/",
         "link": "https://cdn.getyourguide.com/img/location/5a086edc7b91c.jpeg/99.jpg",
         "size": {
            "height": 792,
            "width": 1585
         },
         "source": "www.getyourguide.com"
      },
      {
         "context": "https://www.fodors.com/world/europe/germany/the-bavarian-alps",
         "link": "https://www.fodors.com/assets/destinations/704815/neuschwanstein-castle-the-bavarian-alps-germany_980x650.jpg",
         "size": {
            "height": 650,
            "width": 980
         },
         "source": "www.fodors.com"
      },
      {
         "context": "https://www.macsadventure.com/holiday-2419/walking-in-the-bavarian-alps/",
         "link": "https://d1hirb55zrpywb.cloudfront.net/macs-adventure-tours/routes/WGSWOZ/routeimagegallery/1-rsz-08102019123830439.jpg",
         "size": {
            "height": 825,
            "width": 1182
         },
         "source": "www.macsadventure.com"
      },
      {
         "context": "https://www.britannica.com/place/Bavarian-Alps",
         "link": "https://cdn.britannica.com/26/99626-050-8DCE7876/Neuschwanstein-Castle-Bavarian-Alps-Germany.jpg",
         "size": {
            "height": 1466,
            "width": 970
         },
         "source": "www.britannica.com"
      },
      {
         "context": "https://www.youtube.com/watch?v=WM2_qnWENxA",
         "link": "https://i.ytimg.com/vi/WM2_qnWENxA/maxresdefault.jpg",
         "size": {
            "height": 720,
            "width": 1280
         },
         "source": "www.youtube.com"
      },
      {
         "context": "https://www.britannica.com/place/Bavarian-Alps",
         "link": "https://cdn.britannica.com/26/99626-050-8DCE7876/Neuschwanstein-Castle-Bavarian-Alps-Germany.jpg?w=300&h=169&c=crop",
         "size": {
            "height": 169,
            "width": 300
         },
         "source": "www.britannica.com"
      },
      {
         "context": "https://www.grayline.com/tours/salzburg/bavarian-alps-11862_9_12130_943/",
         "link": "https://cdn.tourcms.com/a/11676/943/1/large.jpg",
         "size": {
            "height": 1000,
            "width": 1500
         },
         "source": "www.grayline.com"
      },
      {
         "context": "https://www.istockphoto.com/photos/bavarian-alps",
         "link": "https://media.istockphoto.com/photos/idyllic-landscape-in-the-alps-with-grazing-cows-in-summer-picture-id537406916?k=20&m=537406916&s=612x612&w=0&h=k_V1j2sJgl1rAMvoLGBSMJU49bonp2NDyZUJkgs1TCg=",
         "size": {
            "height": 407,
            "width": 612
         },
         "source": "www.istockphoto.com"
      },
      {
         "context": "https://www.getyourguide.com/bayerische-alpen-l35352/aktivitaeten-tc54/?categoriesNavigationId=54",
         "link": "https://cdn.getyourguide.com/img/location/5a086edc7b91c.jpeg/88.jpg",
         "size": {
            "height": 1350,
            "width": 2400
         },
         "source": "www.getyourguide.com"
      }
   ]
}
```


