#ifndef VERTEX_H
#define VERTEX_H
#include<string>
#include<vector>
#define undefined -1
using namespace std;
class vertex {
    public:
    string name;
    int index;
    int lowlink;
    bool isonstack;
    vector<vertex*> neighbor;
    vertex(string name);
    void  add_neighbor(vertex* B);
};

#endif
