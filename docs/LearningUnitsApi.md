# osis_learning_unit_sdk.LearningUnitsApi

All URIs are relative to *https://dev.osis.uclouvain.be/api/v1/learning_unit*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_learning_unit_classes**](LearningUnitsApi.md#get_learning_unit_classes) | **GET** /learning_units/{year}/{acronym}/classes | 
[**learningunitachievements_read**](LearningUnitsApi.md#learningunitachievements_read) | **GET** /learning_units/{year}/{acronym}/achievements | 
[**learningunitattributions_read**](LearningUnitsApi.md#learningunitattributions_read) | **GET** /learning_units/{year}/{acronym}/attributions | 
[**learningunitprerequisites_read**](LearningUnitsApi.md#learningunitprerequisites_read) | **GET** /learning_units/{year}/{acronym}/prerequisites | 
[**learningunits_list**](LearningUnitsApi.md#learningunits_list) | **GET** /learning_units | 
[**learningunits_read**](LearningUnitsApi.md#learningunits_read) | **GET** /learning_units/{year}/{acronym} | 
[**learningunitstitle_read**](LearningUnitsApi.md#learningunitstitle_read) | **GET** /learning_units/{year}/{acronym}/title | 
[**learningunitsummaryspecification_read**](LearningUnitsApi.md#learningunitsummaryspecification_read) | **GET** /learning_units/{year}/{acronym}/summary_specification | 
[**learningunitteachingmaterials_read**](LearningUnitsApi.md#learningunitteachingmaterials_read) | **GET** /learning_units/{year}/{acronym}/teaching_materials | 
[**learningunitutilization_read**](LearningUnitsApi.md#learningunitutilization_read) | **GET** /learning_units/{year}/{acronym}/education_group_roots | 


# **get_learning_unit_classes**
> [EffectiveClass] get_learning_unit_classes(year, acronym)



Return the classes of the learning unit

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_learning_unit_sdk.model.effective_class import EffectiveClass
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.get_learning_unit_classes(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->get_learning_unit_classes: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.get_learning_unit_classes(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->get_learning_unit_classes: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[EffectiveClass]**](EffectiveClass.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunitachievements_read**
> [LearningUnitAchievement] learningunitachievements_read(year, acronym)



Return all achievement in order according of the learning unit specified.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_learning_unit_sdk.model.learning_unit_achievement import LearningUnitAchievement
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.learningunitachievements_read(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitachievements_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunitachievements_read(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitachievements_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[LearningUnitAchievement]**](LearningUnitAchievement.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunitattributions_read**
> [LearningUnitAttribution] learningunitattributions_read(year, acronym)



Return all attributions assign to the learning unit

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.learning_unit_attribution import LearningUnitAttribution
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.learningunitattributions_read(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitattributions_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunitattributions_read(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitattributions_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[LearningUnitAttribution]**](LearningUnitAttribution.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunitprerequisites_read**
> LearningUnitPrerequisite learningunitprerequisites_read(year, acronym)



Returns all education groups for which this learning unit year had prerequisites

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.learning_unit_prerequisite import LearningUnitPrerequisite
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.learningunitprerequisites_read(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitprerequisites_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunitprerequisites_read(year, acronym, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitprerequisites_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**LearningUnitPrerequisite**](LearningUnitPrerequisite.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunits_list**
> PaginatedLearningUnitList learningunits_list()



Return a list of all the learning unit with optional filtering.

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.paginated_learning_unit_list import PaginatedLearningUnitList
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    limit = 1 # int |  (optional)
    offset = 1 # int |  (optional)
    acronym = "acronym_example" # str |  (optional)
    acronym_like = "acronym_like_example" # str |  (optional)
    year = 1 # int |  (optional)
    lang = "lang_example" # str |  (optional)
    campus = "campus_example" # str |  (optional)
    stage_dimona = True # bool |  (optional)
    learning_unit_codes = "learning_unit_codes_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunits_list(limit=limit, offset=offset, acronym=acronym, acronym_like=acronym_like, year=year, lang=lang, campus=campus, stage_dimona=stage_dimona, learning_unit_codes=learning_unit_codes, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunits_list: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **int**|  | [optional]
 **offset** | **int**|  | [optional]
 **acronym** | **str**|  | [optional]
 **acronym_like** | **str**|  | [optional]
 **year** | **int**|  | [optional]
 **lang** | **str**|  | [optional]
 **campus** | **str**|  | [optional]
 **stage_dimona** | **bool**|  | [optional]
 **learning_unit_codes** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**PaginatedLearningUnitList**](PaginatedLearningUnitList.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunits_read**
> bool, date, datetime, dict, float, int, list, str, none_type learningunits_read(year, acronym)



Return the detail of the learning unit

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.learning_unit_detailed import LearningUnitDetailed
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_learning_unit_sdk.model.external_learning_unit import ExternalLearningUnit
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.learningunits_read(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunits_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunits_read(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunits_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

**bool, date, datetime, dict, float, int, list, str, none_type**

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunitstitle_read**
> InlineResponse200 learningunitstitle_read(year, acronym)



Return the title of the learning unit

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.inline_response200 import InlineResponse200
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.learningunitstitle_read(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitstitle_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunitstitle_read(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitstitle_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**InlineResponse200**](InlineResponse200.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunitsummaryspecification_read**
> LearningUnitSummarySpecification learningunitsummaryspecification_read(year, acronym)



Return all summary and specification information of the learning unit specified

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_learning_unit_sdk.model.learning_unit_summary_specification import LearningUnitSummarySpecification
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.learningunitsummaryspecification_read(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitsummaryspecification_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunitsummaryspecification_read(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitsummaryspecification_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**LearningUnitSummarySpecification**](LearningUnitSummarySpecification.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunitteachingmaterials_read**
> LearningUnitTeachingMaterial learningunitteachingmaterials_read(year, acronym)



Return all teaching materials of the learning unit

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.learning_unit_teaching_material import LearningUnitTeachingMaterial
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.learningunitteachingmaterials_read(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitteachingmaterials_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunitteachingmaterials_read(year, acronym, lang=lang, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitteachingmaterials_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**LearningUnitTeachingMaterial**](LearningUnitTeachingMaterial.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **learningunitutilization_read**
> [EducationGroupRoot] learningunitutilization_read(year, acronym)



Return all education groups root which utilize the learning unit specified

### Example

* Api Key Authentication (Token):

```python
import time
import osis_learning_unit_sdk
from osis_learning_unit_sdk.api import learning_units_api
from osis_learning_unit_sdk.model.error import Error
from osis_learning_unit_sdk.model.accepted_language_enum import AcceptedLanguageEnum
from osis_learning_unit_sdk.model.education_group_root import EducationGroupRoot
from pprint import pprint
# Defining the host is optional and defaults to https://dev.osis.uclouvain.be/api/v1/learning_unit
# See configuration.py for a list of all supported configuration parameters.
configuration = osis_learning_unit_sdk.Configuration(
    host = "https://dev.osis.uclouvain.be/api/v1/learning_unit"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Token
configuration.api_key['Token'] = 'YOUR_API_KEY'

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Token'] = 'Bearer'

# Enter a context with an instance of the API client
with osis_learning_unit_sdk.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = learning_units_api.LearningUnitsApi(api_client)
    year = 1 # int | 
    acronym = "acronym_example" # str | 
    lang = "lang_example" # str |  (optional)
    ignore_complementary_module = True # bool |  (optional)
    accept_language = AcceptedLanguageEnum("en") # AcceptedLanguageEnum | The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  (optional)
    x_user_first_name = "X-User-FirstName_example" # str |  (optional)
    x_user_last_name = "X-User-LastName_example" # str |  (optional)
    x_user_email = "X-User-Email_example" # str |  (optional)
    x_user_global_id = "X-User-GlobalID_example" # str |  (optional)

    # example passing only required values which don't have defaults set
    try:
        api_response = api_instance.learningunitutilization_read(year, acronym)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitutilization_read: %s\n" % e)

    # example passing only required values which don't have defaults set
    # and optional values
    try:
        api_response = api_instance.learningunitutilization_read(year, acronym, lang=lang, ignore_complementary_module=ignore_complementary_module, accept_language=accept_language, x_user_first_name=x_user_first_name, x_user_last_name=x_user_last_name, x_user_email=x_user_email, x_user_global_id=x_user_global_id)
        pprint(api_response)
    except osis_learning_unit_sdk.ApiException as e:
        print("Exception when calling LearningUnitsApi->learningunitutilization_read: %s\n" % e)
```


### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **year** | **int**|  |
 **acronym** | **str**|  |
 **lang** | **str**|  | [optional]
 **ignore_complementary_module** | **bool**|  | [optional]
 **accept_language** | **AcceptedLanguageEnum**| The header advertises which languages the client is able to understand, and which locale variant is preferred. (By languages, we mean natural languages, such as English, and not programming languages.)  | [optional]
 **x_user_first_name** | **str**|  | [optional]
 **x_user_last_name** | **str**|  | [optional]
 **x_user_email** | **str**|  | [optional]
 **x_user_global_id** | **str**|  | [optional]

### Return type

[**[EducationGroupRoot]**](EducationGroupRoot.md)

### Authorization

[Token](../README.md#Token)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json


### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**404** | The specified resource was not found |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

