#script that asks user about current weather conditions and provides clothing recommendations based on the input

#prompt for weather input
current_weather = str(input("What's the weather like today? (sunny/rainy/cold): "))

#recommendations
if current_weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif current_weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif current_weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")
