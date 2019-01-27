//
// Created by Juan Casado Ballesteros on 1/26/19.
//

#include "Car.hpp"

Car::Car (int w, int h, int y){
    _y = y;
    _data = cv::Mat (h,w, CV_8UC3, cv::Vec3b(0, 150, 255));
}

void Car::update (float time, int key, float pcurvature){
    bool turn = _curvature > pcurvature;
    bool go = abs(_curvature - pcurvature) < 0.2;
    if (go) {
        _speed += 5.0f * time;
    } else {
        _speed -= time * 0.5f;
    }
    if (turn) {
        _curvature -= time * 0.03f;
    } else {
        _curvature += time * 0.03f;
    }
    float mid_separation = abs(_curvature - pcurvature);
    if (mid_separation >= 0.25f){
        _speed -= mid_separation * time * 20;
    }
    if (_speed < 0.0f) _speed = 0.0f;
    if (_speed > 1.0f) _speed = 1.0f;
    if (_curvature < -0.45f) _curvature = -0.45f;
    if (_curvature > 0.45f) _curvature = 0.45f;
    _distance += 10 * _speed * time;

}

cv::Mat *Car::getData (){
    return &_data;
}

int Car::getPos (){
    return _y;
}

cv::Vec3b Car::color () {
    return cv::Vec3b(0, 150, 255);
}

float Car::distance (){
    return _distance;
}

float Car::speed(){
    return _speed;
}

float Car::curvature(){
    return _curvature;
}