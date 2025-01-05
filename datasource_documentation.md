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
    
After cleaning dataset from rows that include real estates without informations about number of beds and bathrooms we can use it to fed our model to check it's performance. 
We choose this dataset because of few reasons. It is quite big (178.86 MB) and comes from relaiable source Data was collected from https://www.realtor.com/ - A real estate listing website operated by the News Corp subsidiary Move, Inc. and based in Santa Clara, California. It is the second most visited real estate listing website in the United States as of 2024, with over 100 million monthly active users. Additionaly it was made for obserwing correlation between parameters of the real estate and its price and that is exactly what our AI model will do.
But it has some fatal flow. It is avaliable only for education purposes so we can't sell it to our client. Futhermore it does not mention few important things like closest public comunication station and is located in America and we are interested in polish data. 

