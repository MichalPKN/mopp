# MOPP
Main purpose is calculating twitch point bets odds for kesha's league of legends twitch stream.  
After inputting an equation like "kills > enemy-kills", it shows the percentage of games this event happened in a player's match history.  
The name mopp comes from miapp + op.gg + kesha's hair looks like a mop.
## How to use
Put an equasion in the field, could be anything from the list, for enemy laner (oposit lane of the player) add "enemy_" before stat name.  
Remember to use logical operators like ==, <, >, <=, >=  
To add recent games in the database click on "refresh data", might take a while if too many games are loading in because of rate limits, check the command line for "loading finished".  
and, or, (), +, *, and other stuff is also supported, actualy anything python goes, even whole scripts, it's really unsafe do not deploy it to public lmao
## Instalation guide
1. install like any other python flask app with requirements.txt
2. make an account and generate a key at [Riot Developer Portal](https://developer.riotgames.com/) - this key lasts for 24 hours, regenerate if expires
3. put it config.py, you can also change the player here if you want (kesha's account for streaming is default)
4. run main.py

![image](https://github.com/user-attachments/assets/16e39e09-b41d-48e2-9a6a-ef88f682d90f)
