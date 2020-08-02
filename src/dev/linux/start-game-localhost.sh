#!/bin/sh
cd ..
cd ..
export PYTHONPATH=dependencies/linux:$PYTHONPATH
# Get the user input:
read -p "Username: " tteUsername

# Export the environment variables:
export tteUsername=$tteUsername
export ttePassword="password"
export TTE_PLAYCOOKIE=$tteUsername
export TTE_GAMESERVER="127.0.0.1"

echo "==============================="
echo "Starting Toontown Galaxy"
echo "Username: $tteUsername"
echo "Gameserver: $TTE_GAMESERVER"
echo "==============================="

/usr/bin/python2 -m toontown.toonbase.ClientStart
