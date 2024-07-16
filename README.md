# MOPP

The main purpose of MOPP is calculating Twitch point bets odds for Kesha's League of Legends Twitch stream.  
After inputting an equation like "kills > enemy-kills", it shows the percentage of games this event happened in Kesha's match history.  
The name MOPP comes from Miapp + op.gg + Kesha's hair looks like a mop.

## How to Use

Put an equation in the field; it could be anything from the list. For the enemy laner (opposite lane of the player), add "enemy_" before the stat name.  
Remember to use logical operators like ==, <, >, <=, >=.  
To add recent games to the database, click on "refresh data". It might take a while if too many games are loading in because of rate limits. Check the command line for "loading finished".  
`and`, `or`, `()`, `+`, `*`, and other operations are also supported. Actually, anything Python goes, even whole scripts. It's really unsafe, so do not deploy it to the public lmao.

## Installation Guide

1. Install like any other Python Flask app with `requirements.txt`.
2. Make an account and generate a key at [Riot Developer Portal](https://developer.riotgames.com/) - this key lasts for 24 hours, regenerate if it expires.
3. Put it in `config.py`. You can also change the player here if you want (Kesha's account for streaming is default).
4. Run `main.py`.

![image](https://github.com/user-attachments/assets/16e39e09-b41d-48e2-9a6a-ef88f682d90f)
