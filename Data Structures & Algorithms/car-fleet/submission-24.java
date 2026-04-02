class Solution {
    public int carFleet(int target, int[] position, int[] speed) {

        class Car {
            public int position, speed;
            public Car(int position, int speed) {
                this.position = position;
                this.speed = speed;
            }
        }

        ArrayList<Car> svArray = new ArrayList<>();
        Stack<Double> stack = new Stack<>();

        for(int i = 0; i < position.length; i++) {
            svArray.add(new Car(position[i], speed[i]));
        }

        if(svArray.size() == 1) {
            return 1;
        }

        svArray.sort((a, b) -> b.position - a.position);
        
        for(Car car : svArray) {
            double time = (double)(target - car.position) / car.speed;
            if(stack.isEmpty() || stack.peek() < time) {
                stack.push(time);
            }
        }

        return stack.size();
    }
}
