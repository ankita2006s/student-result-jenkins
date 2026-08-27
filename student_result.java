import java.util.Scanner;

public class student_result {

    public static void main(String[] args) {

        Scanner sc = new Scanner(System.in);

        System.out.println("===== Student Result System =====");

        System.out.print("Enter Student Name: ");
        String name = sc.nextLine();

        System.out.print("Enter Roll Number: ");
        int rollNo = sc.nextInt();

        System.out.print("Enter marks for Subject 1: ");
        int sub1 = sc.nextInt();

        System.out.print("Enter marks for Subject 2: ");
        int sub2 = sc.nextInt();

        System.out.print("Enter marks for Subject 3: ");
        int sub3 = sc.nextInt();

        int total = sub1 + sub2 + sub3;
        double percentage = total / 3.0;

        System.out.println("\n===== Student Result =====");
        System.out.println("Name       : " + name);
        System.out.println("Roll Number: " + rollNo);
        System.out.println("Total Marks: " + total);
        System.out.printf("Percentage : %.2f%%\n", percentage);

        if (sub1 >= 35 && sub2 >= 35 && sub3 >= 35) {
            System.out.println("Result     : PASS");

            if (percentage >= 75) {
                System.out.println("Grade      : A");
            } else if (percentage >= 60) {
                System.out.println("Grade      : B");
            } else if (percentage >= 50) {
                System.out.println("Grade      : C");
            } else {
                System.out.println("Grade      : D");
            }

        } else {
            System.out.println("Result     : FAIL");
            System.out.println("Grade      : F");
        }

        sc.close();
    }
}