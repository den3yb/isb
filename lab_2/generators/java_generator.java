import java.util.Random;

public class random_generator{
    public static void RandomNumberGenerator() {
        Random random = new Random();
        System.out.print(random.nextInt(2));
    }

    public static void main(String[] args) {
        int size =128;
        for(int i = 0; i<size;i++){
            RandomNumberGenerator();
        }
    }
}