#ifndef TREE_H
#define TREE_H
#include "node.h"
class tree {
    public:
        node * root;
        tree(int data);
        void insert_node(int data);
        static node* max_node(node* root);
        static node* min_node(node* root);
        static node* successor_node(node *root);
        static void transplant(node* u, node* v);
        void delete_node(node* v);
        node* find_node(int data);
};

void in_order_travel(node * root);
#endif
