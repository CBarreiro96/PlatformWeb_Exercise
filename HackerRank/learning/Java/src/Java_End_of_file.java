import java.util.Scanner;

public class Java_End_of_file {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        for(int i = 1;sc.hasNext();i++)
        {
            System.out.println(i +" "+ sc.nextLine());
        }
        sc.close();
    }
}
