import sqlite3 #First thing we did was import the sqlite3 module so we can interact with our database
import os  #A module you might have seen before that lets us work with file paths

#We need to create some absolute paths to the database and the schema - This is a more dynamic approach like I mentioned in class - doens't matter now where we run this app
DB_PATH = os.path.join(os.path.dirname(__file__), 'database.db')
SCHEMA_PATH = os.path.join(os.path.dirname(__file__), 'schema.sql')

def initialize_db():  #Important function here to initialize the database - will be called from the flask app
    """Initialize the database using the schema file.""" 
    try:  #try-except is pretty much the same as try-catch in other languages - if connection is successful then no error will be thrown - otherwise it's a go!!!
        with sqlite3.connect(DB_PATH) as conn:  #We need to establish a connection to the db. We do so using a context manager (with) - ensures database and schema are properly managed!
            cursor = conn.cursor()  #We need to initialize this cursor in order to execute SQL commands!
            with open(SCHEMA_PATH, 'r') as schema_file:  #Again - context manager (with) - as schema_file? schema_file is the actual object you work with!
                cursor.executescript(schema_file.read())  #we make a call to the executescript function - the read function acts upon the schema_file object
            print("Database initialjized successfully.")  #Success message - not much to explain here!
    except sqlite3.Error as e:  #This is where you will catch any sqlite specific errors. 
        print(f"Error initializing database: {e}")  #Error message - not much to explain here - as long as you know why we pass {e} to the f-string and what it is!

def insert_sample_images():  #We need to insert the dinosaur images in the db - however we are really inserting the path to the images - not the image itself!!
    """Insert sample image data into the database if not already present.""" #See context manager below your list of tuples to understand what I mean by "if not already present"  
    sample_images = [  #list of tuples (dinos) name, file_path
        ('Brontosaurus', 'images/bronto.jpg'),
        ('Pterodactyl', 'images/ptera.jpg'),
        ('Stegosaurus', 'images/stego.jpg'),
        ('Tyrannosaurus rex', 'images/trex.jpg'),
        ('Triceratops', 'images/tri.jpg'),
        ('Velociraptor', 'images/veloc.jpg'),
    ]
    
    with sqlite3.connect(DB_PATH) as conn:  #And yet another context manager to connect to the db
        cursor = conn.cursor()  #And yet another cursor object
        for name, file_path in sample_images:  # Iterate over the list of sample images
            cursor.execute('SELECT COUNT(*) FROM images WHERE file_path = ?', (file_path,))  #Handling duplicates (1 way) Check if the image already exists in the database. * = all rows not columns. What is that question mark? 
            #The query above and the '?' is an example of a parameterized query or prepared statement - we went over this in class today 2/13 - you need to be in class unless you are sick! - Helps prevent SQL injection!
            if cursor.fetchone()[0] == 0:  #If the image is not already in the database (count is 0) - What's really going on is that a tuple is being returned and we extract the first value in the tuble [0] - We need to check if the first row is in-fact 0. I make the misake often and forget that stupid tuple comma in my execute functions - if you were in class you know what I mean!
                cursor.execute('INSERT INTO images (name, file_path) VALUES (?, ?)', (name, file_path))  #Where we actually insert the new image into the database
        conn.commit()  #Commit the transaction to save changes
        print("Sample images inserted successfully (if they were not already present).")  #Simple success message!

def get_images():  #Here we defined a function to fetch all images from the database
    """Fetch all images from the database."""
    with sqlite3.connect(DB_PATH) as conn:  #And yet another context manger - connecting to database
        cursor = conn.cursor()  #And yet another cursor to execute SQL commands
        cursor.execute('SELECT id, name, file_path FROM images')  #We executed a SQL query to select all image records
        return cursor.fetchall()  #We return all rows!
    
def get_image_by_id(image_id):  #We defined a function to fetch a specific image by its ID -
    """Fetch a specific image by its ID."""  
    with sqlite3.connect(DB_PATH) as conn:  #Another connection. 
        cursor = conn.cursor()  #Another connection. 
        cursor.execute('SELECT id, name, file_path FROM images WHERE id = ?', (image_id,))  #We executed a SQL query to select an image by its ID
        return cursor.fetchone()  #fetchone returns the first matching row - by id! Make sense?  


#YOU CAN CALL BOTH FUNCTIONS TO MAKE SURE THAT YOUR DB AND SCHEMA ARE CREATED AND READ ACCORDINGLY - AFTERWARDS PLEASE DELETE THESE TWO FUNCTION CALLS. 
#YOU SHOULD INITIALIZE THE DB AND INSERT IMAGES FROM THE FLASK APP - CALL THESE FUNCTION IN THE FLASK APP - MEANING YOU NEED TO IMPORT THIS MODULE - YEA??
initialize_db()
insert_sample_images()