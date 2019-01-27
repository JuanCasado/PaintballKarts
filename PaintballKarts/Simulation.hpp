//
// Created by Juan Casado Ballesteros on 1/26/19.
//

#ifndef PAINTBALLKARTS_SIMULATION_HPP
#define PAINTBALLKARTS_SIMULATION_HPP

#include "Map.hpp"
#include "Car.hpp"
#import <opencv2/opencv.hpp>
#import <vector>
#import <string>
#import <iostream>

class Simulation {
public:
    Simulation (std::string name, int h, int w);
    void startSimulation ();
private:
    std::string _name;
    int _w;
    int _h;
    Car *car;
    Map *map;
};


#endif //PAINTBALLKARTS_SIMULATION_HPP
