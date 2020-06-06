#pragma once
#include<string>
#include<iostream>
#include<map>

class point {
private:
	int name;
	double x;
	double y;
	
	

public:
	std::map<int, int> adjacentPoints;
	point();
	point(int name, double x, double y);
	~point();
	void print_coordinate_point();
	double output_x();
	double output_y();
	void addAdjacentPoints(int name, double magnitude);
	double getAdjacentPoints(int name);
	int getName();

};