# Output Screenshots

A Python Script that generates beautiful screenshots of your Code Output

## Features
* Takes beautiful screenshots powered by [Carbow.now.sh](https://carbow.now.sh)
* Handles both `print` and `input` statements effectively
* Ability to take screenshots of multiple parts of your Python File
* Easy-to-use Interactive Script

## How to Take Screenshots

To take screenshots of your code, run `Output Screenshots.py`. An Interactive Script will ask for your Python File location and execute it.

## Take Multiple Screenshots 

By default, the Script will include all `print` and `input` statements till the end of your file in a single screenshot. But if you want to break your file into multiple screenshots, you can add the comment `#Take Screenshot` to your Python File

Here is an example 

```py
name=input("What is your Name: ")
print("Hello",name)

#Take Screenshot

age = input("What is your Age: ")
print("Your age is",age)
```

The comment `#Take Screenshot` will divide your code into two different segments and take screenshot of both segments separately

## Example Screenshots

![Example Screeshot 1](https://i.ibb.co/8x7Yd7p/Screenshot1.png)
![Example Screeshot 2](https://i.ibb.co/WxkLyFG/Screenshot2.png)

## Credits

This Python Script uses the [Unofficial Carbon API](https://github.com/cyberboysumanjay/Carbon-API) for generating Screenshots
