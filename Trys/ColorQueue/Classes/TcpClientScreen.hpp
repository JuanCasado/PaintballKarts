//
//  TcpClientScreen.hpp
//  ColorQueue
//
//  Created by Juan Casado Ballesteros on 8/2/18.
//

#ifndef TcpClientScreen_hpp
#define TcpClientScreen_hpp
#include "ui/CocosGUI.h"
#include "MainMenu.hpp"
#include "Hilo.hpp"
#include <stdio.h>
#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <netdb.h>
#include <unistd.h>
#include <iostream>
#include <arpa/inet.h>

#define MAXDATASIZE 200

class TcpClientScreen : public cocos2d::Scene{
public:
    static cocos2d::Scene* createScene();
private:
    TcpClientScreen();
    virtual bool init() override;
    CREATE_FUNC(TcpClientScreen);
    void back (void);
    void createConnection (void);
    std::string name;
    std::string pass;
    std::string ip;
    std::string port;
    cocos2d::ui::TextField * nameField;
    cocos2d::ui::TextField * passField;
    cocos2d::ui::TextField * ipField;
    cocos2d::ui::TextField * portField;
    cocos2d::Sprite * nameBackgroudStill;
    cocos2d::Sprite * passBackgroudStill;
    cocos2d::Sprite * ipBackgroudStill;
    cocos2d::Sprite * portBackgroudStill;
    cocos2d::Color3B stillColor;
    cocos2d::Color3B clickedColor;
    void update(float) override;
    std::atomic_bool succesOcurred;
    std::atomic_bool failOcurred;
    void closeConnection(void);
    void connectionSucceded(void);
    void connectionFailed(void);
    cocos2d::Label * banner;
    
    class TcpClient : public Hilo{
    protected:
        virtual void to_do();
        virtual void to_beguin();
        virtual void to_end();
    public:
        TcpClient(std::string name, std::string pass, std::string ip, std::string port, TcpClientScreen * screen);
        ~TcpClient();
    private:
        std::string name;
        std::string pass;
        std::string ip;
        std::string port;
        TcpClientScreen * screen;
        bool isNumber(char c);
        
        int fd;
        struct sockaddr_in server;
        struct hostent *he; 
        char buf[MAXDATASIZE];
        long numbytes;
        bool ok;
    };
    TcpClient * connection;
};

#endif /* TcpClientScreen_hpp */
