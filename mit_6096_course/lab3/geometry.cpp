#include <iostream>
#include "geometry.h"
using namespace std;

Point::Point(int x, int y)
{
    this->x = x;
    this->y = y;
}

int Point::getX() const { return x; }

int Point::getY() const { return y; }

void Point::setX(const int new_x)
{
    x = new_x;
}

void Point::setY(const int new_y)
{
    y = new_y;
}

PointArray::PointArray()
{
    size = 0;
    points = new Point[0];
}

PointArray::PointArray(const Point points[], const int size)
{
    this->size = size;
    this->points = new Point[this->size];
    for (int i = 0; i < size; i++)
    {
        this->points[i] = points[i];
    }
}

PointArray::PointArray(const PointArray &other)
{
    size = other.size;
    points = new Point[size];
    for (int i = 0; i < size; i++)
    {
        points[i] = other.points[i];
    }
}

PointArray::~PointArray()
{
    delete[] points;
}

void PointArray::resize(int newSize) {
    Point *pts = new Point[newSize];
    int minSize = (newSize > size ? size : newSize)
    for (int i = 0; i < minSize; i++) {
        pts[i] = points[i];
    }
    delete[] points;
    size = newSize;
    points = pts;
}

void PointArray::clear() {
    resize(0);
}

void PointArray::push_back(const Point &p) {
    resize(size + 1);
    points[size - 1] = p;
}

void PointArray::insert(const int position, const Point &p) {
    resize(size + 1);
    for (int i = size - 1; i > position; i--) {
        points[i] = points[i - 1];
    }
    points[position] = p;
}

int main()
{
    Point p;
    Point q(1, 2);

    cout << q.getX() << endl;

    q.setY(4);
    cout << q.getY() << endl;

    Point ps[3] = { Point(3, 2), Point(-1, 2), Point() };
    PointArray parr(ps, 3);

    return 0;
}