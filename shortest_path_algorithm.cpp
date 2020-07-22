#include<iostream>
#include<string>
#include<vector>
#include<algorithm>
#include<map>
using namespace std;
using namespace std;

struct vertex {
    string name;
    vector<vertex*> neighboor;
    vertex(string name){
        this-> name = name;
    }
};
class Graph {
    public:
       map<string, vertex*> graph;
       map<string, int> edge;
       map<vertex*, int> dist;  // distance from source to eact vertex
       map<vertex*, vertex*> prev; // prev vertex to source with shortest distance
       Graph(){
        
        }

        void add_edge_from_to(string A, string B, int weight){
            if (graph.find(A) == graph.end()){
                graph[A] = new vertex(A);
                dist[graph[A]] = INT_MAX;
            }
            if (graph.find(B) == graph.end()){
                graph[B] = new vertex(B);
                dist[graph[B]] = INT_MAX;
            }
            
            graph[A]->neighboor.push_back(graph[B]);
            edge[A+"->"+B] = weight;
        }

        void dijkstra(){

            vector<vertex*> Q;

            map <string,  vertex*> :: iterator it;

            for (it = graph.begin(); it != graph.end(); it ++){
                Q.push_back(it->second);
            }
            while(!Q.empty()){
                // find vertex with mind dist
                auto  u  = min_element(Q.begin(), Q.end(), [&](vertex* &A, vertex* &B){ return dist[A] < dist[B]; });
                // for each neighboor vertex
                for(vertex *v : (*u)->neighboor){
                    
                    if( dist[*u] + edge[(*u)->name+"->"+v->name] < dist[v]) {
                        dist[v] = dist[*u] + edge[(*u)->name+"->"+v->name];
                        prev[v] = *u;
                    } 
                }
                Q.erase(u);
            }
        }
        void bellman_ford(){
            
            for (int i = 0 ; i < graph.size(); i++){
                // relax all edges
                map<string, int> :: iterator it;
                for (it = edge.begin(); it != edge.end(); it++ ){
                    string T = it->first;
                    string A = T.substr(0,1);
                    string B = T.substr(3,1);
                    if (dist[graph[A]] + it->second  < dist[graph[B]]){
                        dist[graph[B]] = dist[graph[A]] + it->second;
                        prev[graph[B]] = graph[A];
                    }
                }
            }
        }

        void show_distance(){
            map<vertex*, int> :: iterator  it;
            for (it = dist.begin(); it != dist.end(); it++ ){
                
                cout << "Distance from Source to " + it->first->name +" with previous vertex " + prev[it->first]->name  + " : " +  to_string(it->second) + "\n";
            }
        }
};



int main(void){

    Graph g = Graph();
    g.add_edge_from_to("A", "B", 3);
    g.edge["A->A"] = 0;
    g.dist[g.graph["A"]] = 0;
    g.prev[g.graph["A"]] = g.graph["A"];
    g.add_edge_from_to("A", "C", 5);
    g.add_edge_from_to("B", "D", 10);
    g.add_edge_from_to("C", "D", 13);
    g.add_edge_from_to("D", "E", 100);
    g.add_edge_from_to("B", "E", 50);
    g.add_edge_from_to("C", "E", 10);
    g.add_edge_from_to("A", "E", 200);
    g.dijkstra();
    //g.bellman_ford();
    g.show_distance();
    return 0;
}

