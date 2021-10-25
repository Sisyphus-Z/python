class BaseConfig(object):
    NNN = 123
    MESSAGE_CLASSES = [
        'utils.message.email.Email',
        'utils.message.msg.Msg',
        'utils.message.wx.WeChat',
        'utils.message.dingding.DingDing',
    ]