# pima-indian-diabetes-model-using-keras

Diabetes Model Implemented in Keras Deep learning library. Here Pima-Indian-Diabetes data set is used.

I have used Keras Sequential to create the model, https://keras.io/models/sequential/ </br>

Data set CSV file link : https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.data.csv</br>

Data set Link: https://raw.githubusercontent.com/jbrownlee/Datasets/master/pima-indians-diabetes.names</br>

There are eight input variables and one output variable (the last column) in the Dataset CSV file. We will be learning a model to map rows of input variables (X) to an output variable (y), which we often summarize as y = f(X).

<b> Input Variable (X) </b>
<ul>
  
  <li> Number of times pregnant</li>
  <li>Plasma glucose concentration a 2 hours in an oral glucose tolerance test</li>
  <li>Diastolic blood pressure (mm Hg)</li>
  <li>Triceps skin fold thickness (mm)</li>
  <li>2-Hour serum insulin (mu U/ml)</li>
  <li>Body mass index (weight in kg/(height in m)^2)</li>
  <li>Diabetes pedigree function </li>
  <li>Age (years)</li>
  
</ul>

<b> Output Variables (y)</b>
<ul>
  
  <li> Class variable (0 or 1)</li>
  
</ul>

<h2>Keras Diabetes Model Implementation Steps </h3>
<ol>
  <li> Load Data.</li>
  <li>Define Keras Model.</li>
  <li>Compile Keras Model.</li>
  <li>Fit Keras Model.</li>
  <li>Evaluate Keras Model.</li>
  <li>Make Predictions</li>
 </ol>
 
