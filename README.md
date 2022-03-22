# gimkitbot
This bot beats gimkit.  When the player enters the question tap the bot will automatically detect this.  It will first loop through every question finding the correct answers.  Next it will continue looping through entering the correct answers until it has 100 bait (this can be changed in the code).  Then it will exit the qustion tab.

Requirments:
- Being part of a gimkit class where the gimkit is being run (adding integration for not being in a class later this week)
- Having a password for your gimkit accout (the only way around this is to have selenium automatically login to gimkit which is complecated, but I may add this at a later point)
- The gimkit being fishtopia (adding clasic gimkit integration later this week)
- Having selenium (pip install selenium) and webdriver_manager (pip install webdriver-manager)
