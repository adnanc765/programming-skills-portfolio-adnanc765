#cost of each usb stick 
usb_stick_price= 6

#total amount of money the girl has
total_money= 50

#calculate the number of usb sticks she can buy
num_usb_sticks= total_money // usb_stick_price

#calculate the remaining money after buying usb sticks
remaining_money= total_money % usb_stick_price

#print the results
print(f"The girl can buy {num_usb_sticks} USB sticks.")
print(f"She will have ${remaining_money} left.")