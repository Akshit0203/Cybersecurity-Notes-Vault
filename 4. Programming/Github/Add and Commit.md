
## Add

add - adds new or changed files in your working directory to the Git staging area.
```
git add <- file name->
```

![image-22.png](attachments/image-22.png)

![image-23.png](attachments/image-23.png)

```
git add README.md
git add .  #the "." here specifies to change all files at once
```

![image-24.png](attachments/image-24.png)

All the changes are now ready to be commited

## Commit

commit - it is the record of change
```
git commit -m "some message"
```

![image-25.png](attachments/image-25.png)

It says "your branch is ahead of 'origin/main by 1 commit"

Which means the files are updated in local machine but not on GitHub 

![image-26.png](attachments/image-26.png)

no new "index.html" here

so for this we will use push command