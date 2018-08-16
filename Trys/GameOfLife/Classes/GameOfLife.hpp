#ifndef __MAINMENU_SCENE_H__
#define __MAINMENU_SCENE_H__

#include "cocos2d.h"

class MainMenu : public cocos2d::Scene{
public:
    static cocos2d::Scene* createScene();
private:
    virtual bool init();
    CREATE_FUNC(MainMenu);
};

#endif // __MAINMENU_SCENE_H__
