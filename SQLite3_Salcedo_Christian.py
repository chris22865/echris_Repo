import sqlite3

# connect to the database
conn = sqlite3.connect('PJ2_world.db')

# create a callable variable to interact with the database
c = conn.cursor()

print('a.')

# Look up the columns city table
print('Column names for city table: ')
c.execute("PRAGMA table_info(city)")
print(c.fetchall())

view_row_1 = (5000,)
# create a new row with a unique ID of 5000
c.execute("INSERT INTO city VALUES (5000, 'King''s Landing', 'WTO', Null, 5000000000)")
c.execute("SELECT * FROM city WHERE ID=?", view_row_1)
print(c.fetchone())

print(' ')

print('b.')

# Look up the columns country table
print('Column names for country table: ')
c.execute("PRAGMA table_info(country)")
print(c.fetchall())
# countryName, Continent, Region, Population_country
c.execute("SELECT countryName, Continent, Region, Population_country FROM country WHERE Population_country > 1000000000")
print(c.fetchone())
print("Question: \n Since we already updated the data in step a for "
      "city 'King's Landing' in country 'Westero' (country code WTO), "
      "whose population is 5 billion (larger than 1 billion), did you find"
      "country 'Westero' in the result from step b? Why or why not?")

print("Answer: \n No because the data with the country Westeros was added to the 'city' table, not the 'country' table.")

print(' ')

print('c.')

# look up all cities with a population greater than 1 million
print('All cities with a population greater than 1 million and in the US: ')
c.execute("SELECT * FROM city WHERE Population_city > 1000000 AND CountryCode = 'USA'")
print(c.fetchall())

# look up aggregates count and avg population of cities with a population greater than 1 million and only in the U.S.
c.execute("SELECT COUNT(cityName) AS cityCount, AVG(Population_city) AS Population_avg "
          "FROM city WHERE Population_city > 1000000 AND CountryCode = 'USA' ")
print('Count & Average of cities with a population greater than 1 million and in the US: ')
print(c.fetchall())

# save changes
conn.commit()

# close connection to database
conn.close()
