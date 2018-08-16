//
//  Menu.hpp
//  GameOfLife
//
//  Created by Juan Casado Ballesteros on 7/21/18.
//

#ifndef Menu_hpp
#define Menu_hpp
#include "cocos2d.h"

class Menu : public cocos2d::Scene{
public:
    Menu * createMenu();
private:
    Menu();
    virtual bool init();
};

#endif /* Menu_hpp */
