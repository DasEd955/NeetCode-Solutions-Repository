class TimeMap {

    class ValueTime {

    String value = "";
    int timestamp = 0;

    public ValueTime() {}

    public ValueTime(String value, int timestamp) {
        this.value = value;
        this.timestamp = timestamp;
    }
    }

    HashMap<String, ArrayList<ValueTime>> kvtMap = new HashMap<>();

    public TimeMap() {
        //this.kvtMap = kvtMap;
    }
    
    public void set(String key, String value, int timestamp) {
        if(!kvtMap.containsKey(key)) {
            kvtMap.put(key, new ArrayList<>());
        }
        kvtMap.get(key).add(new ValueTime(value, timestamp));
    }
    
    public String get(String key, int timestamp) {

        if(!kvtMap.containsKey(key)) {return "";}

        int left = 0, right = kvtMap.get(key).size() - 1;

        while(left <= right) {
            int middle = left + (right - left) / 2;
            if(kvtMap.get(key).get(middle).timestamp == timestamp) {
                return kvtMap.get(key).get(middle).value;
            }
            else if(kvtMap.get(key).get(middle).timestamp < timestamp) {
                left = middle + 1;
            }
            else {
                right = middle - 1;
            }
        }
        
        if(right != -1) {
            return kvtMap.get(key).get(right).value;
        }
        else {
            return "";
        }
    }
}
