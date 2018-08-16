//
//  Hilo.cpp
//  ColorQueue
//
//  Created by Juan Casado Ballesteros on 8/2/18.
//

#include "Hilo.hpp"
#include <iostream>

Hilo::Hilo(){
    control = false;
}

Hilo::~Hilo(){
}

bool Hilo::run(){
    if (!control){
        control = true;
        hilo = std::thread(Hilo::action, this);
        return true;
    }
    return false;
}

void Hilo::action(Hilo * runnable){
    runnable->to_beguin();
    while (runnable->control){
        runnable->to_do();
    }
}

void Hilo::end(){
    control = false;
    to_end();
    if(hilo.joinable()){
        hilo.join();
    }
}
