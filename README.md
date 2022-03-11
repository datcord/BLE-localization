# BLE-localization
Raspberry pi localization using BLE ibeacons and trilateration methods

To run the code you will need to install <b>[matplotlib](https://matplotlib.org/stable/users/installing/index.html)</b>
in your raspbery pi
Execute command:
```
sudo bleLocalization N realx realy
```
Where you would change N with the number of repetitions you would like to be made before the average position is taken.
in the realx/y parts you put the known coordinates of your raspberry pi relative to the beacons if you want to calculate the error or difference between real and calculated coordinates.
