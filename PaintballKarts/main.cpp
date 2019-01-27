#include <iostream>
#include <opencv2/opencv.hpp>
#include "Simulation.hpp"

int main() {
    Simulation simulation {"PaintballKarts", 400, 600};
    simulation.startSimulation();
    return 0;
}
