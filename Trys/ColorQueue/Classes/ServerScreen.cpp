//
//  ServerScreen.cpp
//  ColorQueue
//
//  Created by Juan Casado Ballesteros on 8/1/18.
//

#include "ServerScreen.hpp"

USING_NS_CC;

ServerScreen::ServerScreen(){
    succesOcurred = false;
    failOcurred = false;
}

Scene* ServerScreen::createScene(){
    return ServerScreen::create();
}
bool ServerScreen::init(){
    if ( !Scene::init() ){
        return false;
    }
    auto background = Sprite::create("WhiteRect.png");
    if (background==nullptr){
        return false;
    }
    auto title = Label::createWithTTF("Color Queue", "fonts/Marker Felt.ttf", 70);
    if (title ==  nullptr){
        return false;
    }
    auto screen = Director::getInstance()->getSafeAreaRect().size;
    background->setPosition(Vec2(screen.width*0.5, screen.height*0.4));
    background->setContentSize(Size(screen.width*0.6, screen.height*0.6));
    background->setColor(Color3B(193, 242, 185));
    title->setPosition(Vec2(screen.width*0.5, screen.height*0.87));
    title->setColor(Color3B(10, 30, 10));
    
    auto buttonSize = Size(screen.width*0.1, screen.width*0.1);
    auto backStill = Sprite::createWithTexture(background->getTexture());
    backStill->setContentSize(buttonSize);
    backStill->setColor(Color3B(120, 200, 100));
    auto backClicked = Sprite::createWithTexture(background->getTexture());
    backClicked->setContentSize(buttonSize);
    backClicked->setColor(Color3B(20, 50, 0));
    auto back = MenuItemSprite::create(backStill, backClicked, CC_CALLBACK_0(ServerScreen::back, this));
    auto backLabel = Label::createWithTTF("X", "./fonts/Marker Felt.ttf", 10);
    backLabel->setPosition(buttonSize.width/2, buttonSize.height/2);
    back->addChild(backLabel);
    
    auto backHolder = Menu::createWithItem(back);
    backHolder->setAnchorPoint(Vec2(0.5, 0));
    backHolder->setPosition(Vec2(screen.width*0.5, screen.width*0.08));
    
    state = Label::createWithTTF("Creating Server...", "./fonts/Marker Felt.ttf", 30);
    state->setColor(Color3B(20, 40, 20));
    state->setAnchorPoint(Vec2(0.5, 0));
    state->setPosition(Vec2(background->getContentSize().width*0.5, background->getContentSize().height*0.85));

//    TO DO ON SERVER
//    try {
//        server.sin_port = htons(std::stoi(port));
//        ip.erase(std::remove_if(ip.begin(), ip.end(), &TcpClientScreen::TcpClient::isNumber));
//        server.sin_addr.s_addr = htons(std::stoi(ip));
//        if ((fd=socket(AF_INET, SOCK_STREAM, 0)) > 0){
//            server.sin_family = AF_INET;
//            bzero(&(server.sin_zero),8);
//
//        }else{
//            screen->connectionFailed();
//        }
//    }catch(std::exception const & e){
//        screen->connectionFailed();
//    }
    
    background->addChild(state);
    this->addChild(title);
    this->addChild(background);
    this->addChild(backHolder);
    return true;
}

void ServerScreen::update(float t){
    if (succesOcurred){
        state->setString("Server joinable");
        state->setColor(Color3B(20, 150, 20));
    }
    if (failOcurred){
        state->setString("Unable to create server");
        state->setColor(Color3B(150, 20, 20));
    }
}

void ServerScreen::back(void){
    auto scene = MainMenu::createScene();
    if (scene != nullptr){
        Director::getInstance()->replaceScene(scene);
    }
}

void ServerScreen::IpServer::to_beguin(){
    
}
void ServerScreen::IpServer::to_do(){
    
}
void ServerScreen::IpServer::to_end(){
    
}
ServerScreen::IpServer::IpServer(){
    
}
ServerScreen::IpServer::~IpServer(){
    
}
