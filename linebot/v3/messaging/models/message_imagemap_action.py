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


from typing import Optional
from pydantic import BaseModel, StrictStr
from linebot.v3.messaging.models.imagemap_action import ImagemapAction
from linebot.v3.messaging.models.imagemap_area import ImagemapArea

class MessageImagemapAction(ImagemapAction):
    """
    MessageImagemapAction
    """
    text: Optional[StrictStr] = None
    label: Optional[StrictStr] = None
    type: str = "message"

    __properties = ["type", "area", "text", "label"]

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
    def from_json(cls, json_str: str) -> MessageImagemapAction:
        """Create an instance of MessageImagemapAction from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True,
                          exclude={
                          },
                          exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of area
        if self.area:
            _dict['area'] = self.area.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> MessageImagemapAction:
        """Create an instance of MessageImagemapAction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return MessageImagemapAction.parse_obj(obj)

        _obj = MessageImagemapAction.parse_obj({
            "type": obj.get("type"),
            "area": ImagemapArea.from_dict(obj.get("area")) if obj.get("area") is not None else None,
            "text": obj.get("text"),
            "label": obj.get("label")
        })
        return _obj

