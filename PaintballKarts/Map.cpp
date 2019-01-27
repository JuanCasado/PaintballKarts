//
// Created by Juan Casado Ballesteros on 1/26/19.
//

#include "Map.hpp"
#include <iostream>

const auto Map::klight_grass = cv::Vec3b(0, 255, 0);
const auto Map::kdark_grass = cv::Vec3b(0, 180, 0);
const auto Map::kroad = cv::Vec3b(200, 200, 200);
const auto Map::kred_clip = cv::Vec3b(0, 0, 255);
const auto Map::kwhite_clip = cv::Vec3b(255, 255, 255);
const auto Map::klight_sky = cv::Vec3b(255, 100, 50);
const auto Map::kdark_sky = cv::Vec3b(255, 150, 100);
const auto Map::kmountain = cv::Vec3b(0, 40, 60);

Map::Map (int rows, int cols){
    std::srand(std::time(nullptr));
    this->_data = cv::Mat::zeros(rows,cols, CV_8UC3);
    int number_of_tracks = std::rand()%20 + 50;
    _total_length = 100;
    for (int i = 0; i < number_of_tracks; ++i){
        float new_lenght = std::rand()%90 + 20;
        int new_rand;
        float new_turn = 0;
        switch (new_rand = std::rand()%9){
            case 0:
                new_turn = 0.0f;
                break;
            case 1:
            case 2:
            case 3:
            case 4:
                new_turn = (new_rand)/4.0f;
                break;
            case 5:
            case 6:
            case 7:
            case 8:
                new_turn = (new_rand-4)/-4.0f;
                break;
        }
        _total_length += new_lenght;
        _tracks.emplace_back(std::make_pair(new_turn/2,new_lenght));
    }
    _tracks.emplace_back(std::make_pair(0,100));
    _track_img = cv::Mat::zeros(static_cast<int>(rows*0.02f), cols, CV_8UC3);
    int last_drown = 0;
    for (std::pair <float, float> &pair : _tracks){
        auto screen_fraction = static_cast<int>(pair.second / _total_length * cols);
        cv::Vec3b color;
        if (pair.first > 0){
            color = cv::Vec3b(20, 20, static_cast<uchar>(pair.first*200 + 55));
        } else if (pair.first < 0) {
            color = cv::Vec3b(20, static_cast<uchar>(-pair.first*200 + 55), 20);
        } else {
            color = cv::Vec3b(255, 20, 20);
        }
        for (int i = last_drown; i < last_drown+screen_fraction; ++i){
            for (int j = 0; j < _track_img.rows; ++j){
                _track_img.at<cv::Vec3b>(j, i) = color;
            }
        }
        last_drown += screen_fraction;
    }
    for (int i = last_drown; i < cols; ++i){
        for (int j = 0; j < _track_img.rows; ++j){
            _track_img.at<cv::Vec3b>(j, i) = cv::Vec3b(255, 255, 255);
        }
    }
}


void Map::update (float time, float distance, float speed) {
    const int rows = _data.isContinuous()? _data.rows : 1;
    const int cols = _data.isContinuous()? _data.cols : _data.cols * _data.rows ;
    distance -= _lap*_total_length;
    if (distance < 0) distance = 0;
    float draw_distance = distance *100;
    float offset = 0;
    int track_section = 0;
    float car_distance = distance / _total_length * _data.cols;
    while (track_section < _tracks.size() && offset <= distance){
        offset +=_tracks[track_section].second;
        ++track_section;
    }
    if (track_section >= _tracks.size()){
        ++_lap;
    }
    float curvature = _tracks[track_section-1].first;
    float curvature_diff = (curvature - _current_curvature) * time * speed * 0.5f;
    _current_curvature += curvature_diff;

    for (int x = 0; x < cols; ++x) {
        for (int y = 0; y < rows*0.6f; ++y) {
            float perspective = static_cast<float>(y) / (_data.rows / 2.0f);
            float mid_point = 0.5f + _current_curvature * static_cast<float>(pow(1.0f - perspective, 3));
            float road_width = 0.1f + perspective*0.85f;
            float clip_width = road_width * 0.15f;

            road_width *= 0.5f;

            auto kleft_grass = static_cast<int>((mid_point - road_width - clip_width) * cols);
            auto kleft_clip = static_cast<int>((mid_point - road_width) * cols);
            auto kright_grass = static_cast<int>((mid_point + road_width + clip_width) * cols);
            auto kright_clip = static_cast<int>((mid_point + road_width) * cols);

            auto ry = static_cast<int>(_data.rows*0.4f +y);

            cv::Vec3b grass_color = sin(20 * pow(1 - perspective, 3) + draw_distance) > 0? klight_grass:kdark_grass;
            cv::Vec3b clip_color = sin(150 * pow(1 - perspective, 3) + draw_distance) > 0? kred_clip:kwhite_clip;

            if (x < kleft_grass) {
                _data.at<cv::Vec3b>(ry, x) = grass_color;
            } else if (x >= kleft_grass && x < kleft_clip) {
                _data.at<cv::Vec3b>(ry, x) = clip_color;
            } else if (x >= kleft_clip && x < kright_clip) {
                if (track_section == _tracks.size()){
                    _data.at<cv::Vec3b>(ry, x) = kwhite_clip;
                } else {
                    _data.at<cv::Vec3b>(ry, x) = kroad;
                }
            } else if (x >= kright_clip && x < kright_grass) {
                _data.at<cv::Vec3b>(ry, x) = clip_color;
            } else {
                _data.at<cv::Vec3b>(ry, x) = grass_color;
            }
        }
    }
    for (int x = 0; x < cols; ++x) {
        auto hill = static_cast<int>(rows*0.4f-abs(sin(x * 0.002f + _current_curvature)*_data.rows*0.15));
        for (int y = 0; y < rows*0.4f; ++y) {
            if (y <  hill) {
                _data.at<cv::Vec3b>(y, x) = y > rows * 0.2 ? kdark_sky : klight_sky;
            } else {
                _data.at<cv::Vec3b>(y, x) = kmountain;
            }
        }
    }
    for (int x = 0; x < _track_img.cols; ++x) {
        for (int y = 0; y < _track_img.rows; ++y) {
            _data.at<cv::Vec3b>(y, x) = _track_img.at<cv::Vec3b>(y, x);
        }
    }
    for (int y = 0; y < _track_img.rows; ++y) {
        _data.at<cv::Vec3b>(y, car_distance) = cv::Vec3b(0, 150, 255);
    }
}

cv::Mat *Map::getData (){
    return &_data;
}

float Map::curvature() {
    return _current_curvature;
}
