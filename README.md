# Minecraft Settlement Generation AI

## Introduction 
Welcome to our Minecraft Settlement Generation AI project! 
This was a project worked on by Michael Ward & Blake Patterson as a final project for Temple CIS 5603 during the semester of Spring 2022. 
The project itself is a Python script capable of building a settlement at any specified point in any Minecraft world, all while adapting to the environment around it in the most natural way possible. 

## Installation
Installation of this project can be broken into the following three main segments

### 1. Install Minecraft
The first step is to simply install Minecraft Java Edition. 
This can be done by going to the [Minecraft Download Page](https://www.minecraft.net/en-us/download) & installing the version corresponding to your given operating system. 

### 2. Install the Interface Mod
This project makes use of the [Generative Design Minecraft Challenge (GDMC) HTTP Interface](https://github.com/nilsgawlik/gdmc_http_interface) mod in order to communicate between Python & Minecraft using HTTP requests. 
This simply requires the installation of [Forge version 1.16.5-36.1.0](https://files.minecraftforge.net/net/minecraftforge/forge/index_1.16.5.html) (a popular framework for using mods in Minecraft), the GDMC mod itself, and some basic setup steps. 
For the full instructions go [here](https://github.com/nilsgawlik/gdmc_http_interface/wiki/Installation).

### 3. Install the Python Client
Finally, this project makes use of the [Generative Design Python Client (GDPC)](https://github.com/nilsgawlik/gdmc_http_client_python) (developed by the same group who made the mod) in order to steamline the process of making the necessary HTTP requests. 
This can be done by running the following command in your terminal:

    python3 -m pip install gdpc


## Usage
With each of the three necessary components installed, all that is left is to run the project. 
To get the project on your local system, follow one of these steps:
1. Clone this repository: 

        git clone https://github.com/BlakePatterson/CIS-5603-Minecraft-Settlement-Generation-AI.git
3. Download this repository: Click the green "Code" button in the button in the top right & then click "Download ZIP"

With the repository on your local machine, navigate to it using a terminal. 
Once in the repository folder, navigate into the folder where the script is stored using the following command:

    cd temple_mc_ai 
    
As one final step before the script is executed, a Minecraft world must be up and running on your local machine for the script to work. 
Simply open Minecraft, launch the version containing the mods installed prior, and create/open a world. 
With a Minecraft world open & a terminal opened to the necessary folder, the script can simply be run using the following command:

    python temple_mc_ai.py

### Arguments
There are multiple different optional arguments which can be passed to the script in order to alter how it executes
- -p: Takes no additional parameters & uses the player's location as a center point for the build area
- -c: Takes 6 required integer parameters representing a pair of x, y, and z coordinates & uses the specified coordinates as the bounds for the build area 
- -d: Takes no additional parameters & uses the default build area (a 128x128 area starting at x=0 & z=0)
- -t: Takes no additional parameters & will clear all trees & grass in the specified build area prior to placing any structures
- -r: Takes one required integer parameter representing a radius in # of blocks & uses the specified radius as the radius of the build area (default is 128 blocks). 
