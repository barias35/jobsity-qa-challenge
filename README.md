# Jobsity QA Challenge
This project is a challenge from Jobsitity for QA Automation Engineer

For more details here the exercise [qa-challenge](https://github.com/barias35/jobsity-qa-challenge/files/6852710/qa-challenge-reviewed_5e6f90ff6a001.pdf)

**Exercise 1**

Here i share my [Google Sheet](https://docs.google.com/spreadsheets/d/1-6pEZnCQuwIq5jo1GYM507Yp5drtpPhn478aSzQORhw/edit?usp=sharing) containing:

- Smoke Test
- Feedback page test cases list wich also works as report run, this sheet has the links to all test cases sheet individually

Here is my trello [dashboard](https://trello.com/b/cc6weeGX/exercise-1) for managing bugs life cicle, the bugs found on this excercise are in this board

**Exercise 2**

Here i share my [Google Sheet](https://docs.google.com/spreadsheets/d/12PVd7MR4gfmiA17w4d7hivY_doBeJpsenxIeH0B0AfI/edit?usp=sharing) containing:

- Test cases list
- Layout functionalities 
- Search input functionalities
- Contact us form functionalities
- Cart functionalities

In the layouts fuctionality this was the first time i see a perfect-pixel test, i read the following [article](https://www.linkedin.com/pulse/pixel-perfection-easy-achieve-through-testing-abhay-dubey/) in order to do my best

For the automation suite I decided to use pytest because is simple to share a fixture like driver without develope that logic for hanndle the driver across all test

Here is my trello [dashboard](https://trello.com/b/39TSZHQw/exercise-2) for managing bugs life cicle, the bugs found on this excercise are in this board

# Steps for run the automate suite

**Notes**

For this exercise I used Pycharm as IDE, Pytest as Test Runner and Python as Language

If you don't have PyCharm please download [here](https://www.jetbrains.com/pycharm/download/#section=windows)

First you must install python from [here](https://www.python.org/downloads/) if you do not have it already, after is installed you must validate in you cmd or in your terminal inside PyCharm you can run python and pip command if pip is not working please see this [tutorial](https://appuals.com/fix-pip-is-not-recognized-as-an-internal-or-external-command/)

After both commands start working, you need to install the virtual enviroment in order to make things works, go to file then settings
![image](https://user-images.githubusercontent.com/47786738/126605427-2721f198-bda5-4597-b700-17eee0429946.png) 

then go to

![image](https://user-images.githubusercontent.com/47786738/126605631-da3eecf1-60dd-4a97-8767-4d8678215d88.png)

select add, then select new enviroment

![image](https://user-images.githubusercontent.com/47786738/126605716-3689d0fb-9219-4165-997e-3fd7881b732d.png)

You will see the following message

![image](https://user-images.githubusercontent.com/47786738/126605822-05469df6-041e-4691-9667-05e75f0f7397.png)

after is finished you must see the following 

![image](https://user-images.githubusercontent.com/47786738/126605904-ed9b1446-9761-489a-abe0-241371b611a4.png)

Now you are going to activate the venv created before run the following command:

![image](https://user-images.githubusercontent.com/47786738/126606213-54c7c873-25fb-4231-be64-01dfd97ba5bb.png)

Now you will run the package installer in order to get all dependencies:

pip install -r requirements.txt

Now if you go to settings you must see a new packages installed:

![image](https://user-images.githubusercontent.com/47786738/126606552-ec464113-acae-4056-9cd6-6f83a8670671.png)

Finally run pytest on the terminal or you can configure like following:

on the top menu you should see 

![image](https://user-images.githubusercontent.com/47786738/126607825-6030b1de-ae29-45e3-ac7a-216e96cf4c5f.png)

select add new:

![image](https://user-images.githubusercontent.com/47786738/126607966-f27293a9-d957-4924-a9d3-d1b9ff3bdfe2.png)

then select pytest give it a name 
![image](https://user-images.githubusercontent.com/47786738/126608461-8f318289-eb68-4990-a514-f4f17d77aa9f.png)

Run it

Enjoy it!

![image](https://user-images.githubusercontent.com/47786738/126609316-5661a8c0-87c1-460e-b30a-2b6d7e0a53b1.png)



