CREATE TABLE IF NOT EXISTS images (  -- You create a table named images only if it does not already exist
    id INTEGER PRIMARY KEY AUTOINCREMENT,  -- You define id as an integer primary key that auto-increments with each new record
    name TEXT NOT NULL,  -- You define name as a text field that cannot be null (must have a value)
    file_path TEXT NOT NULL  -- You define file_path as a text field that cannot be null (must have a value)
);



