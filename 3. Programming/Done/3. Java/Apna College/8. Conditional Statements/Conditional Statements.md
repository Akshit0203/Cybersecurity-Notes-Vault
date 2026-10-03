
# If else

![image1](../../attachments/857d6b69ceec423a921ea19fbe20ea64.png)

```run-java
public class Main {
    public static void main(String[] args){
        int age = 16;
        if (age>=18) {
            System.out.println("adult : drive , vote");
        }
        else {
            System.out.println("not adult");
        }
    }
}

```


```
public class Main {
    public static void main(String[] args){
        int age = 16;
        if (age>=18) {
            System.out.println("adult : drive , vote");
        }

        if (age>=13 && age<18) {
            System.out.println("Teenager");
        }
        else {
            System.out.println("not adult");
        }
    }
}


Teenager
```

# Print the largest of 2 numbers 

```
public class Main {
    public static void main(String[] args){
        int A = 1;
        int B = 5;
        if (A>=B) {
            System.out.println("A is largest of 2");
        }
        else {
            System.out.println("B is largest of 2");
        }
    }
}


B is largest of 2
```

# Print if number is odd or even

```run-java
import java.util.*;

public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int number = sc.nextInt();

        if (number % 2 == 0) {
            System.out.println("number is even");
        } else {
            System.out.println("number is odd");
        }
    }
}
```

# Else if 

If the first 'if' is true then the 'else if' statement will not be checked
Only if the first 'if' is false then 'else if' will be checked

![image9](../../attachments/7aeaeb80f71747349b4ec40db05db6dc.png)

```run-java
import java.util.Scanner;
public class Main{
    public static void main(String args[]){
        int age = 13;
        if (age>18) {
            System.out.println("adult");
        }
        else if (age>=13 && age<18){
            System.out.println("teenager");
        }
        else {
            System.out.println("child");
        }
        }
    }
```

# Income Tax Calculator

![image15|294x307](../../attachments/6b320070efc447b88c72c5b057879b82.png)
![image16|337x323](../../attachments/4fb475e4f811433ea0144067d0f76cc8.png)

```java
import java.util.Scanner;
public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int income = sc.nextInt();
        if (income < 500000) {
            System.out.println("income tax is 0");
        } else if (income >= 500000 && income <= 1000000) {
            System.out.println("income tax is " + 0.2*income);
        } else {
            System.out.println("income tax is " + 0.3*income);
        }
        }
    }
```

```java
import java.util.Scanner;
public class Main{
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int income = sc.nextInt();
        int tax;

        if (income < 500000) {
            tax = 0;
        } else if (income >= 500000 && income <= 1000000) {
            tax = (int) (income * 0.2);
        } else {
            tax = (int) (income * 0.3);
        }
        System.out.println("your tax is " + tax);
        }
    }
```

# Print the largest of 3 numbers

```java
public class Main {
    public static void main(String args[]){
        int a=1 , b=3 , c=6;
        if (a>=b && a>=c) {
            System.out.println("greatest is " + a);
        }
        else if (b>=c) {
            System.out.println("greatest is " + b);
        }
        else {
            System.out.println("greatest is " + c);
        }
    }
}
```



![image18|424x315](../../attachments/305e87cd881f43d2bbf87ead43c03b68.png)
# <span style="color:rgb(255, 0, 0)">Ternary operator</span>

<span style="color:rgb(255, 0, 0)">Ternary operator is just "if else" combined in a single line</span>

the first "?" means check if the condition before it is true or false
if the condition is true , "statement 1" will be executed
else , "statement 2" will be executed

![image20](../../attachments/49f71348cf7e4d949b0ddc3d87076e03.png)

```
public class Main {
    public static void main(String args[]){
        int number = 4;
        //ternary operator
        String type = ((number%2) == 0) ? "even" : "odd";
        System.out.println(type);
    }
}
```

# Check if a student will Pass or Fail

![image22|453x284](../../attachments/51c4f956dabb43f8a04fe492ec7427b5.png)

```java
import java.util.Scanner;
public class Main {
    public static void main(String args[]){
        Scanner sc = new Scanner(System.in);
        int marks = sc.nextInt();
        String result = marks >= 33 ? "pass":"fail";
        System.out.println(result);
    }
}
```

# Switch statement 

![image24|300x377](../../attachments/b319532d24ff4e5d863a31784edc21e0.png)It matches value after case to variable
Example , if value of variable is 2 , case 2 gets printed

```java
public class Main {
    public static void main(String args[]){
        int number = 2;
        switch(number) {
            case 1 : System.out.println("samosa");
            case 2 : System.out.println("burger");
            case 3 : System.out.println("mango shake");
            default : System.out.println("we wake up");
        }
    }
}
```
What is after the case matches the value of number
If the value is matched it prints what is written in the case
Also , also <span style="color:rgb(255, 0, 0)">lines after the case gets printed if the case is matched</span>

```
public class Main {
    public static void main(String args[]){
        int number = 2;
        switch(number) {
            case 1 : System.out.println("samosa");
            case 2 : System.out.println("burger");
            case 3 : System.out.println("mango shake");
            break;
            default : System.out.println("we wake up");
        }
    }
}
```

```
burger
mango shake
```
To print only the line of the matched case ,
Break ;
Is added after each line

```
public class Main {
    public static void main(String args[]){
        char ch = 'a';
        switch(ch) {
            case 'd' : System.out.println("samosa");
            break;
            case 'c' : System.out.println("burger");
            break;
            case 'a' : System.out.println("mango shake");
            break;
            default : System.out.println("we wake up");
        }
    }
}
```
Characters can also be used instead of numbers
Or float values

# Calculator

In Java, the `Scanner` class has methods to read:

- `nextInt()` → integer
    
- `nextFloat()` → float
    
- `nextDouble()` → double
    
- `next()` → one word (String)
    
- `nextLine()` → whole line (String)
    

But <span style="color:rgb(255, 0, 0)">there is <b>NO method</b> called `nextChar()`.</span>

### ⭐ So how do we read a single character in Java?

We do it using this trick:

`char operator = sc.next().charAt(0);`

Let’s break this into 2 parts:

### 🔹 PART 1: `sc.next()`

`next()` returns a **String**.

Example:

If user types:

`+`

Then:

`sc.next() → "+"`

If user types:

`hello`

Then:

`sc.next() → "hello"`

So `next()` reads **one word** as a String.

---

### 🔹 PART 2: `charAt(0)`

Inside a String, characters are stored in positions:

`"h  e  l  l  o"  0  1  2  3  4   ← index numbers`

So:

- `"hello".charAt(0)` → `'h'`
    
- `"Java".charAt(0)` → `'J'`
    
- `"+" .charAt(0)` → `'+'`
    

---

### ⭐ Now combine both:

`sc.next().charAt(0)`

Example:

User types:

`+`

Step-by-step:

1. `sc.next()` → `"+"`
    
2. `.charAt(0)` → `'+'`
    

So you get **one character** from user input.

---

### 🎯 FINAL RESULT:

This line:

`char operator = sc.next().charAt(0);`

Means:

> “Read a word from the user, then take its first character.”

This is the **standard** way to read a char in Java.

```java
import java.util.Scanner;

public class Test {
    public static void main(String args[]) {
        Scanner sc = new Scanner(System.in);
        System.out.println("enter a : ");
        int a = sc.nextInt();
        System.out.println("enter b : ");
        int b = sc.nextInt();
        System.out.println("enter operator : ");
        char operator = sc.next().charAt(0);
        
    switch (operator) {
        case '+' : System.out.println(a+b);
        break ;
        case '-' : System.out.println(a-b);
        break ;
        case '*' : System.out.println(a*b);
        break ;
        case '/' : System.out.println(a/b);
        break ;
        case '%' : System.out.println(a%b);
        break ;
        default : System.out.println("wrong operator");
    }
    }
}
```

> **“If I just enter 1 letter, why do I still need `.charAt(0)`? Can't Java directly treat it as a char?”**

Let’s clarify this **VERY simply** 👇

---

# ✅ **1. Scanner.next() ALWAYS returns a String**

No matter what you type —  
even **ONE letter** —  
`next()` gives you a **String**, NOT a char.

Example:

You type:

`+`

Java still receives it as:

`"+"`

This is a **String**, not a char.

---

# ⚠️ You CANNOT store a String directly in a char:

`char operator = sc.next();   // ❌ ERROR`

Because:

- `sc.next()` → String
    
- `operator` → char
    

These types do not match.

---

# ✅ **2. `.charAt(0)` converts String → char**

If you typed `"+"`, then:

`sc.next()         → "+" sc.next().charAt(0) → '+'`

This extracts the **first (0th) character** from the string.