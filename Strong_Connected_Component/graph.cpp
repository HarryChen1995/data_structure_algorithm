#include "graph.h"
#include<math.h>
#include<iostream>
graph::graph(){
    index = 0;
}
void graph::add_edge(string A, string B){
    if(this->g.find(A) == g.end()){
        g[A] = new vertex(A);
    }
    if (this->g.find(B)== g.end()){
        g[B] = new vertex(B);
    }
    g[A]->add_neighbor(g[B]);
}
void graph::SCC(){
    
    map<string, vertex*> :: iterator it;
    for(it = g.begin(); it != g.end(); it++){
        if (it->second->index == undefined){
           DFS(it->second);
        }
    }

}

void graph:: DFS(vertex *V){
    V->index = this->index;
    V->lowlink = this->index;
    this->index +=1;
    s.push(V);
    V->isonstack = true;
    for(vertex* w:V->neighbor){
        if (w->index == undefined){
            DFS(w);
            V->lowlink = min(V->lowlink, w->lowlink);
        }else if (w->isonstack == true){
            V->lowlink = min(V->lowlink, w->index);
        }
    }

    if (V->index == V->lowlink){
        vertex * top;
        string str = "";
        do {
            top = s.top();
            s.pop();
            top->isonstack  = false;
            str +=  top->name + " ";
        }while(top != V);
        cout << str << "\n";
    }
}
