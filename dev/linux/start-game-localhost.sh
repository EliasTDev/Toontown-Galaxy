#!/bin/sh
cd ../..

# Get the user input:
read -p "Username: " ttgUsername

# Export the environment variables:
export ttgUsername=$ttgUsername
export ttgPassword="password"
export TTG_PLAYCOOKIE=$ttgUsername
export TTG_GAMESERVER="127.0.0.1"

echo "==============================="
echo "Starting Toontown Galaxy"
echo "Username: $ttgUsername"
echo "Gameserver: $TTG_GAMESERVER"
echo "==============================="

python3.10 -m toontown.toonbase.ToontownStart
