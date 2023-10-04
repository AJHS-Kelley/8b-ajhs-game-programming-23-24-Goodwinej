# ADDING ITEMS
playerInventory = []
while  len(playerInventory)<10:
    item = input("What would you like to add?\n")
    playerInventory.append(item) # .append() adds to END of List.
playerInventory.sort()
# .whatever() is known as a METHOD. It means "do this to that".
print(playerInventory)

# REMOVE ITEMS
while  len(playerInventory) > 5:
    item = input("What would you like to remove?\n")
    playerInventory.remove(item)
playerInventory.sort()     