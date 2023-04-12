<!-- PROJECT NAME -->

<br />
<div align="center">
  <h3 align="center">Playground</h3>
  <p align="center">
    A Space for Exploration
  </p>
</div>


<!-- machine learning -->
## Machine Learning

[Keras Tuner](MachineLearning/KerasTuner.ipynb) -> The notebook aims to use the Keras Tuner to find the best set of hyperparameters to train a neural network model.

<p align="right">(<a href="#top">back to top</a>)</p>


<!-- mlops -->
## MLOps

[Compare Runs from WandB at PR](MLOps/WandBPR) -> YAML file to pull 'comparative runs report' between baseline model and another model (whose run ID is supplied) from Weights&Biases whenever a trigger (in this case '/wandb \<run id>\') is detected in a pull request. The automated comment with a link to the report is made using <a href='https://github.com/fastai/ghapi'>GhApi</a>.

[Automated commenting at PR using GhApi](MLOps/ghapi.yml) -> Code to automate commenting on a PR using <a href='https://github.com/fastai/ghapi'>GhApi</a>.

[Scheduled Workflow](MLOps/scheduled.yml) -> Code to schedule a workflow that triggers every 15mins and echo's a random integer. 


<p align="right">(<a href="#top">back to top</a>)</p>

<!-- miscellaneous -->
## Miscellaneous

[Interacting with APIs](MLOps/InteractingWithAPIs) -> The repo has a Python script and Jupyter file to demonstrate using Python to interact with the <a href='https://www.ravelry.com/api#index'>Revelry API</a> via the requests library to retrieve information about different Revelry resources. It builds upon the work presented in a Medium <a href='https://medium.com/data-science-at-microsoft/how-to-access-an-api-for-first-time-api-users-879002f5f58d'>article</a>.

[Keyword Search using Beautiful Soup](MLOps/keyword_search.ipynb) -> Using Beautiful Soup to extract keywords from an html page. Regular expression is used for keyword matching.

<p align="right">(<a href="#top">back to top</a>)</p>
