class Point {
private:
    int x, y;

public:
    Point(int x = 0, int y = 0);
    int getX() const;
    int getY() const;
    void setX(const int new_x);
    void setY(const int new_y);
};

class PointArray {
private:
    Point *points;
    int size;
    void resize(int n);

public:
    PointArray();
    PointArray(const Point points[], const int size);
    PointArray(const PointArray &pv);
    ~PointArray();
    void clear();
    void push_back(const Point &p);
    void insert(const int position, const Point &p);
    void remove(const int pos);
    const int getSize() const;
    Point *get(const int pos);
    const Point *get(const int pos) const;
};
