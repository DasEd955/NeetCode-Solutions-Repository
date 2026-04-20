class MedianFinder {

    PriorityQueue<Integer> minHeap, maxHeap;

    public MedianFinder() {
        this.minHeap = new PriorityQueue<>();
        this.maxHeap = new PriorityQueue<>();
    }
    
    public void addNum(int num) {
        if(!this.minHeap.isEmpty() && num > this.minHeap.peek()) {
            this.minHeap.offer(num);
        }
        else {
            this.maxHeap.offer(-1 * num);
        }

        if(this.minHeap.size() > this.maxHeap.size() + 1) {
            int popped = this.minHeap.poll();
            this.maxHeap.offer(-1 * popped);
        }
        if(this.maxHeap.size() > this.minHeap.size() + 1) {
            int popped = -this.maxHeap.poll();
            this.minHeap.offer(popped);
        }
    }
    
    public double findMedian() {
        if(this.minHeap.size() == this.maxHeap.size()) {
            return (this.minHeap.peek() + (double)(-this.maxHeap.peek())) / 2;
        }
        else if(this.minHeap.size() > this.maxHeap.size()) {
            return this.minHeap.peek();
        }
        else {
            return -1 * this.maxHeap.peek();
        }
    }
}
