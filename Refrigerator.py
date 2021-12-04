#Harman Gidha
#Assignment 10.1: Your Own Class
#Program implements a refrigerator class with various features

#Class models some features of a real life refrigerator 
class refrigerator():
    #Smart shopping list keeps track of items that run out
    __shoppinglist = []
    #Initalizes function with some default values
    def __init__(self, fridict = None, freezdict = None):
        self.__fridge = fridict
        self.__freezer = freezdict
    #Function returns the fridge content dictionary 
    def get_fridge_contents(self):
        return self.__fridge
    #Function returns the freezer content dictionary 
    def get_freezer_contents(self):
        return self.__freezer
    #Function sets the fridge content dictionary 
    def set_fridge_contents(self,fridict):
        self.__fridge = fridict
    #Function sets the freezer content dictionary
    def set_freezer_contents(self,freezdict):
        self.__freezer = freezdict
    #Function returns the shopping list
    def get_shopping_list(self):
        return self.__shoppinglist
    #Function sets the shopping list
    def set_shopping_list(self,lis):
        self.__shoppinglist = lis
    #Function takes in two dictionaries of the ingredients and number of them taken out of the refrigerator and updates the fridge, freezer, and shopping list accordingly 
    def use_ingredients(self,fresh_ingredients, frozen_ingredients):
        #Iterates through the fresh ingredients being used from the fridge
        for i in fresh_ingredients:
            #Checks if the ingredient is found 
            try:
                #Checks if there is enough of the ingredient
                if(fresh_ingredients[i] > self.__fridge[i]):
                    print(f"Not enough {i} in fridge!")
                    continue
                else:
                    #Updates the remaining number of the ingredient
                    self.__fridge.update({i:(self.__fridge[i] - fresh_ingredients[i])})
                    #Checks if the ingredient has run out and updates the shopping list
                    if self.__fridge[i] == 0:
                        self.__shoppinglist.append(i)
            except KeyError:
                print(f"{i} not found in fridge!")
        #Iterates through the frozen ingredients being used from the fridge
        for i in frozen_ingredients:
            #Checks if the ingredient is found
            try:
                #Checks if there is enough of the ingredient
                if(frozen_ingredients[i] > self.__freezer[i]):
                    print(f"Not enough {i} in freezer!")
                    continue
                else:
                    #Updates the remaining number of the ingredient
                    self.__freezer.update({i:self.__freezer[i] - frozen_ingredients[i]})
                    #Checks if the ingredient has run out and updates the shopping list
                    if self.__freezer[i] == 0:
                        self.__shoppinglist.append(i)
            except KeyError:
                print(f"{i} not found in freezer!")
    #Function takes in two dictionaries of the groceries bought and the number of them put into the refrigerator and updates the fridge, freezer, and shopping list accordingly
    def add_groceries(self, fresh_groceries, frozen_groceries): 
        #Checks if it is a preexisting item
        for p in fresh_groceries:
            flag = True
            try:
                self.__fridge[p]
            except KeyError:
                flag = False
            #If the item already exists it adds the current number to the new number
            if flag == True:
                self.__fridge.update({p:(fresh_groceries[p] + self.__fridge[p])})
            #If new item then creates new key value pair
            elif flag == False:
                self.__fridge.update({p:fresh_groceries[p]})
            #Checks if the new groceries are a part of the shopping list
            try:
                self.__shoppinglist.pop(self.__shoppinglist.index(p))
            except IndexError:
                continue
            except ValueError:
                continue
        #Checks if it is a preexisting item
        for p in frozen_groceries:
            flag = True
            try:
                self.__freezer[p]
            except KeyError:
                flag = False
            #If the item already exists it adds the current number to the new number
            if flag == True:
                self.__freezer.update({p:frozen_groceries[p] + self.__freezer[p]})
            #If new item then creates new key value pair
            elif flag == False:
                self.__freezer.update({p:frozen_groceries[p]})
            #Checks if the new groceries are a part of the shopping list
            try:
                self.__shoppinglist.pop(self.__shoppinglist.index(p))
            except IndexError:
                continue
            except ValueError:
                continue
    
        
#Main function utalizes the features of the class
def main():
    #Creates new refrigerator object
    jerry = refrigerator()
    #Creates a dictionary of fridge contents and updates the default empty fridge
    fridge_contents = {"Milk": 3, "Eggs": 12, "Coke": 6, "Strawberries": 15, "Potato": 25}
    jerry.set_fridge_contents(fridge_contents)
    #Prints the current fridge contents
    print(f"Fridge contents and amounts: {jerry.get_fridge_contents()}")
    #Creates a dictionary of freezer contents and updates the default empty freezer
    freezer_contents = {"Choclate Ice Cream": 1, "Chicken Tendies": 5, "Pizza": 2, "Fries": 1, "Sausages": 5}
    jerry.set_freezer_contents(freezer_contents)
    #Prints the current freezer contents
    print(f"Freezer contents and amounts: {jerry.get_freezer_contents()}")
    
    #Creates a dictionary of ingredients needed to make a meal
    breakfast_fresh = {"Milk": 0.5, "Eggs": 12, "Potato": 3}
    breakfast_frozen = {"Sausages": 5}
    #Calls the use ingredients method
    jerry.use_ingredients(breakfast_fresh,breakfast_frozen)
    #Prints the updated fridge and freezer contents after ingredient use
    print(f"Updated Fridge after cooking: {jerry.get_fridge_contents()}")
    print(f"Updated Freezer after cooking: {jerry.get_freezer_contents()}")

    #Prints the current shopping list after the ingredient use
    print(f"Shopping list: {jerry.get_shopping_list()}")
    
    #Creates a dictionary of groceries to add to the fridge
    fresh_grocerie_list = {"Cheese": 64, "Bacon": 12, "Eggs": 12}
    frozen_grocerie_list = {"Pizza": 1, "Sausages": 10, "Hashbrowns": 2}
    #Calls the add groceries method 
    jerry.add_groceries(fresh_grocerie_list,frozen_grocerie_list)
    #Prints the updated fridge and freezer contents after getting groceries
    print(f"Updated Fridge after going shopping: {jerry.get_fridge_contents()}")
    print(f"Updated Freezer after going shopping: {jerry.get_freezer_contents()}")

    #Prints the current shopping list after the grocerie purchase
    print(f"Updated shopping list: {jerry.get_shopping_list()}")


#Calls main method when program is run
if __name__ == "__main__":
    main()