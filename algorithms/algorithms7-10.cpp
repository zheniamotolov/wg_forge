//1
struct MinHeapNode {
    int v;
    int key;
};

struct MinHeap {
    int size;
    int capacity;
    int* pos;
    struct MinHeapNode** array;
};
void minHeapify( MinHeap* minHeap, int idx)
{
    int smallest, left, right;
    smallest = idx;
    left = 2 * idx + 1;
    right = 2 * idx + 2;
    
    if (left < minHeap->size && minHeap->array[left]->key < minHeap->array[smallest]->key)
        smallest = left;
    
    if (right < minHeap->size && minHeap->array[right]->key < minHeap->array[smallest]->key)
        smallest = right;
    
    if (smallest != idx) {
        MinHeapNode* smallestNode = minHeap->array[smallest];
        MinHeapNode* idxNode = minHeap->array[idx];
        minHeap->pos[smallestNode->v] = idx;
        minHeap->pos[idxNode->v] = smallest;
        swapMinHeapNode(&minHeap->array[smallest], &minHeap->array[idx]);
        minHeapify(minHeap, smallest);
    }
}
 MinHeapNode* extractMin( MinHeap* minHeap)
{
    if (isEmpty(minHeap))
        return NULL;

    MinHeapNode* root = minHeap->array[0];
    MinHeapNode* lastNode = minHeap->array[minHeap->size - 1];
    minHeap->array[0] = lastNode;
    minHeap->pos[root->v] = minHeap->size - 1;
    minHeap->pos[lastNode->v] = 0;
    --minHeap->size;
    minHeapify(minHeap, 0);
    
    return root;
}
void updateToLowereKey( MinHeap* minHeap, int v, int key)
{
    int i = minHeap->position[v]
    minHeap->array[i]->key = key;

    while (i && minHeap->array[i]->key < minHeap->array[(i - 1) / 2]->key) {
        minHeap->pos[minHeap->array[i]->v] = (i - 1) / 2;
        minHeap->pos[minHeap->array[(i - 1) / 2]->v] = i;
        swapMinHeapNode(&minHeap->array[i], &minHeap->array[(i - 1) / 2]);
        i = (i - 1) / 2;
    }
}
bool isInMinHeap( MinHeap* minHeap, int v)
{
    if (minHeap->pos[v] < minHeap->size)
        return true;
    return false;
}

int[] Prim(Graph){
    int mst[v_num];
    int keys[v_num];
    for (int v = 1; v < v_num; ++v) {
        mst[v] = -1;
        keys[v] = INT_MAX; //min weight of adjasent edge
        minHeap->array[v] = new MinHeapNode(v, key[v]);
        minHeap->pos[v] = v;
    }
    // init to start alorithm
    keys[0] = 0;
    minHeap->array[0] = new MinHeapNode(0, key[0]);
    minHeap->pos[0] = 0;
    
    while (!isEmpty(minHeap)) {
        MinHeapNode* minHeapNode = extractMin(minHeap);
        AdjListNode* adjList = graph->array[u].head;
        while (adjList != NULL) {
            int v = adjList->curr_vertex;
            
            if (isInMinHeap(minHeap, v) && adjList->weight < key[v]) {
                key[v] = adjList->weight;
                parent[v] = u;
                updateToLowereKey(minHeap, v, key[v]);
            }
            adjList = adjList->next;
        }
    }
return mst
    
}
//2
O(E*(V+E))
