from pythonosc import osc_message_builder
from pythonosc import udp_client

# Define
class Network:
    IP_ADDRESS:str = "127.0.0.1"
    SEND_PORT:int = 39570
    RECEIVE_PORT:int = 39571

class Enable:
    DISABLE:int = int(0)
    ENABLE_TRACKER:int = int(1)
    ENABLE_CONTROLLER_L:int = int(2)
    ENABLE_CONTROLLER_R:int = int(3)
    ENABLE_TRACKING_REFERENCE:int = int(4)
    ENABLE_CONTROLLER_L_COMPATIBLE:int = int(5)
    ENABLE_CONTROLLER_R_COMPATIBLE:int = int(6)
    ENABLE_TRACKER_COMPATIBLE:int = int(7)

class Button:
    INDEX_BUTTON0:int = int(0) # System
    INDEX_BUTTON1:int = int(1) # A
    INDEX_BUTTON3:int = int(3) # B
    BUTTON_RELEASE:int = int(0)
    BUTTON_PRESS:int = int(1)
    BUTTON_TOUCH_RELEASE:int = int(0)
    BUTTON_TOUCH_PRESS:int = int(1)

class Trigger:
    INDEX_TRIGGER0:int = int(0)
    INDEX_TRIGGER1:int = int(1)
    TRIGGER_TOUCH_RELEASE:int = int(0)
    TRIGGER_TOUCH_PRESS:int = int(1)
    TRIGGER_CLICK_RELEASE:int = int(0)
    TRIGGER_CLICK__PRESS:int = int(1)

class Joystick:
    INDEX_JOYSTICK:int = int(0)
    INDEX_JOYSTICK_TOUCH:int = int(0)
    JOYSTICK_TOUCH_RELEASE:int = int(0)
    JOYSTICK_TOUCH_PRESS:int = int(1)
    JOYSTICK_CLICK_RELEASE:int = int(0)
    JOYSTICK_CLICK__PRESS:int = int(1)

class Index:
    HMD:int = int(0)
    CONTROLLER_L:int = int(1)
    CONTROLLER_R:int = int(2)

class BoneSetIndex:
    RootAndWrist:int = int(0)
    Thumb:int = int(1)
    Index:int = int(2)
    Middle:int = int(3)
    Ring:int = int(4)
    Pinky:int = int(5)

class BoneIndex:
    Root:int = int(0)
    Wrist:int = int(1)
    Thumb0_ThumbProximal:int = int(2)
    Thumb1_ThumbIntermediate:int = int(3)
    Thumb2_ThumbDistal:int = int(4)
    Thumb3_ThumbEnd:int = int(5)
    IndexFinger0_IndexProximal:int = int(6)
    IndexFinger1_IndexIntermediate:int = int(7)
    IndexFinger2_IndexDistal:int = int(8)
    IndexFinger3_IndexDistal2:int = int(9)
    IndexFinger4_IndexEnd:int = int(10)
    MiddleFinger0_MiddleProximal:int = int(11)
    MiddleFinger1_MiddleIntermediate:int = int(12)
    MiddleFinger2_MiddleDistal:int = int(13)
    MiddleFinger3_MiddleDistal2:int = int(14)
    MiddleFinger4_MiddleEnd:int = int(15)
    RingFinger0_RingProximal:int = int(16)
    RingFinger1_RingIntermediate:int = int(17)
    RingFinger2_RingDistal:int = int(18)
    RingFinger3_RingDistal2:int = int(19)
    RingFinger4_RingEnd:int = int(20)
    PinkyFinger0_LittleProximal:int = int(21)
    PinkyFinger1_LittleIntermediate:int = int(22)
    PinkyFinger2_LittleDistal:int = int(23)
    PinkyFinger3_LittleDistal2:int = int(24)
    PinkyFinger4_LittleEnd:int = int(25)
    Aux_Thumb_ThumbHelper:int = int(26)
    Aux_IndexFinger_IndexHelper:int = int(27)
    Aux_MiddleFinger_MiddleHelper:int = int(28)
    Aux_RingFinger_RingHelper:int = int(29)
    Aux_PinkyFinger_LittleHelper:int = int(30)

class RoomMatrix:
    def __init__(self):
        self.m1:float = float(0)
        self.m2:float = float(0)
        self.m3:float = float(0)
        self.m4:float = float(0)
        self.m5:float = float(0)
        self.m6:float = float(0)
        self.m7:float = float(0)
        self.m8:float = float(0)
        self.m9:float = float(0)
        self.m10:float = float(0)
        self.m11:float = float(0)
        self.m12:float = float(0)

class Position:
    def __init__(self):
        self.x:float = float(0)
        self.y:float = float(0)
        self.z:float = float(0)

class Rotation:
    def __init__(self):
        self.x:float = float(0)
        self.y:float = float(0)
        self.z:float = float(0)
        self.w:float = float(0)

class Transform:
    def __init__(self):
        self.position = Position()
        self.rotation = Rotation()

class Target:
    def __init__(self):
        self.transform = Transform()

# Function
def VMTRoomUnity(index:int, enable:int, target:Target, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Room/Unity")
    message.add_arg(index)
    message.add_arg(enable)
    message.add_arg(time_offset)
    message.add_arg(target.transform.position.x)
    message.add_arg(target.transform.position.y)
    message.add_arg(target.transform.position.z)
    message.add_arg(target.transform.rotation.x)
    message.add_arg(target.transform.rotation.y)
    message.add_arg(target.transform.rotation.z)
    message.add_arg(target.transform.rotation.w)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTRawUnity(index:int, enable:int, target:Target, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Raw/Unity")
    message.add_arg(index)
    message.add_arg(enable)
    message.add_arg(time_offset)
    message.add_arg(target.transform.position.x)
    message.add_arg(target.transform.position.y)
    message.add_arg(target.transform.position.z)
    message.add_arg(target.transform.rotation.x)
    message.add_arg(target.transform.rotation.y)
    message.add_arg(target.transform.rotation.z)
    message.add_arg(target.transform.rotation.w)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTJointUnity(index:int, enable:int, target:Target, targetDevice:str, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Joint/Unity")
    message.add_arg(index)
    message.add_arg(enable)
    message.add_arg(time_offset)
    message.add_arg(target.transform.position.x)
    message.add_arg(target.transform.position.y)
    message.add_arg(target.transform.position.z)
    message.add_arg(target.transform.rotation.x)
    message.add_arg(target.transform.rotation.y)
    message.add_arg(target.transform.rotation.z)
    message.add_arg(target.transform.rotation.w)
    message.add_arg(targetDevice)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTFollowUnity(index:int, enable:int, target:Target, targetDevice:str, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Follow/Unity")
    message.add_arg(index)
    message.add_arg(enable)
    message.add_arg(time_offset)
    message.add_arg(target.transform.position.x)
    message.add_arg(target.transform.position.y)
    message.add_arg(target.transform.position.z)
    message.add_arg(target.transform.rotation.x)
    message.add_arg(target.transform.rotation.y)
    message.add_arg(target.transform.rotation.z)
    message.add_arg(target.transform.rotation.w)
    message.add_arg(targetDevice)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTSkeletonScalar(index:int, boneSetIndex:int, value:float, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Skeleton/Scalar")
    message.add_arg(index)
    message.add_arg(boneSetIndex)
    message.add_arg(value)
    message.add_arg(int(0))
    message.add_arg(int(0))
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTSkeletonUnity(index:int, boneIndex:int, target:Target, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Skeleton/Unity")
    message.add_arg(index)
    message.add_arg(boneIndex)
    message.add_arg(target.transform.position.x)
    message.add_arg(target.transform.position.y)
    message.add_arg(target.transform.position.z)
    message.add_arg(target.transform.rotation.x)
    message.add_arg(target.transform.rotation.y)
    message.add_arg(target.transform.rotation.z)
    message.add_arg(target.transform.rotation.w)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTSkeletonApply(index:int, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Skeleton/Apply")
    message.add_arg(index)
    message.add_arg(time_offset)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTInputButton(index:int, buttonindex:int, value:int, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Input/Button")
    message.add_arg(index)
    message.add_arg(buttonindex)
    message.add_arg(time_offset)
    message.add_arg(value)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTInputButtonTouch(index:int, buttonindex:int, value:int, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Input/Button/Touch")
    message.add_arg(index)
    message.add_arg(buttonindex)
    message.add_arg(time_offset)
    message.add_arg(value)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTInputTrigger(index:int, triggerIndex:int, value:float, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Input/Trigger")
    message.add_arg(index)
    message.add_arg(triggerIndex)
    message.add_arg(time_offset)
    message.add_arg(value)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTInputTriggerTouch(index:int, triggerIndex:int, value:int, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Input/Trigger/Touch")
    message.add_arg(index)
    message.add_arg(triggerIndex)
    message.add_arg(time_offset)
    message.add_arg(value)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTInputTriggerClick(index:int, triggerIndex:int, value:int, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Input/Trigger/Click")
    message.add_arg(index)
    message.add_arg(triggerIndex)
    message.add_arg(time_offset)
    message.add_arg(value)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTInputJoystick(index:int, joystickIndex:int, x:float, y:float, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Input/Joystick")
    message.add_arg(index)
    message.add_arg(joystickIndex)
    message.add_arg(time_offset)
    message.add_arg(x)
    message.add_arg(y)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTInputJoystickTouch(index:int, joystickIndex:int, value:int, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Input/Joystick/Touch")
    message.add_arg(index)
    message.add_arg(joystickIndex)
    message.add_arg(time_offset)
    message.add_arg(value)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTInputJoystickClick(index:int, joystickIndex:int, value:int, time_offset:float=float(0), network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Input/Joystick/Click")
    message.add_arg(index)
    message.add_arg(joystickIndex)
    message.add_arg(time_offset)
    message.add_arg(value)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTReset(network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Reset")
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTLoadSetting(network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/LoadSetting")
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTSetRoomMatrix(roomMatrix:RoomMatrix, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Set/RoomMatrix")
    message.add_arg(roomMatrix.m1)
    message.add_arg(roomMatrix.m2)
    message.add_arg(roomMatrix.m3)
    message.add_arg(roomMatrix.m4)
    message.add_arg(roomMatrix.m5)
    message.add_arg(roomMatrix.m6)
    message.add_arg(roomMatrix.m7)
    message.add_arg(roomMatrix.m8)
    message.add_arg(roomMatrix.m9)
    message.add_arg(roomMatrix.m10)
    message.add_arg(roomMatrix.m11)
    message.add_arg(roomMatrix.m12)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTSetAutoPoseUpdate(enable:int, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Set/AutoPoseUpdate")
    message.add_arg(enable)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTGetDevicesList(network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Get/Devices/List")
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTSubscribeDevice(targetDevice:str, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Subscribe/Device")
    message.add_arg(targetDevice)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTUnsubscribeDevice(targetDevice:str, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Unsubscribe/Device")
    message.add_arg(targetDevice)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTRequestRestart(network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/RequestRestart")
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTSetDiagLog(enable:int, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/SetDiagLog")
    message.add_arg(enable)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTConfig(name:str, value:str, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Config")
    message.add_arg(name)
    message.add_arg(value)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTSetDestination(ip_address:str, port:int, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Set/Destination")
    message.add_arg(ip_address)
    message.add_arg(port)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

def VMTDebug(command:str, network:Network=Network) -> None:
    message = osc_message_builder.OscMessageBuilder(address="/VMT/Debug")
    message.add_arg(command)
    message = message.build()

    client = udp_client.SimpleUDPClient(network.IP_ADDRESS, network.SEND_PORT)
    client.send(message)

if __name__ == "__main__":
    target_HMD = Target()
    target_L = Target()
    target_R = Target()

    # HMDの起動
    VMTRoomUnity(Index.HMD, Enable.ENABLE_TRACKER, target_HMD)

    # 左手の起動
    VMTRoomUnity(Index.CONTROLLER_L, Enable.ENABLE_CONTROLLER_L, target_L)

    # 右手の起動
    VMTRoomUnity(Index.CONTROLLER_R, Enable.ENABLE_CONTROLLER_R, target_R)

    # VMTUnsubscribeDevice("HMD")
    # VMTOutSubscribedDevice()
