//
//  Menu.cpp
//  GameOfLife
//
//  Created by Juan Casado Ballesteros on 7/21/18.
//

#include "Menu.hpp"

USING_NS_CC;

Menu::Menu(){}

Menu * Menu::createMenu(){
    Menu * menu = new Menu();
    if (menu && menu->init()){
        menu->autorelease();
        return menu;
    }else{
        delete menu;
        menu = nullptr;
        return nullptr;
    }
}

bool Menu::init(){
    if (!Scene::init()){
        return false;
    }
    auto img = Sprite::create("WhiteRect.png");
    if (img ==nullptr){
        return false;
    }
    auto screen = Director::getInstance()->getVisibleSize();
    
    
    return true;
}
