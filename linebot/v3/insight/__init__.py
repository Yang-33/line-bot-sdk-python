# coding: utf-8

# flake8: noqa

"""
    LINE Messaging API(Insight)

    This document describes LINE Messaging API(Insight).  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


__version__ = "3.0.0"

# import apis into sdk package
from linebot.v3.insight.api.insight import Insight

from linebot.v3.insight.api.async_insight import AsyncInsight


# import ApiClient
from linebot.v3.insight.api_response import ApiResponse
from linebot.v3.insight.api_client import ApiClient
from linebot.v3.insight.async_api_client import AsyncApiClient
from linebot.v3.insight.configuration import Configuration
from linebot.v3.insight.exceptions import OpenApiException
from linebot.v3.insight.exceptions import ApiTypeError
from linebot.v3.insight.exceptions import ApiValueError
from linebot.v3.insight.exceptions import ApiKeyError
from linebot.v3.insight.exceptions import ApiAttributeError
from linebot.v3.insight.exceptions import ApiException

# import models into sdk package
from linebot.v3.insight.models.age_tile import AgeTile
from linebot.v3.insight.models.app_type_tile import AppTypeTile
from linebot.v3.insight.models.area_tile import AreaTile
from linebot.v3.insight.models.error_detail import ErrorDetail
from linebot.v3.insight.models.error_response import ErrorResponse
from linebot.v3.insight.models.gender_tile import GenderTile
from linebot.v3.insight.models.get_friends_demographics_response import GetFriendsDemographicsResponse
from linebot.v3.insight.models.get_message_event_response import GetMessageEventResponse
from linebot.v3.insight.models.get_message_event_response_click import GetMessageEventResponseClick
from linebot.v3.insight.models.get_message_event_response_message import GetMessageEventResponseMessage
from linebot.v3.insight.models.get_message_event_response_overview import GetMessageEventResponseOverview
from linebot.v3.insight.models.get_number_of_followers_response import GetNumberOfFollowersResponse
from linebot.v3.insight.models.get_number_of_message_deliveries_response import GetNumberOfMessageDeliveriesResponse
from linebot.v3.insight.models.get_statistics_per_unit_response import GetStatisticsPerUnitResponse
from linebot.v3.insight.models.get_statistics_per_unit_response_click import GetStatisticsPerUnitResponseClick
from linebot.v3.insight.models.get_statistics_per_unit_response_message import GetStatisticsPerUnitResponseMessage
from linebot.v3.insight.models.get_statistics_per_unit_response_overview import GetStatisticsPerUnitResponseOverview
from linebot.v3.insight.models.subscription_period_tile import SubscriptionPeriodTile
