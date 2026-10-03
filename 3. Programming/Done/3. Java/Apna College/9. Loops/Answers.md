# ANS 1

Hello is printed 2 times.

# ANS 2 

import java.util.Scanner;
public class basics {
public static void main(String\[\] args) {
Scanner scanner = new Scanner(System.in);
int evenSum = 0;
int oddSum = 0;
System.out.println("enter integers (enter 0 to stop): ");
while(true) {
int num = scanner.nextInt();
if (num == 0){
break;
}
if (num % 2 == 0) {
evenSum += num;
} else {
oddSum += num;
}
}
System.out.println("sum of even numbers: " + evenSum);
System.out.println("sum of odd number " + oddSum);
scanner.close();
}
}

# ANS 3

![image1](../../attachments/953acaee8c784e1eb2cec6659b18b84f.png)

# ANS 4

![image2](../../attachments/7a021a0fa96d4d049dc86155dde79fde.png)

# ANS 5 

![image3](../../attachments/9b774dd678654ccaa77077eb6024258b.png)

![image4](../../attachments/5ea3ed479c154d0f9c7f221a34c9ffcf.png)

