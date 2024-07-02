import java.util.concurrent.CountDownLatch;

public class CarService {
    public static void main(String[] args) throws InterruptedException {
        CountDownLatch carService = new CountDownLatch(3);

        // Kitchen tasks for each course
        new Thread(new CookingTask("OilChange", carService)).start();
        new Thread(new CookingTask("TireRotation", carService)).start();
        new Thread(new CookingTask("15-Point Inspection", carService)).start();

        // Wait for all courses to be ready
        carService.await();

        System.out.println("Your oil change is complete.");
    }
}

class CookingTask implements Runnable {
    private final String course;
    private final CountDownLatch latch;

    public CookingTask(String course, CountDownLatch latch) {
        this.course = course;
        this.latch = latch;
    }

    @Override
    public void run() {
        // Simulate cooking time
        try {
            Thread.sleep((long) (Math.random() * 1000));
            System.out.println(course + " is ready!");
            latch.countDown(); // Signal that this course is ready
        } catch (InterruptedException e) {
            Thread.currentThread().interrupt();
        }
    }
}
