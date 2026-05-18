
If we are pushing a repo online 

and we want some files to never get pushed online

we add a ".gitignore" file and in that we mention the names of all the files which we do not want to upload

![image-107.png](attachments/image-107.png)

"*.log" means all files will be ignored

![image-108.png](attachments/image-108.png)
if we do 'git status'
if says untracked file is only one 
even though we had created many files
this is because all new files are in ".gitignore" file 

![image-109.png](attachments/image-109.png)

```
git status
git add .gitignore
git commit -m "Adding gitignore file"
git push
```



