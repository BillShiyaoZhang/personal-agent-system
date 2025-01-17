import unittest
from unittest.mock import patch, Mock
import ModelMgr

class TestModelMgr(unittest.TestCase):
    @patch('requests.get')
    def setUp(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'models': [{'name': 'model1'}, {'name': 'model2'}]})
        self.model_mgr = ModelMgr.ModelMgr()

    @patch('requests.post')
    def test_download_model_Success(self, mock_post):
        mock_post.return_value = Mock(status_code=200)
        result = self.model_mgr.download_model('new_model')
        self.assertTrue(result)
        self.assertIn('qwen2.5:14b-instruct', self.model_mgr.local_models)

    @patch('requests.post')
    def test_download_model_Failure(self, mock_post):
        mock_post.return_value = Mock(status_code=500)
        result = self.model_mgr.download_model('new_model')
        self.assertFalse(result)
        self.assertNotIn('new_model', self.model_mgr.local_models)

    @patch('requests.delete')
    def test_remove_local_model_Success(self, mock_delete):
        mock_delete.return_value = Mock(status_code=200)
        result = self.model_mgr.remove_local_model('model1')
        self.assertTrue(result)
        self.assertNotIn('model1', self.model_mgr.local_models)

    @patch('requests.delete')
    def test_remove_local_model_Failure(self, mock_delete):
        mock_delete.return_value = Mock(status_code=500)
        result = self.model_mgr.remove_local_model('model1')
        self.assertFalse(result)
        self.assertIn('model1', self.model_mgr.local_models)

    @patch('requests.get')
    def test_get_local_models_Success(self, mock_get):
        mock_get.return_value = Mock(status_code=200, json=lambda: {'models': [{'name': 'model3'}, {'name': 'model4'}]})
        models = self.model_mgr.get_local_models()
        self.assertEqual(models, ['model3', 'model4'])

    @patch('requests.get')
    def test_get_local_models_Failure(self, mock_get):
        mock_get.return_value = Mock(status_code=500)
        models = self.model_mgr.get_local_models()
        self.assertEqual(models, [])

    @patch('requests.post')
    def test_show_model_details_Success(self, mock_post):
        mock_post.return_value = Mock(status_code=200, json=lambda: {'details': 'model details'})
        details = self.model_mgr.show_model_details('model1')
        self.assertEqual(details, {'details': 'model details'})

    @patch('requests.post')
    def test_show_model_details_Failure(self, mock_post):
        mock_post.return_value = Mock(status_code=500)
        details = self.model_mgr.show_model_details('model1')
        self.assertIsNone(details)

    def test_get_downloadable_models_NotImplemented(self):
        result = self.model_mgr.get_downloadable_models()
        self.assertIsNone(result)