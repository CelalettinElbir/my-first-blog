# my-first-blog

### What can you do?

1. User can register, login , logout 
2. Authenticated users can create a post and update their posts.
3. User is able to filter posts by categories.
4. User can go detail page of a specific post and see additional information. 
5. Authenticated users can delete their posts.


### How to Install and Run the Project
#### Packages
1. Django==3.1.6
2. Django-crispy-forms==1.11.1
3. Pillow==8.1.1
#### Installing 
1. you need to install the packages specified above. 
2. you should go to the directory where manage.py exists and run the commands 'make makemigrations' and 'migrate'.
3. run the command 'manage.py runserver' now you can see my website at http://127.0.0.1:8000/.


### How to Use the Project

<img src="https://user-images.githubusercontent.com/73540960/212503274-df7b5897-1945-4e29-b043-97664d66db97.png" alt="Website home" height ="400px;" width = "auto;" >
when you are at home you can see the listed post. you can filter categories on the right side of website or you can go specific post by cliking the title of the post.
You can see all posts of an auhtor by clicking auhtor name. you can go profile and update your user information.



<img src="https://user-images.githubusercontent.com/73540960/212503602-da80330a-3fe7-44c4-b63d-c4b8922d00ea.png" alt="Website home" height ="400px;" width = "auto;" >




if you want to create a post you need to register and then click 'create Post' on the navbar. after you click you will see the page above you can fill and select more than one category with ctrl + right click 
after create you will redirect the post detail page. You can delete and edit option if the author of the post is you. you can see it below.




<img src="https://user-images.githubusercontent.com/73540960/212503726-aa897db8-b9e1-453f-a314-314d0adba6a8.png" alt="Website home" height ="400px;" width = "auto;" >


if you want to see admin page you need to create a super user in django and go to /admin.You will see a page like below.you can add delete update  post user , category models. 



<img src="https://user-images.githubusercontent.com/73540960/212503901-60476267-11d3-43b8-a035-612e43239f3b.png" alt="Website home" height ="400px;" width = "auto;" >




