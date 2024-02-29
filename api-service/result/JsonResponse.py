# -*- coding: utf-8 -*-


class JsonResponse(object):
    """
    统一的json返回格式
    """

    def __init__(self, userMsg, code):
        self.code = code
        self.userMsg = userMsg

    @classmethod
    def success(cls, userMsg=None, code=1):
        return cls(userMsg, code)

    @classmethod
    def error(cls, userMsg=None, code=0):
        return cls(userMsg, code)

    def to_dict(self):
        return {
            "code": self.code,
            "userMsg": self.userMsg,
        }
