"""
    Learning Unit Service

    A set of API endpoints that allow you to get information about learning unit  # noqa: E501

    The version of the OpenAPI document: 1.13
    Generated by: https://openapi-generator.tech
"""


import sys
import unittest

import osis_learning_unit_sdk
from osis_learning_unit_sdk.model.learning_unit import LearningUnit
from osis_learning_unit_sdk.model.paginated_learning_unit_list_all_of import PaginatedLearningUnitListAllOf
from osis_learning_unit_sdk.model.pagination import Pagination
globals()['LearningUnit'] = LearningUnit
globals()['PaginatedLearningUnitListAllOf'] = PaginatedLearningUnitListAllOf
globals()['Pagination'] = Pagination
from osis_learning_unit_sdk.model.paginated_learning_unit_list import PaginatedLearningUnitList


class TestPaginatedLearningUnitList(unittest.TestCase):
    """PaginatedLearningUnitList unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPaginatedLearningUnitList(self):
        """Test PaginatedLearningUnitList"""
        # FIXME: construct object with mandatory attributes with example values
        # model = PaginatedLearningUnitList()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()
