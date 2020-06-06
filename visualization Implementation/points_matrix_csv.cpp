#define FREEGLUT_STATIC
#include <GL/freeglut.h>
#include "math.h";
#include<iostream>
#include<fstream>
#include<sstream>
#include<string>
#include <vector>
#include <stdlib.h>
#include "Point.h"
#include <conio.h>



using namespace std;
/*csv*/
int noodrows(string location_cp);
int noodcols(string location_cp);
string** gen_Matrix(int rows, int cols);
void printMatrix(string** matrix, int rows, int cols);
void printMatrix_1(string** matrix, int rows, int cols);
void printMatrix_2(string** matrix_,int rows,int cols);
void printMatrix_3(string** matrix_, int rows, int cols);
void InputMatrix(string location_cp,string** matrix, int rows, int cols);
/*points*/
vector<point> createPoints(vector<point> new_vector, string** matrix, int rows, int cols);
/*openGL*/
void display_points();
void display_busy_lines();
void display_one_lines();
void display_sub_lines();
void print_two_points_line(string a, string b);
void when_in_mainloop();
void OnTimer(int value);
void keyboard_input(unsigned char key, int x, int y);
void InputMatrix(string location_cp, vector<vector<double>>& matrix);

//write text
void print_bitmap_string(void* font, const char* s);
int TextOut(float x, float y, const char* cstr);

//parameter
string location = "D:\\Final-Year-Project-master\\FYP\\points_matrix.csv";
string location1 = "D:\\Final-Year-Project-master\\FYP\\bus_busy_matrix.csv";
string location2 = "D:\\Final-Year-Project-master\\FYP\\lines.csv";
string location3 = "D:\\Final-Year-Project-master\\FYP\\sub_lines.csv";

vector<point> point_vector;
vector<vector<string>> iteration_lines;
vector<vector<string>> cuting_lines;
vector<vector<double>> matrix_sub_lines;
int time_interval = 16;

//the times of iteration:
int input_iteration = 9;

//the number of cut_edges
int cut_edge = 4;
int cut_iteration = 4;

string tmp_point1;
string tmp_point2;
vector<int> color_1 = { 0,0,1,0,0 };
vector<int> color_2 = { 0,1,1,0,1 };
vector<int> color_3 = { 0,0,0,1,1 };



void* bitmap_fonts[7] = {
		GLUT_BITMAP_9_BY_15,
		GLUT_BITMAP_8_BY_13,
		GLUT_BITMAP_TIMES_ROMAN_10,
		GLUT_BITMAP_TIMES_ROMAN_24,
		GLUT_BITMAP_HELVETICA_10,
		GLUT_BITMAP_HELVETICA_12,
		GLUT_BITMAP_HELVETICA_18
};






void main(int argc, char** argv) {
	char ch;




	/*Display the location*/
	int rows, cols;
	rows = noodrows(location);
	cols = noodcols(location);
	cout << "no of rows are: " << rows << "\t";
	cout << "no of cols are: " << cols << "\t"<<endl;
	string** matrix = gen_Matrix(rows, cols);
	
	InputMatrix(location,matrix, rows, cols);
	printMatrix(matrix, rows, cols);


	/*Create the vector of points*/
	vector<point> new_vector(rows);
	point_vector = createPoints(new_vector, matrix, rows, cols);

	cout << "enter (ESC) to escape the program!" << endl;

	cout << "Input Your options for the demo: \n1.'a' - the points reflection\n2.'b' - the busy-lines reflection\n3.'c' - the one-line reflection\n4.'d' - the sub-lines reflection" << endl;
	while (_getch() != 27) {
		
		
		cin >> ch;



		if (ch == 'a') {
			cout << "Display the different points by random cities" << endl;

			/*opengl-display*/
			glutInit(&argc, argv);

			glutInitWindowSize(600, 400);
			glutInitWindowPosition(50, 50);


			glutCreateWindow("Graphics Perimitives");

			glutDisplayFunc(display_points);
			glutMainLoop();
		}
		else if (ch == 'b') {
			cout << "Display the busy_lines in the map" << endl;
			/*Display the busy_lines*/
			int rows1, cols1;
			rows1 = noodrows(location1);
			cols1 = noodcols(location1);
			cout << "no of rows are: " << rows1 << "\t";
			cout << "no of cols are: " << cols1 << "\t" << endl;
			string** matrix_1 = gen_Matrix(rows1, cols1);
			InputMatrix(location1, matrix_1, rows1, cols1);
			printMatrix_1(matrix_1, rows1, cols1);
			/*opengl-display*/
			glutInit(&argc, argv);

			glutInitWindowSize(600, 400);
			glutInitWindowPosition(50, 50);


			glutCreateWindow("Graphics Perimitives");


			glutDisplayFunc(display_busy_lines);

			glutMainLoop();
		}
		else if (ch == 'c') {

			cout << "Display one Line for the map" << endl;
			/*Display the lines*/
			int rows2, cols2;
			rows2 = noodrows(location2);
			cols2 = noodcols(location2);
			cout << "no of rows are: " << rows2 << "\t";
			cout << "no of cols are: " << cols2 << "\t" << endl;
			string** matrix_2 = gen_Matrix(rows2, cols2);
			InputMatrix(location2, matrix_2, rows2, cols2);
			printMatrix_2(matrix_2, rows2, cols2);

			/*opengl-display*/
			glutInit(&argc, argv);

			glutInitWindowSize(600, 400);
			glutInitWindowPosition(50, 50);


			glutCreateWindow("Graphics Perimitives");



			glutDisplayFunc(display_one_lines);
			glutMainLoop();

		}
		else if(ch == 'd') {
			cout << "Display all the sub-lines" << endl;
			/*Display the sub_lines*/
			int rows3, cols3;
			rows3 = noodrows(location3);
			cols3 = noodcols(location3);
			cout << "no of rows are: " << rows3 << "\t";
			cout << "no of cols are: " << cols3 << "\t" << endl;
			string** matrix_3 = gen_Matrix(rows3, cols3);
			InputMatrix(location3, matrix_3, rows3, cols3);
			InputMatrix(location3, matrix_sub_lines);
			printMatrix_3(matrix_3, rows3, cols3);


			/*opengl-display*/
			glutInit(&argc, argv);

			glutInitWindowSize(600, 400);
			glutInitWindowPosition(50, 50);


			glutCreateWindow("Graphics Perimitives");



			glutDisplayFunc(display_sub_lines);
			glutMainLoop();

		}
		}
	}





	


	

	




	






void keyboard_input(unsigned char key, int x, int y) {
	if (key == 'q' || key == 'Q')
		exit(0);
	else if (key == 'p' || key == 'P')
		system("pause");
}





void when_in_mainloop() {
	glutPostRedisplay();
}

void OnTimer(int value) {
	print_two_points_line(tmp_point1, tmp_point2);

	when_in_mainloop();
	glutTimerFunc(time_interval, OnTimer, 1);
}

void display_points() {
	glClearColor(1, 1, 1, 1);
	glClear(GL_COLOR_BUFFER_BIT);


	//TASK 2		
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-100, 100, -100, 100);






	//TASK 3
	glLineWidth(1.0);
	glColor3f(0, 0, 0);

	glBegin(GL_LINES);
	glVertex2f(-225, 0);
	glVertex2f(225, 0);
	glEnd();

	glBegin(GL_LINES);
	glVertex2f(0, -75);
	glVertex2f(0, 75);
	glEnd();


	//TASK 4
	glPointSize(5.0);
	glColor3f(1, 0, 0);
	int length = point_vector.size();
	
	for (int i = 0; i < length; i++) {
		glBegin(GL_POINTS);
		glVertex2f(point_vector[i].output_x(), point_vector[i].output_y());
		glEnd();
	}


	glFlush();



}



void display_busy_lines() {
	glClearColor(1, 1, 1, 1);
	glClear(GL_COLOR_BUFFER_BIT);


	//TASK 2		
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-400, 400, -100, 100);






	//TASK 3
	glLineWidth(1.0);
	glColor3f(0, 0, 0);

	glBegin(GL_LINES);
	glVertex2f(-225, 0);
	glVertex2f(225, 0);
	glEnd();

	glBegin(GL_LINES);
	glVertex2f(0, -75);
	glVertex2f(0, 75);
	glEnd();


	//TASK 4
	glPointSize(5.0);
	glColor3f(1, 0, 0);
	int length = point_vector.size();

	for (int i = 0; i < length; i++) {
		glBegin(GL_POINTS);
		glVertex2f(point_vector[i].output_x(), point_vector[i].output_y());
		glEnd();
	}



	for (int i = 0; i < length; i++) {
		for (int j = 0; j < length; j++) {
			int line_size = point_vector[i].adjacentPoints[j];
			if (line_size != 0) {
				double color = line_size*2 / 365;
				glLineWidth(line_size);
				glColor3f(color, color, color);
				glBegin(GL_LINES);
				glVertex2f(point_vector[i].output_x(), point_vector[i].output_y());
				glVertex2f(point_vector[j].output_x(), point_vector[j].output_y());
				glEnd();
			}
		}





		glFlush();



	}
}

void display_one_lines() {
	glClearColor(1, 1, 1, 1);
	glClear(GL_COLOR_BUFFER_BIT);


	//TASK 2		
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-400, 400, -100, 100);






	//TASK 3
	glLineWidth(1.0);
	glColor3f(0, 0, 0);

	glBegin(GL_LINES);
	glVertex2f(-225, 0);
	glVertex2f(225, 0);
	glEnd();

	glBegin(GL_LINES);
	glVertex2f(0, -75);
	glVertex2f(0, 75);
	glEnd();


	//TASK 4
	glPointSize(5.0);
	glColor3f(1, 0, 0);
	int length = point_vector.size();

	for (int i = 0; i < length; i++) {
		glBegin(GL_POINTS);
		glVertex2f(point_vector[i].output_x(), point_vector[i].output_y());
		glEnd();
	}



		int iteration = iteration_lines.size();
		glColor3f(0, 0, 0);
		for (int i = 0; i < iteration; i++) {
			if (i == input_iteration) { //打印最后一次迭代的效果
				
				vector<string> new_vector_double = iteration_lines[i];
				int length = new_vector_double.size();

				for (int j = 0; j < length; j++) {
					if (j == 0) {
						string new_iteration = new_vector_double[j];
						const char* pchar = new_iteration.c_str();
						TextOut(100, 50, pchar);
					}
					else if (j == 1) {
						string new_iteration = new_vector_double[j];
						const char* pchar = new_iteration.c_str();
						TextOut(-50, -100, pchar);
					}
					else {
						if (j < length - 1) {
							glColor3f(0, 0, 0);
							int k = 1;
							tmp_point1 = new_vector_double[j];
							k = j + k;
							tmp_point2 = new_vector_double[k];
							OnTimer(time_interval);
						}

					}

				}

			}
			else {
				continue;
			}

		}
		




	glFlush();

}


void display_sub_lines() {
	glClearColor(1, 1, 1, 1);
	glClear(GL_COLOR_BUFFER_BIT);


	//TASK 2		
	glMatrixMode(GL_PROJECTION);
	glLoadIdentity();
	gluOrtho2D(-400, 400, -100, 100);






	//TASK 3
	glLineWidth(1.0);
	glColor3f(0, 0, 0);

	glBegin(GL_LINES);
	glVertex2f(-225, 0);
	glVertex2f(225, 0);
	glEnd();

	glBegin(GL_LINES);
	glVertex2f(0, -75);
	glVertex2f(0, 75);
	glEnd();


	//TASK 4
	glPointSize(5.0);
	glColor3f(1, 0, 0);
	int length = point_vector.size();

	for (int i = 0; i < length; i++) {
		glBegin(GL_POINTS);
		glVertex2f(point_vector[i].output_x(), point_vector[i].output_y());
		glEnd();
	}




	int length_cuting = matrix_sub_lines.size()/ cut_edge;
	int input_rows = cut_iteration * cut_edge;
	int z = 0;
	if (input_rows > length_cuting) {
		cout << "error input!" <<endl;
	}



	for (int i = input_rows; i < input_rows+ cut_edge; i++) {
			vector<double> new_vector_double = matrix_sub_lines[i];
			int length = new_vector_double.size();
			
			glColor3f(color_1[z],color_2[z],color_3[z]);
			z = z + 1;
			for (int j = 0; j < length; j++) {
				
				if (i== input_rows && j == 0) {
					string new_iteration = to_string(new_vector_double[j]);
					const char* pchar = new_iteration.c_str();
					TextOut(-50, -100, pchar);
				}else {
					

					if (j < length - 1) {
						int k = 1;
						tmp_point1 = to_string(new_vector_double[j]);
						k = j + k;
						tmp_point2 = to_string(new_vector_double[k]);
				
							OnTimer(time_interval);
					
					}
					}
				

				

			}

		
		
		

	}





	glFlush();

}



void print_two_points_line(string a, string b) {
	int a_i = atoi(a.c_str());
	int b_i = atoi(b.c_str());
	double x_1;
	double y_1;
	double x_2;
	double y_2;


	int length = point_vector.size();
	for (int i = 0; i < length; i++) {
		if (point_vector[i].getName() == a_i) {
			x_1 = point_vector[i].output_x();
			y_1 = point_vector[i].output_y();
		}

		if (point_vector[i].getName() == b_i) {
			x_2 = point_vector[i].output_x();
			y_2 = point_vector[i].output_y();
		}

	}

	glLineWidth(3);
	//glColor3f(0, 0, 0);
	glBegin(GL_LINES);
	glVertex2f(x_1,y_1);
	glVertex2f(x_2, y_2);
	glEnd();




	
}




int noodcols(string location_cp) {

	//get the colume for the csv.
	ifstream file3(location_cp);
	string data;
	int counter = 0;
	getline(file3, data);
	stringstream sstream(data);
	while (!sstream.eof()) {
		getline(sstream, data, ',');
		counter++;
	}
	return counter;


}





int noodrows(string location_cp) {
	//get the row for the csv
	ifstream file2(location_cp);
	if (!file2.is_open()) {
		cout << "cannot open the file" << endl;

	}

	string data;
	int counter = 0;


	while (getline(file2, data)) {
		//cout << data << endl;
		counter++;
	}
	return counter;
}


string** gen_Matrix(int rows, int cols) {
	//generate the empty matrix
	string** matrix = new string * [rows];
	for (int i = 0; i < rows; i++) {
		matrix[i] = new string[cols];
	}
	return matrix;
}

void printMatrix(string** matrix, int rows, int cols) {
	//print the result of matrix
	for (int i = 0; i < rows; ++i) {
		cout << "the line of: " << i<<endl;
		for (int j = 0; j < 2; ++j) {
			cout << matrix[i][j] << " ";
		}
		cout << endl;
	}
}

void printMatrix_1(string** matrix, int rows, int cols) {
	//print the result of matrix
	for (int i = 0; i < rows; ++i) {
		cout << "the line of: " << i << endl;
		for (int j = 0; j < cols; ++j) {
			
				//add elements to the maps
				double x = atof(const_cast<const char*>(matrix[i][j].c_str()));   //string to double
				point_vector[i].addAdjacentPoints(j, x);
				cout << point_vector[i].getName() << "-->"<<j<<": " << x << endl;
			
		}
		cout << endl;
	}
}


void printMatrix_2(string** matrix, int rows, int cols) {

	vector<vector<string>> new_iteration_lines(rows);
	iteration_lines = new_iteration_lines;

	for (int i = 0; i < rows; i++) {
		cout << "the line of: " << i << endl;
		vector<string> l1(cols);
		for (int j = 0; j < cols; j++) {
			//double x = atof(const_cast<const char*>(matrix[i][j].c_str()));   //string to double
			l1[j] = matrix[i][j];
			cout << matrix[i][j] << endl;
		}
		iteration_lines[i] = l1;
		l1.clear();
	}




}

void printMatrix_3(string** matrix, int rows, int cols) {

	vector<vector<string>> new_cuting_sub_lines(rows);
	cuting_lines = new_cuting_sub_lines;

	for (int i = 0; i < rows; i++) {
		cout << "the line of: " << i << endl;
		vector<string> l1(cols);
		for (int j = 0; j < cols; j++) {
			//double x = atof(const_cast<const char*>(matrix[i][j].c_str()));   //string to double
			l1[j] = matrix[i][j];
			cout << matrix[i][j] << endl;
		}
		cuting_lines[i] = l1;
		l1.clear();
	}




}







vector<point> createPoints(vector<point> new_vector,string** matrix,int rows,int cols) {
	
	double x;
	double y;

	
	for (int row = 0; row < rows; ++row) {
		for (int col = 0; col < 2; ++col) {
			if (col == 0) {
				string str1 = matrix[row][col];
				x = atof(const_cast<const char*>(str1.c_str()));   //string to double
			}
			else {
				string str2 = matrix[row][col];
				y = atof(const_cast<const char*>(str2.c_str()));   //string to double
			}

			

		}
		point new_point(row, x, y);
		new_point.print_coordinate_point();
		new_vector[row] = new_point;



	}
	return new_vector;
}




void InputMatrix(string location_cp,string** matrix, int rows, int cols) {
	ifstream file(location_cp);
	stringstream buffer;
	buffer << file.rdbuf();
	string data;
	for (int i = 0; i < rows; i++) {
		for (int j = 0; j < cols; j++) {
			if (j == cols - 1) {
				getline(buffer, data, '\n');
				matrix[i][j] = data;
				j++;
				continue;
			}
			else {
				getline(buffer, data, ',');
				matrix[i][j] = data;
			}

		}
	}


}

void InputMatrix(string location_cp, vector<vector<double>>& matrix) {
	ifstream file(location_cp);
	if (!file)return;

	matrix.clear();
	string data;

	while(getline(file, data))	
	{
		for (int j = 0; j < data.size(); j++)
		{
			if (data[j] == ',')data[j] = ' ';
		}
		istringstream out(data);

		string tem;
		vector<double>vec;
		while (out >> tem)
		{
			vec.push_back(atof(tem.c_str()));
		}
		matrix.push_back(vec);
		vec.clear();		
	}
}




void print_bitmap_string(void* font, const char* s)
{
	if (s && strlen(s)) {
		while (*s) {
			glutBitmapCharacter(font, *s);
			s++;
		}
	}
}


int TextOut(float x, float y, const char* cstr)
{
	glRasterPos2f(x, y);
	print_bitmap_string(bitmap_fonts[4], cstr);
	return 1;
}

