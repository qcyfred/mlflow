import mlflow

# Create a features.txt artifact file
features = "rooms, zipcode, median_price, school_rating, transport"
with open("features.txt", 'w') as f:
    f.write(features)

# With artifact_path=None write features.txt under
# root artifact_uri/artifacts directory

uri = f'ftp://u1:p1@localhost/mlruns'
mlflow.set_tracking_uri(uri)

with mlflow.start_run():

    # 通过http存到远端
    # run_file_path = '/home/omaka_shared/qcy/mlruns'
    # uri = f'file://{run_file_path}'
    # uri = "http://172.17.16.13:1234" # 一定要用db，才能注册模型？
    # mlflow.set_tracking_uri(uri)

    tracking_uri = mlflow.get_tracking_uri()
    print("Current tracking uri: {}".format(tracking_uri))

    mlflow.log_artifact("features.txt")


# # --------------- 测试保存整个文件夹
# 网页上没有找到直接打包成压缩包的按钮
# import mlflow

# with mlflow.start_run():
#     arti_folder_path = '/home/omaka_shared/qcy/code/mlflow/examples/log_artifact_demo/my_arti_folder'
    # name = 'backtest_output'
#     mlflow.log_artifacts(local_dir=arti_folder_path, artifact_path=name)

    
# # # ---------------- 测试 load artifacts
# # 下载 artifacts 文件夹
# import mlflow
# # import mlflow.artifacts
#
# name = 'backtest_output'
#
# # print(1)
# # file:///home/omaka_shared/qcy/code/mlflow/examples/log_artifact_demo/mlruns/0/ba6fce36753b4fbb9ccc5ebf78bd436d/artifacts/backtest_output
# artifact_uri = f'runs:/ba6fce36753b4fbb9ccc5ebf78bd436d/{name}'
# run_id = 'ba6fce36753b4fbb9ccc5ebf78bd436d'
# # mlflow.artifacts.download_artifacts(artifact_uri=artifact_uri, )
# dst_path=f'/home/omaka_shared/qcy/downloads'
# mlflow.artifacts.download_artifacts(run_id=run_id, dst_path=dst_path) # 导出整个文件夹 至 dst_path 目录


"""
windows 
mlflow server --backend-store-uri file:/D:\ftp\backend --default-artifact-root ftp://u1:p1@localhost/artifact --host 0.0.0.0 --port 1234

mlflow server --backend-store-uri file:/D:\ftp\backend --default-artifact-root ftp://u1:u1@localhost/artifact --host 0.0.0.0 --port 1234

"""