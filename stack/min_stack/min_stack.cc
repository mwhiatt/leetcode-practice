#include <stack>

using namespace std;

class MinStack {
private:
    stack<int> stck;
    stack<int> min;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        stck.push(val);
        if (min.empty() || val < min.top()) {
            min.push(val);
        } else {
            min.push(min.top());
        }
    }
    
    void pop() {
        stck.pop();
        min.pop();
    }
    
    int top() {
        return stck.top();
    }
    
    int getMin() {
        return min.top();
    }
};

/**
 * Your MinStack object will be instantiated and called as such:
 * MinStack* obj = new MinStack();
 * obj->push(val);
 * obj->pop();
 * int param_3 = obj->top();
 * int param_4 = obj->getMin();
 */