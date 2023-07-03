# coding: utf-8

"""
    LINE Messaging API

    This document describes LINE Messaging API.  # noqa: E501

    The version of the OpenAPI document: 0.0.1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import List, Optional
from pydantic import BaseModel, Field, StrictStr, conlist

class GetFollowersResponse(BaseModel):
    """
    GetFollowersResponse
    https://developers.line.biz/en/reference/messaging-api/#get-follower-ids
    """
    user_ids: conlist(StrictStr, max_items=1000) = Field(..., alias="userIds", description="An array of strings indicating user IDs of users that have added the LINE Official Account as a friend. Only users of LINE for iOS and LINE for Android are included in `userIds`. ")
    next: Optional[StrictStr] = Field(None, description="A continuation token to get the next array of user IDs. Returned only when there are remaining user IDs that weren't returned in `userIds` in the original request. The number of user IDs in the `userIds` element doesn't have to reach the maximum number specified by `limit` for the `next` property to be included in the response.  ")

    __properties = ["userIds", "next"]

    class Config:
        """Pydantic configuration"""
        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> GetFollowersResponse:
        """Create an instance of GetFollowersResponse from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> GetFollowersResponse:
        """Create an instance of GetFollowersResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return GetFollowersResponse.parse_obj(obj)

        _obj = GetFollowersResponse.parse_obj({
            "user_ids": obj.get("userIds"),
            "next": obj.get("next")
        })
        return _obj

