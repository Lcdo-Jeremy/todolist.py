import json

class GroceryList:

  def __init__(self):
    self.items = []
    self.load_list()

  def load_list(self):
    try:
      with open("grocery_list.json", "r") as file:
        self.items = json.load(file)
    except FileNotFoundError:
      self.items = []

  def save_list(self):
    with open("grocery_list.json", "w") as file:
      json.dump(self.items, file)

  def add_item(self, item):
    if len(self.items) == 10:
      raise ValueError(
        "¡La lista ya tiene 10 elementos! No se pueden agregar más.")
    if item in self.items:
      print(f"'{item}' ya está en la lista de compras.")
    else:
      self.items.append(item)
      self.save_list()
      print(f"Se ha agregado '{item}' a la lista de compras.")

  def remove_item(self, item):
    if len(self.items) == 0:
      print("La lista de compras está vacía.")
    else:
      if len(self.items) == 10:
        raise ValueError(
          "La lista tiene 10 elementos. No se pueden eliminar más elementos.")
      if item in self.items:
        self.items.remove(item)
        self.save_list()
        print(f"Se ha eliminado '{item}' de la lista de compras.")
      else:
        print(f"No se encontró '{item}' en la lista de compras.")

  def modify_item(self, item, new_item):
    if item in self.items:
      index = self.items.index(item)
      self.items[index] = new_item
      self.save_list()
      print(
        f"Se ha modificado '{item}' a '{new_item}' en la lista de compras.")
    else:
      print(f"No se encontró '{item}' en la lista de compras.")

  def print_list(self):
    if len(self.items) == 0:
      print("La lista de compras está vacía.")
    else:
      print("Lista de compras:")
      for index, item in enumerate(self.items, start=1):
        print(f"{index}. {item}")


# Ejemplo de uso
my_grocery_list = GroceryList()
#my_grocery_list.add_item("Leche")
#my_grocery_list.add_item("Manzanas")
#my_grocery_list.add_item("Leche")
my_grocery_list.print_list()