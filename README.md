# Attention: This is an old scraper (3+ years old). There is a lot to be refactored, especially in the way concurrency was implemented.
# RSS / Atom Feed Scraper
Scraper designed to extract the RSS or Atom feed URL, fetch the feed contents and return data from some attributes.

##### By default the scraper will stract data from the following websites: 

- https://www.theverge.com/
- https://www.phoronix.com/
- https://es.gizmodo.com/
- https://www.engadget.com/

# Run
* Clone the repository.
* Run the command `pip install -r requirements.txt`.
* Inside the system directory run the command `python main.py`. <br/>
If the scraper run successfully the output will be a data.json file inside the system directory.

# Run with Docker
* Inside the project repository run the command `docker build -t <container name> .`
* Run the command `docker run <container name>`
* Copy the data.json file to the currenty directory with the following command `docker cp <container id>:/data.json .`