//
// Created by Juan Casado Ballesteros on 1/26/19.
//

#ifndef PAINTBALLKARTS_MAP_HPP
#define PAINTBALLKARTS_MAP_HPP
#include <opencv2/opencv.hpp>
#include <string>
#include <vector>

class Map {
public:
    Map (int rows, int cols);
    void update (float time, float distance, float speed);
    cv::Mat *getData ();
    float curvature();
private:
    cv::Mat _data;
    cv::Mat _track_img;
    std::vector<std::pair <float, float>> _tracks;
    int _total_length;
    int _lap = 0;
    float _current_curvature = 0;

    static const cv::Vec3b klight_grass;
    static const cv::Vec3b kdark_grass;
    static const cv::Vec3b kroad;
    static const cv::Vec3b kred_clip;
    static const cv::Vec3b kwhite_clip;
    static const cv::Vec3b kdark_sky;
    static const cv::Vec3b klight_sky;
    static const cv::Vec3b kmountain;
};


#endif //PAINTBALLKARTS_MAP_HPP
