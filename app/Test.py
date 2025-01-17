import unittest
from unittest.mock import patch, Mock

import ModelMgr


class TestModelMgr(unittest.TestCase):
    def test_get_local_models(self):
        # 创建 ModelMgr 实例
        model_mgr = ModelMgr.ModelMgr()

        # 调用 get_local_models 方法
        local_models = model_mgr.get_local_models()

        # 打印实际获取的本地模型列表
        print(f"Actual local models: {local_models}")

        # 断言结果，首先判断返回的是一个列表
        self.assertIsInstance(local_models, list)

    def test_show_local_model_details(self):
        # 创建 ModelMgr 实例
        model_mgr = ModelMgr.ModelMgr()

        # 获取一个本地模型名称
        local_models = model_mgr.get_local_models()
        if not local_models:
            self.skipTest("No local models available to test.")

        model_name = local_models[0]

        # 调用 show_local_model_details 方法
        print(model_mgr.show_model_details(model_name))

    def test_download_model(self):
        # 创建 ModelMgr 实例
        model_mgr = ModelMgr.ModelMgr()

        # 定义要下载的模型名称
        model_name = "qwen2.5:0.5b"

        # 调用 download_model 方法
        model_mgr.download_model(model_name)

        # 检查模型是否在本地模型列表中
        self.assertIn(model_name, model_mgr.local_models)

    def test_remove_local_model(self):
        # 创建 ModelMgr 实例
        model_mgr = ModelMgr.ModelMgr()

        # 定义要删除的模型名称
        model_name = "qwen2.5:0.5b"

        # 先确保模型存在
        if model_name not in model_mgr.local_models:
            model_mgr.download_model(model_name)

        # 调用 remove_local_model 方法
        model_mgr.remove_local_model(model_name)

        # 检查模型是否已从本地模型列表中移除
        self.assertNotIn(model_name, model_mgr.local_models)
