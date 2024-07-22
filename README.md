# MOPP

Calculator for Twitch point bets odds for Kesha's League of Legends Twitch stream. Can be modified to calculate other acounts' stats.
After inputting an equation like "kills > enemy_kills", it shows the percentage of games this event happened in Kesha's match history.  
The name MOPP comes from Miapp + op.gg + Kesha's hair looks like a mop.

## How to Use

Put an equation in the field; it could be anything from the list. For the enemy laner (opposite lane of the player), add "enemy_" before the stat name.  
Remember to use logical operators like `==`, `<`, `>`, `<=`, `>=`.  
To add recent games to the database, get yourself an API key from [Riot Developer Portal](https://developer.riotgames.com/) (expires in 24 hours).
`and`, `or`, `()`, `+`, `*`, and other operations are also supported, follows python syntax.

## Installation Guide

1. Install like any other Python Flask app with `requirements.txt`.
3. If you want to change the user and add it to database, change the account information in `config.py`.
4. Run `main.py`.

![image](https://github.com/user-attachments/assets/16e39e09-b41d-48e2-9a6a-ef88f682d90f)
