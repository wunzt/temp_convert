# Author: Thomas Wunz
# GitHub username: wunzt
# Date: 4/5/2022
# Description: Asks the user to input a temperature in Celsius and prints the equivalent in Fahrenheit.

print("Please enter a Celsius temperature.")
temp_1 = float(input())
print("The equivalent Fahrenheit temperature is:")
print(temp_1 * (9 / 5) + 32) # in a more complex code, this might be better done by creating a method/function