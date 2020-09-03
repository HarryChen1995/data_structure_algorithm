#include "vertex.h"
vertex:: vertex(string name){
    this->name = name;
    this->index = undefined;
    this->lowlink = undefined;
    this->isonstack = false;
}
void vertex:: add_neighbor(vertex* B){
    this->neighbor.push_back(B);
}
