int max(int a, int b);
int min(int a, int b);

int maxArea(int* height, int heightSize){
    int l = 0;
    int r = heightSize - 1;
    int maxHeight = 0;
    for (int i = 0; i < heightSize; i++) {
        if (height[i] > maxHeight) {
            maxHeight = height[i];
        }
    }
    int area = 0;
    while (l < r) {
        area = max(area, min(height[l], height[r]) * (r-l));
        if (height[l] < height[r]) {
            l++;
        } else if (height[r] <= height[l]) {
            r--;
        }
        if (((r-l) * maxHeight) < area) {
            break;
        }
    }
    return area;
}

int max(int a, int b) {
    if (a > b) {
        return a;
    } else {
        return b;
    }
}

int min(int a, int b) {
    if (a < b) {
        return a;
    } else {
        return b;
    }
}