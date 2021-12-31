<h2>Ticket Dashboard</h2>
This ticket dashboard is the end result of the <a href=https://learn.acloud.guru/handson/924ced29-d09e-40d5-ba73-2507c1d318f0/course/df3778be-ba58-4be7-a232-aa658bed7517>Building a Web Application with Python and Flask</a> lab

<h3>Prompt</h3>
You've been asked to build a dashboard for your boss so that he can see the status of the various bug tickets that exist in your system. Tickets are extremely simple and only have a few points of information:

  Name: Required.
  Status: Required, available options are:
      0 (Reported)
      1 (In Progress)
      2 (In Review)
      3 (Resolved)
  URL: Optional

<h2>Getting Started</h2>
To run this web application first start the lab, linked above at the top of this readme, which instantiates the database server with the docker posgres image with our ticket information. 
<br>Then clone this repo to the server you want to run the flask app from. This could be from the cloud server workstation provided with the lab, your local machine, or where have you. If not using the lab provided workstation make sure you have <a href='https://www.python.org/downloads/'>python3</a> and <a href='https://pipenv.pypa.io/en/latest/install/'>Pipenv</a> installed on the machine.
<br>Next create the below environment variables, coinciding with the a cloud guru provided database server information, on the server where you will be running the flask app:
<ul>
  <li>DB_HOST='<DB_PRIVATE_IP>'</li>
  <li>DB_NAME='<DB_NAME>'<</li>
  <li>DB_PASSWORD='<DB_PASSWORD>'</li>
  <li>DB_PORT='<DB_PORT>'</li>
  <li>DB_USERNAME='<DB_USERNAME>'<</li>
  <li>FLASK_ENV='development';</li>
  <li>FLASK_APP='./flaskr/'</li>
</ul>
if doing this in a .env file remember to source it afterwards (`source .env` for the unitiated)
<br>Run `pipenv install` to install the project dependencies and create a virtual environemnt. Then run `pipenv shell` to activate the the newly minted virtual environment
<br>Finally you can start the app with `flask run --host=0.0.0.0 --port=3000` and you can open the ip address in your favorite browser


