import decimal

guest = 2;
bill = 80;
tipPercentage = 10;

guestTip = decimal.Decimal(bill/guest * tipPercentage/100)
guestTip = round(guestTip, 2).normalize()
guestBill = round(decimal.Decimal(bill/guest), 2).normalize() + guestTip

print(f"Each guest needs to pay: " + str(guestBill)  + " euro")
print(f"The amount of tip for each guest is: " + str(guestTip) + " euro")