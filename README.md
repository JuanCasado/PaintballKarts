# PaintballKarts

This is supposed to be a car raccing game with the Mario Kart style, so you will need not only to race the fastest you can but also to avoid and trhro projectiles to your opponents.

The objetive of the project is to learn so the final visual design won't be as important as its internall code design or features.

## Game architecture
* The game ui will be done int cocos2d-x c++ game engine.
* This will be a centralized multiplayer game, to accomplish that the project will be compounded of two different parts
* **Part 1 (player):** The players will join the server to be able to play the game. Once the are all ready to play the game will start. Disconnections will be handled by removing the players. The players will do a soft update of the game state, it will be updated with the previous data until the server send new one.
* **Part 2 (server):** The server will be responsible to "join" the players, the players won't connect one with each other, the are connected only by the server. The server is responsible to handle colissions and to update the game state of the players. All data that will need to be store like the player goals or the wins of each player will be done by the server.
* At the begging of each game the field will be randomly generated by the server and distributed to the players once they are connected.

## Game desing
The game will hace a 2d view from above, each player will have the cammera center on itself, also they will have a minimap that will resume the possition of each one in the field. There will be three type of objects, max speed powerups, boost speed powerups and projectiles. The gameplay and efects of each object will be defined as the game is created.

## History of the project
At this point i've decided to make the game with the cocos2d-x c++ engine, but this decision may chage in the future. When i first thought of this project i though the best idea was to make the ui with python using pygame and do the main heavy task of the game like updating the game state or handling colission, even connecting with other players with c++.
For that propouse i would launch a python script that held the ui, this scrip would also launch a c++ process with wich it would communicate by pipes. Theres's an example of this in the trys folder.
Since I have discovered cocos2d-x c++ engine this is no longer needed since i can do everything with c++.
Nevertheless the propose of this project is to learn, as i said it after, and while i was testing python to use pygame i learned a lot of thing about the language specially about python's multithreading syntax.

I'm doing this kind of projects in summen in my university holidays so since i been doing some other games to practice with the cocos2d-x c++ engine i haven't foucus as much in this one so i might countinue it next summer 2019.
