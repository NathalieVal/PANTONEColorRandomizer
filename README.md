# PANTONEColorRandomizer

## Demo
Demo Video: <URL>

## GitHub Repository
GitHub Repo: https://github.com/NathalieVal/PANTONEColorRandomizer

## Description

PANTONEColorRandomizer is a color radomizer program based on the actual catalogue for PANTONE Solid Coated colors.

The program is meant to be a different way to randomize colors from a well known company within the design world. It's made with digital artists in mind, taking 
into consideration that designers may want to get the RGB values of the color that theyr'e actively viewing. By clicking on the name of the color on the color card, 
the program opens a window on the user's default browser to the color on the official PANTONE website.

I added an intro scene that displays a stylized version of PANTONE's logo. This scene can be sped up by clicking on the screen. It wasn't really needed, and if 
anything it may slow down the usage of what is already a very simple program, but I personally like to hear the music start before the main menu appears.

Speaking of music, the program also has SFX and audio to accompany it. Initially there was going to be much more going on in terms of visuals and audio, but due to time 
constraints and a general lack of artistic direction, I ended up making everything very simple and clean. I feel like this worked for the better at the end, because now 
it feels like a much calmer experience. The music is also great background noise in my opinion.

The entire program is built with each scene being a different class. This allowed me to create a SceneManager class where transitions can be handled between scenes.
In this case, the buttons slide to the left and the new scenes fade into the screen. Previously, I didn't even know that classes could be used like this, and was just leaving 
everything outside in the wild (at this point I didn't even have a Main class yet), but once I had the idea to create transitions between scenes I had to look up how to do it.


