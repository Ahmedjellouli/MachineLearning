
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
For linear regression, we use the Euclidean norm to measure the errors between 𝒇(𝒙) and (𝒚). Concretely, here is the formula to express the error E between the 𝒚(𝒊) and the prediction .
From the collected Dataset, we can develop a linear model of the type:
```
    f(x)= ax + b        Where 𝒂 and 𝒃 are the model parameters.
```
A good model gives small errors between its predictions 𝒇(𝒙) and the examples (𝒚) of the Dataset. 
We do not know the values of the parameters 𝒂 and 𝒃, it will be the role of the machine to find them using the gradient descent, so as to draw a model that fits well in our point cloud.
## **COST FUNCTION**
For linear regression, we use the Euclidean norm to measure the errors between 𝒇(𝒙) and the model 𝒚.
![image](https://user-images.githubusercontent.com/90426606/162482149-b6648431-4fd2-4b1b-b6d6-b20961fd5eae.png)

Each prediction comes with an error, so we have 𝒎 errors. We define the Cost Function 𝑱(𝒂,𝒃) to be the average of all errors:
![image](https://user-images.githubusercontent.com/90426606/162481932-6bc7b101-8cf1-43cf-b3cf-0fc604257d89.png)

The cost function is a square function so the appearance of this function can take the following form:

# Author

* **Ahmed Jellouli** - *ELECTRICAL ENGINEERING STUDENT INTERESTED IN DATA ANALYSIS*

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details


