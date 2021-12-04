Github: https://github.com/HarmanG1/Assignment-10.1-Refrigerator-Class

Class Documentation
Refrigerator Class:
The refrigerator class implements some features of a modern refrigerator such as accessing the contents of the refrigerator, storing things inside the refrigerator, a smart shopping list,etc. The refrigerator also distinguishes between the fridge side and the freezer side for division of the contents. 

__shoppinglist:
This class attribute is a list that holds the names of the items in the refrigerator that run out when used.

self.__fridge
This data variable holds a dictionary of the contents of the fridge section of the refrigerator.

self.__freezer
This data variable holds a dictionary of the contents of the freezer section of the refrigerator.

 def __init__(self, fridict = None, freezdict = None):
This method is the initializer for all refrigerator objects. The method works with no input as it has default values for the two variables but if desired the arguments needed are two dictionaries. 
def get_fridge_contents(self):
 This method returns the self.__fridge variable. This method has no needed input.

def get_freezer_contents(self):
	This method returns the self.__freezer variable. This method has no needed input.

def set_fridge_contents(self,fridict):
This method sets the value of the self.__fridge variable. This method  requires the input of a dictionary.

 def set_freezer_contents(self,freezdict):
This method sets the value of the self.__freezer variable. This method  requires the input of a dictionary.

def get_shopping_list(self):
	This method returns the __shoppinglist variable. This method has no needed input.

def set_shopping_list(self,lis):
This method sets the value of the __shoppinglist variable. This method  requires the input of a list


def use_ingredients(self,fresh_ingredients, frozen_ingredients):
This method takes in two dictionaries of the ingredients and number of them taken out of the refrigerator and updates the fridge, freezer, and shopping list accordingly. This method takes in two dictionaries as input.

def add_groceries(self, fresh_groceries, frozen_groceries):
This method takes in two dictionaries of the groceries bought and the number of them put into the refrigerator and updates the fridge, freezer, and shopping list accordingly. This method takes in two dictionaries as input.

Demo Program Documentation
Description: 
This demo program utilizes the methods and variables of the refrigerator class to create a refrigerator object. The program starts by replacing the default empty values of the fridge and freezer with values using the various set methods and then displays it using get methods. The program then uses a list of freezer and fridge dictionaries to call the use_ingredient method and then uses get methods to display the new contents and shopping list. It then calls the add_groceries method and uses get methods to display the updated contents and shopping list.

Instructions:
Open program in desired environment.
Edit any values of the main function if desired to try out different food and drink combos inside the refrigerator.
Run the program and view the result.




