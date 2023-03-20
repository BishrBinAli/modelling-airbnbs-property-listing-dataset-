# %%
import pandas as pd


def remove_rows_with_missing_ratings(df):
    rating_columns = [col for col in df.columns if col.endswith('_rating')]
    df = df.dropna(subset=rating_columns, how='all')
    return df


def combine_description_strings(df):
    # Lists are stored as string in csv file
    df['Description'] = df['Description'].apply(
        lambda x: pd.eval(x) if pd.notna(x) else x)
    df = df.dropna(subset='Description')
    # Removing empty quotes and first title in list
    df['Description'] = df['Description'].apply(
        lambda x: [val for val in x if val != "" and val != "About this space"])
    # Combining to single string
    df['Description'] = df['Description'].apply(lambda x: " ".join(x))
    return df


def set_default_feature_values(df):
    df = df.fillna({'guests': 1, 'beds': 1, 'bathrooms': 1, 'bedrooms': 1})
    return df


def clean_tabular_data(df):
    df = remove_rows_with_missing_ratings(df)
    df = combine_description_strings(df)
    df = set_default_feature_values(df)
    return df


def load_airbnb(df, label):
    numerical_columns = ['guests', 'beds', 'bathrooms', 'Price_Night', 'Cleanliness_rating', 'Accuracy_rating',
                         'Communication_rating', 'Location_rating', 'Check-in_rating', 'Value_rating', 'amenities_count', 'bedrooms']
    labels = df[label]
    features = df[[column for column in numerical_columns if column != label]]
    return (features, labels)


# %%
if __name__ == "__main__":
    # %%
    listings_df = pd.read_csv(
        './airbnb-property-listings/tabular_data/listing.csv')

    # %%
    # There is a row with column values from the third column shifted to the right by one resulting in an extra unnamed column
    shifted_ind = listings_df.index.get_indexer(
        listings_df[listings_df['Unnamed: 19'].notna()].index)
    listings_df.iloc[shifted_ind, 3:-1] = listings_df.iloc[shifted_ind, 4:]
    listings_df = listings_df.drop(columns='Unnamed: 19')

    # %%
    listings_df = clean_tabular_data(listings_df)

    # %%
    listings_df.to_csv(
        './airbnb-property-listings/tabular_data/clean_tabular_data.csv', index=False)
