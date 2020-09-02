#include "node.h"
#include<iostream>
node:: node(int data){
    this->data = data;
    this->parent = NULL;
    this->left = NULL;
    this->right = NULL;
}

