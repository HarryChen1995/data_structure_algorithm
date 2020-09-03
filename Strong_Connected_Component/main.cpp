#include<iostream>
#include "graph.h"
#include<string>
using namespace std;

int main(){
    graph G;
    string parser = "";
    while(cin >> parser){
        string A = parser.substr(0,1);
        string B = parser.substr(3,1);
        G.add_edge(A,B);

    }
    G.SCC();
    return 0;
}
