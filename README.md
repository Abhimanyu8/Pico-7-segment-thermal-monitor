# Pico-7-segment-thermal-monitor
Cause , everyone has a few of them glowy bois lying around somewhere right ?
<p align="center">
  <img src="https://user-images.githubusercontent.com/54982599/156930553-48122d22-27af-41d5-b1e1-b49a5a986857.jpg" width="700" />
</p>

This is a quick and dirty 15-minute raspberry pi pico project involving two 7-segment displays and loads of micropython.
Works as a temp checking tool for PCs, Chainsaw Engines, Your cup of coffee.... basically anywhere you can stick the RP2040 on 

## Recipe :
<p align="center">
  <img src="https://user-images.githubusercontent.com/54982599/156931188-dbaa4320-f7ce-49aa-a303-2e6d7c1343aa.png" />
  
The pinouts of the pico are 18,19,13,14,15,17 and 16 for A, B, C, D, E, F and G respectively, 
  
  <img src="https://user-images.githubusercontent.com/54982599/156930844-3a5bd250-9a96-4f52-89e0-2c55700d893d.jpg" />
  </p>
  
  
  main.py contains the full pinout so check it out 👀
  
  
  <p align="center">
  <img src="https://user-images.githubusercontent.com/54982599/156931826-e76659ee-fbce-4774-ac3f-08ccd250a3d5.png" />
</p>


Do note that the displays are connected PARALLEL-y and current is pulled straight from 5V VBUS for maximum brightness 🔆

An UP signal controls display 1 and a DOWN signal controls the other. 


![DSC_6189-min](https://user-images.githubusercontent.com/54982599/156930846-6676dc9e-1e1f-44d6-ba0c-6a8d1595b482.jpg)


This leads to both displays being powered at the same time and each one shows the inverse of the other . You can connect the displays
seperately but I find this wacky so it stays.

![DSC_6191-min](https://user-images.githubusercontent.com/54982599/156930850-0f65390e-a2ad-4913-b262-b89fbb5706fc.jpg)


Add a tiny button to make it manual and go full monke🍌

(or be a robot 🤖 and leave it on automatic, I wont judge ( •̀ ω •́ )y )
<hr>
