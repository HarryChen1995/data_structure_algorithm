#include "tree.h"
#include<iostream>

using namespace std;

int main(){

    tree t(12);
    t.insert_node(20);
    t.insert_node(100);
    t.insert_node(30);
    t.insert_node(1);
    in_order_travel(t.root);
    t.delete_node(t.find_node(30));
    cout << "\n";
    in_order_travel(t.root);
    
    return 0;

}
