import database

# Create the database if it doesn't exist
database.create_database()

database.create_user()

database.delete_user()

# Print the contents of the database
database.print_database()