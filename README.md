# Python-Week-3
Python Week 3

Week 3 mainly focused on the theory side of programming, like what should the program accomplish and all the thing you can accomplish by automating processes.

# 1.Project Planning 

![img_2.png](img_2.png)

But before we dive deeper into this project, take a moment and urge you to do something important. Pause for a while and brainstorm at least three project ideas that are inspired by your own life. Jot them down on paper or type them out on your device.
    - A notepad application to take notes for efficiently
    - A music app to play music on my phone and categorize them automatically
    - A app that has plans out my week and what to accomplish, achieving goals and planning of study times

User stories can be added to the application in the format of "As a, I want, So that" 

Remember, when writing user stories, focus on the user's goals and reasons, rather than specific interface details or implementation methods. Take a moment to write your own set of user stories for your Python project before proceeding with this course. This practice will be valuable for your project development.

Apart from user stories, another useful planning tool for applications is called a use case. Use cases typically include a title, an actor (a user or system), and a scenario that describes how a goal is achieved.

![img.png](img.png)

Apart from the user stories and use cases there are also the traditional requirements of the application.

These requirements are kept at a high level, omitting specific details such as the forecast duration or temperature unit. For personal projects, this level of detail suffices, and elaboration can be left for implementation. Additional functional requirements related to the admin include configuring content sources, adding and removing recipients, scheduling the email digest, and setting email account credentials.

![img_1.png](img_1.png)

# Architecture

Now that the requirements are captured, it's time to organize and structure the code for the application. With Python being an object-oriented programming language, considering objects and classes is essential. Looking at the requirements, use cases, and user stories, identifying nouns helps determine potential objects. For instance, in the functional requirements, words like quote, forecast, location, trends, article, content, email, and recipients stand out as potential objects.

![img_3.png](img_3.png)

# 1.Content Retrieval

Daily inspirational quotes

4 functions will be added to dd_content.py

![img_4.png](img_4.png)


To implement the "get_random_quote" function, the source of random quotes needs to be determined.

In the "dd_content.py" file, the "get_random_quote" function is implemented, starting at line seven. The function takes a named parameter for the quotes file location, with a default value of "quotes.csv".

![img_5.png](img_5.png)





































