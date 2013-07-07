"""
Place Blocks, a Minecraft structure creation tool which is part of Minekit
Copyright 2013 L. Mars, R. Pierick

This file is part of Minekit.

Minekit is free software: you can redistribute it and/or modify
it under the terms of the GNU General Public License as published by
the Free Software Foundation, either version 3 of the License, or
(at your option) any later version.

Minekit is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with Minekit.  If not, see <http://www.gnu.org/licenses/>.
"""

#!/usr/bin/env python
#import the minecraft.py module from the minecraft directory
import minecraft.minecraft as minecraft
#import minecraft block module
import minecraft.block as block
# Import `time` so that we can use delays
import time
# Import `sys` so that we can quit with an exit
import sys

# Global Variables

# Auxillary functions

def printchat(text):
    mc.postToChat(text)

def printcap(text):
    print(text)
    mc.postToChat(text)

#Checker functions

def validate_block_type(type_of_block):
    if (type_of_block >= -1  and  type_of_block <= 247):
        return type_of_block
    else:
        print("Whoops! Your block type was not recognized!")
        sys.exit(-1)

def validate_shape(obj_shape):
    if (obj_shape == "Tower" or obj_shape == "Cube" or obj_shape == "Box" or obj_shape == "Pyramid"):
        return obj_shape
    else:
        print("Whoops! Your shape was not recognized!")
        sys.exit(-1)

def validate_convert_yn(ynstr):
    if (ynstr == "y" or ynstr == "Y"):
        return True
    elif (ynstr == "n" or ynstr == "N"):
        return False
    else:
        print("Uh Oh, you tried to say something other than yes or no!")

def validate_size(obj_size, minsize, maxsize, sizeheight):
    if obj_size > maxsize:
        print("Do you really want to continue?")
        print("I take no responsibility whatsoever for any damage caused,")
        print("and indemnify myself from all legal action taken against me.")
        print("This could wipe out your whole world or crash your computer.")
        cont = validate_convert_yn(raw_input("Do you still want to continue (Y/N)?"))
        if cont == False:
            sys.exit(0)
        else:
            print("Do you really want to continue?")
            print("You heard me already!")
            cont = validate_convert_yn(raw_input("Continue (Y/N)?"))
            if cont == False:
                sys.exit(0)
            else:
                print("OK, I'll do it...")
                return obj_size
    elif obj_size < minsize:
        print("Sorry, the " + sizeheight + " can't be less than " + minsize)
    else:
        return obj_size

# Shape creation routines!

def do_tower():
    print("Please enter the height of the tower.")
    tower_height = validate_size(int(raw_input("Height? ")), -40, 40, "height")
    time.sleep(0.5)
    print("Creating a tower of block type " + str(block_type))
    print("Quick, get back to the game!")
    print("I'll give you 5 seconds...")
    time.sleep(5)
    printcap("5 seconds is up!")
    time.sleep(0.25)
    playerPos = mc.player.getPos()
    printcap("Your location is " + str(playerPos.x) + str(playerPos.y) + str(playerPos.z))
    time.sleep(0.25)
    printcap("Create blocks - making a block type " + str(block_type) + " tower")
    for up in range(0, tower_height):
            mc.setBlock(playerPos.x, playerPos.y + up, playerPos.z, block.Block(block_type))
    printcap("Done!")
    sys.exit(0)

def do_cube():
    print("Please enter the size of the cube.")
    cube_size = validate_size(int(raw_input("Size? ")), 1, 20, "size")
    cube_hollow = validate_convert_yn(raw_input("Do you want a hollow cube (Y/N)? "))
    time.sleep(0.5)
    print("Creating a cube of block type " + str(block_type))
    print("Quick, get back to the game!")
    print("I'll give you 5 seconds...")
    time.sleep(5)
    printcap("5 seconds is up!")
    time.sleep(0.25)
    playerPos = mc.player.getPos()
    printcap("Your location is " + str(playerPos.x) + str(playerPos.y) + str(playerPos.z))
    time.sleep(0.25)
    printcap("Create blocks - making a block type " + str(block_type) + " cube")
    count = 1
    if not cube_hollow:
        for x in range(0, cube_size):
            for y in range(0, cube_size):
                for z in range(0, cube_size):
                    print("[" + str(count) + "] " + str(x) + " " + str(y) + " " + str(z))
                    mc.setBlock(playerPos.x + 1 + x, playerPos.y + y, playerPos.z + z, block.Block(block_type))
                    count = count + 1
    else:
        for x in range(0, cube_size):
            for y in range(0, cube_size):
                for z in range(0, cube_size):
                    if (x == 0 or x == cube_size - 1) or (y == 0 or y == cube_size - 1) or (z == 0 or z == cube_size - 1):
                        print("[" + str(count) + "] " + str(x) + " " + str(y) + " " + str(z))
                        mc.setBlock(playerPos.x + 1 + x, playerPos.y + y, playerPos.z + z, block.Block(block_type))
                        count = count + 1
    printcap("Done!")
    sys.exit(0)

def do_box():
    print("Please enter the dimensions of the box.")
    xrad = validate_size(int(raw_input("Enter cube x: ")), 1, 30, "x size")
    yrad = validate_size(int(raw_input("Enter cube y: ")), 1, 30, "y size")
    zrad = validate_size(int(raw_input("Enter cube z: ")), 1, 30, "z size")
    box_hollow = validate_convert_yn(raw_input("Do you want a hollow box (Y/N)? "))
    time.sleep(0.5)
    print("Creating a box of block type " + str(block_type))
    print("Quick, get back to the game!")
    print("I'll give you 5 seconds...")
    time.sleep(5)
    printcap("5 seconds is up!")
    time.sleep(0.25)
    playerPos = mc.player.getPos()
    printcap("Your location is " + str(playerPos.x) + str(playerPos.y) + str(playerPos.z))
    time.sleep(0.25)
    printcap("Create blocks - making a block type " + str(block_type) + " box")
    count = 1
    if not box_hollow:
        for x in range(0, xrad):
            for y in range(0, zrad):
                for z in range(0, yrad):
                    print("[" + str(count) + "] " + str(x) + " " + str(y) + " " + str(z))
                    mc.setBlock(playerPos.x + 1 + x, playerPos.y + y, playerPos.z + z, block.Block(block_type))
                    count = count + 1
    else:
        for x in range(0, xrad):
            for y in range(0, zrad):
                for z in range(0, yrad):
                    if (x == 0 or x == xrad-1) or (y == 0 or y == zrad-1) or (z == 0 or z == yrad-1):
                        print("[" + str(count) + "] " + str(x) + " " + str(y) + " " + str(z))
                        mc.setBlock(playerPos.x + 1 + x, playerPos.y + y, playerPos.z + z, block.Block(block_type))
                        count = count + 1
    printcap("Done!")
    sys.exit(0)

def do_pyramid():
    print("Please enter the dimensions of the pyramid.")
    blen = validate_size(int(raw_input("Enter pyramid base length: ")), 1, 30, "x size")
    pyr_hollow = validate_convert_yn(raw_input("Do you want a hollow pyramid (Y/N)? "))
    if pyr_hollow:
        pyr_closed = validate_convert_yn(raw_input("Do you want the hollow pyramid to be closed (Y/N)? "))
    time.sleep(0.5)
    print("Creating a pyramid of block type " + str(block_type))
    print("Quick, get back to the game!")
    print("I'll give you 5 seconds...")
    time.sleep(5)
    printcap("5 seconds is up!")
    time.sleep(0.25)
    playerPos = mc.player.getPos()
    printcap("Your location is " + str(playerPos.x) + str(playerPos.y) + str(playerPos.z))
    time.sleep(0.25)
    printcap("Create blocks - making a block type " + str(block_type) + " pyramid")
    count = 1
    pyrx = playerPos.x
    pyry = playerPos.z
    pyrz = playerPos.y
    pyrxoff = 0
    pyryoff = 0
    pyrzoff = 0
    pyrcont = True
    if not pyr_hollow:
        while pyrcont:
            #plane(x + pyrxoff, y + pyryoff, z + pyrzoff, blen, blen)
            for plx in range(0, blen):
                for ply in range(0, blen):
                    mc.setBlock(pyrx + plx + pyrxoff + 1, pyrzoff + pyrz, pyry + ply + pyryoff, block.Block(block_type))
                    count +=1
                    print(str(count) + " ; " + str(plx + pyrxoff) + " " + str(ply + pyryoff) + " " + str(pyrzoff))

            pyrxoff += 1
            pyryoff += 1
            pyrzoff += 1
            blen -= 2

            if blen <= 0:
                pyrcont == False
                print("pyrcontified")
                break
    else:
        while pyrcont:
            #plane(x + pyrxoff, y + pyryoff, z + pyrzoff, blen, blen)
            for plx in range(0, blen):
                for ply in range(0, blen):
                    #print(blen)
                    if ((plx == 0 or plx == blen - 1) or (ply == 0 or ply == blen - 1)) and not pyr_closed:
                        mc.setBlock(pyrx + plx + pyrxoff + 1, pyrzoff + pyrz, pyry + ply + pyryoff, block.Block(block_type))
                        count +=1
                        print(str(count) + " ; " + str(plx + pyrxoff) + " " + str(ply + pyryoff) + " " + str(pyrzoff))
                    elif pyr_closed:
                        if pyrzoff == 0:
                            mc.setBlock(pyrx + plx + pyrxoff + 1, pyrzoff + pyrz, pyry + ply + pyryoff, block.Block(block_type))
                            count +=1
                            print(str(count) + " ; " + str(plx + pyrxoff) + " " + str(ply + pyryoff) + " " + str(pyrzoff))
                        elif pyrzoff != 0:
                            if ((plx == 0 or plx == blen - 1) or (ply == 0 or ply == blen - 1)):
                                mc.setBlock(pyrx + plx + pyrxoff + 1, pyrzoff + pyrz, pyry + ply + pyryoff, block.Block(block_type))
                                count +=1
                                print(str(count) + " ; " + str(plx + pyrxoff) + " " + str(ply + pyryoff) + " " + str(pyrzoff))

                            

            pyrxoff += 1
            pyryoff += 1
            pyrzoff += 1
            blen -= 2
            if blen <= 0:
                pyrcont == False
                print("pyrcontified")
                break

def do_shifted_pyramid():
    print("Please enter the dimensions of the pyramid.")
    blen = validate_size(int(raw_input("Enter pyramid base length: ")), 1, 30, "x size")
    pyr_hollow = validate_convert_yn(raw_input("Do you want a hollow pyramid (Y/N)? "))
    if pyr_hollow:
        pyr_closed = validate_convert_yn(raw_input("Do you want the hollow pyramid to be closed (Y/N)? "))
    time.sleep(0.5)
    print("Creating a pyramid of block type " + str(block_type))
    print("Quick, get back to the game!")
    print("I'll give you 5 seconds...")
    time.sleep(5)
    printcap("5 seconds is up!")
    time.sleep(0.25)
    playerPos = mc.player.getPos()
    printcap("Your location is " + str(playerPos.x) + str(playerPos.y) + str(playerPos.z))
    time.sleep(0.25)
    printcap("Create blocks - making a block type " + str(block_type) + " pyramid")
    count = 1
    pyrx = playerPos.x
    pyry = playerPos.z
    pyrz = playerPos.y
    pyrxoff = 0
    pyryoff = 0
    pyrzoff = 0
    pyrcont = True
    if not pyr_hollow:
        while pyrcont:
            #plane(x + pyrxoff, y + pyryoff, z + pyrzoff, blen, blen)
            for plx in range(0, blen):
                for ply in range(0, blen):
                    mc.setBlock(pyrx + plx + pyrxoff + 1, pyrzoff + pyrz, pyry + ply + pyryoff, block.Block(block_type))
                    count +=1
                    print(str(count) + " ; " + str(plx + pyrxoff) + " " + str(ply + pyryoff) + " " + str(pyrzoff))

            #pyrxoff += 1
            #pyryoff += 1
            pyrzoff += 1
            blen -= 1

            if blen <= 0:
                pyrcont == False
                print("pyrcontified")
                break
    else:
        while pyrcont:
            #plane(x + pyrxoff, y + pyryoff, z + pyrzoff, blen, blen)
            for plx in range(0, blen):
                for ply in range(0, blen):
                    #print(blen)
                    if ((plx == 0 or plx == blen - 1) or (ply == 0 or ply == blen - 1)) and not pyr_closed:
                        mc.setBlock(pyrx + plx + pyrxoff + 1, pyrzoff + pyrz, pyry + ply + pyryoff, block.Block(block_type))
                        count +=1
                        print(str(count) + " ; " + str(plx + pyrxoff) + " " + str(ply + pyryoff) + " " + str(pyrzoff))
                    elif pyr_closed:
                        if pyrzoff == 0:
                            mc.setBlock(pyrx + plx + pyrxoff + 1, pyrzoff + pyrz, pyry + ply + pyryoff, block.Block(block_type))
                            count +=1
                            print(str(count) + " ; " + str(plx + pyrxoff) + " " + str(ply + pyryoff) + " " + str(pyrzoff))
                        elif pyrzoff != 0:
                            if ((plx == 0 or plx == blen - 1) or (ply == 0 or ply == blen - 1)):
                                mc.setBlock(pyrx + plx + pyrxoff + 1, pyrzoff + pyrz, pyry + ply + pyryoff, block.Block(block_type))
                                count +=1
                                print(str(count) + " ; " + str(plx + pyrxoff) + " " + str(ply + pyryoff) + " " + str(pyrzoff))

                            

            #pyrxoff += 1
            #pyryoff += 1
            pyrzoff += 1
            blen -= 1
            if blen <= 0:
                pyrcont == False
                print("pyrcontified")
                break

print("***Place Blocks 0.2.2*****")
print("***Written by L.Mars,*****")
print("**With help from Rowen P.*")

time.sleep(1)

print("")
print("")

print("Trying to connect to Minecraft...")
try:
    mc = minecraft.Minecraft.create()
except:
    print("Sorry, I think you forgot to open a Minecraft world (or open Minecraft)...")
    print("I'm quitting, so go start Minecraft and try again!")
    raise
print("Connected to Minecraft!")

time.sleep(0.25)

print("You must now enter the block type number.")
print("Some common block types are:")
print("Air = 0")
print("Stone = 1")
print("Grass = 2")
print("Dirt = 3")
print("Cobblestone = 4")
print("Wood Planks = 5")
print("Sapling = 6")
print("Bedrock = 7")
print("Water = 8")
print("Still Water = 9")
print("Lava = 10")
print("Still Lava = 11")
print("Sand = 12")
print("Gravel = 13")
print("Wood = 17")
print("Glass = 20")
print("Majestic Butter!!! = 41")
print("Brick = 45")
print("Boom Boom!!! = 46")
print("Moss Stone = 48")
#No support...[sigh]
#print("Fire = 51")
print("Plain Old Diamond = 57")

block_type = validate_block_type(int(raw_input("Enter Choice: ")))

if block_type == -1:
    print("Settings")
    settings_dialog()
    sys.exit

print("Now you must enter the shape that you vant.")
print("The shape must be one of the following:")
print("Tower")
print("Cube")
print("Box")
print("Pyramid")
print("Pyramid-Shifted")

object_shape = raw_input("Shape: ")

if object_shape == "Tower":
    do_tower()
elif object_shape == "Cube":
    do_cube()
elif object_shape == "Box":
    do_box()
elif object_shape == "Pyramid":
    do_pyramid()
elif object_shape == "Pyramid-Shifted":
    do_shifted_pyramid()
else:
    print("Whoops! Your shape was not recognized!")
    sys.exit(-1)
