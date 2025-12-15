[Conditional Questions.pdf](530b267a110e4cd1b226e7f904c1c630.pdf)
![image1](../../attachments/412baa5bffb241cfbd5ea069804b6d5e.png)![image2](../../attachments/4f19529781a24f51a66138e40b48bd19.png)[Conditional Solutions.pdf](b83418daa18545f1adb4479d0235441f.pdf)![image3](../../attachments/e995856175f84814a6801c570aac21c5.png)![image4](../../attachments/a400175b692343bb81c5cfc6e7a7d47e.png)![image5](../../attachments/df81ee9eb438462383d22968e802f7b9.png)
Q1
```java
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        if (a >= 0) {
            System.out.println("positive");
        } else {
                System.out.println("Negative");
            }
        }
    }
```

Q2
```java
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        double temp = 103.5;
        if (temp>100) {
            System.out.println("you have fever");
        } else {
            System.out.println("no fever");
        }
        }
    }
```

Q3
```java
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter week day number");
        int n = sc.nextInt();

        switch (n) {
        case (1) : System.out.println("monday");
        break;
        case (2) : System.out.println("tuesday");
        break;
        case (3) : System.out.println("wednesday");
        break;
        case (4) : System.out.println("thursday");
        break;
        case (5) : System.out.println("friday");
        break;
        case (6) : System.out.println("saturday");
        break;
        case (7) : System.out.println("sunday");
        default : System.out.println("enter a valid day of week (between 1 to 7)");
        }
        }
}
```


Q5
```java
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter year");
        int year = sc.nextInt();
        if ((year % 400 ==0) || (year % 4 == 0 && year % 100 != 0)) {
            System.out.println("leap year");
        } else {
            System.out.println("not a leap year");
        }
        }
}
```

A year is a leap year if:
1) divisible by 400  → leap  
OR  
2) divisible by 4 AND not divisible by 100 → leap

