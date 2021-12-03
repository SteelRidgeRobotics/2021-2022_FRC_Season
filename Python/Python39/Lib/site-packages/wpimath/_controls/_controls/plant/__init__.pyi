import wpimath._controls._controls.plant
import typing

__all__ = [
    "DCMotor"
]


class DCMotor():
    """
    Holds the constants for a DC motor.
    """
    @staticmethod
    def CIM(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of CIM.
        """
    @staticmethod
    def NEO(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of NEO brushless motor.
        """
    @staticmethod
    def NEO550(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of NEO 550 brushless motor.
        """
    @staticmethod
    def RS775_125(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Andymark RS 775-125.
        """
    def __init__(self, nominalVoltage: volts, stallTorque: newton_meters, stallCurrent: amperes, freeCurrent: amperes, freeSpeed: radians_per_second, numMotors: int = 1) -> None: 
        """
        Constructs a DC motor.

        :param nominalVoltage: Voltage at which the motor constants were measured.
        :param stallTorque:    Torque when stalled.
        :param stallCurrent:   Current draw when stalled.
        :param freeCurrent:    Current draw under no load.
        :param freeSpeed:      Angular velocity under no load.
        :param numMotors:      Number of motors in a gearbox.
        """
    @staticmethod
    def andymark9015(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Andymark 9015.
        """
    @staticmethod
    def bag(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Bag motor.
        """
    @staticmethod
    def banebotsRS550(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Banebots RS 550.
        """
    @staticmethod
    def banebotsRS775(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Banebots RS 775.
        """
    def current(self, speed: radians_per_second, inputVoltage: volts) -> amperes: 
        """
        Returns current drawn by motor with given speed and input voltage.

        :param speed:        The current angular velocity of the motor.
        :param inputVoltage: The voltage being applied to the motor.
        """
    @staticmethod
    def falcon500(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Falcon 500 brushless motor.
        """
    @staticmethod
    def miniCIM(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of MiniCIM.
        """
    @staticmethod
    def vex775Pro(numMotors: int = 1) -> DCMotor: 
        """
        Returns instance of Vex 775 Pro.
        """
    @property
    def Kt(self) -> volt_seconds:
        """
        :type: volt_seconds
        """
    @property
    def Kv(self) -> radians_per_second_per_volt:
        """
        :type: radians_per_second_per_volt
        """
    @property
    def R(self) -> ohms:
        """
        :type: ohms
        """
    @property
    def freeCurrent(self) -> amperes:
        """
        :type: amperes
        """
    @property
    def freeSpeed(self) -> radians_per_second:
        """
        :type: radians_per_second
        """
    @property
    def nominalVoltage(self) -> volts:
        """
        :type: volts
        """
    @property
    def stallCurrent(self) -> amperes:
        """
        :type: amperes
        """
    @property
    def stallTorque(self) -> newton_meters:
        """
        :type: newton_meters
        """
    pass
