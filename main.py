import pandas

# Read data to variable
data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")





colors = ["Gray", "Cinnamon", "Black"]
for color in colors:
    color_count = len(data[data["Primary Fur Color"] == color])
    print(color_count)
    with open("temp_file.txt", "a") as file:
        file.write(str(color_count))
        file.write("\n")

Black = len(data[data["Primary Fur Color"] == "Black"])
Cinnamon = len(data[data["Primary Fur Color"] == "Cinnamon"])
Gray = len(data[data["Primary Fur Color"] == "Gray"])

data_dict = {
    "Fur Color" : ["Gray", "Cinnamon", "Black,"],
    "Count": [Gray, Cinnamon, Black]
}

#Now convert to dataframe for pandas to handle
df = pandas.DataFrame(data_dict)

#Convert to csv using pandas
df.to_csv("Squirrel_Color_count.csv")
print(data_dict)


