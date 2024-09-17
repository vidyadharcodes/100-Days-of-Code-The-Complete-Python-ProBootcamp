states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland",
                     "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island",
                     "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois",
                     "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin",
                     "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado",
                     "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma",
                     "New Mexico", "Arizona", "Alaska", "Hawaii"]
length = len(states_of_america)
print(states_of_america[length - 1])

fruits = ["Cherry", "Apple", "Pear"]
veg = ["Cucumber", "Kale", "Spinach"]
fruits_and_veg = [fruits, veg] #Concatinate the two list into one group
#The list would look like this: [["Cherry", "Apple", "Pear"], ["Cucumber", "Kale", "Spinach"]]
print(fruits_and_veg)
print(fruits[-1])
print(fruits_and_veg[1][1])

# try out
print(fruits_and_veg[0])
print(fruits_and_veg[1])
# Observation -> It prints the index of the sublist , here both the list acts as a whole se of list
print(fruits_and_veg[1][2])
print(fruits_and_veg[0][1])
