## Boilerplate code

```
public class JavaBasics {
    public static void main(String args[]) {
        //code here
    }
}
//boiler plate code
```
This template will stay same everywhere
## Output in Java

![image2](../../attachments/8c2b99dc992f4ff697184a40215fa81a.png)
ln - add line
\n - add line

```
public class JavaBasics {
    public static void main(String args[]) {
        System.out.println("Hello World");
        System.out.println("Hello World");
        System.out.println("Hello World");
    }
}
```

## Print a pattern

![image4](../../attachments/57130516cd7a463eaec832a5324a161b.png)

```
public class JavaBasics {
    public static void main(String args[]) {
        System.out.println("****");
        System.out.println("***");
        System.out.println("**");
        System.out.println("*");
    }
}
```
## Variables in Java

![image6](../../attachments/293865313ff6467abb8536653c2ea3b3.png)

Literals - whose values don’t change
Ex. \* , @ , 2

![image7](../../attachments/bce9fc5a5e1c452da1c8e823d0c542a5.png)
![image8](../../attachments/9c2392d613f7457ebb91ffe04210b4d7.png)

```
public class JavaBasics {
    public static void main(String args[]) {
        int a = 10;
        int b = 5;
        System.out.println(a);
        System.out.println(b);
        String name = "Tony Stark";
        System.out.println(name);
        a = 50;
        System.out.println(a);
    }
}
```
![image10](../../attachments/424049299cd74cf2b79fa6cc30a33173.png)
Can change variable value anytime

Note : we don’t have to print 'a' in double quotes , as it will print letter 'a' itself only
```
public class JavaBasics {
    public static void main(String args[]) {
        int a = 10;
        int b = 5;
        System.out.println("a");
    }
}
```
![image12](../../attachments/4c1a0ccdfba3461c9b51b2b3ee93661d.png)
## Data Types in Java

![image13](../../attachments/992922bc1f87486096756867868d5094.png)
### Primitive Data Types

These are the **built-in** data types in Java.  
They hold **simple values**, not objects.
There are **8 primitive types** grouped by category:

| Category           | Type      | Size              | Range                             | Example                               | Default Value |
| ------------------ | --------- | ----------------- | --------------------------------- | ------------------------------------- | ------------- |
| **Integer**        | `byte`    | 1 byte            | -128 to 127 (total 256 numbers)   | `byte age = 25;`                      | 0             |
|                    | `short`   | 2 bytes           | -32,768 to 32,767                 | `short salary = 32000;`               | 0             |
|                    | `int`     | 4 bytes           | -2,147,483,648 to 2,147,483,647   | `int population = 100000;`            | 0             |
|                    | `long`    | 8 bytes           | ±9 quintillion                    | `long worldPopulation = 8000000000L;` | 0L            |
| **Floating Point** | `float`   | 4 bytes           | ~6–7 decimal digits               | `float price = 9.99f;`                | 0.0f          |
|                    | `double`  | 8 bytes           | ~15 decimal digits                | `double pi = 3.1415926535;`           | 0.0d          |
| **Character**      | `char`    | 2 bytes           | Single Unicode character (a to z) | `char grade = 'A';`                   | '\u0000'      |
| **Boolean**        | `boolean` | 1 bit (virtually) | true or false                     | `boolean isOn = true;`                | false         |

### Non-Primitive Data Types

Also called **reference types** — they store **references (addresses)** to objects rather than the actual values.

| Type        | Description                      | Example                            |
| ----------- | -------------------------------- | ---------------------------------- |
| **String**  | Sequence of characters           | `String name = "Akshit";`          |
| **Arrays**  | Collection of similar data types | `int[] numbers = {1, 2, 3};`       |
| **Classes** | Blueprint for creating objects   | `class Car { ... }`                |
```
public class JavaBasics {
    public static void main(String args[]) {
        byte b = 8;
        System.out.println(b);
        char ch = 'a';
        System.out.println(ch);
        boolean var = false;
        float price = 25;
        int number = 25;
        short n = 240;
    }
}
```

![image15](../../attachments/1dcfb9690d194a40aab66886b1f92003.png)

## Sum of a and b

![image16](../../attachments/fd66e5412187422697222fa2293e13b0.png)

![image17](../../attachments/092c51fe6fa14797ba76154e562b188a.png)

```
public class JavaBasics {
    public static void main(String args[]) {
        int a = 10;
        int b = 5;
        int sum = a + b;
        System.out.println(sum);
    }
}
```

![image19](../../attachments/1baee5ecf2a24e7aa2d0f4ce76a24caa.png)
## Comments in java

That part of code that doesn’t get executed
![image20](../../attachments/a40292c4328e47d6b80633fa71f4a15c.png)

![image21](../../attachments/b69c02cfdb424613b2740a906d3c46b7.png)

## Input in java

```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String input = sc.next();
        System.out.println(input);
    }
}

hello
hello
```
java.util.* - comprises of all the pre made classes 
scanner here is a pre made class
"Scanner sc" - here , 'scanner' is class and 'sc' is the new object
"System.in" - to give input , tell to take an input
"sc.next()" - to take any input
"next()" - it is a function which stores input
"String input" - we will store the input in a string named input , 'input' is our variable here


```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String name = sc.nextLine();
        System.out.println(name);
    }
}

hello this is java
hello this is java
```
Next() - only prints a single word /till space
nextLine() - prints the entire line


```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        
        int number = sc.nextInt();
        System.out.println(number);

        float price = sc.nextFloat();
        System.out.println(price);
        
        Boolean number = sc.nextBoolean();
        System.out.println(number);
    }
}


4
4
3.14
3.14
true
true
```
to input integer we use "nextInt()"
"nextFloat()" for float value
we modify the next function according to the type of value we want to take input as

![image26](../../attachments/8a4a75aa452f47ca9e8544ea9d53cd46.png)

## Sum of a and b (input from user)


![image27](../../attachments/7120a0071bf548ddb9459c22aaaac90e.png)

```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int sum = a + b;
        System.out.println(sum);
    }
}
```

![image29](../../attachments/d2ac35235d2742b6a9a92517e6773af6.png)

# Product of a and b

![image30](../../attachments/49e4951e8385474c931173441a431f22.png)

```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int a = sc.nextInt();
        int b = sc.nextInt();
        int sum = a * b;
        System.out.println(sum);
    }
}
```

![image32](../../attachments/0d95d1829ded4bffaa7f53fda9454148.png)

# Area of a circle

![image33](../../attachments/131c49057ade467db2e4896d1ec14738.png)

![image34](../../attachments/82b7074f783b447bb714ef810e24b7b2.png)

![image35](../../attachments/9315101ceccb4cdebf88d64fd8fbed2b.png)

Add f after 3.14 to specify the value as float (or select the value as double)
**Any number with a decimal point is automatically a `double` unless you add `f`**
```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter radius");
        float radius = sc.nextFloat();
        float area = 3.14f * radius * radius;
        System.out.println("Area is " + area);
    }
}
```


![image37](../../attachments/5cbcd21dd2b4415f9498fda2e383a1e9.png)

# Type Conversion

```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        int a = 25;
        long b = a;
        System.out.println(b);
    }
}
```

![image39](../../attachments/83c9df8860f84f8b8b785448cf9d0a8f.png)

![image40](../../attachments/7966d578ebcc4447885fccda7fe00fe4.png)

Lossy conversion
Since some data will get lost
Due to transfer from 8 bytes to 4 bytes

# Type casting 

```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        float a = 25.22;
        int b = a;
        System.out.println(b);
    }
}
```

![image42](../../attachments/ccfe71f306434980a970ea6cfc206c68.png)

❌ **Error 1 — 25.22 is NOT a float**

`25.22` is **double** by default.
So Java sees this:
`float a = double value;`

This is illegal because **double → float** can lose precision.

Fix:
`float a = 25.22f;`
Add the `f` → now it’s a float literal.

---

❌ **Error 2 — You cannot directly convert float → int**

You wrote:
`int b = a;`

This is **not allowed** because:
- `float` has decimals
    
- `int` does NOT support decimals
    
- So this conversion **loses decimal information**
    

Java **blocks it** to prevent accidental data loss.
This is called:
👉 **lossy conversion: float → int**

---

✅ **How to fix it?**

You need to use **explicit casting**:

`float a = 25.22f; int b = (int) a;   // explicit cast System.out.println(b);`

---

🧠 Output:
`25`

Why 25?
Because converting float → int **removes the decimal part** (not round).

We now add "f" after decimal value
And put (int) before a
To forcefully convert the float value into integer

```
import java.util.*;
public class Main {
    public static void main(String[] args) {
        float a = 25.999f;
        int b = (int) a;
        System.out.println(b);
    }
}
```

![image44](../../attachments/dd3f20a59c8744ee8af54ea4d1e228a7.png)


Character's value's starts from 97
A = 97
B = 98….

```
public class Main {
    public static void main(String[] args) {
        char ch1 = 'a';
        char ch2 = 'b';
        int number1 = ch1;
        int number2 = ch2;
        System.out.println(number1);
        System.out.println(number2);
    }
}
```

![image46](../../attachments/43613c2076ec4d4eaa15c9aeb855085c.png)

![image47](../../attachments/573f203c8a49462fb0053eabf57c9c89.png)

# Type promotion in expressions


Important
1. When evaluation an expression - byte , short , char > integer
2. long , float , double > gets converted to largest one respectively

![image48](../../attachments/c21e9baf0ba844b6b030d9d48d7c3a55.png)

```
public class Main {
    public static void main(String[] args) {
        char a = 'a';
        char b = 'b';
        System.out.println(b - a);
    }
}


Output :
1
```


Here, the character "a" and "b" first gets converted to "int" value
Then subtracts

![image51](../../attachments/c8534074b60c4b789c916fbea804e974.png)

![image52](../../attachments/2b5faef207a8411a9f9ef02a51797b0e.png)

We are getting error of lossy conversion
So we do type casting to forcefully convert it to byte value

```
public class Main {
    public static void main(String[] args) {
        short a = 5;
        byte b = 25;
        char c = 'c';
        byte bt = (byte) (a + b + c);
        System.out.println(bt);
    }
}


-127
```

```
public class Main {
    public static void main(String[] args) {
        int a = 10;
        float b = 20.25f;
        long c = 25;
        double d = 30;
        double ans = a + b + c + d;
        System.out.println(ans);
    }
}



85.25
```

```
public class Main {
    public static void main(String[] args) {
        int a = 10;
        float b = 20.25f;
        long c = 25;
        double d = 30;
        double ans = (int) (a + b + c + d);
        System.out.println(ans);
    }
}


85.0
```



Here , we have to add "(byte)" before the expressions

Because if we don't add ,
Java will do type promotion and consider 'b' as an integer and not as a byte
and will do type promotion automatically since it a expression
so byte will get converted to int

![image59](../../attachments/0488713596e3420e9f10cbbbec774299.png)

Error code :

```
public class Main {
    public static void main(String[] args) {
        byte b = 5;
        byte a = b * 2;
        System.out.println(a);
    }
}


// since b*2 becomes an expression , 
```

![image61](../../attachments/ae6a16a6dc8c4d5b9cf4f4927b432203.png)

Correct code :

```
public class Main {
    public static void main(String[] args) {
        byte b = 5;
        byte a = (byte) (b * 2);
        System.out.println(a);
    }
}


10
```

# How does java code run ?

![image64](../../attachments/73dacaafa639438a8b7350cb30c6873a.png)

![image65](../../attachments/d5374bcc3c0046d4b584da2ccdc8183f.png)

JVM converts the byte code to native code i.e different for windows , linux , mac

c++ is not a portable language because after the code gets converted into a byte class , it will not run on every machine

But java's byte code (.class) will run on any machine
