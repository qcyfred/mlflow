# # -*- coding: utf-8 -*-
# """
# Created on Mon Aug  7 10:20:09 2017
# @author: qcy
# """
#
# from urllib.request import urlopen
# import json
#
# # GET?
# url = 'http://localhost:1234'
# content = {'a': 3, 's': 4}
# data_json = json.dumps(content)
# print(data_json)
# web = urlopen(url, bytes(data_json, encoding='utf-8'))
# rawtext = web.read()
# sss = rawtext.decode('utf8')
# print(sss)


# from random import random, randint
# import mlflow
#
# if __name__ == "__main__":
#     exp_name = 'testname4'
#     mlflow.create_experiment(exp_name, artifact_location='ftp://u1:u1@localhost/ftp/artifact')
#     # mlflow.create_experiment(exp_name, artifact_location='ftp://u1:u1@localhost/ftp/artifact')
#     mlflow.set_tracking_uri("http://localhost:1234")
#     mlflow.set_experiment(exp_name)
#     mlflow.log_param("param1", randint(0, 100))
#
#     mlflow.log_artifact("test.txt")  # File contains "Hello world!"

#
import mlflow

remote_server_uri = "http://localhost:1234"  # set to your server URI
mlflow.set_tracking_uri(remote_server_uri)
# Note: on Databricks, the experiment name passed to mlflow_set_experiment must be a
# valid path in the workspace
mlflow.set_experiment("/my-experiment")
with mlflow.start_run():
    mlflow.log_param("a", 1)
    mlflow.log_metric("b", 2)
    mlflow.log_artifact("test.txt")  # File contains "Hello world!"

    """
    exp = mlflow.get_experiment_by_name('/my-experiment')
    exp.artifact_location
    'ftp://u1:u1@localhost/artifact/409773156666662413'
    """
