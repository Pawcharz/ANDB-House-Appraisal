"USA Real Estate Dataset" is a dataset that contains such tables

    brokered by (categorically encoded agency/broker)
    status (Housing status - a. ready for sale or b. ready to build)
    price (Housing price, it is either the current listing price or recently sold price if the house is sold recently)
    bed (# of beds)
    bath (# of bathrooms)
    acre_lot (Property / Land size in acres)
    street (categorically encoded street address)
    city (city name)
    state (state name)
    zip_code (postal code of the area)
    house_size (house area/size/living space in square feet)
    prev_sold_date (Previously sold date)
    
After cleaning the dataset by removing rows that include real estate entries without information about the number of bedrooms and bathrooms, we can use it to feed our model and evaluate its performance.

We chose this dataset for several reasons. It is quite large (178.86 MB) and comes from a reliable source. The data was collected from https://www.realtor.com/ — a real estate listing website operated by the News Corp subsidiary Move, Inc., based in Santa Clara, California. As of 2024, it is the second most visited real estate listing website in the United States, with over 100 million monthly active users. Additionally, it was created for observing correlations between real estate parameters and their prices, which aligns perfectly with the goals of our AI model.

However, the dataset has some significant flaws. It is available only for educational purposes, so we cannot sell it to our client. Furthermore, it lacks crucial information, such as the proximity of public transportation stations, and it is focused on American real estate, while we are primarily interested in Polish data.

