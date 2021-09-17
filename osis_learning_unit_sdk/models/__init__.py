# flake8: noqa

# import all models into this package
# if you have many models here with many references from one model to another this may
# raise a RecursionError
# to avoid this, import only the models that you directly need like:
# from from osis_learning_unit_sdk.model.pet import Pet
# or import this package, but before doing it, use:
# import sys
# sys.setrecursionlimit(n)

from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_learning_unit_sdk.model.attribution_function_enum import AttributionFunctionEnum
from osis_learning_unit_sdk.model.component_type_enum import ComponentTypeEnum
from osis_learning_unit_sdk.model.decree_category_enum import DecreeCategoryEnum
from osis_learning_unit_sdk.model.duration_unit_enum import DurationUnitEnum
from osis_learning_unit_sdk.model.education_group_root import EducationGroupRoot
from osis_learning_unit_sdk.model.education_group_type_enum import EducationGroupTypeEnum
from osis_learning_unit_sdk.model.effective_class import EffectiveClass
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.external_learning_unit import ExternalLearningUnit
from osis_learning_unit_sdk.model.external_learning_unit_all_of import ExternalLearningUnitAllOf
from osis_learning_unit_sdk.model.inline_response200 import InlineResponse200
from osis_learning_unit_sdk.model.learning_unit import LearningUnit
from osis_learning_unit_sdk.model.learning_unit_achievement import LearningUnitAchievement
from osis_learning_unit_sdk.model.learning_unit_attribution import LearningUnitAttribution
from osis_learning_unit_sdk.model.learning_unit_attribution_substitute import LearningUnitAttributionSubstitute
from osis_learning_unit_sdk.model.learning_unit_campus import LearningUnitCampus
from osis_learning_unit_sdk.model.learning_unit_component import LearningUnitComponent
from osis_learning_unit_sdk.model.learning_unit_detailed import LearningUnitDetailed
from osis_learning_unit_sdk.model.learning_unit_detailed_all_of import LearningUnitDetailedAllOf
from osis_learning_unit_sdk.model.learning_unit_detailed_all_of_proposal import LearningUnitDetailedAllOfProposal
from osis_learning_unit_sdk.model.learning_unit_prerequisite import LearningUnitPrerequisite
from osis_learning_unit_sdk.model.learning_unit_subtype_enum import LearningUnitSubtypeEnum
from osis_learning_unit_sdk.model.learning_unit_summary_specification import LearningUnitSummarySpecification
from osis_learning_unit_sdk.model.learning_unit_teaching_material import LearningUnitTeachingMaterial
from osis_learning_unit_sdk.model.learning_unit_type_enum import LearningUnitTypeEnum
from osis_learning_unit_sdk.model.pagination import Pagination
from osis_learning_unit_sdk.model.periodicity_enum import PeriodicityEnum
from osis_learning_unit_sdk.model.quadrimester_enum import QuadrimesterEnum
