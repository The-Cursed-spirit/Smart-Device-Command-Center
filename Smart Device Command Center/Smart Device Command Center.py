from abc import ABC, abstractmethod

# Abstract Class
class SmartDevice(ABC):

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass


# Light Class
class SmartLight(SmartDevice):

    def turn_on(self):
        print("Smart Light is ON. Lights are glowing!")

    def turn_off(self):
        print("Smart Light is OFF.")


# Fan Class
class SmartFan(SmartDevice):

    def turn_on(self):
        print("Smart Fan is ON. Fan is spinning!")

    def turn_off(self):
        print("Smart Fan is OFF.")


# Speaker Class
class SmartSpeaker(SmartDevice):

    def turn_on(self):
        print("Smart Speaker is ON. Music is playing!")

    def turn_off(self):
        print("Smart Speaker is OFF.")


# Smart Device Command Center
devices = [SmartLight(), SmartFan(), SmartSpeaker()]

print("===== SMART DEVICE COMMAND CENTER =====")

for device in devices:
    device.turn_on()

print("\nTurning OFF all devices...")

for device in devices:
    device.turn_off()