#include <iostream>
using namespace std;

//1
void reverseOrderOfList(Node *curNode) {
    Node *nextNode,*prevNode = NULL;
    while (curNode != NULL) {
        nextNode=curNode->next;
        curNode->next=prevNode;
        prevNode=curNode;
        curNode=nextNode;
    }
}

//2
bool isPowerOfTwo(int a) {
    return ((a > 0) && (a & (a - 1)) == 0);
}

//3
void swap(int a, int b) {
    a = a ^ b;
    b = a ^ b;
    a = a ^ b;
}

//4
void deleteNode(Node *node) {
    node->data = node->next->data;
    node->next = node->next->next;
}

//5
bool isListCircular(Node *node) {
    struct Node *nextNode = node->next;
    while (nextNode != NULL) {
        nextNode = nextNode->next;
        if (nextNode == node) {
            return true;
        }
    }
    return false;
}

//6
int insertBitSequence(int a, int b, int i, int j) {
    int leftMaskPart = (~0) << (j + 1);
    int rightMaskPart = (1 << i) - 1;
    int mask = leftMaskPart | rightMaskPart;
    int updatedA = a & mask;
    int updatedB = b << i;
    return updatedA | updatedB;
    
}
