##---------------------------------------------##
## JJx World Builder [Python Edition]          ##
## Created By: Ryan Smith                      ##
##---------------------------------------------##
## World I/O                                   ##
##---------------------------------------------##

## Imports
from typing import Tuple, BinaryIO, TypeVar

import struct, gzip, zlib, io

if __name__ == "__main__":
	import world_components
else:
	from . import world_components

## Constants
jjx_map_header = b'\x4A\x4A\x58\x4D\x01\x00\x13\x00\x00\x00\x00\x00\x01\x00\x00\x00\xF0\x00\x00\x00\xE0\x00\x00\x00\x04\x00\x00\x00\xD0\x01\x00\x00'
jjx_adv_header = b'\x4A\x4A\x58\x4D\x02\x00\x02\x00\x00\x00\x00\x00\x01\x00\x00\x00\x24\x00\x00\x00\xE0\x00\x00\x00\x14\x00\x00\x00\x04\x01\x00\x00'

## Functions

##-------- Retrieve World Data --------##

def Import_World(file_path: str) -> Tuple[dict, bytes]:
	'''
	Returns a dictionary of the world properties and a bytestring of the decompressed world.'''
	with open(file_path, 'rb') as importing_world:
		file_header = importing_world.read(32)

		# -Single World Import
		if (file_header == jjx_map_header):
			print("Single-World Import")

			return Decompress_World_File(importing_world, debug_text = True)

		# -Adventure Worlds Import
		elif (file_header == jjx_adv_header):
			print("Multi-World Import")

		# -Invalid World Format
		else:
			print("Invalid World Format.")
			return None

def Decompress_World_File(world_file_object: BinaryIO, **kwargs) -> Tuple[dict, bytes]:
	'''
	Returns a dictionary of the world properties and a bytestring of the decompressed world.
	If debug mode is enabled, will return world properties, decompressed world, full header, and full footer.'''

	## Header Data
	world_file_object.seek(40, 0)
	header_size_numerical = struct.unpack('<i', world_file_object.read(4))[0]
	world_size_numerical = struct.unpack('<i', world_file_object.read(4))[0]
	gamemode_type = world_file_object.read(4)
	footer_location = struct.unpack('<i', world_file_object.read(4))[0]

		# -Gamemode Handler
	if gamemode_type == b'\x12\x00\x00\x00' or gamemode_type == b'\x00\x00\x00\x00': # -Creative / Flat || Auto
		pass
		# -Discover Footer Segment Null
		discover_footer_size_numerical = None
		discover_footer_location = None
		chest_location = struct.unpack('<i', world_file_object.read(4))[0]
		chest_size_numerical = struct.unpack('<i', world_file_object.read(4))[0]
		entity_location = struct.unpack('<i', world_file_object.read(4))[0]
		entity_size_numerical = struct.unpack('<i', world_file_object.read(4))[0]

	elif gamemode_type == b'\x03\x00\x00\x01': # -Adventure / Survival
		pass
		# -Discover Footer Segment Set
		discover_footer_size_numerical = struct.unpack('<i', world_file_object.read(4))[0]
		discover_footer_location = footer_location
		world_file_object.seek(4, 1)
		footer_location = struct.unpack('<i', world_file_object.read(4))[0]

	#print(world_file_object.read(4)) # -Read 4 bytes - check position


	## Properties Data

	## Decompressed Data

	## Footer Data

	## Debug
		# -Debug Mode

		# -Debug Text
	if 'debug_text' in kwargs and kwargs['debug_text'] == True:
		print(f"Header Size: {header_size_numerical} bytes.")
		print(f"World Size: {world_size_numerical} bytes.")
		if discover_footer_location:
			print(f"Discover Footer Location: {discover_footer_location}.")
			print(f"Discover Footer Size: {discover_footer_size_numerical} bytes")
		print(f"Footer Location: {footer_location}.")
		print(f"Footer Data:\n\tChest Location: {chest_location}\n\tChest Size: {chest_size_numerical}\n\tEntity Location:{entity_location}\n\tEntity Size:{entity_size_numerical}")


	#return world_size_numerical

def Decompress_World_Properties(*args, **kwargs) -> dict:
	'''
	Returns a dictionary of the world properties.'''

	"""
	World Name
	World Size
	Skybox Offset
	Planet
	Spawn Position
	Player Position
	Gamemode
	Chest Data
	Entity Data
	Weather Data
	Time Data
	"""
	pass

##-------- Store World Data --------##

def Export_World(world_properties: dict, decompressed_world: bytes, folder_path: str) -> None:
	'''
	Returns none, but writes the compressed file format to the folder path given.'''
	export_world_data = Compress_World(world_properties, decompressed_world)

	with open(folder_path, 'wb') as export_world:
		export_world.write(export_world_data)

def Compress_World(world_properties: dict, decompressed_world: bytes) -> bytes:
	'''
	Returns a bytestring of the compressed world.'''
	pass

## Main

## Temporary
data = Import_World("debug/[B-Data] Wooden Chest-O.dat")

print(data)