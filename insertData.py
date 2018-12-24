import sqlite3


movie_name = '"Christmas Vacation"'
movie_release_year = '1989'
column1 = 'movie_name'
column2 = 'movie_release_year'


# Present user with options for tables
print('''
 TABLES
 1) Movies
 2) Seasons
 3) Weathers
 4) Temperatures
 5) Holidays
 6) Movie Seasons
 7) Movie Weathers
 8) Movies Temperatures
 9) Movie Holidays
''')

# Ask user which table to edit
# Store user selection in integer, variable: table_number
table_number = int(input('Which table do you want to edit? Choose a number > '))

# Find the correct table based on user's selection, add to table_name variable
if table_number == 1:
    table_name = 'movie_table'
elif table_number == 2:
    table_name = 'season_table'
elif table_number == 3:
    table_name = 'weather_table'
elif table_number == 4:
    table_name = 'temperature_table'
elif table_number == 5:
    table_name = 'holiday_table'
elif table_number == 6:
    table_name = 'movie_season_table'
elif table_number == 7:
    table_name = 'movie_weather_table'
elif table_number == 8:
    table_name = 'movie_temperature_table'
elif table_number == 9:
    table_name = 'movie_holiday_table'
else:
    print('You dun goofed! Restart the app and try again for now.')

# Connect to the database file
conn = sqlite3.connect('movie_settings_db.sqlite')
c = conn.cursor()

# Check table for number of columns: PRAGMA table_info(table_name)
## get the columns of a given table from SQLite DB
c.execute('PRAGMA table_info({tn})'.format(tn=table_name))
## put the column names in an array
## this is explained in getTableColumns_Explanation.py file
column_names = [tup[1] for tup in c.fetchall()]
## get the length of the array to determine number of columns in the table
number_of_columns = len(column_names)
print(number_of_columns)
print(column_names)

# Present columns to user for data entry, but skip first column because it is
## auto-generated
### https://docs.python.org/3/library/sqlite3.html#module-sqlite3
### https://stackoverflow.com/questions/8316176/insert-list-into-my-database-using-python
table_entry = []

for x in column_names[1:]:
    data_field_entry = input('What would you like to enter in ' + x + '? ')
    table_entry.append(data_field_entry)
    print(table_entry)
    print(x)
    

### https://www.geeksforgeeks.org/python-format-function/
### https://www.learnpython.org/en/String_Formatting
### https://stackoverflow.com/questions/44778/how-would-you-make-a-comma-separated-string-from-a-list-of-strings
print(len(column_names) -1)
column_names_string = ", ".join(column_names[1:])
entry_string = ', '.join('?' * (len(column_names) - 1))
query_string = 'INSERT INTO %s (%s) VALUES (%s);' % (table_name, column_names_string, entry_string)
c.execute(query_string, table_entry)



"""
c.execute("INSERT INTO {tn} ({cn}) VALUES ({te})".\
    format(tn=table_name, cn=x, te=data_field_entry))
       

varlist = [variable_1,variable_2]
var_string = ', '.join('?' * len(varlist))
query_string = 'INSERT INTO table VALUES (%s);' % var_string
cursor.execute(query_string, varlist)
"""

"""
# NEED to check for movie already existing in the table before adding it
# C) Updates the newly inserted or pre-existing entry            
c.execute('''
 INSERT INTO {tn} ({col1}, {col2}) VALUES
  ({val1}, {val2})
'''.\
 format(tn=table_name, col1=column1, col2=column2, val1=movie_name,
 val2=movie_release_year))
"""

conn.commit()
conn.close()