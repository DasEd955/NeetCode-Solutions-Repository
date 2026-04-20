class Twitter {

    private int count = 0;
    Map<Integer, Set<Integer>> following;
    Map<Integer, List<int[]>> tweets;

    public Twitter() {
        this.count = 0;
        this.following = new HashMap<>();
        this.tweets = new HashMap<>();
    }
    
    public void postTweet(int userId, int tweetId) {
        this.tweets.putIfAbsent(userId, new ArrayList<>());
        if(this.tweets.get(userId).size() > 10) {
            this.tweets.get(userId).remove(0);
        }
        this.tweets.get(userId).add(new int[]{count--, tweetId});
    }
    
    public List<Integer> getNewsFeed(int userId) {
        List<Integer> result = new ArrayList<>();
        PriorityQueue<int[]> minHeap = new PriorityQueue<>(Comparator.comparingInt(a -> a[0]));

        this.following.computeIfAbsent(userId, k -> new HashSet<>()).add(userId);
        for(int followeeId : this.following.get(userId)) {
            if(this.tweets.containsKey(followeeId)) {
                List<int[]> tweets = this.tweets.get(followeeId);
                int index = tweets.size() - 1;
                int[] tweet = tweets.get(index);
                minHeap.offer(new int[]{tweet[0], tweet[1], followeeId, index});
            }
        }

        while(!minHeap.isEmpty() && result.size() < 10) {
            int[] current = minHeap.poll();
            result.add(current[1]);
            int index = current[3];
            if(index > 0) {
                int[] tweet = this.tweets.get(current[2]).get(index - 1);
                minHeap.offer(new int[]{tweet[0], tweet[1], current[2], index - 1});
            }
        }

        return result;
    }
    
    public void follow(int followerId, int followeeId) {
        this.following.computeIfAbsent(followerId, k -> new HashSet<>()).add(followeeId);
    }
    
    public void unfollow(int followerId, int followeeId) {
        this.following.computeIfPresent(followerId, (k, v) -> {
            v.remove(followeeId);
            return v;
        });
    }
}
