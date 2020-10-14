# Django-by-example-3d-edition-workthrough
Contains the code for Django by example third edition
## What?
The book in question can be found [here](https://www.packtpub.com/product/django-3-by-example-third-edition/9781838981952)
## How far have you worked through the book?
Currently the entirety of Chapter 1 is finished. Chapter 2 should follow somewhat shortly
## CSS?
All of the CSS is directly from the book and without modification (I was instructed to leave it unmodified)
## How do I run this?
First, you need [Django](https://pypi.org/project/Django/) (I'm assuming you already have [Python.](https://www.python.org/)) A virtual environment may not hurt, either. If you possess all of the above, run
```
python manage.py createsuperuser
```
and
```
python manage.py runserver
```
to witness the beauty of code.
## Where do I run this?
I am using a WSL on a windows 10, that is, running Django on WSL and editing files on windows. I strongly recommend you do the same.
## Are there any additional Python packages needed to be installed?
Below you will find packages split under their respective folder headings so that you may choose to install a particular subset rather than forced to guess at the requirements of a particular project
### blog_site
*[Django-taggit](https://pypi.org/project/django-taggit/)
## Are there any additional Linux packages needed to be installed?
As of now, no. This will change in the future, however, so keep an eye on this section.
## Wait... What is happening?
If you are confused as to how to get started with Django, [this link](https://docs.djangoproject.com/en/3.1/intro/tutorial01/) should clear some things up for you. If you do not know how to install WSL, I recommend googling your issue. Better yet, [this guide](https://docs.microsoft.com/en-us/windows/wsl/install-win10) will show you everything you need to know. If you are confused on how to use Linux, that is out of my jurisdiction.
## Why WSL?
I chose to go with Linux because it (should) save me some hassle when installing packages. The book did mention that you can do it all on Windows, but some things may be more difficult to get working
## Do you accept contributions?
While I appreciate the thought, this is more of a playground for me. I am planning to stick to the book and go back to earlier projects when I learn a new feature. For example, when the book touches upon authorization, I will most likely add it to the blog project and expand it to include user accounts.
## Repo structure
Chapter 1: blog_site
