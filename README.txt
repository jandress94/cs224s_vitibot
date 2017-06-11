To use Vitibot, first install all the required dependencies.
Afterwards, run the following command:

python ./vitibot <flags>

Vitibot is written for Python 2.7.x and has not been tested
with newer versions of Python.

By default, Vitibot will run in speech mode, meaning you speak to
Vitibot.  The flags supported are the following:

-t: typed input to vitibot rather than spoken
-v: verbose
-b: use baseline implementation
-d: debug

When running in typed mode, type out your responses when prompted
and press enter when finished.

==============================================
Sample usage of Vitibot in typed mode:

Hello there!  I am VitiBot, your personal wine expert.  Let me know if there 
is anything I can search for you.

>  I'm looking for a red wine that goes well beef.

Ok, I'll take that into consideration.
You're looking for a red wine.
How will you be preparing the beef?  Will it be with herbs, hot spices, 
mushroom, as a stew, barbeque, burgers, or none of these?
>  I'll be having a barbeque today.

Sounds delicious!  I will definitely take these foods into consideration! 
BBQ sauce has a sweet and spicy component that marries well with a structured 
wine with concentrated fruit. Try Zinfandel, Malbec, Australian Reds, 
Mourvedre/Monastrell or Petite Sirah. Are you on a budget? If so, what's 
your spending range?
>
===============================================

To quit Vitibot, tell it "Exit" and confirm that you wish to exit.
