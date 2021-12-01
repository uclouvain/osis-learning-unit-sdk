"""
    Learning Unit Service

    A set of API endpoints that allow you to get information about learning unit  # noqa: E501

    The version of the OpenAPI document: 1.09
    Generated by: https://openapi-generator.tech
"""


import unittest

import osis_learning_unit_sdk
from osis_learning_unit_sdk.api.learning_units_api import LearningUnitsApi  # noqa: E501


class TestLearningUnitsApi(unittest.TestCase):
    """LearningUnitsApi unit test stubs"""

    def setUp(self):
        self.api = LearningUnitsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_learning_unit_classes(self):
        """Test case for get_learning_unit_classes

        """
        pass

    def test_learningunitachievements_read(self):
        """Test case for learningunitachievements_read

        """
        pass

    def test_learningunitattributions_read(self):
        """Test case for learningunitattributions_read

        """
        pass

    def test_learningunitprerequisites_read(self):
        """Test case for learningunitprerequisites_read

        """
        pass

    def test_learningunits_list(self):
        """Test case for learningunits_list

        """
        pass

    def test_learningunits_read(self):
        """Test case for learningunits_read

        """
        pass

    def test_learningunitstitle_read(self):
        """Test case for learningunitstitle_read

        """
        pass

    def test_learningunitsummaryspecification_read(self):
        """Test case for learningunitsummaryspecification_read

        """
        pass

    def test_learningunitteachingmaterials_read(self):
        """Test case for learningunitteachingmaterials_read

        """
        pass

    def test_learningunitutilization_read(self):
        """Test case for learningunitutilization_read

        """
        pass


if __name__ == '__main__':
    unittest.main()
