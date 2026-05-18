
An event that takes place when Git is unable to automatically resolve differences in code between two commits.

![image-69.png](attachments/image-69.png)
In main , this code is there 
we added a "(button)" text and then 'add' and 'commit'

![image-70.png](attachments/image-70.png)
now we switch to 'feature1' branch 
and add 'dropdown' text here
then 'add' and 'push'

![image-71.png](attachments/image-71.png)
now we check the differences between both the branches using
```
git diff main
```


## To merge now

![image-72.png](attachments/image-72.png)

```
git merge main (name of the other branch here to which we want to merge)
```

the vs code will show error now
these are known as conflicts

It gives options to resolve conflicts 
![image-73.png](attachments/image-73.png)

'Accept current change' - the current change/newest change is kept and overwritten on older ones
'Accept incoming change' - the older changes are overwritten on newer ones

in order to manually do , we need to remove the extra lines first which have come

![image-74.png](attachments/image-74.png)

These 3 lines are new and need to be removed

after removing :
![image-75.png](attachments/image-75.png)

now if we save from here , that means we need both of the features

if we remove 1 line and keep other , the other change stays

We keep both in this case and check status :
![image-76.png](attachments/image-76.png)

now add and commit both the features
![image-77.png](attachments/image-77.png)





```
git checkout main
```

When we shift to main branch now , we see that the features from feature1 branch are not since 
since main branch was merged with feature1 and not vice versa

we merge feature 1 with main now 
![image-78.png](attachments/image-78.png)

now we have resolved conflicts 
and now both will be updated on github 

![image-79.png](attachments/image-79.png)


