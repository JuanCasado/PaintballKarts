# PaintballKarts

This is supposed to be a car raccing game with the Mario Kart style, so you will need not only to race the fastest you can but also to avoid and trhro projectiles to your opponents.

The objetive of the project is to learn so the final visual design won't be as important as its internall code design or features.

## Game architecture


At this point i've decided to make the game with the cocos2d-x c++ engine, but this decision may chage in the future. When i first thought of this project i though the best idea was to make the ui with python using pygame and do the main heavy task of the game like updating the game state or handling colission, even connecting with other players with c++.
For that propouse i would launch a python script that held the ui, this scrip would also launch a c++ process with wich it would communicate by pipes. Theres's an example of this in the trys folder.
Since I have discovered cocos2d-x c++ engine this is no longer needed since i can do everything with c++.
Nevertheless the propose of this project is to learn, as i said it after, and while i was testing python to use pygame i learned a lot of thing about the language specially about python's multithreading syntax.

I'm doing this kind of projects in summen in my university holidays so since i been doing some other games to practice with the cocos2d-x c++ engine i haven't foucus as much in this one so i might countinue it next summer 2019.
