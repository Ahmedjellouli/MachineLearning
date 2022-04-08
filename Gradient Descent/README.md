
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
## **LINEAR MODEL** 
From the collected Dataset, we can develop a linear model of the type:
```
    f(x)= ax + b        Where 𝒂 and 𝒃 are the model parameters.
```
A good model gives small errors between its predictions 𝒇(𝒙) and the examples (𝒚) of the Dataset. 
We do not know the values of the parameters 𝒂 and 𝒃, it will be the role of the machine to find them, so as to draw a model that fits well in our point cloud.
## **COST FUNCTION** 
Each prediction comes with an error, so we have 𝒎 errors. We define the Cost Function 𝑱(𝒂,𝒃) to be the average of all errors:
```
pip install numpy 
```
# Author

* **Ahmed Jellouli** - *ELECTRICAL ENGINEERING STUDENT INTERESTED IN DATA ANALYSIS*

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


