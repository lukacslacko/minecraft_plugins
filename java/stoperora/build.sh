#!/bin/bash
javac Stopper.java -cp /home/minecraft/spigot-1.13.2.jar
jar -cf Stopper.jar Stopper.class plugin.yml
cp Stopper.jar /home/minecraft/plugins/
