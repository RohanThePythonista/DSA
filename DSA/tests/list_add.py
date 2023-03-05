# # list_test = list()
#
# list_test[0] = 12
#
# print(list_test)
#
from enum import Enum


class MessageSendResult(Enum):
    Ok = 1



print(type(MessageSendResult.Ok))