//
// Created by Juan Casado Ballesteros on 1/26/19.
//

#include "Simulation.hpp"

Simulation::Simulation (std::string name, int h, int w){
    cv::namedWindow(name);
    _h = h;
    _w = w;
    _name = name;
    map = new Map (h,w);
    car = new Car {static_cast<int>((h+w)*0.05f),
             static_cast<int>((h+w)*0.04f),
             static_cast<int>(h*0.7f)};
}

void Simulation::startSimulation (){
    auto t = (float)cv::getTickCount();
    int key = 0;
    while ((key = cv::waitKey(1)) != 27){
        car->update(((float)cv::getTickCount() - t)/(float)cv::getTickFrequency()*10.0f, key, map->curvature());
        map->update(((float)cv::getTickCount() - t)/(float)cv::getTickFrequency()*10.0f, car->distance(), car->speed());
        t = (float)cv::getTickCount();
        cv::Mat screen = *map->getData();
        const int rows = (*car->getData()).isContinuous()? (*car->getData()).rows : 1;
        const int cols = (*car->getData()).isContinuous()? (*car->getData()).cols :
                (*car->getData()).cols * (*car->getData()).rows ;
        for (int x = 0; x < cols; ++x) {
            for (int y = 0; y < rows; ++y) {
                const auto y_screen = static_cast<int>(y + _w/2.0f + _w * (map->curvature() - car->curvature()) - (*car->getData()).cols/2.0f);
                const int x_screen = x + car->getPos();
                screen.at<cv::Vec3b>(x_screen, y_screen) = (*car->getData()).at<cv::Vec3b>(y, x);
            }
        }
        cv::imshow(_name, screen);
    }
}