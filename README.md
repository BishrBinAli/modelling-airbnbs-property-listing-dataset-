# modelling-airbnbs-property-listing-dataset

Build a framework to systematically train, tune, and evaluate models on several tasks that are tackled by the Airbnb team

# Milestone 3 - Data Preparation

- Loaded the raw tabular data of airbnb property listings. The dataset has the following columns:

  - ID: Unique identifier for the listing
  - Category: The category of the listing
  - Title: The title of the listing
  - Description: The description of the listing
  - Amenities: The available amenities of the listing
  - Location: The location of the listing
  - guests: The number of guests that can be accommodated in the listing
  - beds: The number of available beds in the listing
  - bathrooms: The number of bathrooms in the listing
  - Price_Night: The price per night of the listing
  - Cleanliness_rating: The cleanliness rating of the listing
  - Accuracy_rating: How accurate the description of the listing is, as reported by previous guests
  - Communication_rating: The rating of the communication of the host
  - Location_rating: The rating of the location of the listing
  - Check-in_rating: The rating of check-in process given by the host
  - Value_rating: The rating of value given by the host
  - amenities_count: The number of amenities in the listing
  - url: The URL of the listing
  - bedrooms: The number of bedrooms in the listing

- Created function remove_rows_with_missing_ratings() to remove rows that did not have any rating values
- Description column in the raw dataset is stored as a list of strings. Created function combine_description_strings() to clean and combine the list of description strings to a single string
- Created function set_default_feature_values() to replace the empty values of "guests", "beds", "bathrooms" and "bedrooms" columns with 1
- Created function load_airbnb() that accepts a label column name and splits the dataset to features & labels and returns them as a tuple. The function only considers the numerical columns in the dataset
