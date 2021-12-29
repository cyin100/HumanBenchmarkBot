# Human Benchmark Bot
Produces high scores on the Human Benchmark Tests (humanbenchmark.com)
Designed for entertainment and proof of concept

## Features
Reaction Time: 25-50 ms*  
Aim: 45-60 ms* [WIP]  
Number Memory: Endless  
Verbal Memory: Endless  
Chimp Test: 41  
Typing: 520-570 wpm*  

*Scores may vary depending on computer processing speed

## Instructions
1. Run pip install pynput
2. Run pip install selenium
3. Run python FILENAME.py (FILENAME being the test you'd like to perform)
4. Peak human performance

## Additional Notes
Verbal Memory: Change variable DESIRED_SCORE to desired score, default is 1000. Alternatively, comment out line 22 (place a '#' in front) for an endless and faster performance  
Number Memory: Change variable DESIRED_SCORE to desired score, default is 20. May not be 100% accurate due to unknown timing methods  
Chimp Test: Change variable DESIRED_SCORE to desired score, default is 30. Desired scores above 41 will only result in 41, as it's the maximum achievable score  
Aim Test: Still debugging  



