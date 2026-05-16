
# Types of operators

![image1](../../attachments/eab48f956946415ab1d09bdcae4e319c.png)

![image2](../../attachments/eaab61cf7be44563a27d7233759b0b18.png)

# Arithmetic Operators

Binary - 2 operands
Unary - single operand

![image3](../../attachments/dbf77f6046af40718972c5a72df64b24.png)

```
public class Main {
    public static void main(String[] args){
        int A = 10;
        int B = 5;
        System.out.println("modulo(remainder) = " + (A%B));
    }
}
```

# Unary Operators

![image5](../../attachments/de904ee9d5164d1a9e61ff010ef2b52f.png)

![image6](../../attachments/f6c81609b54c4e5fa89538ab60925d7c.png)


✅ **1. `++a` → PREFIX (Increment first, use later)**

Meaning:
> Increase `a` **first**,  
> then use the new value.
### Example:
`int a = 10; System.out.println(++a);`

Step-by-step:
- First: `a` becomes `11`
    
- Then: print `11`
    
### Output:
`11`

---

✅ **2. `a++` → POSTFIX (Use first, increment later)**
### Meaning:
> Use the value **first**,  
> then increase it.
### Example:
`int a = 10; System.out.println(a++);`

Step-by-step:

- First: print `10`
    
- Then: `a` becomes `11`
    
### Output:
`10`

---

# 🎯 SUPER SIMPLE SUMMARY

|Expression|When increment happens|Printed value|
|---|---|---|
|`++a`|BEFORE printing|prints **11**|
|`a++`|AFTER printing|prints **10**|

Both result in `a = 11` after the line runs —  
the only difference is **when** the increment occurs.

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = ++a;
        System.out.println(a);
        System.out.println(b);
    }
}


11
11
```

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = a++;
        System.out.println(a);
        System.out.println(b);
    }
}


11
10
```


```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = --a;
        System.out.println(a);
        System.out.println(b);
    }
}


9
9
```

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = a--;
        System.out.println(a);
        System.out.println(b);
    }
}


9
10
```


![image15](../../attachments/ec48308223164ba5a67492bffd05d0b7.png)

# Relational Operators

![image16](../../attachments/908774980cda43bdb88ae5d7d0a8b82c.png)

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = 10;
        System.out.println(a == b);
    }
}


true
```

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = 5;
        System.out.println(a == b);
    }
}

false
```

![image21](../../attachments/9fc51491685a4bada2e130239096bdea.png)

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = 10;
        System.out.println(a != b);
    }
}


false
```

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = 5;
        System.out.println(a != b);
    }
}


true
```


![image26](../../attachments/ef85252ed87445d1b3fe85df79cc0a37.png)

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = 5;
        System.out.println(a > b);
    }
}



true
```

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = 5;
        System.out.println(a < b);
    }
}



false
```

![image31](../../attachments/97d896c056d749ec991bb7d74bae432c.png)

```
public class Main {
    public static void main(String[] args){
        int a = 10;
        int b = 5;
        System.out.println(a <= b);
    }
}



false
```

# Logical Operators

![image34](../../attachments/b58de54bf5cd4d938695c8645dc11ac3.png)

```
public class Main {
    public static void main(String[] args){
        System.out.println( (3>2) && (5>0));
    }
}


true
```

```
public class Main {
    public static void main(String[] args){
        System.out.println( (3<2) && (5>0));
    }
}


false
```


![image39](../../attachments/cbb0164ec686484b869bf83acd7c4e95.png)

![image40](../../attachments/3aea801890ae4656b5abe98592b359e8.png)

```
public class Main {
    public static void main(String[] args){
        System.out.println( (3<2) || (5<0));
    }
}


false
```


```
public class Main {
    public static void main(String[] args){
        System.out.println( (3<2) || (5>0));
    }
}


true
```

![image45](../../attachments/52f5e10fc1e0479faaa8d1a9bb1d49df.png)

Logical NOT converts a true value to false 
and a false value to true

Just put it in front of a expression 

![image46](../../attachments/7abe291adf094070b67fc3f82e46b641.png)

```
public class Main {
    public static void main(String[] args){
        System.out.println( !(3>2));
    }
}


false
```

```
public class Main {
    public static void main(String[] args){
        System.out.println( !(0>5));
    }
}


true
```


# Assignment Operators

![image51](../../attachments/2dda8f025d084fc2a8e3723546a6b93f.png)

![image52](../../attachments/cc87fbb5ae3841149b90190d94b4ab2b.png)


```
public class Main {
    public static void main(String[] args){
        int A = 10;
        A = A + 10;
        System.out.println(A);
    }
}


20
```

```
public class Main {
    public static void main(String[] args){
        int A = 10;
        //A = A + 10;
        A += 10; //Faster execution
        System.out.println(A);
    }
}


20
```

```
public class Main {
    public static void main(String[] args){
        int B = 5;
        // B = B -5;
        B -= 5;
        System.out.println(B);
    }
}


0
```


```
public class Main {
    public static void main(String[] args){
        int B = 5;
        B *= 5; // B = B * 5;
        System.out.println(B);
    }
}


25
```

```
public class Main {
    public static void main(String[] args){
        int B = 5;
        B /= 5;
        System.out.println(B);
    }
}

1
```

```
public class Main {
    public static void main(String[] args){
        int B = 5;
        B %= 5;
        System.out.println(B);
    }
}

0
```

