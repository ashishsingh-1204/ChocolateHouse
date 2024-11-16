# ChocolateHouse
This is a simple Python application for managing a fictional chocolate house. It uses SQLite to manage seasonal flavor offerings, ingredient inventory, and customer flavor suggestions with allergy concerns.

Setup and Running
Option 1: Running locally
Clone this repository:
git clone https://github.com/yourusername/chocolate-house.git
cd chocolate-house

Create a virtual environment and activate it:
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`

Install the required packages:
pip install -r requirements.txt

Run the application:
python app.py
Open a web browser and navigate to http://localhost:5000

Option 2: Running with Docker
Make sure you have Docker installed on your system.
Build the Docker image:
docker build -t chocolate-house .

Run the Docker container:
docker run -p 5000:5000 chocolate-house

Open a web browser and navigate to http://localhost:5000

Testing
To test the application, follow these steps:
Add a seasonal flavor:

Navigate to the "Seasonal Flavors" page
Enter a flavor name (e.g., "Dark Chocolate Peppermint") and season (e.g., "Winter")
Click "Add Flavor"
Verify that the new flavor appears in the list
Add an ingredient to the inventory:

Navigate to the "Ingredient Inventory" page
Enter an ingredient name (e.g., "Cocoa Powder") and quantity (e.g., 100)
Click "Add Ingredient"
Verify that the new ingredient appears in the list
Submit a customer suggestion:

Navigate to the "Customer Suggestions" page
Enter a suggested flavor (e.g., "Lavender White Chocolate") and any allergy concerns (e.g., "Nuts")
Click "Submit Suggestion"
Verify that the new suggestion appears in the list
Test edge cases:

Try submitting empty forms
Try adding duplicate flavors or ingredients
Test with very long input strings
SQL Queries and ORM Usage
This application uses SQLAlchemy as an ORM (Object-Relational Mapping) to interact with the SQLite database. Here are some example SQL queries and their ORM equivalents:

Retrieve all seasonal flavors:

SQL: SELECT * FROM seasonal_flavor;
ORM: SeasonalFlavor.query.all()
Add a new ingredient:

SQL: INSERT INTO ingredient (name, quantity) VALUES ('Sugar', 500);
ORM:
new_ingredient = Ingredient(name='Sugar', quantity=500)
db.session.add(new_ingredient)
db.session.commit()
Update an existing flavor:

SQL: UPDATE seasonal_flavor SET season = 'Summer' WHERE name = 'Strawberry Delight';
ORM:
flavor = SeasonalFlavor.query.filter_by(name='Strawberry Delight').first()
flavor.season = 'Summer'
db.session.commit()
Delete a customer suggestion:

SQL: DELETE FROM customer_suggestion WHERE flavor = 'Bacon Chocolate';
ORM:
suggestion = CustomerSuggestion.query.filter_by(flavor='Bacon Chocolate').first()
db.session.delete(suggestion)
db.session.commit()

These examples demonstrate how the ORM abstracts the SQL queries, making it easier to work with the database using Python objects and methods.
