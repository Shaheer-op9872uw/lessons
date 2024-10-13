def hotel_cost(nights):
    return 140*nights

def plane_ride_cost(city):
    if "berlin" == city:
        return 189
    elif "Delhi" == city:
        return 498
    elif "nyc" == city:
        return 938
    elif "Mars" == city:
       return 900000
    
def rental_car_cost(days):
    if days>=7 :
        return 40*days - 50
    elif days>=3 :
        return 40*days - 20
    else:
        return 40*days
    
def trip_cost(city, days, speding_mpney):
    return rental_car_cost(days) + hotel_cost(days) + plane_ride_cost(city) + speding_mpney
print("Cost of car rental:", rental_car_cost(5))
print("cost of plane:", plane_ride_cost("nyc"))
print("cost of hotel room:", hotel_cost(7))
print("total cost of your very long and good trip is :",trip_cost("nyc", 7,500))
