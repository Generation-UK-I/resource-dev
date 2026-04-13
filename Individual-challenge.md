# Python Individual Challenge

At this point you're about half way through your first Python Project, and for your next sprint you will start to incorporate different technologies, therefore before we move on, we want to spend some time consolidating and evidencing your individual progress.

To do so, we're going to ask you to apply the skills and strategies you've developed to complete a half day task.

## Task Overview

As a developer, you are tasked with submitting a prosposed solution to the client which meets their requirements as closely as possible. 

### Client Requirements

We need a simple user management system to handle to sit in front of our client facing application. The app should have the following features:

- An interface to add new users.
- A method of storing currently active users.
- A method of storing user accounts which are disabled.
- A way to view current active and disabled users.
- A way to manually disable/enable user accounts.

### Pseudo Code

```
START APP
    CREATE ACTIVE USER LIST
    CREATE DISABLED USER LIST

DISPLAY MENU:
    MENU ITEM 1 = ADD USER
    MENU ITEM 2 = VIEW USERS ACTIVE/DISABLED
    MENU ITEM 3 = ENABLE/DISABLE USERS
    MENU ITEM 0 = EXIT APP

IF MENU ITEM 1
    # CAPTURE USER INFO
    INPUT NEW USERNAME
    ADD TO USER LIST

IF MENU ITEM 2
    LIST ACTIVE/DISABLED USERS

IF MENU ITEM 3
    MOVE USER FROM ACTIVE/DISABLED LIST TO OPPOSITE

IF MENU ITEM 0
    EXIT APP


# STRETCH GOAL - INCLUDE PASSWORDS

EACH USER SHOULD BE DICTIONARY WITH NAME AND PASSWORD KEYS
USERLIST = LIST OF DICTIONARIES

ADD_USER FUNCTION REQUESTS USERNAME AND PASSWORD

CREATE MENU ITEM 4 = TEST LOGIN
    IF USERNAME AND PASSWORD INPUT == USERNAME AND PASSWORD VALUES
    PRINT "ACCESS GRANTED"
```

## Assessment

Success criteria will be based upon meeting the clients requirements, with each one simply `met` or `not met`. Two additional stretch goals will also be considered:

- Are user items saved as dictionaries with name and password keys?
- Has a mock login function been created and works?

>The results are for internal use only, to ascertain relevant support which may be offered to help you achieve your program outcomes.
