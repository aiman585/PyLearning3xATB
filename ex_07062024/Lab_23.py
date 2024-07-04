# List - Shopping List
# milk, bread, butter, poha
# 1. Add item
# 2. Remove item
# 3. Update item
# 4. View item
# 5. Exit


shopping_list = ["milk", "bread", "butter", "poha"]
print(shopping_list)
print(len(shopping_list))
print(shopping_list[0])
print(shopping_list[-1])

shopping_list.append("Curd") # append-> Add the item in the end
print(shopping_list)
shopping_list.insert(3,'jam') # insert -> Add items in the middle
print(shopping_list)

shopping_list.extend(["chips", "salt"]) #Add multiple items in the end
print(shopping_list)

shopping_list.remove("bread") # remove -> remove the item
print(shopping_list.pop())
print(shopping_list.index("butter"))
shopping_list.reverse()
shopping_list.sort()
print(shopping_list)
shopping_list[0]="Aiman"
print(shopping_list)


#my_list = [1, 2, 3, 4, True, 3.14, "Aiman"]
#print(type(my_list)) # <class 'list'>
