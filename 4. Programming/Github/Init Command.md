
**init - used to create a new git repo**

```
git init
git remote add origin <- link ->
git remote -v (to verify remote)
git branch (to check branch)
git branch -M main (to rename branch)
git push origin main
```

```
cd ..
mkdir LocalRepo
```

![image-33.png](attachments/image-33.png)

```
cd LocalRepo
```

![image-34.png](attachments/image-34.png)
We first have to make it a git repo
we know its not a git repo currently because when we check all the hidden files in the folder we dont find any git file

![image-35.png](attachments/image-35.png)

```
git init
```
to initialize git repository

![image-36.png](attachments/image-36.png)
make 2 files and check status

![image-37.png](attachments/image-37.png)

![image-38.png](attachments/image-38.png)
All these changer were made still on Local system

to do that first make a new repo

![image-39.png](attachments/image-39.png)

![image-40.png](attachments/image-40.png)

dont initialise readme right now 
because if we do , we have to make it in our local system also



```
git remote add origin <- link ->
```
![image-41.png](attachments/image-41.png)
set origin first



```
git remote -v (to verify remote)
```
![image-42.png](attachments/image-42.png)
to verify remote


```
git branch (to check branch)
```
![image-43.png](attachments/image-43.png)


```
git branch -M main (to rename branch)
```


```
git push -u origin main
```
![image-45.png](attachments/image-45.png)
-u to set as primary 
so next time onwards we can just write "git push" and it knows which branch to put into

![image-46.png](attachments/image-46.png)

![image-47.png](attachments/image-47.png)

