#!/bin/bash
cp helper.java helper2.java
javac Eval.java helper2.java -cp /home/minecraft/spigot-1.13.2.jar
jar -cf Eval.jar Eval.class helper2.class plugin.yml
cp Eval.jar /home/minecraft/plugins/
