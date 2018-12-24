import sqlite3

# Connecting to the database file
conn = sqlite3.connect('movie_settings_db.sqlite')
c = conn.cursor()

# Movie Table
# Create movie table and movie_id as primary key with integer data type
# the triple quotes (''') continue the line even though I moved to the
# next line down
c.execute('''
 CREATE TABLE movie_table (
  movie_id INTEGER PRIMARY KEY,
  movie_name TEXT,
  movie_release_year INTEGER
  )
''')

# Season Table
c.execute('''
 CREATE TABLE season_table (
  season_id INTEGER PRIMARY KEY,
  season_name TEXT
  )
''')

# Weather Table
c.execute('''
 CREATE TABLE weather_table (
  weather_id INTEGER PRIMARY KEY,
  weather_name TEXT
  )
''')

# Temperature Table
c.execute('''
 CREATE TABLE temperature_table (
  temperature_id INTEGER PRIMARY KEY,
  temperature_name TEXT
  )
''')

# Holiday Table
c.execute('''
 CREATE TABLE holiday_table (
  holiday_id INTEGER PRIMARY KEY,
  holiday_name TEXT
  )
''')

# Movie Season Table
# FOREIGN KEY pulls movie_id and season_id from their respective tables
c.execute('''
 CREATE TABLE movie_season_table (
  movie_id INTEGER,
  season_id INTEGER,
   FOREIGN KEY (movie_id) REFERENCES movie_table(movie_id),
   FOREIGN KEY (season_id) REFERENCES season_table(season_id),
   PRIMARY KEY (movie_id, season_id)
  )
''')

# Movie Weather Table
c.execute('''
 CREATE TABLE movie_weather_table (
  movie_id INTEGER,
  weather_id INTEGER,
   FOREIGN KEY (movie_id) REFERENCES movie_table(movie_id),
   FOREIGN KEY (weather_id) REFERENCES weather_table(weather_id),
   PRIMARY KEY (movie_id, weather_id)
  )
''')

# Movie Temperature Table
c.execute('''
 CREATE TABLE movie_temperature_table (
  movie_id INTEGER,
  temperature_id INTEGER,
   FOREIGN KEY (movie_id) REFERENCES movie_table(movie_id),
   FOREIGN KEY (temperature_id) REFERENCES temperature_table(temperature_id),
   PRIMARY KEY (movie_id, temperature_id)
  )
''')

# Movie Holiday Table
c.execute('''
 CREATE TABLE movie_holiday_table (
  movie_id INTEGER,
  holiday_id INTEGER,
   FOREIGN KEY (movie_id) REFERENCES movie_table(movie_id),
   FOREIGN KEY (holiday_id) REFERENCES holiday_table(holiday_id),
   PRIMARY KEY (movie_id, holiday_id)
  )
''')

# Committing changes and closing the connection to the database file
conn.commit()
conn.close()