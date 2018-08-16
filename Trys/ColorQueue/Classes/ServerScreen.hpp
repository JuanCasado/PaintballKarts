//
//  ServerScreen.hpp
//  ColorQueue
//
//  Created by Juan Casado Ballesteros on 8/1/18.
//

#ifndef ServerScreen_hpp
#define ServerScreen_hpp
#include "MainMenu.hpp"
#include "Hilo.hpp"

class ServerScreen : public cocos2d::Scene{
public:
    static cocos2d::Scene* createScene();
private:
    ServerScreen();
    virtual bool init() override;
    CREATE_FUNC(ServerScreen);
    void back (void);
    void update (float t) override;
    std::atomic_bool succesOcurred;
    std::atomic_bool failOcurred;
    cocos2d::Label * state;
    
    class IpServer : public Hilo{
    protected:
        virtual void to_do();
        virtual void to_beguin();
        virtual void to_end();
    public:
        IpServer();
        ~IpServer();
    private:
        ServerScreen * screen;
    };
    
    IpServer * server;
};

#endif /* ServerScreen_hpp */
