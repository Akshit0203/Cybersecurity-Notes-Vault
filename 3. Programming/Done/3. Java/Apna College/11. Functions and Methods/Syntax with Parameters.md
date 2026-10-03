
Parameters = input of functions

To calculate sum
```
import java.util.*;
public class basics {
    public static void CalculateSum() {
        Scanner sc = new Scanner (System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int sum = a + b;
        System.out.println("Sum is " + sum);
    }
    public static void main(String[] args) {
        CalculateSum(); //calls function
    }
}
```


To take input in main code not function
```
import java.util.*;
public class basics {
    public static void CalculateSum(int num1 , int num2) {
        int sum = num1 + num2;
        System.out.println("Sum is " + sum);
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        CalculateSum(a, b);
    }
}
```


Printing the sum can also be done in the main function
Both the sum variables are different as they are of different functions
```
import java.util.*;
public class basics {
    
    public static int CalculateSum(int num1 , int num2) {
        int sum = num1 + num2;
        return sum;
    }
    public static void main(String[] args) {
        Scanner sc = new Scanner (System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int sum = CalculateSum(a, b);
        System.out.println("Sum is " + sum);
    }
}
```

