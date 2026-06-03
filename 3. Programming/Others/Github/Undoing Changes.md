
## Case 1: staged changes ("add" but not "commit")

i.e changed which have been "add" but not "commit"
```
git reset <- file name ->
git reset
```

![image-80.png](attachments/image-80.png)
if we delete a line and add it

```
git reset
```

![image-81.png](attachments/image-81.png)

The changes now are removed of 'add'
so we have to first 'add' now then 'commit'

## Case 2: committed changes (for one commit)

```
git reset HEAD~1
```

If we "add" and "commit" both mistakenly
![image-82.png](attachments/image-82.png)

![image-83.png](attachments/image-83.png)
undo change of latest commit
and restore to second last commit

![image-84.png](attachments/image-84.png)
now the old change will become latest change

![image-85.png](attachments/image-85.png)
now the change has reset to the stage before "add"

we can use 
```
git log
```
to check the history of commits
![image-86.png](attachments/image-86.png)
press "q" to quit

## Case 3: committed changes (for many commits)
```
git reset <- commit hash ->
git reset --hard <- commit hash ->
```

![image-87.png](attachments/image-87.png)
If we don't want to go only 1 commit before 
rather , 'n' number of commits before

![image-88.png](attachments/image-88.png)

hash of a particular commit can be found using
```
git log
```

![image-89.png](attachments/image-89.png)

![image-90.png](attachments/image-90.png)

now our "HEAD" has been changed and we have gotten to the mentioned commit


![image-91.png](attachments/image-91.png)

add "--hard" to remove all visible changes from local machine and GitHub after the rest commit

