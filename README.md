
# Conference management system

## This is a backend for a conference management system.
## It is built using Python, Django, PostgreSQL and docker.


### Run the project ::

- Clone this repo
- Run the command ```docker-compose up -d```
- Go to http://localhost:8000/docs/ to see the API and model schema along with a swagger testing interface.


### REST APIs available ::
Base URL - http://localhost:8000

- Conference
  - Create - POST on /conference/
  - List - GET on /conference/
  - Edit - PUT on /conference/{conference_id}/
  - List specific conference with talks and people - GET on /conference/{conference_id}/

- Talk
  - List - GET on /talk/
  - Create - POST on /talk/
  - Edit - PUT on /talk/{talk_id}/ - (Also has ability to pass full list of people to be in the talk - bulk add/remove)

- Person
  - List - GET on /person/ - DONE.
  - Create - POST on /person/ - DONE.

- Custom talk APIs
  - Add person to talk - POST on /talk_person/{talk_id}/
  - Remove person from talk - PUT on /talk_person/{talk_id}/
