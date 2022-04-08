
# find the optimal model using the gradient descent algorithm

in this code we will take any dataset with one feature and one target and try to find their optimal linear model, and minimize the cost of this linear model using the gradient descent algorithm.

<p align="center">
  <img width="550" height="380" src="optimalModele.png">
</p>

# Prerequisites

after all make sure that you have already install the folowing libraries:

- matplotlib
```
pip install matplotlib
```
-  sklearn 
```
pip install sklearn 
```
- numpy 
```
pip install numpy 
```

# THEORY
## **Database** Folder
To determine the faces that our program should know
- Put the **face image** as **.png** or **.jpg** format in **Database** Folder
- using the name of the image:
   <br /> you can add The name and also a small description as follow : 
   
  ```
  Name1-Name2-Name3-First description line- second description line- third description line- ... .jpg
  ```
  Note: **"-"** used to write in new line
  <br />Example: 
  
  ```
  Angela-Merkel-[German politician serving- as Chancellor of Germany- since 2005].jpg
  ```
  
## code 

- Fonctionnalities avaliable in this code:

interesting instance :
```
Recognizer = Recognizer(Database="Database",
                        Tolerance=0.55,
                        detectFrontalFace=False, 
                        detectLandmarks=True)

Image = Image(Recognizer=Recognizer,
              filename="Faces\\angela-merkel.jpeg",
              Save=True) 

Video = Video(Recognizer=Recognizer,
              filename="Videos\elon.mp4",   
              )
```

``` 
        - Database              = To choose which database direction you will use         
        - Tolerance             = 0 to 1 to determine tolerance of Recognition        
        - detectFrontalFace     = True or false to detect frontale face in video or Image
        - detectLandmarks       = True or false to detect 68 landmarks in video or Image 
        - save                  = True or false to save image after Recognition
        
``` 
 
- start detection with :
``` 
        - Image.RecognizeFaces() : to Recognitize faces in image
        - Video.RecognizeFaces() : to Recognitize faces in Video
        - Video.AddAudio()       : to add audio to Video after face Recognition
``` 
# Author

* **Ahmed Jellouli** - *ELECTRICAL ENGINEERING STUDENT INTERESTED IN DATA ANALYSIS*

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


