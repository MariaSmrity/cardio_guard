# Cardio Guard

This is our project repo and regular updating (ie. whenever you make a working component or changes that others should see) is recommended. Also remember to regularly `git pull` to get changes from other group members and avoid merge conflicts.

## Getting started

### Setting up repository on command line
1. Keep on the Group 2 front page and click the blue `code` button on the right of the page. 
2. If you have an ssh key set to your git, copy the `ssh` address that is now shown or otherwise copy the `https` address. 
3. Now go to your terminal/command line and navigate to a folder of your choice
4. Type `git clone <repo address>`. If you chose the `https` address you may need to sign in to Gitlab at this point (will happen on command line also).
5. You should now see all the files in the repo and be able to add your own code!

### Make your own branch and start coding there
Create your own branch with command `git checkout -b <branch-name-here>`. Now your changes will not interfere withe others if you stick to your own branch. If you want to visit other branches, just type `git checkout <branch-name>`, no need for the -b option.

### Adding changes on command line
Whenever you want to share something for the group, you should add the to Git. This is fairly simple and requires three steps:
1. On command line, navigate to your project folder make sure youu are on `main` branch and type `git pull`. This pulls changes made and committed by others into your local files so they become up to date. `git pull`is also useful to do every time someone makes changes to avoid merge conflicts.
2. Next, switch to your own branch and type `git add <name of the file or directory to be added>`. This adds pieces of codes to the next `commit`(think it as a version of the project). The adds and commits do not change any files that weren't added but will overwrite those parts that were changed by you. 
3. `git commit -m "Short but informative description of your changes here"`to make a new local version of the project. At this point you have made a valid version that can be returned to later if you need to but it isn't yet shown to others neither is it visible in Gitlab.
4. To share the commit with others, type `git push`. You may need to sign in to Gitlab at this point but once the push is finished, the code will be available for others.
5. Finally, if you want to merge your code to the main project, create a merge request. For this, go to gitlab with your browser, click "merge requests" and "create a merge request". Fill in the important details and click "create merge request". Your part is done now, let others review and accept your code.

### Same with Git GUI
No clue, ask the internet or someone else but Essi can't help :)

## Merge conflict?!??
These happen when two people edit the same file at the same time. Git can solve some conflicts automatically but at times it has to be manually. You'll notice a merge conflict during `git pull` as it fails and complains you about merge conflicts. At this point conflict markings appear to your conflicting files and the easiest thing is to try figure them out manually. Delete the conflict markings and add the new code to your file so that it works with your changes. Finally try to `git pull` again. Merge conflicts can be tricky and super annoying sometimes so let's ask and offer each other help when needed. 

**!!! Never use --force or -f options if you are not 100% sure what you are doing! Particularly, do NEVER use -d or --delete without consulting the group first !!!**

