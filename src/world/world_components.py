##---------------------------------------------##
## JJx World Builder [Python Edition]          ##
## Created By: Ryan Smith                      ##
##---------------------------------------------##
## World I/O Componenets                       ##
##---------------------------------------------##

## Imports
from typing import Union
import json, os.path as ospath, struct

## Constants
__location = ospath.abspath(ospath.join(ospath.dirname(__file__), "world_components.json"))

## Functions

##-------- Update Data --------##
def __Fix_JSON_Component(str_id: str, num_id: int) -> dict:
	'''Recieves a string and a numerical id and returns a value specific dictionary with the string, numerical id, and hexadecimal id (in little endian format) of the given data.'''
	return {
		'str_id' : str_id,
		'num_id' : num_id,
		'hex_id' : struct.pack('<h', num_id).hex().upper()
	}

def Update_JSON_Components(file_path: str) -> None:
	'''For updating world json data (items | entities) to current english.json game data. Called with a file path string to the english.json and outputs the updated syntax into "world_components.json" in this directory.'''
	## Get JSON Data
	with open(file_path, 'r', encoding = 'utf-8') as updating_file:
		update_data = json.load(updating_file)

	## Reconstruct Items
	items = [__Fix_JSON_Component(item['name'], item['id']) for item in update_data['treasures']]

	## Reconstruct Entities
	entities = [__Fix_JSON_Component(mob, i) for i, mob in enumerate(update_data['mobs'])]

	with open(__location, 'w') as updated_file:
		json.dump(
		{
			'item'   : items,
			'entity' : entities,
		}, updated_file, indent = 4)

##-------- Component Data --------##

def String_To_Hex(str_id: str, component_type: Union['item', 'entity']) -> hex:
	'''Takes in a component name string and a component type string and returns the component type's hex string.'''
	for component in world_components[component_type]:
		if str_id == component['str_id']:
			return component['hex_id']

def Hex_To_String(hex_id: Union[bytes, hex], component_type: Union['item', 'entity']) -> str:
	'''Takes in a byte string or hex string and a component type string and returns the component type's string name.'''
	if isinstance(hex_id, bytes):
		hex_id = hex_id.hex().upper()

	for component in world_components[component_type]:
		if hex_id == component['hex_id']:
			return component['str_id']

##-------- Entity Conversion --------##

def Create_Entity_List_From_ByteString(entity_list_bytestring: bytes) -> list:
	''''''
	pass

def Create_ByteString_From_Entity_List(entity_list: list) -> bytes:
	''''''
	pass

##-------- Chest Conversion --------##

def Create_Chest_List_From_ByteString(chest_list_bytestring: bytes) -> list:
	''''''
	pass

def Create_ByteString_From_Chest_List(chest_list: list) -> bytes:
	''''''
	pass

## Classes
class Item(object):
	pass
	# -Constructor
	def __init__(self):
		pass

	# -Dunder Methods

	# -Class Methods
	@classmethod
	def Create_From_ByteString(cls, bytestring: bytes, slot: int):
		''''''
		pass

	# -Static Methods

	# -Instance Methods
	def Translate_To_Dictionary(self) -> dict:
		''''''
		pass

	def Translate_To_ByteString(self) -> bytes:
		''''''
		pass

	# -Class Variables

class Entity(object):
	pass
	# -Constructor
	def __init__(self):
		pass

	# -Dunder Methods

	# -Class Methods
	@classmethod
	def Create_From_ByteString(cls, bytestring: bytes):
		''''''
		pass

	# -Static Methods

	# -Instance Methods
	def Translate_To_ByteString(self) -> bytes:
		''''''
		pass

	# -Class Variables

class Chest(object):
	pass
	# -Constructor
	def __init__(self):
		pass

	# -Dunder Methods

	# -Class Methods
	@classmethod
	def Create_From_ByteString(cls, bytestring: bytes):
		''''''
		pass

	# -Static Methods

	# -Instance Methods
	def Translate_To_ByteString(self) -> bytes:
		''''''
		pass

	# -Class Variables

## Main

## __Main__
if __name__ == "__main__":
	if ospath.exists("english.json"):
		print("Updating from english.json!")
		Update_JSON_Components("english.json")
	else:
		print("english.json not found!")
else:
	with open(__location, 'r') as component_data:
		world_components = json.load(component_data)

## Temporary