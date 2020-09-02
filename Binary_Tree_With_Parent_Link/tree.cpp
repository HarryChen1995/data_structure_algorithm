#include "tree.h"
#include<iostream>
tree::tree(int data){
    this->root = new node(data);
}
void tree::insert_node(int data){
    node * current = root;
    node * parent = NULL;
    while(current != NULL){
        parent = current;
        if (data <current->data){
            current = current->left;
        } 
        else{
            current = current->right;
        }
    }
    node * inserted_node = new node(data);
    inserted_node->parent = parent;
    if (parent == NULL){
        this->root = inserted_node;
    }
    else if (data < parent->data){
        parent->left = inserted_node;
    }
    else{
        parent->right = inserted_node;
    }
}
node* tree::max_node(node* root){
    node* current = root;
    while(current->right != NULL){
        current = current->right;
    }
    return current;
}
node* tree:: min_node(node* root){
    node* current = root;
    while(current->left != NULL){
        current = current->left;
    }
    return current;
}
node* tree::successor_node(node* root){
    if (root == NULL){
        return root;
    }
    node * current = root;
    if(current->right != NULL){
        current = current->right;
        tree::min_node(current);
        std::cout << "good\n";
    }
    node * parent = current->parent;
    while((parent != NULL) && (current == parent->right)){
        current = parent;
        parent = current->parent;
    }
    return parent;

}
void tree:: transplant(node* u, node* v){
    if (u == u->parent->right){
        u->parent->right = v;
    }else{
       u->parent->left = v;
    }
    if (v != NULL){
        v->parent = u->parent;
    }
}
void tree::delete_node(node* v){
    if (v->right == NULL){
        tree::transplant(v,v->left);
    }else if (v->left == NULL){
        tree::transplant(v,v->right);
    }else{
        node* successor = tree::successor_node(v);
        if(successor != v->right){
        tree::transplant(successor, successor->right);
        successor->right = v->right;
        v->right->parent = successor;
        }
        tree::transplant(v,successor);
        successor->left = v->left;
        v->left->parent = successor;
    
   }
}
void in_order_travel(node * root){
    if (root != NULL){
    in_order_travel(root->left);
    std::cout << root->data << "\n";
    in_order_travel(root->right);
    }
}

node* tree::find_node(int data){
    if (this->root==NULL){
        return this->root;
    }
    node* current = this->root;
    while(current != NULL){
        if(current->data == data){
            return current;
        }else if (data < current->data){
            current = current->left;
        }else{
            current = current->right;
        }
    }
    return current;
}


