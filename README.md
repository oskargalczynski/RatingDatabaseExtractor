# RatingDatabaseExtractor
### Complex solution simulating  two different environmetns: one with database ([PostgreSQL][3]) and one with extraction sctript (Python in [Jupyter Notebook][4]).

## Database
Docker container with basic [PostgreSQL][3] instaled and inserted data from [MovieLens][1], [ml-latest-small.zip][2]:
> This dataset (ml-latest-small) describes 5-star rating and free-text tagging activity from MovieLens, a movie recommendation service. It contains 100836 ratings and 3683 tag applications across 9742 movies. These data were created by 610 users between March 29, 1996 and September 24, 2018.

For users statistics tracking table with 610 users has been added.

All data inserted into database is stored in [data folder][11].
#### Database schema:
[![db scheme](https://raw.githubusercontent.com/oskargalczynski/RatingDatabaseExtractor/main/mydbScheme.png "db scheme")](https://raw.githubusercontent.com/oskargalczynski/RatingDatabaseExtractor/main/mydbScheme.png "db scheme")

## Extraction script
Simple Python script to extract data from [PostgreSQL][3] database container using [psycopg2-binary][5] package executed in [Jupyter Notebook][4] Docker container

Actual script is stored in jupyter folder in repository and is accesible in the http://0.0.0.0:8888/notebooks/work/DataBaseExtractor.ipynb after setting up container.

#### Script functions:
1. **top10movies()** - prints top 10 movies with the highest average rating score
2. **countMovies()** - prints number of all movies
3. **mostCommonGenre()** - prints most commor movie genre
4. **mostRatingUser()** - prints 5 users with highest number of ratings
5. **firstAndLastRate()** - using two sql querries prints both first and last rate
6. **moviesFromYear(year)** - prints movies from inserted year

## Requirements
- [Docker][7]
- [Docker-Compose][8]

Addittional:
- [Python3][8] - to execute [changePath.py ][10] script for changing path in docker-compose.yml file

## Instalation
1. Clone repository to desired folder
2. Execute [changePath.py ][10]script in repository path or change change all paths marked as '#absolute path to repository#' in docker-compose.yml to repository local path
3. Run docker-compose up and wait for all docker images being downloaded and extracted
4. After extracting all images docker-compose will set up everythink for you and launch both database and jupyter notebook container

## Usage
Both [PostgreSQL][3] and [Jupyter Notebook][4] are accesible on 0.0.0.0 host.
[PostgreSQL][3] database credentials:
- user = user
- password = pass123
- internal docker host = 172.20.0.5
- port = 5432
- database = mydb

[Jupyter Notebook][4] credentials:
- internal docker host = 172.20.0.4
- port = 8888
-password/token = pass123

To acces Jupyter Notebook open http://0.0.0.0:8888 and using passowrd provided above, log in. In folder "work" you can find [DataBaseExtractor.ipynb][12] notebook with both script and exectution results.

To re-do this solution simply create new notebook, import [psycopg2-binary][5]:
`pip install psycopg2-binary` press run,
then paste script from [DataBaseExtractor.ipynb][12] and execute.

## Technical notes
Database data and Jupyter Notebook storage files are stored in repository, only docker images will be downloaded during setting up docker containers.

##### Cititation:
> F. Maxwell Harper and Joseph A. Konstan. 2015. The MovieLens Datasets: History and Context. ACM Transactions on Interactive Intelligent Systems (TiiS) 5, 4: 19:1–19:19. https://doi.org/10.1145/2827872

[1]: https://movielens.org/
[2]: https://files.grouplens.org/datasets/movielens/ml-latest-small.zip
[3]: https://www.postgresql.org/ "PostgreSQL"
[4]: https://jupyter.org/ "Jupyter Notebook"
[5]: https://pypi.org/project/psycopg2-binary/ "psycopg2-binary"
[7]: https://docs.docker.com/engine/install/ "Docker"
[8]: https://docs.docker.com/compose/install/ "Docker-Compose"
[8]: https://www.python.org/downloads/ "Python3 "
[10]: https://github.com/oskargalczynski/RatingDatabaseExtractor/blob/main/changePath.py "changePath.py "
[11]: https://github.com/oskargalczynski/RatingDatabaseExtractor/tree/main/data "data folder"
[12]: http://0.0.0.0:8888/notebooks/work/DataBaseExtractor.ipynb
