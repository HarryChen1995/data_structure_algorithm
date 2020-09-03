#ifndef GRAPH_H
#define GRAPH_H
#include "vertex.h"
#include<map>
#include<string>
#include<stack>
using namespace std;
class graph {
   public:
       int index;
       stack<vertex*> s;
       map<string, vertex*>g;
       graph();
       void add_edge(string A, string B);
       void SCC();
       void DFS(vertex * V);
};
#endif 
