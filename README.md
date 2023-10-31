# MLOPS Project 2

This is a project for the HSLU Course MLOPS.

To install it on your local machine, just clone this project.

To run the app, you have to install Docker first.

## Docker installation
If you're using a Windows Machine, you can look up how to install Docker Desktop on the following site: https://docs.docker.com/desktop/install/windows-install <br> 
For a Linux Machine this site should help you: https://docs.docker.com/desktop/install/linux-install

## Configure the Logger
Before you build your app, you want to configure the Logger to see the Results of your run.
For this Project, wandb is used for logging the run.
For that, you have to adapt config.json file inside a config folder with your personal subscription key:

```json
{
  "wandb": {
    "subscription_key" : "<YOUR_SUBSCRIPTION_KEY>"
  }
}
```

## Build the project

After that you can continue to build the app:

```console
foo@bar:~$ docker build -t mlops-app .
```

This will create the docker image, this might take a while, as it is installing all the required packages.

## Running the project

After that you want to run the image, use the following command for that:

```console
foo@bar:~$ docker run mlops-app
```

The training of the transformer should now start and logging will be done inside your wandb project under the name mlops-project2.


