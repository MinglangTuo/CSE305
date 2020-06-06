#include<iostream>
#include"Point.h"

point::point() {
	name = 0;
	x = 0;
	y = 0;
}

point::point(int new_name, double x_cp, double y_cp) {
	name = new_name;
	x = x_cp;
	y = y_cp;
}


point::~point() {

}


void point::print_coordinate_point() {
	std::cout << "the point of " << name << " , and its coordinate is (" << x << "," << y << "). \n";
}

double point::output_x() {
	return x;
}

double point::output_y() {
	return y;
}

void point::addAdjacentPoints(int name, double magnitude) {
	adjacentPoints[name] = magnitude;
}

double point::getAdjacentPoints(int name) {
	return adjacentPoints[name];
}



int point::getName() {
	return name;
}