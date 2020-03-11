
# AFS

  

[![N|Solid](https://alpes.cloud/up/04f421c9980ab436d97dd6a910bcaf49.svg)](https://www.systemcorp.ai)

  
  
  

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)]()

  

nightwalker is a Python based library, that helps Deep / Machine Learning specialists to track their models during training without accessing server, and getting notifications full of their desired information via nightwalker App.



  

[![N|Solid](https://alpes.cloud/up/32bddf91ffdf1fc2a66614f8a2fbbdaa.png)](https://www.systemcorp.ai)

  
  
  
  

# PROS

- Easy to install and use

- Takes Steps, Epochs, Train & Test Loss, Acc as arguments so you can have all useful metrics in your app

- No registration required, just take the unique code after walker.UID generates it for you, and share it with any number of co-workers to add the model to their apps

  
  

### Used Frameworks & Libraries

  

AFS is built totally on Python & Node.JS.

  

* [Python 3] - for library building

*  [Node.JS] - for Back-End

  
  

### Installation

  

Python 3.6+ required to use.

  

Get the package from [PyPi]

  

```sh

$ pip install nightwalker

```

  
  
  

### Usage

  

Import the nightwalker and reach 'walker' function.

Define the walker function inside the training loop, and pass the arguments.

  

```sh

$ from nightwalker import walker 

$ walker(arg1, arg2)

```

  

After executing the training loop, the library will generate and print unique id for you, by which you'll then verify your session within the app.
It'll look like this:

  

```sh

$ Your unique ID is --- 1sy45kd9

```

Add new model to your app using the generated unique id.


  
  

# Arguments

  

```sh


$iteration argument is for counting iterations. type = number.


$itercount argument is basically a divider, for every how many iterations do you need to send the metric update. type = number.


$maxiter is a maximum of iterations, after which the model finishes training. type = number.

  
$epoch counts epochs. type = number.


$maxepoch is a maximum number of epochs, after which nightwalker will decide the model had finished training.
    

$testloss takes test loss as a metric. type = number.


$trainloss takes validation loss as a metric. type = number.


$acc takes accuracy as a metric. type = number.

  

```

  
 
  

# Suggestions

  

In case you have any suggestions how to improve the app and library functionalities for you, please feel free to open new Issue, or contact us at CONTACT@SYSTEMCORP.AI

  
  
  
  

License

----

  

BSD 3-Clause Licence

  
  
  
  

[//]: #  (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)

  
  

[dill]: <https://github.com/joemccann/dillinger>

[git-repo-url]: <https://github.com/joemccann/dillinger.git>

[john gruber]: <http://daringfireball.net>

[df1]: <http://daringfireball.net/projects/markdown/>

[markdown-it]: <https://github.com/markdown-it/markdown-it>

[Ace Editor]: <http://ace.ajax.org>

[node.js]: <http://nodejs.org>

[Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>

[jQuery]: <http://jquery.com>

[@tjholowaychuk]: <http://twitter.com/tjholowaychuk>

[express]: <http://expressjs.com>

[AngularJS]: <http://angularjs.org>

[Gulp]: <http://gulpjs.com>

[OpenCV]: <https://opencv.org>

[Single Shot Detection (SSD)]: <https://arxiv.org/pdf/1512.02325.pdf>

[ResNet50]: <https://arxiv.org/pdf/1512.03385.pdf>

[Python 3]: <https://python.org>

[Flask]: <http://flask.pocoo.org>

[PyPi]: <https://pypi.org>

[Slack]: <https://slack.com>

[Discord]: <https://discordapp.com>

  

[PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>

[PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>

[PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>

[PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>

[PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>

[PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>