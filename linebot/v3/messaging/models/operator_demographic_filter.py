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
from pydantic import BaseModel, Field, conlist
from linebot.v3.messaging.models.demographic_filter import DemographicFilter

class OperatorDemographicFilter(DemographicFilter):
    """
    OperatorDemographicFilter
    """
    var_and: Optional[conlist(DemographicFilter)] = Field(None, alias="and")
    var_or: Optional[conlist(DemographicFilter)] = Field(None, alias="or")
    var_not: Optional[DemographicFilter] = Field(None, alias="not")
    type: str = "operator"

    __properties = ["type", "and", "or", "not"]

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
    def from_json(cls, json_str: str) -> OperatorDemographicFilter:
        """Create an instance of OperatorDemographicFilter from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of each item in var_and (list)
        _items = []
        if self.var_and:
            for _item in self.var_and:
                if _item:
                    _items.append(_item.to_dict())
            _dict['and'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in var_or (list)
        _items = []
        if self.var_or:
            for _item in self.var_or:
                if _item:
                    _items.append(_item.to_dict())
            _dict['or'] = _items
        # override the default output from pydantic by calling `to_dict()` of var_not
        if self.var_not:
            _dict['not'] = self.var_not.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> OperatorDemographicFilter:
        """Create an instance of OperatorDemographicFilter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return OperatorDemographicFilter.parse_obj(obj)

        _obj = OperatorDemographicFilter.parse_obj({
            "type": obj.get("type"),
            "var_and": [DemographicFilter.from_dict(_item) for _item in obj.get("and")] if obj.get("and") is not None else None,
            "var_or": [DemographicFilter.from_dict(_item) for _item in obj.get("or")] if obj.get("or") is not None else None,
            "var_not": DemographicFilter.from_dict(obj.get("not")) if obj.get("not") is not None else None
        })
        return _obj

