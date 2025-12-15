# While loop

execute the statement till the condition is true

![image1|585x245](../../attachments/d94ed52620e34407b998283fc64bddc7.png)

```java
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        int counter = 0;
        while(counter < 10){
            System.out.println("Hello world");
            counter++;
        }
        System.out.println("printed hw 10x");
        }
}
```

```java
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        int counter = 0;
        while(true){
            System.out.println(counter);
            counter++;
        }
        }
}
```
We can write (true) to print infinitely

# Print numbers from 1 to 10

```java
public class Main {
    public static void main(String args[]) {
        int a = 1;
        while ( a <= 10) {
            System.out.println(a);
            a++;
        }
        }
}
```

```java
public class Main {
    public static void main(String args[]) {
        int a = 1;
        while ( a <= 10) {
            System.out.print(a + " ");
            a++;
        }
        }
}
```

```
1 2 3 4 5 6 7 8 9 10 
```
# Print numbers from 1 to n

```java
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int a = 1;
        while ( a <= n) {
            System.out.print(a + " ");
            a++;
        }
        }
}
```

```
9
1 2 3 4 5 6 7 8 9 
```
# Sum of first N natural numbers

```
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        int n = sc.nextInt();
        int i = 1;
        int sum = 0;
        while ( i <= n) {
            sum = sum + i;
            i++;
        }
        System.out.println("sum of first " + n + " natural numbers is: " + sum);
        }
}
```

```
3
sum of first 3 natural numbers is: 6
```
# For loop

![image8](../../attachments/27e527d9461e4ac293ce133ec73da02b.png)

```java
public class Main {
    public static void main(String args[]) {
        for(int i=1;i<=10;i++){
            System.out.println("hello world");
        }
        }
}
```

# Print a square pattern 

![image10](../../attachments/87afb5bca753443e8121cbd4806ec4b0.png)

```
public class Main {
    public static void main(String args[]) {
        for(int i=1;i<=4;i++){
            System.out.println("****");
        }
        }
}
```

```
****
****
****
****
```

# Print reverse of a number

![image13](../../attachments/db46178784e241b8826e8c87182641af.png)

```
import java.util.Scanner;

public class Main {
    public static void main(String args[]) {
        int n = 10899;

        while (n > 0) {
            int lastdigit = n % 10;
            System.out.print(lastdigit);
            n = n /10; // n is getting smaller every time
        }
        }
}
```

![image15](../../attachments/db7fff3893cd48dba339b393d95b5060.png)

# Reverse the given number

![image16](../../attachments/1cfd66b9a05a4d0885191072945670f3.png)

![image17](../../attachments/24aaa5b378b84efd90becc7d17edec34.png)

![image18](../../attachments/6aacaa3004c849309617c49272d52527.png)

![image19](../../attachments/511a31fe3714438e94dbc06171d3d72f.png)

![image20](../../attachments/7274ee71a2a449fbb24e607ece6d6111.png)

![image21](../../attachments/45c80f25bea44debbce2e40ed2b8ed58.png)

![image22](../../attachments/3447291c00784f4e8771187b9349cdb2.png)

![image23](../../attachments/b0ad59be981943748d72dd6fbfddf8e9.png)

# Do while loop

![image24](../../attachments/50c86db107fe461287b600762c1f9d83.png)

![image25](../../attachments/40e8f03e51184ee5961378d36154eef2.png)

# Break statement

![image26](../../attachments/a0d47448489e4c7ab70c84a34140318d.png)

![image27](../../attachments/d92ba7b4e45b417f9ebd5558b186ec69.png)

# Question - break keyword

![image28](../../attachments/89f38dbe5e124aa6aed9e3ff58bfbb52.png)

![image29](../../attachments/9ba484007bd648d99c305d1628ae21af.png)

# Continue statement

![image30](../../attachments/770d66a6161e4159b966ffab097a1df0.png)

![image31](../../attachments/7e49d6ff2fdd430598eb94ef7501b384.png)

# Question - continue keyword

![image32](../../attachments/1f33ced18af94e8c93fcaa56285c6099.png)

![image33](../../attachments/ba3dda32ed5a4cbead45dbfe44d2fbac.png)

# Check if a number is prime or not 

![image34](../../attachments/93565ef76ac64be2877f53228b66f593.png)

![image35](../../attachments/d4ded7c2c35d4da0b814e839c4c941dc.png)

![image36](../../attachments/d0cc57fcf53f4e16ab998cbd11269881.png)

![image37](../../attachments/b253d5f1ca5246338ccdff9388fcc435.png)

