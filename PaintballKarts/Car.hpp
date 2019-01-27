//
// Created by Juan Casado Ballesteros on 1/26/19.
//

#ifndef PAINTBALLKARTS_CAR_HPP
#define PAINTBALLKARTS_CAR_HPP
#include <opencv2/opencv.hpp>
#include <string>


class Car {
public:
    Car (int w = 50, int h = 70, int y = 300);
    void update (float time, int key, float pcurvature);
    cv::Mat *getData ();
    int getPos ();
    cv::Vec3b color ();
    float distance ();
    float speed ();
    float curvature ();
private:
    int _y;
    float _speed = 0;
    cv::Mat _data;
    float _distance = 0;
    float _curvature = 0;
};


#endif //PAINTBALLKARTS_CAR_HPP
