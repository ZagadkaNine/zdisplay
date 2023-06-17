# ZDisplay

## ZDisplay
Some context :P For some time now I started using tiling window managers. I use in my home computer but also at my work laptop. At work I can connect my laptop to up to 3 screens, 
but then disconnect for a meeting, connect to two screens at home, and there is more, my laptop screen is 4k and my screens are 1920x1080. 
With gnome it works well. As I need a quick auto detection and a easy way to reconfigure my screens.
But when I tried to use Gnome with tiling managers things get complicated.

The project i3-gnome from [Lorenzo Villani](https://github.com/lvillani) works well but then some times I get weird behaviors as soon as I tried some modifications.
Also I want to use other tiling windows managers; I have already tried Xmonad, Qtile... And my prefered one is Qtile. 
My aim is to stop using the Gnome and be able to intall a lightDM + Qtile system for professionnal use.

And the first step is to work on a way to easy configure my screens. \

Here is what I need:

- If the lid is closed, disable the display.
- If it is open set the scale for this display to 200%.
- When other displays are connected create a simple config file were i just need to change the order of the displays.
- As I connect different numbers of screens different config files are created, thus if one is already exists it will take its config into account.
- The event of closing and opening the lid will launch this reconfiguration tool.
- must be easy to install (one command).
- the tool can be launched manually.
- the config will reside in the .config folder of the user.

## This is a working in progress project
As for now I can get the state of the lid. And working on getting logs (syslog) whenever the lid is closed or opened.

## Installing 

```
git clone https://github.com/ZagadkaNine/ansible-boilerplate.git ansibleproject/
ansible-playbook playbook.yml
```
