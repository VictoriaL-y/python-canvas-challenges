import decimal

guest = 2;
bill = 80;
tipPercentage = 10;

guestTip = decimal.Decimal(bill/guest * tipPercentage/100) # I use decimal, because otherwise the result of calculationg will be a float.
# With float numbers I can't use "round" and "normalize" functions, but with decimal - I can
# Here I am rounding with "round" the number to the second digit after the decimal point
guestTip = round(guestTip, 2).normalize() # "normalize" is for removing extra zeros after the decimal point
guestBill = round(decimal.Decimal(bill/guest), 2).normalize() + guestTip

print(f"Each guest needs to pay: " + str(guestBill)  + " euro")
print(f"The amount of tip for each guest is: " + str(guestTip) + " euro")