import java.util.Random;

public class random_generator{
    public static void RandomNumberGenerator(int size) {
        Random random = new Random();
        for(int i = 0; i<size;i++){
            System.out.print(random.nextInt(2));
        }
    }

    public static void main(String[] args) {
        RandomNumberGenerator(128);
    }
}