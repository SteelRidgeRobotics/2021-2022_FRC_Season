import hal._wpiHal
import typing

__all__ = [
    "AccelerometerRange",
    "AddressableLEDData",
    "AllianceStationID",
    "AnalogTriggerType",
    "CANDeviceType",
    "CANManufacturer",
    "CANStreamMessage",
    "CAN_CloseStreamSession",
    "CAN_GetCANStatus",
    "CAN_OpenStreamSession",
    "CAN_ReceiveMessage",
    "CAN_SendMessage",
    "ControlWord",
    "CounterMode",
    "EncoderEncodingType",
    "EncoderIndexingType",
    "HandleEnum",
    "I2CPort",
    "JoystickAxes",
    "JoystickButtons",
    "JoystickDescriptor",
    "JoystickPOVs",
    "MatchInfo",
    "MatchType",
    "RuntimeType",
    "SPIPort",
    "SerialPort",
    "SimBoolean",
    "SimDevice",
    "SimDouble",
    "SimEnum",
    "SimInt",
    "SimLong",
    "SimValue",
    "SimValueDirection",
    "allocateDigitalPWM",
    "calibrateAnalogGyro",
    "cancelNotifierAlarm",
    "checkAnalogInputChannel",
    "checkAnalogModule",
    "checkAnalogOutputChannel",
    "checkCompressorModule",
    "checkDIOChannel",
    "checkPDPChannel",
    "checkPDPModule",
    "checkPWMChannel",
    "checkRelayChannel",
    "checkSolenoidChannel",
    "checkSolenoidModule",
    "cleanAnalogTrigger",
    "cleanCAN",
    "cleanInterrupts",
    "cleanNotifier",
    "cleanPDP",
    "clearAllPCMStickyFaults",
    "clearCounterDownSource",
    "clearCounterUpSource",
    "clearPDPStickyFaults",
    "clearSerial",
    "closeI2C",
    "closeSPI",
    "closeSerial",
    "configureSPIAutoStall",
    "createHandle",
    "createPortHandle",
    "createPortHandleForSPI",
    "createSimDevice",
    "createSimValue",
    "createSimValueBoolean",
    "createSimValueDouble",
    "createSimValueEnum",
    "createSimValueInt",
    "createSimValueLong",
    "disableInterrupts",
    "disableSerialTermination",
    "enableInterrupts",
    "enableSerialTermination",
    "exitMain",
    "expandFPGATime",
    "fireOneShot",
    "flushSerial",
    "forceSPIAutoRead",
    "freeAddressableLED",
    "freeAnalogGyro",
    "freeAnalogInputPort",
    "freeAnalogOutputPort",
    "freeCounter",
    "freeDIOPort",
    "freeDigitalPWM",
    "freeDutyCycle",
    "freeEncoder",
    "freePWMPort",
    "freeRelayPort",
    "freeSPIAuto",
    "freeSimDevice",
    "freeSolenoidPort",
    "getAccelerometerX",
    "getAccelerometerY",
    "getAccelerometerZ",
    "getAccumulatorCount",
    "getAccumulatorOutput",
    "getAccumulatorValue",
    "getAllSolenoids",
    "getAllianceStation",
    "getAnalogAverageBits",
    "getAnalogAverageValue",
    "getAnalogAverageVoltage",
    "getAnalogGyroAngle",
    "getAnalogGyroCenter",
    "getAnalogGyroOffset",
    "getAnalogGyroRate",
    "getAnalogLSBWeight",
    "getAnalogOffset",
    "getAnalogOutput",
    "getAnalogOversampleBits",
    "getAnalogSampleRate",
    "getAnalogTriggerFPGAIndex",
    "getAnalogTriggerInWindow",
    "getAnalogTriggerOutput",
    "getAnalogTriggerTriggerState",
    "getAnalogValue",
    "getAnalogValueToVolts",
    "getAnalogVoltage",
    "getAnalogVoltsToValue",
    "getBrownedOut",
    "getCompressor",
    "getCompressorClosedLoopControl",
    "getCompressorCurrent",
    "getCompressorCurrentTooHighFault",
    "getCompressorCurrentTooHighStickyFault",
    "getCompressorNotConnectedFault",
    "getCompressorNotConnectedStickyFault",
    "getCompressorPressureSwitch",
    "getCompressorShortedFault",
    "getCompressorShortedStickyFault",
    "getControlWord",
    "getCounter",
    "getCounterDirection",
    "getCounterPeriod",
    "getCounterSamplesToAverage",
    "getCounterStopped",
    "getCurrentThreadPriority",
    "getDIO",
    "getDIODirection",
    "getDutyCycleFPGAIndex",
    "getDutyCycleFrequency",
    "getDutyCycleOutput",
    "getDutyCycleOutputRaw",
    "getDutyCycleOutputScaleFactor",
    "getEncoder",
    "getEncoderDecodingScaleFactor",
    "getEncoderDirection",
    "getEncoderDistance",
    "getEncoderDistancePerPulse",
    "getEncoderEncodingScale",
    "getEncoderEncodingType",
    "getEncoderFPGAIndex",
    "getEncoderPeriod",
    "getEncoderRate",
    "getEncoderRaw",
    "getEncoderSamplesToAverage",
    "getEncoderStopped",
    "getErrorMessage",
    "getFPGAButton",
    "getFPGARevision",
    "getFPGATime",
    "getFPGAVersion",
    "getFilterPeriod",
    "getFilterSelect",
    "getHandleIndex",
    "getHandleType",
    "getHandleTypedIndex",
    "getJoystickAxes",
    "getJoystickAxisType",
    "getJoystickButtons",
    "getJoystickDescriptor",
    "getJoystickIsXbox",
    "getJoystickName",
    "getJoystickPOVs",
    "getJoystickType",
    "getMatchInfo",
    "getMatchTime",
    "getNumAccumulators",
    "getNumAddressableLEDs",
    "getNumAnalogInputs",
    "getNumAnalogOutputs",
    "getNumAnalogTriggers",
    "getNumCounters",
    "getNumDigitalChannels",
    "getNumDigitalHeaders",
    "getNumDigitalPWMOutputs",
    "getNumDutyCycles",
    "getNumEncoders",
    "getNumInterrupts",
    "getNumPCMModules",
    "getNumPDPChannels",
    "getNumPDPModules",
    "getNumPWMChannels",
    "getNumPWMHeaders",
    "getNumRelayChannels",
    "getNumRelayHeaders",
    "getNumSolenoidChannels",
    "getPCMSolenoidBlackList",
    "getPCMSolenoidVoltageFault",
    "getPCMSolenoidVoltageStickyFault",
    "getPDPAllChannelCurrents",
    "getPDPChannelCurrent",
    "getPDPTemperature",
    "getPDPTotalCurrent",
    "getPDPTotalEnergy",
    "getPDPTotalPower",
    "getPDPVoltage",
    "getPWMConfigRaw",
    "getPWMCycleStartTime",
    "getPWMEliminateDeadband",
    "getPWMLoopTiming",
    "getPWMPosition",
    "getPWMRaw",
    "getPWMSpeed",
    "getPort",
    "getPortHandleChannel",
    "getPortHandleModule",
    "getPortHandleSPIEnable",
    "getPortWithModule",
    "getRelay",
    "getRuntimeType",
    "getSPIAutoDroppedCount",
    "getSPIHandle",
    "getSerialBytesReceived",
    "getSerialFD",
    "getSimValue",
    "getSimValueBoolean",
    "getSimValueDouble",
    "getSimValueEnum",
    "getSimValueInt",
    "getSimValueLong",
    "getSolenoid",
    "getSystemActive",
    "getSystemClockTicksPerMicrosecond",
    "getUserActive3V3",
    "getUserActive5V",
    "getUserActive6V",
    "getUserCurrent3V3",
    "getUserCurrent5V",
    "getUserCurrent6V",
    "getUserCurrentFaults3V3",
    "getUserCurrentFaults5V",
    "getUserCurrentFaults6V",
    "getUserVoltage3V3",
    "getUserVoltage5V",
    "getUserVoltage6V",
    "getVinCurrent",
    "getVinVoltage",
    "hasMain",
    "initAccumulator",
    "initSPIAuto",
    "initialize",
    "initializeAddressableLED",
    "initializeAnalogGyro",
    "initializeAnalogInputPort",
    "initializeAnalogOutputPort",
    "initializeAnalogTrigger",
    "initializeAnalogTriggerDutyCycle",
    "initializeCAN",
    "initializeCompressor",
    "initializeCounter",
    "initializeDIOPort",
    "initializeDriverStation",
    "initializeDutyCycle",
    "initializeEncoder",
    "initializeI2C",
    "initializeInterrupts",
    "initializeNotifier",
    "initializePDP",
    "initializePWMPort",
    "initializeRelayPort",
    "initializeSPI",
    "initializeSerialPort",
    "initializeSerialPortDirect",
    "initializeSolenoidPort",
    "isAccumulatorChannel",
    "isAnyPulsing",
    "isHandleCorrectVersion",
    "isHandleType",
    "isNewControlData",
    "isPulsing",
    "latchPWMZero",
    "loadExtensions",
    "loadOneExtension",
    "observeUserProgramAutonomous",
    "observeUserProgramDisabled",
    "observeUserProgramStarting",
    "observeUserProgramTeleop",
    "observeUserProgramTest",
    "pulse",
    "readCANPacketLatest",
    "readCANPacketNew",
    "readCANPacketTimeout",
    "readI2C",
    "readInterruptFallingTimestamp",
    "readInterruptRisingTimestamp",
    "readSPI",
    "readSPIAutoReceivedData",
    "readSerial",
    "releaseDSMutex",
    "releaseWaitingInterrupt",
    "report",
    "requestInterrupts",
    "resetAccumulator",
    "resetAnalogGyro",
    "resetCounter",
    "resetEncoder",
    "resetPDPTotalEnergy",
    "resetSimValue",
    "runMain",
    "sendConsoleLine",
    "sendError",
    "setAccelerometerActive",
    "setAccelerometerRange",
    "setAccumulatorCenter",
    "setAccumulatorDeadband",
    "setAddressableLEDBitTiming",
    "setAddressableLEDLength",
    "setAddressableLEDOutputPort",
    "setAddressableLEDSyncTime",
    "setAllSolenoids",
    "setAnalogAverageBits",
    "setAnalogGyroDeadband",
    "setAnalogGyroParameters",
    "setAnalogGyroVoltsPerDegreePerSecond",
    "setAnalogInputSimDevice",
    "setAnalogOutput",
    "setAnalogOversampleBits",
    "setAnalogSampleRate",
    "setAnalogTriggerAveraged",
    "setAnalogTriggerFiltered",
    "setAnalogTriggerLimitsDutyCycle",
    "setAnalogTriggerLimitsRaw",
    "setAnalogTriggerLimitsVoltage",
    "setCompressorClosedLoopControl",
    "setCounterAverageSize",
    "setCounterDownSource",
    "setCounterDownSourceEdge",
    "setCounterExternalDirectionMode",
    "setCounterMaxPeriod",
    "setCounterPulseLengthMode",
    "setCounterReverseDirection",
    "setCounterSamplesToAverage",
    "setCounterSemiPeriodMode",
    "setCounterUpDownMode",
    "setCounterUpSource",
    "setCounterUpSourceEdge",
    "setCounterUpdateWhenEmpty",
    "setCurrentThreadPriority",
    "setDIO",
    "setDIODirection",
    "setDIOSimDevice",
    "setDigitalPWMDutyCycle",
    "setDigitalPWMOutputChannel",
    "setDigitalPWMRate",
    "setDutyCycleSimDevice",
    "setEncoderDistancePerPulse",
    "setEncoderIndexSource",
    "setEncoderMaxPeriod",
    "setEncoderMinRate",
    "setEncoderReverseDirection",
    "setEncoderSamplesToAverage",
    "setEncoderSimDevice",
    "setFilterPeriod",
    "setFilterSelect",
    "setInterruptUpSourceEdge",
    "setJoystickOutputs",
    "setNotifierName",
    "setNotifierThreadPriority",
    "setOneShotDuration",
    "setPWMConfig",
    "setPWMConfigRaw",
    "setPWMDisabled",
    "setPWMEliminateDeadband",
    "setPWMPeriodScale",
    "setPWMPosition",
    "setPWMRaw",
    "setPWMSpeed",
    "setRelay",
    "setSPIAutoTransmitData",
    "setSPIChipSelectActiveHigh",
    "setSPIChipSelectActiveLow",
    "setSPIHandle",
    "setSPIOpts",
    "setSPISpeed",
    "setSerialBaudRate",
    "setSerialDataBits",
    "setSerialFlowControl",
    "setSerialParity",
    "setSerialReadBufferSize",
    "setSerialStopBits",
    "setSerialTimeout",
    "setSerialWriteBufferSize",
    "setSerialWriteMode",
    "setShowExtensionsNotFoundMessages",
    "setSimValue",
    "setSimValueBoolean",
    "setSimValueDouble",
    "setSimValueEnum",
    "setSimValueInt",
    "setSimValueLong",
    "setSolenoid",
    "setupAnalogGyro",
    "shutdown",
    "simPeriodicAfter",
    "simPeriodicBefore",
    "startAddressableLEDOutput",
    "startSPIAutoRate",
    "startSPIAutoTrigger",
    "stopAddressableLEDOutput",
    "stopCANPacketRepeating",
    "stopNotifier",
    "stopSPIAuto",
    "tInstances",
    "tResourceType",
    "transactionI2C",
    "transactionSPI",
    "updateNotifierAlarm",
    "waitForDSData",
    "waitForDSDataTimeout",
    "waitForInterrupt",
    "waitForNotifierAlarm",
    "writeAddressableLEDData",
    "writeCANPacket",
    "writeCANPacketRepeating",
    "writeCANRTRFrame",
    "writeI2C",
    "writeSPI",
    "writeSerial"
]


class AccelerometerRange():
    """
    The acceptable accelerometer ranges.

    Members:

      k2G

      k4G

      k8G
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'k2G': <AccelerometerRange.k2G: 0>, 'k4G': <AccelerometerRange.k4G: 1>, 'k8G': <AccelerometerRange.k8G: 2>}
    k2G: hal._wpiHal.AccelerometerRange # value = <AccelerometerRange.k2G: 0>
    k4G: hal._wpiHal.AccelerometerRange # value = <AccelerometerRange.k4G: 1>
    k8G: hal._wpiHal.AccelerometerRange # value = <AccelerometerRange.k8G: 2>
    pass
class AddressableLEDData():
    def __init__(self) -> None: ...
    @property
    def b(self) -> int:
        """
        :type: int
        """
    @b.setter
    def b(self, arg0: int) -> None:
        pass
    @property
    def g(self) -> int:
        """
        :type: int
        """
    @g.setter
    def g(self, arg0: int) -> None:
        pass
    @property
    def padding(self) -> int:
        """
        :type: int
        """
    @padding.setter
    def padding(self, arg0: int) -> None:
        pass
    @property
    def r(self) -> int:
        """
        :type: int
        """
    @r.setter
    def r(self, arg0: int) -> None:
        pass
    pass
class AllianceStationID():
    """
    Members:

      kRed1

      kRed2

      kRed3

      kBlue1

      kBlue2

      kBlue3
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kRed1': <AllianceStationID.kRed1: 0>, 'kRed2': <AllianceStationID.kRed2: 1>, 'kRed3': <AllianceStationID.kRed3: 2>, 'kBlue1': <AllianceStationID.kBlue1: 3>, 'kBlue2': <AllianceStationID.kBlue2: 4>, 'kBlue3': <AllianceStationID.kBlue3: 5>}
    kBlue1: hal._wpiHal.AllianceStationID # value = <AllianceStationID.kBlue1: 3>
    kBlue2: hal._wpiHal.AllianceStationID # value = <AllianceStationID.kBlue2: 4>
    kBlue3: hal._wpiHal.AllianceStationID # value = <AllianceStationID.kBlue3: 5>
    kRed1: hal._wpiHal.AllianceStationID # value = <AllianceStationID.kRed1: 0>
    kRed2: hal._wpiHal.AllianceStationID # value = <AllianceStationID.kRed2: 1>
    kRed3: hal._wpiHal.AllianceStationID # value = <AllianceStationID.kRed3: 2>
    pass
class AnalogTriggerType():
    """
    The type of analog trigger to trigger on.

    Members:

      kInWindow

      kState

      kRisingPulse

      kFallingPulse
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kInWindow': <AnalogTriggerType.kInWindow: 0>, 'kState': <AnalogTriggerType.kState: 1>, 'kRisingPulse': <AnalogTriggerType.kRisingPulse: 2>, 'kFallingPulse': <AnalogTriggerType.kFallingPulse: 3>}
    kFallingPulse: hal._wpiHal.AnalogTriggerType # value = <AnalogTriggerType.kFallingPulse: 3>
    kInWindow: hal._wpiHal.AnalogTriggerType # value = <AnalogTriggerType.kInWindow: 0>
    kRisingPulse: hal._wpiHal.AnalogTriggerType # value = <AnalogTriggerType.kRisingPulse: 2>
    kState: hal._wpiHal.AnalogTriggerType # value = <AnalogTriggerType.kState: 1>
    pass
class CANDeviceType():
    """
    The CAN device type.

    Teams should use HAL_CAN_Dev_kMiscellaneous

    Members:

      kBroadcast

      kRobotController

      kMotorController

      kRelayController

      kGyroSensor

      kAccelerometer

      kUltrasonicSensor

      kGearToothSensor

      kPowerDistribution

      kPneumatics

      kMiscellaneous

      kIOBreakout

      kFirmwareUpdate
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kBroadcast': <CANDeviceType.kBroadcast: 0>, 'kRobotController': <CANDeviceType.kRobotController: 1>, 'kMotorController': <CANDeviceType.kMotorController: 2>, 'kRelayController': <CANDeviceType.kRelayController: 3>, 'kGyroSensor': <CANDeviceType.kGyroSensor: 4>, 'kAccelerometer': <CANDeviceType.kAccelerometer: 5>, 'kUltrasonicSensor': <CANDeviceType.kUltrasonicSensor: 6>, 'kGearToothSensor': <CANDeviceType.kGearToothSensor: 7>, 'kPowerDistribution': <CANDeviceType.kPowerDistribution: 8>, 'kPneumatics': <CANDeviceType.kPneumatics: 9>, 'kMiscellaneous': <CANDeviceType.kMiscellaneous: 10>, 'kIOBreakout': <CANDeviceType.kIOBreakout: 11>, 'kFirmwareUpdate': <CANDeviceType.kFirmwareUpdate: 31>}
    kAccelerometer: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kAccelerometer: 5>
    kBroadcast: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kBroadcast: 0>
    kFirmwareUpdate: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kFirmwareUpdate: 31>
    kGearToothSensor: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kGearToothSensor: 7>
    kGyroSensor: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kGyroSensor: 4>
    kIOBreakout: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kIOBreakout: 11>
    kMiscellaneous: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kMiscellaneous: 10>
    kMotorController: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kMotorController: 2>
    kPneumatics: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kPneumatics: 9>
    kPowerDistribution: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kPowerDistribution: 8>
    kRelayController: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kRelayController: 3>
    kRobotController: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kRobotController: 1>
    kUltrasonicSensor: hal._wpiHal.CANDeviceType # value = <CANDeviceType.kUltrasonicSensor: 6>
    pass
class CANManufacturer():
    """
    The CAN manufacturer ID.

    Teams should use HAL_CAN_Man_kTeamUse.

    Members:

      kBroadcast

      kNI

      kLM

      kDEKA

      kCTRE

      kREV

      kGrapple

      kMS

      kTeamUse

      kKauaiLabs

      kCopperforge

      kPWF

      kStudica
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kBroadcast': <CANManufacturer.kBroadcast: 0>, 'kNI': <CANManufacturer.kNI: 1>, 'kLM': <CANManufacturer.kLM: 2>, 'kDEKA': <CANManufacturer.kDEKA: 3>, 'kCTRE': <CANManufacturer.kCTRE: 4>, 'kREV': <CANManufacturer.kREV: 5>, 'kGrapple': <CANManufacturer.kGrapple: 6>, 'kMS': <CANManufacturer.kMS: 7>, 'kTeamUse': <CANManufacturer.kTeamUse: 8>, 'kKauaiLabs': <CANManufacturer.kKauaiLabs: 9>, 'kCopperforge': <CANManufacturer.kCopperforge: 10>, 'kPWF': <CANManufacturer.kPWF: 11>, 'kStudica': <CANManufacturer.kStudica: 12>}
    kBroadcast: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kBroadcast: 0>
    kCTRE: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kCTRE: 4>
    kCopperforge: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kCopperforge: 10>
    kDEKA: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kDEKA: 3>
    kGrapple: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kGrapple: 6>
    kKauaiLabs: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kKauaiLabs: 9>
    kLM: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kLM: 2>
    kMS: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kMS: 7>
    kNI: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kNI: 1>
    kPWF: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kPWF: 11>
    kREV: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kREV: 5>
    kStudica: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kStudica: 12>
    kTeamUse: hal._wpiHal.CANManufacturer # value = <CANManufacturer.kTeamUse: 8>
    pass
class CANStreamMessage():
    """
    Storage for CAN Stream Messages.
    """
    def __init__(self) -> None: ...
    @property
    def data(self) -> memoryview:
        """
        :type: memoryview
        """
    @property
    def dataSize(self) -> int:
        """
        :type: int
        """
    @dataSize.setter
    def dataSize(self, arg0: int) -> None:
        pass
    @property
    def messageID(self) -> int:
        """
        :type: int
        """
    @messageID.setter
    def messageID(self, arg0: int) -> None:
        pass
    @property
    def timeStamp(self) -> int:
        """
        :type: int
        """
    @timeStamp.setter
    def timeStamp(self, arg0: int) -> None:
        pass
    pass
class ControlWord():
    def __init__(self) -> None: ...
    @property
    def autonomous(self) -> int:
        """
        :type: int
        """
    @autonomous.setter
    def autonomous(self, arg1: int) -> None:
        pass
    @property
    def control_reserved(self) -> int:
        """
        :type: int
        """
    @control_reserved.setter
    def control_reserved(self, arg1: int) -> None:
        pass
    @property
    def dsAttached(self) -> int:
        """
        :type: int
        """
    @dsAttached.setter
    def dsAttached(self, arg1: int) -> None:
        pass
    @property
    def eStop(self) -> int:
        """
        :type: int
        """
    @eStop.setter
    def eStop(self, arg1: int) -> None:
        pass
    @property
    def enabled(self) -> int:
        """
        :type: int
        """
    @enabled.setter
    def enabled(self, arg1: int) -> None:
        pass
    @property
    def fmsAttached(self) -> int:
        """
        :type: int
        """
    @fmsAttached.setter
    def fmsAttached(self, arg1: int) -> None:
        pass
    @property
    def test(self) -> int:
        """
        :type: int
        """
    @test.setter
    def test(self, arg1: int) -> None:
        pass
    pass
class CounterMode():
    """
    The counter mode.

    Members:

      kTwoPulse

      kSemiperiod

      kPulseLength

      kExternalDirection
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kTwoPulse': <CounterMode.kTwoPulse: 0>, 'kSemiperiod': <CounterMode.kSemiperiod: 1>, 'kPulseLength': <CounterMode.kPulseLength: 2>, 'kExternalDirection': <CounterMode.kExternalDirection: 3>}
    kExternalDirection: hal._wpiHal.CounterMode # value = <CounterMode.kExternalDirection: 3>
    kPulseLength: hal._wpiHal.CounterMode # value = <CounterMode.kPulseLength: 2>
    kSemiperiod: hal._wpiHal.CounterMode # value = <CounterMode.kSemiperiod: 1>
    kTwoPulse: hal._wpiHal.CounterMode # value = <CounterMode.kTwoPulse: 0>
    pass
class EncoderEncodingType():
    """
    The encoding scaling of the encoder.

    Members:

      Encoder_k1X

      Encoder_k2X

      Encoder_k4X
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    Encoder_k1X: hal._wpiHal.EncoderEncodingType # value = <EncoderEncodingType.Encoder_k1X: 0>
    Encoder_k2X: hal._wpiHal.EncoderEncodingType # value = <EncoderEncodingType.Encoder_k2X: 1>
    Encoder_k4X: hal._wpiHal.EncoderEncodingType # value = <EncoderEncodingType.Encoder_k4X: 2>
    __members__: dict # value = {'Encoder_k1X': <EncoderEncodingType.Encoder_k1X: 0>, 'Encoder_k2X': <EncoderEncodingType.Encoder_k2X: 1>, 'Encoder_k4X': <EncoderEncodingType.Encoder_k4X: 2>}
    pass
class EncoderIndexingType():
    """
    The type of index pulse for the encoder.

    Members:

      kResetWhileHigh

      kResetWhileLow

      kResetOnFallingEdge

      kResetOnRisingEdge
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kResetWhileHigh': <EncoderIndexingType.kResetWhileHigh: 0>, 'kResetWhileLow': <EncoderIndexingType.kResetWhileLow: 1>, 'kResetOnFallingEdge': <EncoderIndexingType.kResetOnFallingEdge: 2>, 'kResetOnRisingEdge': <EncoderIndexingType.kResetOnRisingEdge: 3>}
    kResetOnFallingEdge: hal._wpiHal.EncoderIndexingType # value = <EncoderIndexingType.kResetOnFallingEdge: 2>
    kResetOnRisingEdge: hal._wpiHal.EncoderIndexingType # value = <EncoderIndexingType.kResetOnRisingEdge: 3>
    kResetWhileHigh: hal._wpiHal.EncoderIndexingType # value = <EncoderIndexingType.kResetWhileHigh: 0>
    kResetWhileLow: hal._wpiHal.EncoderIndexingType # value = <EncoderIndexingType.kResetWhileLow: 1>
    pass
class HandleEnum():
    """
    Enum of HAL handle types. Vendors/Teams should use Vendor (17).

    Members:

      Undefined

      DIO

      Port

      Notifier

      Interrupt

      AnalogOutput

      AnalogInput

      AnalogTrigger

      Relay

      PWM

      DigitalPWM

      Counter

      FPGAEncoder

      Encoder

      Compressor

      Solenoid

      AnalogGyro

      Vendor

      SimulationJni

      CAN

      SerialPort

      DutyCycle

      DMA

      AddressableLED
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    AddressableLED: hal._wpiHal.HandleEnum # value = <HandleEnum.AddressableLED: 23>
    AnalogGyro: hal._wpiHal.HandleEnum # value = <HandleEnum.AnalogGyro: 16>
    AnalogInput: hal._wpiHal.HandleEnum # value = <HandleEnum.AnalogInput: 6>
    AnalogOutput: hal._wpiHal.HandleEnum # value = <HandleEnum.AnalogOutput: 5>
    AnalogTrigger: hal._wpiHal.HandleEnum # value = <HandleEnum.AnalogTrigger: 7>
    CAN: hal._wpiHal.HandleEnum # value = <HandleEnum.CAN: 19>
    Compressor: hal._wpiHal.HandleEnum # value = <HandleEnum.Compressor: 14>
    Counter: hal._wpiHal.HandleEnum # value = <HandleEnum.Counter: 11>
    DIO: hal._wpiHal.HandleEnum # value = <HandleEnum.DIO: 1>
    DMA: hal._wpiHal.HandleEnum # value = <HandleEnum.DMA: 22>
    DigitalPWM: hal._wpiHal.HandleEnum # value = <HandleEnum.DigitalPWM: 10>
    DutyCycle: hal._wpiHal.HandleEnum # value = <HandleEnum.DutyCycle: 21>
    Encoder: hal._wpiHal.HandleEnum # value = <HandleEnum.Encoder: 13>
    FPGAEncoder: hal._wpiHal.HandleEnum # value = <HandleEnum.FPGAEncoder: 12>
    Interrupt: hal._wpiHal.HandleEnum # value = <HandleEnum.Interrupt: 4>
    Notifier: hal._wpiHal.HandleEnum # value = <HandleEnum.Notifier: 3>
    PWM: hal._wpiHal.HandleEnum # value = <HandleEnum.PWM: 9>
    Port: hal._wpiHal.HandleEnum # value = <HandleEnum.Port: 2>
    Relay: hal._wpiHal.HandleEnum # value = <HandleEnum.Relay: 8>
    SerialPort: hal._wpiHal.HandleEnum # value = <HandleEnum.SerialPort: 20>
    SimulationJni: hal._wpiHal.HandleEnum # value = <HandleEnum.SimulationJni: 18>
    Solenoid: hal._wpiHal.HandleEnum # value = <HandleEnum.Solenoid: 15>
    Undefined: hal._wpiHal.HandleEnum # value = <HandleEnum.Undefined: 0>
    Vendor: hal._wpiHal.HandleEnum # value = <HandleEnum.Vendor: 17>
    __members__: dict # value = {'Undefined': <HandleEnum.Undefined: 0>, 'DIO': <HandleEnum.DIO: 1>, 'Port': <HandleEnum.Port: 2>, 'Notifier': <HandleEnum.Notifier: 3>, 'Interrupt': <HandleEnum.Interrupt: 4>, 'AnalogOutput': <HandleEnum.AnalogOutput: 5>, 'AnalogInput': <HandleEnum.AnalogInput: 6>, 'AnalogTrigger': <HandleEnum.AnalogTrigger: 7>, 'Relay': <HandleEnum.Relay: 8>, 'PWM': <HandleEnum.PWM: 9>, 'DigitalPWM': <HandleEnum.DigitalPWM: 10>, 'Counter': <HandleEnum.Counter: 11>, 'FPGAEncoder': <HandleEnum.FPGAEncoder: 12>, 'Encoder': <HandleEnum.Encoder: 13>, 'Compressor': <HandleEnum.Compressor: 14>, 'Solenoid': <HandleEnum.Solenoid: 15>, 'AnalogGyro': <HandleEnum.AnalogGyro: 16>, 'Vendor': <HandleEnum.Vendor: 17>, 'SimulationJni': <HandleEnum.SimulationJni: 18>, 'CAN': <HandleEnum.CAN: 19>, 'SerialPort': <HandleEnum.SerialPort: 20>, 'DutyCycle': <HandleEnum.DutyCycle: 21>, 'DMA': <HandleEnum.DMA: 22>, 'AddressableLED': <HandleEnum.AddressableLED: 23>}
    pass
class I2CPort():
    """
    Members:

      kInvalid

      kOnboard

      kMXP
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kInvalid': <I2CPort.kInvalid: -1>, 'kOnboard': <I2CPort.kOnboard: 0>, 'kMXP': <I2CPort.kMXP: 1>}
    kInvalid: hal._wpiHal.I2CPort # value = <I2CPort.kInvalid: -1>
    kMXP: hal._wpiHal.I2CPort # value = <I2CPort.kMXP: 1>
    kOnboard: hal._wpiHal.I2CPort # value = <I2CPort.kOnboard: 0>
    pass
class JoystickAxes():
    def __init__(self) -> None: ...
    @property
    def axes(self) -> memoryview:
        """
        :type: memoryview
        """
    @property
    def count(self) -> int:
        """
        :type: int
        """
    @count.setter
    def count(self, arg0: int) -> None:
        pass
    pass
class JoystickButtons():
    def __init__(self) -> None: ...
    @property
    def buttons(self) -> int:
        """
        :type: int
        """
    @buttons.setter
    def buttons(self, arg0: int) -> None:
        pass
    @property
    def count(self) -> int:
        """
        :type: int
        """
    @count.setter
    def count(self, arg0: int) -> None:
        pass
    pass
class JoystickDescriptor():
    def __init__(self) -> None: ...
    @property
    def axisCount(self) -> int:
        """
        :type: int
        """
    @axisCount.setter
    def axisCount(self, arg0: int) -> None:
        pass
    @property
    def axisTypes(self) -> memoryview:
        """
        :type: memoryview
        """
    @property
    def buttonCount(self) -> int:
        """
        :type: int
        """
    @buttonCount.setter
    def buttonCount(self, arg0: int) -> None:
        pass
    @property
    def isXbox(self) -> int:
        """
        :type: int
        """
    @isXbox.setter
    def isXbox(self, arg0: int) -> None:
        pass
    @property
    def name(self) -> memoryview:
        """
        :type: memoryview
        """
    @property
    def povCount(self) -> int:
        """
        :type: int
        """
    @povCount.setter
    def povCount(self, arg0: int) -> None:
        pass
    @property
    def type(self) -> int:
        """
        :type: int
        """
    @type.setter
    def type(self, arg0: int) -> None:
        pass
    pass
class JoystickPOVs():
    def __init__(self) -> None: ...
    @property
    def count(self) -> int:
        """
        :type: int
        """
    @count.setter
    def count(self, arg0: int) -> None:
        pass
    @property
    def povs(self) -> memoryview:
        """
        :type: memoryview
        """
    pass
class MatchInfo():
    def __init__(self) -> None: ...
    @property
    def eventName(self) -> memoryview:
        """
        :type: memoryview
        """
    @property
    def gameSpecificMessage(self) -> memoryview:
        """
        :type: memoryview
        """
    @property
    def gameSpecificMessageSize(self) -> int:
        """
        :type: int
        """
    @gameSpecificMessageSize.setter
    def gameSpecificMessageSize(self, arg0: int) -> None:
        pass
    @property
    def matchNumber(self) -> int:
        """
        :type: int
        """
    @matchNumber.setter
    def matchNumber(self, arg0: int) -> None:
        pass
    @property
    def matchType(self) -> MatchType:
        """
        :type: MatchType
        """
    @matchType.setter
    def matchType(self, arg0: MatchType) -> None:
        pass
    @property
    def replayNumber(self) -> int:
        """
        :type: int
        """
    @replayNumber.setter
    def replayNumber(self, arg0: int) -> None:
        pass
    pass
class MatchType():
    """
    Members:

      none

      practice

      qualification

      elimination
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'none': <MatchType.none: 0>, 'practice': <MatchType.practice: 1>, 'qualification': <MatchType.qualification: 2>, 'elimination': <MatchType.elimination: 3>}
    elimination: hal._wpiHal.MatchType # value = <MatchType.elimination: 3>
    none: hal._wpiHal.MatchType # value = <MatchType.none: 0>
    practice: hal._wpiHal.MatchType # value = <MatchType.practice: 1>
    qualification: hal._wpiHal.MatchType # value = <MatchType.qualification: 2>
    pass
class RuntimeType():
    """
    Members:

      HAL_Athena

      HAL_Mock
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    HAL_Athena: hal._wpiHal.RuntimeType # value = <RuntimeType.HAL_Athena: 0>
    HAL_Mock: hal._wpiHal.RuntimeType # value = <RuntimeType.HAL_Mock: 1>
    __members__: dict # value = {'HAL_Athena': <RuntimeType.HAL_Athena: 0>, 'HAL_Mock': <RuntimeType.HAL_Mock: 1>}
    pass
class SPIPort():
    """
    Members:

      kInvalid

      kOnboardCS0

      kOnboardCS1

      kOnboardCS2

      kOnboardCS3

      kMXP
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kInvalid': <SPIPort.kInvalid: -1>, 'kOnboardCS0': <SPIPort.kOnboardCS0: 0>, 'kOnboardCS1': <SPIPort.kOnboardCS1: 1>, 'kOnboardCS2': <SPIPort.kOnboardCS2: 2>, 'kOnboardCS3': <SPIPort.kOnboardCS3: 3>, 'kMXP': <SPIPort.kMXP: 4>}
    kInvalid: hal._wpiHal.SPIPort # value = <SPIPort.kInvalid: -1>
    kMXP: hal._wpiHal.SPIPort # value = <SPIPort.kMXP: 4>
    kOnboardCS0: hal._wpiHal.SPIPort # value = <SPIPort.kOnboardCS0: 0>
    kOnboardCS1: hal._wpiHal.SPIPort # value = <SPIPort.kOnboardCS1: 1>
    kOnboardCS2: hal._wpiHal.SPIPort # value = <SPIPort.kOnboardCS2: 2>
    kOnboardCS3: hal._wpiHal.SPIPort # value = <SPIPort.kOnboardCS3: 3>
    pass
class SerialPort():
    """
    Members:

      Onboard

      MXP

      USB1

      USB2
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    MXP: hal._wpiHal.SerialPort # value = <SerialPort.MXP: 1>
    Onboard: hal._wpiHal.SerialPort # value = <SerialPort.Onboard: 0>
    USB1: hal._wpiHal.SerialPort # value = <SerialPort.USB1: 2>
    USB2: hal._wpiHal.SerialPort # value = <SerialPort.USB2: 3>
    __members__: dict # value = {'Onboard': <SerialPort.Onboard: 0>, 'MXP': <SerialPort.MXP: 1>, 'USB1': <SerialPort.USB1: 2>, 'USB2': <SerialPort.USB2: 3>}
    pass
class SimValue():
    """
    Readonly wrapper around a HAL simulator value.

    It is not useful to construct these directly -- they are returned from
    :meth:`.SimDeviceSim.getValue` or :meth:`.SimDevice.createValue`.
    """
    def __bool__(self) -> bool: ...
    def __init__(self, handle: int) -> None: 
        """
        Wraps a simulated value handle as returned by HAL_CreateSimValue().

        :param handle: simulated value handle
        """
    def __repr__(self) -> str: ...
    @property
    def value(self) -> object:
        """
        :type: object
        """
    pass
class SimDevice():
    """
    Wrapper around a HAL simulation 'device'

    This creates a simulated 'device' object that can be interacted with
    from user SimDeviceSim objects or via the Simulation GUI.

    .. note:: To interact with an existing device use
              :class:`hal.simulation.SimDeviceSim` instead.
    """
    class Direction():
        """
        Direction of a simulated value (from the perspective of user code).

        Members:

          kInput

          kOutput

          kBidir
        """
        def __eq__(self, other: object) -> bool: ...
        def __getstate__(self) -> int: ...
        def __hash__(self) -> int: ...
        def __index__(self) -> int: ...
        def __init__(self, value: int) -> None: ...
        def __int__(self) -> int: ...
        def __ne__(self, other: object) -> bool: ...
        def __repr__(self) -> str: ...
        def __setstate__(self, state: int) -> None: ...
        @property
        def name(self) -> str:
            """
            :type: str
            """
        @property
        def value(self) -> int:
            """
            :type: int
            """
        __members__: dict # value = {'kInput': <Direction.kInput: 0>, 'kOutput': <Direction.kOutput: 1>, 'kBidir': <Direction.kBidir: 2>}
        kBidir: hal._wpiHal.SimDevice.Direction # value = <Direction.kBidir: 2>
        kInput: hal._wpiHal.SimDevice.Direction # value = <Direction.kInput: 0>
        kOutput: hal._wpiHal.SimDevice.Direction # value = <Direction.kOutput: 1>
        pass
    def __bool__(self) -> bool: ...
    @typing.overload
    def __init__(self, name: str) -> None: 
        """
        Creates a simulated device.

        The device name must be unique.  Returns null if the device name
        already exists.  If multiple instances of the same device are desired,
        recommend appending the instance/unique identifer in brackets to the base
        name, e.g. "device[1]".

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name: device name

        Creates a simulated device.

        The device name must be unique.  Returns null if the device name
        already exists.  This is a convenience method that appends index in
        brackets to the device name, e.g. passing index=1 results in "device[1]"
        for the device name.

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name:  device name
        :param index: device index number to append to name

        Creates a simulated device.

        The device name must be unique.  Returns null if the device name
        already exists.  This is a convenience method that appends index and
        channel in brackets to the device name, e.g. passing index=1 and channel=2
        results in "device[1,2]" for the device name.

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name:    device name
        :param index:   device index number to append to name
        :param channel: device channel number to append to name
        """
    @typing.overload
    def __init__(self, name: str, index: int) -> None: ...
    @typing.overload
    def __init__(self, name: str, index: int, channel: int) -> None: ...
    def __repr__(self) -> str: ...
    def createBoolean(self, name: str, direction: int, initialValue: bool) -> SimBoolean: 
        """
        Creates a boolean value on the simulated device.

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name:         value name
        :param direction:    input/output/bidir (from perspective of user code)
        :param initialValue: initial value

        :returns: simulated boolean value object
        """
    def createDouble(self, name: str, direction: int, initialValue: float) -> SimDouble: 
        """
        Creates a double value on the simulated device.

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name:         value name
        :param direction:    input/output/bidir (from perspective of user code)
        :param initialValue: initial value

        :returns: simulated double value object
        """
    def createEnum(self, name: str, direction: int, options: typing.List[str], initialValue: int) -> SimEnum: 
        """
        Creates an enumerated value on the simulated device.

        Enumerated values are always in the range 0 to numOptions-1.

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name:         value name
        :param direction:    input/output/bidir (from perspective of user code)
        :param options:      array of option descriptions
        :param initialValue: initial value (selection)

        :returns: simulated enum value object
        """
    def createEnumDouble(self, name: str, direction: int, options: typing.List[str], optionValues: typing.List[float], initialValue: int) -> SimEnum: 
        """
        Creates an enumerated value on the simulated device with double values.

        Enumerated values are always in the range 0 to numOptions-1.

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name:         value name
        :param direction:    input/output/bidir (from perspective of user code)
        :param options:      array of option descriptions
        :param optionValues: array of option values (must be the same size as
                             options)
        :param initialValue: initial value (selection)

        :returns: simulated enum value object
        """
    def createInt(self, name: str, direction: int, initialValue: int) -> SimInt: 
        """
        Creates an int value on the simulated device.

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name:         value name
        :param direction:    input/output/bidir (from perspective of user code)
        :param initialValue: initial value

        :returns: simulated double value object
        """
    def createLong(self, name: str, direction: int, initialValue: int) -> SimLong: 
        """
        Creates a long value on the simulated device.

        If not in simulation, results in an "empty" object that evaluates to false
        in a boolean context.

        :param name:         value name
        :param direction:    input/output/bidir (from perspective of user code)
        :param initialValue: initial value

        :returns: simulated double value object
        """
    @property
    def name(self) -> str:
        """
        :type: str
        """
    pass
class SimDouble(SimValue):
    """
    Wrapper around a HAL simulator double value.

    It is not useful to construct these directly -- they are returned from
    :meth:`.SimDeviceSim.getDouble` or :meth:`.SimDevice.createDouble`.
    """
    def __init__(self, handle: int) -> None: 
        """
        Wraps a simulated value handle as returned by HAL_CreateSimValueDouble().

        :param handle: simulated value handle
        """
    def __repr__(self) -> str: ...
    def get(self) -> float: 
        """
        Gets the simulated value.

        :returns: The current value
        """
    def reset(self) -> None: 
        """
        Resets the simulated value to 0. Use this instead of Set(0) for resetting
        incremental sensor values like encoder counts or gyro accumulated angle
        to ensure correct behavior in a distributed system (e.g. WebSockets).
        """
    def set(self, value: float) -> None: 
        """
        Sets the simulated value.

        :param value: the value to set
        """
    @property
    def value(self) -> float:
        """
        :type: float
        """
    @value.setter
    def value(self, arg1: float) -> None:
        pass
    pass
class SimEnum(SimValue):
    """
    Wrapper around a HAL simulator enum value.

    It is not useful to construct these directly -- they are returned from
    :meth:`.SimDeviceSim.getEnum` or :meth:`.SimDevice.createEnum`.
    """
    def __init__(self, handle: int) -> None: 
        """
        Wraps a simulated value handle as returned by HAL_CreateSimValueEnum().

        :param handle: simulated value handle
        """
    def __repr__(self) -> str: ...
    def get(self) -> int: 
        """
        Gets the simulated value.

        :returns: The current value
        """
    def set(self, value: int) -> None: 
        """
        Sets the simulated value.

        :param value: the value to set
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    @value.setter
    def value(self, arg1: int) -> None:
        pass
    pass
class SimInt(SimValue):
    """
    Wrapper around a HAL simulator int value handle.

    It is not useful to construct these directly, they are returned
    from various functions.
    """
    def __init__(self, handle: int) -> None: 
        """
        Wraps a simulated value handle as returned by HAL_CreateSimValueInt().

        :param handle: simulated value handle
        """
    def get(self) -> int: 
        """
        Gets the simulated value.

        :returns: The current value
        """
    def reset(self) -> None: 
        """
        Resets the simulated value to 0. Use this instead of Set(0) for resetting
        incremental sensor values like encoder counts or gyro accumulated angle
        to ensure correct behavior in a distributed system (e.g. WebSockets).
        """
    def set(self, value: int) -> None: 
        """
        Sets the simulated value.

        :param value: the value to set
        """
    pass
class SimLong(SimValue):
    """
    Wrapper around a HAL simulator long value handle.

    It is not useful to construct these directly, they are returned
    from various functions.
    """
    def __init__(self, handle: int) -> None: 
        """
        Wraps a simulated value handle as returned by HAL_CreateSimValueLong().

        :param handle: simulated value handle
        """
    def get(self) -> int: 
        """
        Gets the simulated value.

        :returns: The current value
        """
    def reset(self) -> None: 
        """
        Resets the simulated value to 0. Use this instead of Set(0) for resetting
        incremental sensor values like encoder counts or gyro accumulated angle
        to ensure correct behavior in a distributed system (e.g. WebSockets).
        """
    def set(self, value: int) -> None: 
        """
        Sets the simulated value.

        :param value: the value to set
        """
    pass
class SimBoolean(SimValue):
    """
    Wrapper around a HAL simulator boolean value.

    It is not useful to construct these directly -- they are returned from
    :meth:`.SimDeviceSim.getBoolean` or :meth:`.SimDevice.createBoolean`.
    """
    def __init__(self, handle: int) -> None: 
        """
        Wraps a simulated value handle as returned by HAL_CreateSimValueBoolean().

        :param handle: simulated value handle
        """
    def __repr__(self) -> str: ...
    def get(self) -> bool: 
        """
        Gets the simulated value.

        :returns: The current value
        """
    def set(self, value: bool) -> None: 
        """
        Sets the simulated value.

        :param value: the value to set
        """
    @property
    def value(self) -> bool:
        """
        :type: bool
        """
    @value.setter
    def value(self, arg1: bool) -> None:
        pass
    pass
class SimValueDirection():
    """
    Direction of a simulated value (from the perspective of user code).

    Members:

      HAL_SimValueInput : input to user code from the simulator

      HAL_SimValueOutput : output from user code to the simulator

      HAL_SimValueBidir : bidirectional between user code and simulator
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    HAL_SimValueBidir: hal._wpiHal.SimValueDirection # value = <SimValueDirection.HAL_SimValueBidir: 2>
    HAL_SimValueInput: hal._wpiHal.SimValueDirection # value = <SimValueDirection.HAL_SimValueInput: 0>
    HAL_SimValueOutput: hal._wpiHal.SimValueDirection # value = <SimValueDirection.HAL_SimValueOutput: 1>
    __members__: dict # value = {'HAL_SimValueInput': <SimValueDirection.HAL_SimValueInput: 0>, 'HAL_SimValueOutput': <SimValueDirection.HAL_SimValueOutput: 1>, 'HAL_SimValueBidir': <SimValueDirection.HAL_SimValueBidir: 2>}
    pass
class tInstances():
    """
    Members:

      kLanguage_LabVIEW

      kLanguage_CPlusPlus

      kLanguage_Java

      kLanguage_Python

      kLanguage_DotNet

      kLanguage_Kotlin

      kCANPlugin_BlackJagBridge

      kCANPlugin_2CAN

      kFramework_Iterative

      kFramework_Simple

      kFramework_CommandControl

      kFramework_Timed

      kFramework_ROS

      kFramework_RobotBuilder

      kRobotDrive_ArcadeStandard

      kRobotDrive_ArcadeButtonSpin

      kRobotDrive_ArcadeRatioCurve

      kRobotDrive_Tank

      kRobotDrive_MecanumPolar

      kRobotDrive_MecanumCartesian

      kRobotDrive2_DifferentialArcade

      kRobotDrive2_DifferentialTank

      kRobotDrive2_DifferentialCurvature

      kRobotDrive2_MecanumCartesian

      kRobotDrive2_MecanumPolar

      kRobotDrive2_KilloughCartesian

      kRobotDrive2_KilloughPolar

      kDriverStationCIO_Analog

      kDriverStationCIO_DigitalIn

      kDriverStationCIO_DigitalOut

      kDriverStationEIO_Acceleration

      kDriverStationEIO_AnalogIn

      kDriverStationEIO_AnalogOut

      kDriverStationEIO_Button

      kDriverStationEIO_LED

      kDriverStationEIO_DigitalIn

      kDriverStationEIO_DigitalOut

      kDriverStationEIO_FixedDigitalOut

      kDriverStationEIO_PWM

      kDriverStationEIO_Encoder

      kDriverStationEIO_TouchSlider

      kADXL345_SPI

      kADXL345_I2C

      kCommand_Scheduler

      kCommand2_Scheduler

      kSmartDashboard_Instance

      kKinematics_DifferentialDrive

      kKinematics_MecanumDrive

      kKinematics_SwerveDrive

      kOdometry_DifferentialDrive

      kOdometry_MecanumDrive

      kOdometry_SwerveDrive
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kLanguage_LabVIEW': <tInstances.kLanguage_LabVIEW: 1>, 'kLanguage_CPlusPlus': <tInstances.kLanguage_CPlusPlus: 2>, 'kLanguage_Java': <tInstances.kLanguage_Java: 3>, 'kLanguage_Python': <tInstances.kLanguage_Python: 4>, 'kLanguage_DotNet': <tInstances.kLanguage_DotNet: 5>, 'kLanguage_Kotlin': <tInstances.kLanguage_Kotlin: 6>, 'kCANPlugin_BlackJagBridge': <tInstances.kLanguage_LabVIEW: 1>, 'kCANPlugin_2CAN': <tInstances.kLanguage_CPlusPlus: 2>, 'kFramework_Iterative': <tInstances.kLanguage_LabVIEW: 1>, 'kFramework_Simple': <tInstances.kLanguage_CPlusPlus: 2>, 'kFramework_CommandControl': <tInstances.kLanguage_Java: 3>, 'kFramework_Timed': <tInstances.kLanguage_Python: 4>, 'kFramework_ROS': <tInstances.kLanguage_DotNet: 5>, 'kFramework_RobotBuilder': <tInstances.kLanguage_Kotlin: 6>, 'kRobotDrive_ArcadeStandard': <tInstances.kLanguage_LabVIEW: 1>, 'kRobotDrive_ArcadeButtonSpin': <tInstances.kLanguage_CPlusPlus: 2>, 'kRobotDrive_ArcadeRatioCurve': <tInstances.kLanguage_Java: 3>, 'kRobotDrive_Tank': <tInstances.kLanguage_Python: 4>, 'kRobotDrive_MecanumPolar': <tInstances.kLanguage_DotNet: 5>, 'kRobotDrive_MecanumCartesian': <tInstances.kLanguage_Kotlin: 6>, 'kRobotDrive2_DifferentialArcade': <tInstances.kRobotDrive2_DifferentialArcade: 7>, 'kRobotDrive2_DifferentialTank': <tInstances.kRobotDrive2_DifferentialTank: 8>, 'kRobotDrive2_DifferentialCurvature': <tInstances.kRobotDrive2_DifferentialCurvature: 9>, 'kRobotDrive2_MecanumCartesian': <tInstances.kRobotDrive2_MecanumCartesian: 10>, 'kRobotDrive2_MecanumPolar': <tInstances.kRobotDrive2_MecanumPolar: 11>, 'kRobotDrive2_KilloughCartesian': <tInstances.kRobotDrive2_KilloughCartesian: 12>, 'kRobotDrive2_KilloughPolar': <tInstances.kRobotDrive2_KilloughPolar: 13>, 'kDriverStationCIO_Analog': <tInstances.kLanguage_LabVIEW: 1>, 'kDriverStationCIO_DigitalIn': <tInstances.kLanguage_CPlusPlus: 2>, 'kDriverStationCIO_DigitalOut': <tInstances.kLanguage_Java: 3>, 'kDriverStationEIO_Acceleration': <tInstances.kLanguage_LabVIEW: 1>, 'kDriverStationEIO_AnalogIn': <tInstances.kLanguage_CPlusPlus: 2>, 'kDriverStationEIO_AnalogOut': <tInstances.kLanguage_Java: 3>, 'kDriverStationEIO_Button': <tInstances.kLanguage_Python: 4>, 'kDriverStationEIO_LED': <tInstances.kLanguage_DotNet: 5>, 'kDriverStationEIO_DigitalIn': <tInstances.kLanguage_Kotlin: 6>, 'kDriverStationEIO_DigitalOut': <tInstances.kRobotDrive2_DifferentialArcade: 7>, 'kDriverStationEIO_FixedDigitalOut': <tInstances.kRobotDrive2_DifferentialTank: 8>, 'kDriverStationEIO_PWM': <tInstances.kRobotDrive2_DifferentialCurvature: 9>, 'kDriverStationEIO_Encoder': <tInstances.kRobotDrive2_MecanumCartesian: 10>, 'kDriverStationEIO_TouchSlider': <tInstances.kRobotDrive2_MecanumPolar: 11>, 'kADXL345_SPI': <tInstances.kLanguage_LabVIEW: 1>, 'kADXL345_I2C': <tInstances.kLanguage_CPlusPlus: 2>, 'kCommand_Scheduler': <tInstances.kLanguage_LabVIEW: 1>, 'kCommand2_Scheduler': <tInstances.kLanguage_CPlusPlus: 2>, 'kSmartDashboard_Instance': <tInstances.kLanguage_LabVIEW: 1>, 'kKinematics_DifferentialDrive': <tInstances.kLanguage_LabVIEW: 1>, 'kKinematics_MecanumDrive': <tInstances.kLanguage_CPlusPlus: 2>, 'kKinematics_SwerveDrive': <tInstances.kLanguage_Java: 3>, 'kOdometry_DifferentialDrive': <tInstances.kLanguage_LabVIEW: 1>, 'kOdometry_MecanumDrive': <tInstances.kLanguage_CPlusPlus: 2>, 'kOdometry_SwerveDrive': <tInstances.kLanguage_Java: 3>}
    kADXL345_I2C: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kADXL345_SPI: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kCANPlugin_2CAN: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kCANPlugin_BlackJagBridge: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kCommand2_Scheduler: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kCommand_Scheduler: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kDriverStationCIO_Analog: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kDriverStationCIO_DigitalIn: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kDriverStationCIO_DigitalOut: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Java: 3>
    kDriverStationEIO_Acceleration: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kDriverStationEIO_AnalogIn: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kDriverStationEIO_AnalogOut: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Java: 3>
    kDriverStationEIO_Button: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Python: 4>
    kDriverStationEIO_DigitalIn: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Kotlin: 6>
    kDriverStationEIO_DigitalOut: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_DifferentialArcade: 7>
    kDriverStationEIO_Encoder: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_MecanumCartesian: 10>
    kDriverStationEIO_FixedDigitalOut: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_DifferentialTank: 8>
    kDriverStationEIO_LED: hal._wpiHal.tInstances # value = <tInstances.kLanguage_DotNet: 5>
    kDriverStationEIO_PWM: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_DifferentialCurvature: 9>
    kDriverStationEIO_TouchSlider: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_MecanumPolar: 11>
    kFramework_CommandControl: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Java: 3>
    kFramework_Iterative: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kFramework_ROS: hal._wpiHal.tInstances # value = <tInstances.kLanguage_DotNet: 5>
    kFramework_RobotBuilder: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Kotlin: 6>
    kFramework_Simple: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kFramework_Timed: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Python: 4>
    kKinematics_DifferentialDrive: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kKinematics_MecanumDrive: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kKinematics_SwerveDrive: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Java: 3>
    kLanguage_CPlusPlus: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kLanguage_DotNet: hal._wpiHal.tInstances # value = <tInstances.kLanguage_DotNet: 5>
    kLanguage_Java: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Java: 3>
    kLanguage_Kotlin: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Kotlin: 6>
    kLanguage_LabVIEW: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kLanguage_Python: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Python: 4>
    kOdometry_DifferentialDrive: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kOdometry_MecanumDrive: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kOdometry_SwerveDrive: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Java: 3>
    kRobotDrive2_DifferentialArcade: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_DifferentialArcade: 7>
    kRobotDrive2_DifferentialCurvature: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_DifferentialCurvature: 9>
    kRobotDrive2_DifferentialTank: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_DifferentialTank: 8>
    kRobotDrive2_KilloughCartesian: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_KilloughCartesian: 12>
    kRobotDrive2_KilloughPolar: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_KilloughPolar: 13>
    kRobotDrive2_MecanumCartesian: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_MecanumCartesian: 10>
    kRobotDrive2_MecanumPolar: hal._wpiHal.tInstances # value = <tInstances.kRobotDrive2_MecanumPolar: 11>
    kRobotDrive_ArcadeButtonSpin: hal._wpiHal.tInstances # value = <tInstances.kLanguage_CPlusPlus: 2>
    kRobotDrive_ArcadeRatioCurve: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Java: 3>
    kRobotDrive_ArcadeStandard: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    kRobotDrive_MecanumCartesian: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Kotlin: 6>
    kRobotDrive_MecanumPolar: hal._wpiHal.tInstances # value = <tInstances.kLanguage_DotNet: 5>
    kRobotDrive_Tank: hal._wpiHal.tInstances # value = <tInstances.kLanguage_Python: 4>
    kSmartDashboard_Instance: hal._wpiHal.tInstances # value = <tInstances.kLanguage_LabVIEW: 1>
    pass
class tResourceType():
    """
    Members:

      kResourceType_Controller

      kResourceType_Module

      kResourceType_Language

      kResourceType_CANPlugin

      kResourceType_Accelerometer

      kResourceType_ADXL345

      kResourceType_AnalogChannel

      kResourceType_AnalogTrigger

      kResourceType_AnalogTriggerOutput

      kResourceType_CANJaguar

      kResourceType_Compressor

      kResourceType_Counter

      kResourceType_Dashboard

      kResourceType_DigitalInput

      kResourceType_DigitalOutput

      kResourceType_DriverStationCIO

      kResourceType_DriverStationEIO

      kResourceType_DriverStationLCD

      kResourceType_Encoder

      kResourceType_GearTooth

      kResourceType_Gyro

      kResourceType_I2C

      kResourceType_Framework

      kResourceType_Jaguar

      kResourceType_Joystick

      kResourceType_Kinect

      kResourceType_KinectStick

      kResourceType_PIDController

      kResourceType_Preferences

      kResourceType_PWM

      kResourceType_Relay

      kResourceType_RobotDrive

      kResourceType_SerialPort

      kResourceType_Servo

      kResourceType_Solenoid

      kResourceType_SPI

      kResourceType_Task

      kResourceType_Ultrasonic

      kResourceType_Victor

      kResourceType_Button

      kResourceType_Command

      kResourceType_AxisCamera

      kResourceType_PCVideoServer

      kResourceType_SmartDashboard

      kResourceType_Talon

      kResourceType_HiTechnicColorSensor

      kResourceType_HiTechnicAccel

      kResourceType_HiTechnicCompass

      kResourceType_SRF08

      kResourceType_AnalogOutput

      kResourceType_VictorSP

      kResourceType_PWMTalonSRX

      kResourceType_CANTalonSRX

      kResourceType_ADXL362

      kResourceType_ADXRS450

      kResourceType_RevSPARK

      kResourceType_MindsensorsSD540

      kResourceType_DigitalGlitchFilter

      kResourceType_ADIS16448

      kResourceType_PDP

      kResourceType_PCM

      kResourceType_PigeonIMU

      kResourceType_NidecBrushless

      kResourceType_CANifier

      kResourceType_TalonFX

      kResourceType_CTRE_future1

      kResourceType_CTRE_future2

      kResourceType_CTRE_future3

      kResourceType_CTRE_future4

      kResourceType_CTRE_future5

      kResourceType_CTRE_future6

      kResourceType_LinearFilter

      kResourceType_XboxController

      kResourceType_UsbCamera

      kResourceType_NavX

      kResourceType_Pixy

      kResourceType_Pixy2

      kResourceType_ScanseSweep

      kResourceType_Shuffleboard

      kResourceType_CAN

      kResourceType_DigilentDMC60

      kResourceType_PWMVictorSPX

      kResourceType_RevSparkMaxPWM

      kResourceType_RevSparkMaxCAN

      kResourceType_ADIS16470

      kResourceType_PIDController2

      kResourceType_ProfiledPIDController

      kResourceType_Kinematics

      kResourceType_Odometry

      kResourceType_Units

      kResourceType_TrapezoidProfile

      kResourceType_DutyCycle

      kResourceType_AddressableLEDs

      kResourceType_FusionVenom
    """
    def __eq__(self, other: object) -> bool: ...
    def __getstate__(self) -> int: ...
    def __hash__(self) -> int: ...
    def __index__(self) -> int: ...
    def __init__(self, value: int) -> None: ...
    def __int__(self) -> int: ...
    def __ne__(self, other: object) -> bool: ...
    def __repr__(self) -> str: ...
    def __setstate__(self, state: int) -> None: ...
    @property
    def name(self) -> str:
        """
        :type: str
        """
    @property
    def value(self) -> int:
        """
        :type: int
        """
    __members__: dict # value = {'kResourceType_Controller': <tResourceType.kResourceType_Controller: 0>, 'kResourceType_Module': <tResourceType.kResourceType_Module: 1>, 'kResourceType_Language': <tResourceType.kResourceType_Language: 2>, 'kResourceType_CANPlugin': <tResourceType.kResourceType_CANPlugin: 3>, 'kResourceType_Accelerometer': <tResourceType.kResourceType_Accelerometer: 4>, 'kResourceType_ADXL345': <tResourceType.kResourceType_ADXL345: 5>, 'kResourceType_AnalogChannel': <tResourceType.kResourceType_AnalogChannel: 6>, 'kResourceType_AnalogTrigger': <tResourceType.kResourceType_AnalogTrigger: 7>, 'kResourceType_AnalogTriggerOutput': <tResourceType.kResourceType_AnalogTriggerOutput: 8>, 'kResourceType_CANJaguar': <tResourceType.kResourceType_CANJaguar: 9>, 'kResourceType_Compressor': <tResourceType.kResourceType_Compressor: 10>, 'kResourceType_Counter': <tResourceType.kResourceType_Counter: 11>, 'kResourceType_Dashboard': <tResourceType.kResourceType_Dashboard: 12>, 'kResourceType_DigitalInput': <tResourceType.kResourceType_DigitalInput: 13>, 'kResourceType_DigitalOutput': <tResourceType.kResourceType_DigitalOutput: 14>, 'kResourceType_DriverStationCIO': <tResourceType.kResourceType_DriverStationCIO: 15>, 'kResourceType_DriverStationEIO': <tResourceType.kResourceType_DriverStationEIO: 16>, 'kResourceType_DriverStationLCD': <tResourceType.kResourceType_DriverStationLCD: 17>, 'kResourceType_Encoder': <tResourceType.kResourceType_Encoder: 18>, 'kResourceType_GearTooth': <tResourceType.kResourceType_GearTooth: 19>, 'kResourceType_Gyro': <tResourceType.kResourceType_Gyro: 20>, 'kResourceType_I2C': <tResourceType.kResourceType_I2C: 21>, 'kResourceType_Framework': <tResourceType.kResourceType_Framework: 22>, 'kResourceType_Jaguar': <tResourceType.kResourceType_Jaguar: 23>, 'kResourceType_Joystick': <tResourceType.kResourceType_Joystick: 24>, 'kResourceType_Kinect': <tResourceType.kResourceType_Kinect: 25>, 'kResourceType_KinectStick': <tResourceType.kResourceType_KinectStick: 26>, 'kResourceType_PIDController': <tResourceType.kResourceType_PIDController: 27>, 'kResourceType_Preferences': <tResourceType.kResourceType_Preferences: 28>, 'kResourceType_PWM': <tResourceType.kResourceType_PWM: 29>, 'kResourceType_Relay': <tResourceType.kResourceType_Relay: 30>, 'kResourceType_RobotDrive': <tResourceType.kResourceType_RobotDrive: 31>, 'kResourceType_SerialPort': <tResourceType.kResourceType_SerialPort: 32>, 'kResourceType_Servo': <tResourceType.kResourceType_Servo: 33>, 'kResourceType_Solenoid': <tResourceType.kResourceType_Solenoid: 34>, 'kResourceType_SPI': <tResourceType.kResourceType_SPI: 35>, 'kResourceType_Task': <tResourceType.kResourceType_Task: 36>, 'kResourceType_Ultrasonic': <tResourceType.kResourceType_Ultrasonic: 37>, 'kResourceType_Victor': <tResourceType.kResourceType_Victor: 38>, 'kResourceType_Button': <tResourceType.kResourceType_Button: 39>, 'kResourceType_Command': <tResourceType.kResourceType_Command: 40>, 'kResourceType_AxisCamera': <tResourceType.kResourceType_AxisCamera: 41>, 'kResourceType_PCVideoServer': <tResourceType.kResourceType_PCVideoServer: 42>, 'kResourceType_SmartDashboard': <tResourceType.kResourceType_SmartDashboard: 43>, 'kResourceType_Talon': <tResourceType.kResourceType_Talon: 44>, 'kResourceType_HiTechnicColorSensor': <tResourceType.kResourceType_HiTechnicColorSensor: 45>, 'kResourceType_HiTechnicAccel': <tResourceType.kResourceType_HiTechnicAccel: 46>, 'kResourceType_HiTechnicCompass': <tResourceType.kResourceType_HiTechnicCompass: 47>, 'kResourceType_SRF08': <tResourceType.kResourceType_SRF08: 48>, 'kResourceType_AnalogOutput': <tResourceType.kResourceType_AnalogOutput: 49>, 'kResourceType_VictorSP': <tResourceType.kResourceType_VictorSP: 50>, 'kResourceType_PWMTalonSRX': <tResourceType.kResourceType_PWMTalonSRX: 51>, 'kResourceType_CANTalonSRX': <tResourceType.kResourceType_CANTalonSRX: 52>, 'kResourceType_ADXL362': <tResourceType.kResourceType_ADXL362: 53>, 'kResourceType_ADXRS450': <tResourceType.kResourceType_ADXRS450: 54>, 'kResourceType_RevSPARK': <tResourceType.kResourceType_RevSPARK: 55>, 'kResourceType_MindsensorsSD540': <tResourceType.kResourceType_MindsensorsSD540: 56>, 'kResourceType_DigitalGlitchFilter': <tResourceType.kResourceType_DigitalGlitchFilter: 57>, 'kResourceType_ADIS16448': <tResourceType.kResourceType_ADIS16448: 58>, 'kResourceType_PDP': <tResourceType.kResourceType_PDP: 59>, 'kResourceType_PCM': <tResourceType.kResourceType_PCM: 60>, 'kResourceType_PigeonIMU': <tResourceType.kResourceType_PigeonIMU: 61>, 'kResourceType_NidecBrushless': <tResourceType.kResourceType_NidecBrushless: 62>, 'kResourceType_CANifier': <tResourceType.kResourceType_CANifier: 63>, 'kResourceType_TalonFX': <tResourceType.kResourceType_TalonFX: 64>, 'kResourceType_CTRE_future1': <tResourceType.kResourceType_CTRE_future1: 65>, 'kResourceType_CTRE_future2': <tResourceType.kResourceType_CTRE_future2: 66>, 'kResourceType_CTRE_future3': <tResourceType.kResourceType_CTRE_future3: 67>, 'kResourceType_CTRE_future4': <tResourceType.kResourceType_CTRE_future4: 68>, 'kResourceType_CTRE_future5': <tResourceType.kResourceType_CTRE_future5: 69>, 'kResourceType_CTRE_future6': <tResourceType.kResourceType_CTRE_future6: 70>, 'kResourceType_LinearFilter': <tResourceType.kResourceType_LinearFilter: 71>, 'kResourceType_XboxController': <tResourceType.kResourceType_XboxController: 72>, 'kResourceType_UsbCamera': <tResourceType.kResourceType_UsbCamera: 73>, 'kResourceType_NavX': <tResourceType.kResourceType_NavX: 74>, 'kResourceType_Pixy': <tResourceType.kResourceType_Pixy: 75>, 'kResourceType_Pixy2': <tResourceType.kResourceType_Pixy2: 76>, 'kResourceType_ScanseSweep': <tResourceType.kResourceType_ScanseSweep: 77>, 'kResourceType_Shuffleboard': <tResourceType.kResourceType_Shuffleboard: 78>, 'kResourceType_CAN': <tResourceType.kResourceType_CAN: 79>, 'kResourceType_DigilentDMC60': <tResourceType.kResourceType_DigilentDMC60: 80>, 'kResourceType_PWMVictorSPX': <tResourceType.kResourceType_PWMVictorSPX: 81>, 'kResourceType_RevSparkMaxPWM': <tResourceType.kResourceType_RevSparkMaxPWM: 82>, 'kResourceType_RevSparkMaxCAN': <tResourceType.kResourceType_RevSparkMaxCAN: 83>, 'kResourceType_ADIS16470': <tResourceType.kResourceType_ADIS16470: 84>, 'kResourceType_PIDController2': <tResourceType.kResourceType_PIDController2: 85>, 'kResourceType_ProfiledPIDController': <tResourceType.kResourceType_ProfiledPIDController: 86>, 'kResourceType_Kinematics': <tResourceType.kResourceType_Kinematics: 87>, 'kResourceType_Odometry': <tResourceType.kResourceType_Odometry: 88>, 'kResourceType_Units': <tResourceType.kResourceType_Units: 89>, 'kResourceType_TrapezoidProfile': <tResourceType.kResourceType_TrapezoidProfile: 90>, 'kResourceType_DutyCycle': <tResourceType.kResourceType_DutyCycle: 91>, 'kResourceType_AddressableLEDs': <tResourceType.kResourceType_AddressableLEDs: 92>, 'kResourceType_FusionVenom': <tResourceType.kResourceType_FusionVenom: 93>}
    kResourceType_ADIS16448: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_ADIS16448: 58>
    kResourceType_ADIS16470: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_ADIS16470: 84>
    kResourceType_ADXL345: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_ADXL345: 5>
    kResourceType_ADXL362: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_ADXL362: 53>
    kResourceType_ADXRS450: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_ADXRS450: 54>
    kResourceType_Accelerometer: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Accelerometer: 4>
    kResourceType_AddressableLEDs: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_AddressableLEDs: 92>
    kResourceType_AnalogChannel: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_AnalogChannel: 6>
    kResourceType_AnalogOutput: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_AnalogOutput: 49>
    kResourceType_AnalogTrigger: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_AnalogTrigger: 7>
    kResourceType_AnalogTriggerOutput: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_AnalogTriggerOutput: 8>
    kResourceType_AxisCamera: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_AxisCamera: 41>
    kResourceType_Button: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Button: 39>
    kResourceType_CAN: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CAN: 79>
    kResourceType_CANJaguar: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CANJaguar: 9>
    kResourceType_CANPlugin: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CANPlugin: 3>
    kResourceType_CANTalonSRX: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CANTalonSRX: 52>
    kResourceType_CANifier: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CANifier: 63>
    kResourceType_CTRE_future1: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CTRE_future1: 65>
    kResourceType_CTRE_future2: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CTRE_future2: 66>
    kResourceType_CTRE_future3: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CTRE_future3: 67>
    kResourceType_CTRE_future4: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CTRE_future4: 68>
    kResourceType_CTRE_future5: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CTRE_future5: 69>
    kResourceType_CTRE_future6: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_CTRE_future6: 70>
    kResourceType_Command: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Command: 40>
    kResourceType_Compressor: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Compressor: 10>
    kResourceType_Controller: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Controller: 0>
    kResourceType_Counter: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Counter: 11>
    kResourceType_Dashboard: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Dashboard: 12>
    kResourceType_DigilentDMC60: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_DigilentDMC60: 80>
    kResourceType_DigitalGlitchFilter: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_DigitalGlitchFilter: 57>
    kResourceType_DigitalInput: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_DigitalInput: 13>
    kResourceType_DigitalOutput: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_DigitalOutput: 14>
    kResourceType_DriverStationCIO: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_DriverStationCIO: 15>
    kResourceType_DriverStationEIO: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_DriverStationEIO: 16>
    kResourceType_DriverStationLCD: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_DriverStationLCD: 17>
    kResourceType_DutyCycle: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_DutyCycle: 91>
    kResourceType_Encoder: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Encoder: 18>
    kResourceType_Framework: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Framework: 22>
    kResourceType_FusionVenom: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_FusionVenom: 93>
    kResourceType_GearTooth: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_GearTooth: 19>
    kResourceType_Gyro: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Gyro: 20>
    kResourceType_HiTechnicAccel: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_HiTechnicAccel: 46>
    kResourceType_HiTechnicColorSensor: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_HiTechnicColorSensor: 45>
    kResourceType_HiTechnicCompass: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_HiTechnicCompass: 47>
    kResourceType_I2C: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_I2C: 21>
    kResourceType_Jaguar: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Jaguar: 23>
    kResourceType_Joystick: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Joystick: 24>
    kResourceType_Kinect: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Kinect: 25>
    kResourceType_KinectStick: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_KinectStick: 26>
    kResourceType_Kinematics: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Kinematics: 87>
    kResourceType_Language: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Language: 2>
    kResourceType_LinearFilter: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_LinearFilter: 71>
    kResourceType_MindsensorsSD540: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_MindsensorsSD540: 56>
    kResourceType_Module: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Module: 1>
    kResourceType_NavX: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_NavX: 74>
    kResourceType_NidecBrushless: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_NidecBrushless: 62>
    kResourceType_Odometry: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Odometry: 88>
    kResourceType_PCM: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PCM: 60>
    kResourceType_PCVideoServer: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PCVideoServer: 42>
    kResourceType_PDP: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PDP: 59>
    kResourceType_PIDController: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PIDController: 27>
    kResourceType_PIDController2: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PIDController2: 85>
    kResourceType_PWM: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PWM: 29>
    kResourceType_PWMTalonSRX: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PWMTalonSRX: 51>
    kResourceType_PWMVictorSPX: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PWMVictorSPX: 81>
    kResourceType_PigeonIMU: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_PigeonIMU: 61>
    kResourceType_Pixy: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Pixy: 75>
    kResourceType_Pixy2: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Pixy2: 76>
    kResourceType_Preferences: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Preferences: 28>
    kResourceType_ProfiledPIDController: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_ProfiledPIDController: 86>
    kResourceType_Relay: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Relay: 30>
    kResourceType_RevSPARK: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_RevSPARK: 55>
    kResourceType_RevSparkMaxCAN: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_RevSparkMaxCAN: 83>
    kResourceType_RevSparkMaxPWM: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_RevSparkMaxPWM: 82>
    kResourceType_RobotDrive: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_RobotDrive: 31>
    kResourceType_SPI: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_SPI: 35>
    kResourceType_SRF08: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_SRF08: 48>
    kResourceType_ScanseSweep: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_ScanseSweep: 77>
    kResourceType_SerialPort: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_SerialPort: 32>
    kResourceType_Servo: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Servo: 33>
    kResourceType_Shuffleboard: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Shuffleboard: 78>
    kResourceType_SmartDashboard: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_SmartDashboard: 43>
    kResourceType_Solenoid: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Solenoid: 34>
    kResourceType_Talon: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Talon: 44>
    kResourceType_TalonFX: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_TalonFX: 64>
    kResourceType_Task: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Task: 36>
    kResourceType_TrapezoidProfile: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_TrapezoidProfile: 90>
    kResourceType_Ultrasonic: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Ultrasonic: 37>
    kResourceType_Units: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Units: 89>
    kResourceType_UsbCamera: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_UsbCamera: 73>
    kResourceType_Victor: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_Victor: 38>
    kResourceType_VictorSP: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_VictorSP: 50>
    kResourceType_XboxController: hal._wpiHal.tResourceType # value = <tResourceType.kResourceType_XboxController: 72>
    pass
def CAN_CloseStreamSession(sessionHandle: int) -> None:
    """
    Closes a CAN stream.

    :param sessionHandle: the session to close
    """
def CAN_GetCANStatus() -> typing.Tuple[float, int, int, int, int, int]:
    """
    Gets CAN status information.

    :param percentBusUtilization: the bus utilization
    :param busOffCount:           the number of bus off errors
    :param txFullCount:           the number of tx full errors
    :param receiveErrorCount:     the number of receive errors
    :param transmitErrorCount:    the number of transmit errors
    """
def CAN_OpenStreamSession(messageID: int, messageIDMask: int, maxMessages: int) -> typing.Tuple[int, int]:
    """
    Opens a CAN stream.

    :param sessionHandle: output for the session handle
    :param messageID:     the message ID to read
    :param messageIDMask: the mssage ID mask
    :param maxMessages:   the maximum number of messages to stream
    """
def CAN_ReceiveMessage(messageIDMask: int, data: buffer) -> typing.Tuple[int, int, int, int]:
    """
    Receives a CAN message.

    :param messageID:     store for the received message ID
    :param messageIDMask: the message ID mask to look for
    :param data:          data output (8 bytes)
    :param dataSize:      data length (0-8 bytes)
    :param timeStamp:     the packet received timestamp (based off of
                          CLOCK_MONOTONIC)
    """
def CAN_SendMessage(messageID: int, data: buffer, periodMs: int) -> int:
    """
    Sends a CAN message.

    :param messageID: the CAN ID to send
    :param data:      the data to send (0-8 bytes)
    :param dataSize:  the size of the data to send (0-8 bytes)
    :param periodMs:  the period to repeat the packet at. Use
                      HAL_CAN_SEND_PERIOD_NO_REPEAT to not repeat.
    """
def allocateDigitalPWM() -> typing.Tuple[int, int]:
    """
    Allocates a DO PWM Generator.

    :returns: the allocated digital PWM handle
    """
def calibrateAnalogGyro(handle: int) -> int:
    """
    Calibrates the analog gyro.

    This happens by calculating the average value of the gyro over 5 seconds, and
    setting that as the center. Note that this call blocks for 5 seconds to
    perform this.

    :param handle: the gyro handle
    """
def cancelNotifierAlarm(notifierHandle: int) -> int:
    """
    Cancels the next notifier alarm.

    This does not cause HAL_WaitForNotifierAlarm to return.

    :param notifierHandle: the notifier handle
    """
def checkAnalogInputChannel(channel: int) -> int:
    """
    Checks that the analog output channel number is value.
    Verifies that the analog channel number is one of the legal channel numbers.
    Channel numbers are 0-based.

    :param channel: The analog output channel number.

    :returns: Analog channel is valid
    """
def checkAnalogModule(module: int) -> int:
    """
    Checks that the analog module number is valid.

    :param module: The analog module number.

    :returns: Analog module is valid and present
    """
def checkAnalogOutputChannel(channel: int) -> int:
    """
    Checks that the analog output channel number is value.

    Verifies that the analog channel number is one of the legal channel numbers.
    Channel numbers are 0-based.

    :returns: Analog channel is valid
    """
def checkCompressorModule(module: int) -> int:
    """
    Gets if a compressor module is valid.

    :param module: the module number

    :returns: true if the module is valid, otherwise false
    """
def checkDIOChannel(channel: int) -> int:
    """
    Checks if a DIO channel is valid.

    :param channel: the channel number to check

    :returns: true if the channel is correct, otherwise false
    """
def checkPDPChannel(channel: int) -> int:
    """
    Checks if a PDP channel is valid.

    :param channel: the channel to check

    :returns: true if the channel is valid, otherwise false
    """
def checkPDPModule(module: int) -> int:
    """
    Checks if a PDP module is valid.

    :param channel: the module to check

    :returns: true if the module is valid, otherwise false
    """
def checkPWMChannel(channel: int) -> int:
    """
    Checks if a pwm channel is valid.

    :param channel: the channel to check

    :returns: true if the channel is valid, otherwise false
    """
def checkRelayChannel(channel: int) -> int:
    """
    Checks if a relay channel is valid.

    :param channel: the channel to check

    :returns: true if the channel is valid, otherwise false
    """
def checkSolenoidChannel(channel: int) -> int:
    """
    Checks if a solenoid channel is in the valid range.

    :param channel: the channel number to check

    :returns: true if the channel number is valid, otherwise false
    """
def checkSolenoidModule(module: int) -> int:
    """
    Checks if a solenoid module is in the valid range.

    :param module: the module number to check

    :returns: true if the module number is valid, otherwise false
    """
def cleanAnalogTrigger(analogTriggerHandle: int) -> int:
    """
    Frees an analog trigger.

    :param analogTriggerHandle: the trigger handle
    """
def cleanCAN(handle: int) -> None:
    """
    Frees a CAN device

    :param handle: the CAN handle
    """
def cleanInterrupts(interruptHandle: int) -> typing.Tuple[capsule, int]:
    """
    Frees an interrupt.

    :param interruptHandle: the interrupt handle

    :returns: the param passed to the interrupt, or nullptr if one
              wasn't passed.
    """
def cleanNotifier(notifierHandle: int) -> int:
    """
    Cleans a notifier.

    Note this also stops a notifier if it is already running.

    :param notifierHandle: the notifier handle
    """
def cleanPDP(handle: int) -> None:
    """
    Cleans a PDP module.

    :param handle: the module handle
    """
def clearAllPCMStickyFaults(module: int) -> int:
    """
    Clears all faults on a module.

    :param module: the module to clear
    """
def clearCounterDownSource(counterHandle: int) -> int:
    """
    Disables the down counting source to the counter.

    :param counterHandle: the counter handle
    """
def clearCounterUpSource(counterHandle: int) -> int:
    """
    Disables the up counting source to the counter.

    :param counterHandle: the counter handle
    """
def clearPDPStickyFaults(handle: int) -> int:
    """
    Clears any PDP sticky faults.

    :param handle: the module handle
    """
def clearSerial(handle: int) -> int:
    """
    Clears the receive buffer of the serial port.

    :param handle: the serial port handle
    """
def closeI2C(port: I2CPort) -> None:
    """
    Closes an I2C port

    :param port: The I2C port, 0 for the on-board, 1 for the MXP.
    """
def closeSPI(port: SPIPort) -> None:
    """
    Closes the SPI port.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for MXP
    """
def closeSerial(handle: int) -> int:
    """
    Closes a serial port.

    :param handle: the serial port handle to close
    """
def configureSPIAutoStall(port: SPIPort, csToSclkTicks: int, stallTicks: int, pow2BytesPerRead: int) -> int:
    """
    Configure the Auto SPI Stall time between reads.

    :param port:             The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                             MXP.
    :param csToSclkTicks:    the number of ticks to wait before asserting the cs pin
    :param stallTicks:       the number of ticks to stall for
    :param pow2BytesPerRead: the number of bytes to read before stalling
    """
def createHandle(index: int, handleType: HandleEnum, version: int) -> int:
    """
    Create a handle for a specific index, type and version.

    Note the version is not checked on the roboRIO.

    :param index:      the index
    :param handleType: the handle type
    :param version:    the handle version

    :returns: the created handle
    """
def createPortHandle(channel: int, module: int) -> int:
    """
    Create a port handle.

    :param channel: the channel
    :param module:  the module

    :returns: port handle for the module and channel
    """
def createPortHandleForSPI(channel: int) -> int:
    """
    Create a port handle for SPI.

    :param channel: the SPI channel

    :returns: port handle for the channel
    """
def createSimDevice(name: str) -> int:
    """
    Creates a simulated device.

    The device name must be unique.  0 is returned if the device name already
    exists.  If multiple instances of the same device are desired, recommend
    appending the instance/unique identifer in brackets to the base name,
    e.g. "device[1]".

    0 is returned if not in simulation.

    :param name: device name

    :returns: simulated device handle
    """
def createSimValue(device: int, name: str, direction: int, initialValue: HAL_Value) -> int:
    pass
def createSimValueBoolean(device: int, name: str, direction: int, initialValue: int) -> int:
    """
    Creates a boolean value on a simulated device.

    Returns 0 if not in simulation; this can be used to avoid calls
    to Set/Get functions.

    :param device:       simulated device handle
    :param name:         value name
    :param direction:    input/output/bidir (from perspective of user code)
    :param initialValue: initial value

    :returns: simulated value handle
    """
def createSimValueDouble(device: int, name: str, direction: int, initialValue: float) -> int:
    """
    Creates a double value on a simulated device.

    Returns 0 if not in simulation; this can be used to avoid calls
    to Set/Get functions.

    :param device:       simulated device handle
    :param name:         value name
    :param direction:    input/output/bidir (from perspective of user code)
    :param initialValue: initial value

    :returns: simulated value handle
    """
def createSimValueEnum(device: int, name: str, direction: bool, options: typing.List[str], initialValue: int) -> int:
    """
    Creates an enumerated value on a simulated device.

    Enumerated values are always in the range 0 to numOptions-1.

    Returns 0 if not in simulation; this can be used to avoid calls
    to Set/Get functions.

    :param device:       simulated device handle
    :param name:         value name
    :param direction:    input/output/bidir (from perspective of user code)
    :param numOptions:   number of enumerated value options (length of options)
    :param options:      array of option descriptions
    :param initialValue: initial value (selection)

    :returns: simulated value handle
    """
def createSimValueInt(device: int, name: str, direction: int, initialValue: int) -> int:
    """
    Creates an int value on a simulated device.

    Returns 0 if not in simulation; this can be used to avoid calls
    to Set/Get functions.

    :param device:       simulated device handle
    :param name:         value name
    :param direction:    input/output/bidir (from perspective of user code)
    :param initialValue: initial value

    :returns: simulated value handle
    """
def createSimValueLong(device: int, name: str, direction: int, initialValue: int) -> int:
    """
    Creates a long value on a simulated device.

    Returns 0 if not in simulation; this can be used to avoid calls
    to Set/Get functions.

    :param device:       simulated device handle
    :param name:         value name
    :param direction:    input/output/bidir (from perspective of user code)
    :param initialValue: initial value

    :returns: simulated value handle
    """
def disableInterrupts(interruptHandle: int) -> int:
    """
    Disables interrupts without without deallocating structures.

    :param interruptHandle: the interrupt handle
    """
def disableSerialTermination(handle: int) -> int:
    """
    Disables a termination character for reads.

    :param handle: the serial port handle
    """
def enableInterrupts(interruptHandle: int) -> int:
    """
    Enables interrupts to occur on this input.

    Interrupts are disabled when the RequestInterrupt call is made. This gives
    time to do the setup of the other options before starting to field
    interrupts.

    :param interruptHandle: the interrupt handle
    """
def enableSerialTermination(handle: int, terminator: str) -> int:
    """
    Sets the termination character that terminates a read.

    By default this is disabled.

    :param handle:     the serial port handle
    :param terminator: the termination character to set
    """
def exitMain() -> None:
    """
    Causes HAL_RunMain() to exit.

    If HAL_SetMain() has been called, this calls the exit function provided
    to that function.
    """
def expandFPGATime(unexpanded_lower: int) -> typing.Tuple[int, int]:
    """
    Given an 32 bit FPGA time, expand it to the nearest likely 64 bit FPGA time.

    Note: This is making the assumption that the timestamp being converted is
    always in the past.  If you call this with a future timestamp, it probably
    will make it in the past.  If you wait over 70 minutes between capturing the
    bottom 32 bits of the timestamp and expanding it, you will be off by
    multiples of 1<<32 microseconds.

    :returns: The current time in microseconds according to the FPGA (since FPGA
              reset) as a 64 bit number.
    """
def fireOneShot(solenoidPortHandle: int) -> int:
    """
    Fires a single pulse on a solenoid channel.

    The pulse is the duration set by HAL_SetOneShotDuration().

    :param solenoidPortHandle: the solenoid handle
    """
def flushSerial(handle: int) -> int:
    """
    Flushes the serial write buffer out to the port.

    :param handle: the serial port handle
    """
def forceSPIAutoRead(port: SPIPort) -> int:
    """
    Immediately forces an SPI read to happen.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                 MXP.
    """
def freeAddressableLED(handle: int) -> None:
    pass
def freeAnalogGyro(handle: int) -> None:
    """
    Frees an analog gyro.

    :param handle: the gyro handle
    """
def freeAnalogInputPort(analogPortHandle: int) -> None:
    """
    Frees an analog input port.

    :param analogPortHandle: Handle to the analog port.
    """
def freeAnalogOutputPort(analogOutputHandle: int) -> None:
    """
    Frees an analog output port.

    :param analogOutputHandle: the analog output handle
    """
def freeCounter(counterHandle: int) -> int:
    """
    Frees a counter.

    :param counterHandle: the counter handle
    """
def freeDIOPort(dioPortHandle: int) -> None:
    pass
def freeDigitalPWM(pwmGenerator: int) -> int:
    """
    Frees the resource associated with a DO PWM generator.

    :param pwmGenerator: the digital PWM handle
    """
def freeDutyCycle(dutyCycleHandle: int) -> None:
    """
    Free a DutyCycle.

    :param dutyCycleHandle: the duty cycle handle
    """
def freeEncoder(encoderHandle: int) -> int:
    """
    Frees an encoder.

    :param encoderHandle: the encoder handle
    """
def freePWMPort(pwmPortHandle: int) -> int:
    """
    Frees a PWM port.

    :param pwmPortHandle: the pwm handle
    """
def freeRelayPort(relayPortHandle: int) -> None:
    """
    Frees a relay port.

    :param relayPortHandle: the relay handle
    """
def freeSPIAuto(port: SPIPort) -> int:
    """
    Frees an SPI automatic accumulator.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                 MXP.
    """
def freeSimDevice(handle: int) -> None:
    """
    Frees a simulated device.

    This also allows the same device name to be used again.
    This also frees all the simulated values created on the device.

    :param handle: simulated device handle
    """
def freeSolenoidPort(solenoidPortHandle: int) -> None:
    """
    Frees a solenoid port.

    :param solenoidPortHandle: the solenoid handle
    """
def getAccelerometerX() -> float:
    """
    Gets the x-axis acceleration.

    This is a floating point value in units of 1 g-force.

    :returns: the X acceleration
    """
def getAccelerometerY() -> float:
    """
    Gets the y-axis acceleration.

    This is a floating point value in units of 1 g-force.

    :returns: the Y acceleration
    """
def getAccelerometerZ() -> float:
    """
    Gets the z-axis acceleration.

    This is a floating point value in units of 1 g-force.

    :returns: the Z acceleration
    """
def getAccumulatorCount(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Read the number of accumulated values.

    Read the count of the accumulated values since the accumulator was last
    Reset().

    :param analogPortHandle: Handle to the analog port.

    :returns: The number of times samples from the channel were accumulated.
    """
def getAccumulatorOutput(analogPortHandle: int) -> typing.Tuple[int, int, int]:
    """
    Read the accumulated value and the number of accumulated values atomically.

    This function reads the value and count from the FPGA atomically.
    This can be used for averaging.

    :param analogPortHandle: Handle to the analog port.
    :param value:            Pointer to the 64-bit accumulated output.
    :param count:            Pointer to the number of accumulation cycles.
    """
def getAccumulatorValue(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Read the accumulated value.

    Read the value that has been accumulating on channel 1.
    The accumulator is attached after the oversample and average engine.

    :param analogPortHandle: Handle to the analog port.

    :returns: The 64-bit value accumulated since the last Reset().
    """
def getAllSolenoids(module: int) -> typing.Tuple[int, int]:
    """
    Gets the status of all solenoids on a specific module.

    :param module: the module to check

    :returns: bitmask of the channels, 1 for on 0 for off
    """
def getAllianceStation() -> typing.Tuple[AllianceStationID, int]:
    """
    Gets the current alliance station ID.

    :param status: the error code, or 0 for success

    :returns: the alliance station ID
    """
def getAnalogAverageBits(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the number of averaging bits.

    This gets the number of averaging bits from the FPGA. The actual number of
    averaged samples is 2**bits. The averaging is done automatically in the FPGA.

    :param analogPortHandle: Handle to the analog port to use.

    :returns: Bits to average.
    """
def getAnalogAverageValue(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets a sample from the output of the oversample and average engine for the
    channel.

    The sample is 12-bit + the value configured in SetOversampleBits().
    The value configured in SetAverageBits() will cause this value to be averaged
    2**bits number of samples. This is not a sliding window.  The sample will not
    change until 2**(OversamplBits + AverageBits) samples have been acquired from
    the module on this channel. Use GetAverageVoltage() to get the analog value
    in calibrated units.

    :param analogPortHandle: Handle to the analog port to use.

    :returns: A sample from the oversample and average engine for the channel.
    """
def getAnalogAverageVoltage(analogPortHandle: int) -> typing.Tuple[float, int]:
    """
    Gets a scaled sample from the output of the oversample and average engine for
    the channel.

    The value is scaled to units of Volts using the calibrated scaling data from
    GetLSBWeight() and GetOffset(). Using oversampling will cause this value to
    be higher resolution, but it will update more slowly. Using averaging will
    cause this value to be more stable, but it will update more slowly.

    :param analogPortHandle: Handle to the analog port to use.

    :returns: A scaled sample from the output of the oversample and average engine
              for the channel.
    """
def getAnalogGyroAngle(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the gyro angle in degrees.

    :param handle: the gyro handle

    :returns: the gyro angle in degrees
    """
def getAnalogGyroCenter(handle: int) -> typing.Tuple[int, int]:
    """
    Gets the calibrated gyro center.

    Can be used to not repeat a calibration but reconstruct the gyro object.

    :param handle: the gyro handle

    :returns: the gyro center
    """
def getAnalogGyroOffset(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the calibrated gyro offset.

    Can be used to not repeat a calibration but reconstruct the gyro object.

    :param handle: the gyro handle

    :returns: the gryo offset
    """
def getAnalogGyroRate(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the gyro rate in degrees/second.

    :param handle: the gyro handle

    :returns: the gyro rate in degrees/second
    """
def getAnalogLSBWeight(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the factory scaling least significant bit weight constant.
    The least significant bit weight constant for the channel that was calibrated
    in manufacturing and stored in an eeprom in the module.

    Volts = ((LSB_Weight * 1e-9) * raw) - (Offset * 1e-9)

    :param analogPortHandle: Handle to the analog port to use.

    :returns: Least significant bit weight.
    """
def getAnalogOffset(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the factory scaling offset constant.
    The offset constant for the channel that was calibrated in manufacturing and
    stored in an eeprom in the module.

    Volts = ((LSB_Weight * 1e-9) * raw) - (Offset * 1e-9)

    :param analogPortHandle: Handle to the analog port to use.

    :returns: Offset constant.
    """
def getAnalogOutput(analogOutputHandle: int) -> typing.Tuple[float, int]:
    """
    Gets the current analog output value.

    :param analogOutputHandle: the analog output handle

    :returns: the current output voltage (0-5v)
    """
def getAnalogOversampleBits(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the number of oversample bits.

    This gets the number of oversample bits from the FPGA. The actual number of
    oversampled values is 2**bits. The oversampling is done automatically in the
    FPGA.

    :param analogPortHandle: Handle to the analog port to use.

    :returns: Bits to oversample.
    """
def getAnalogSampleRate() -> typing.Tuple[float, int]:
    """
    Gets the current sample rate.

    This assumes one entry in the scan list.
    This is a global setting for the Athena and effects all channels.

    :returns: Sample rate.
    """
def getAnalogTriggerFPGAIndex(analogTriggerHandle: int) -> typing.Tuple[int, int]:
    """
    Get the FPGA index for the AnlogTrigger.

    :param analogTriggerHandle: the trigger handle

    :returns: the FPGA index
    """
def getAnalogTriggerInWindow(analogTriggerHandle: int) -> typing.Tuple[int, int]:
    """
    Returns the InWindow output of the analog trigger.

    True if the analog input is between the upper and lower limits.

    :param analogTriggerHandle: the trigger handle

    :returns: the InWindow output of the analog trigger
    """
def getAnalogTriggerOutput(analogTriggerHandle: int, type: AnalogTriggerType) -> typing.Tuple[int, int]:
    """
    Gets the state of the analog trigger output.

    :param analogTriggerHandle: the trigger handle
    :param type:                the type of trigger to trigger on

    :returns: the state of the analog trigger output
    """
def getAnalogTriggerTriggerState(analogTriggerHandle: int) -> typing.Tuple[int, int]:
    """
    Returns the TriggerState output of the analog trigger.

    True if above upper limit.
    False if below lower limit.
    If in Hysteresis, maintain previous state.

    :param analogTriggerHandle: the trigger handle

    :returns: the TriggerState output of the analog trigger
    """
def getAnalogValue(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets a sample straight from the channel on this module.

    The sample is a 12-bit value representing the 0V to 5V range of the A/D
    converter in the module. The units are in A/D converter codes.  Use
    GetVoltage() to get the analog value in calibrated units.

    :param analogPortHandle: Handle to the analog port to use.

    :returns: A sample straight from the channel on this module.
    """
def getAnalogValueToVolts(analogPortHandle: int, rawValue: int) -> typing.Tuple[float, int]:
    """
    Get the analog voltage from a raw value.

    :param analogPortHandle: Handle to the analog port the values were read from.
    :param rawValue:         The raw analog value

    :returns: The voltage relating to the value
    """
def getAnalogVoltage(analogPortHandle: int) -> typing.Tuple[float, int]:
    """
    Gets a scaled sample straight from the channel on this module.

    The value is scaled to units of Volts using the calibrated scaling data from
    GetLSBWeight() and GetOffset().

    :param analogPortHandle: Handle to the analog port to use.

    :returns: A scaled sample straight from the channel on this module.
    """
def getAnalogVoltsToValue(analogPortHandle: int, voltage: float) -> typing.Tuple[int, int]:
    """
    Converts a voltage to a raw value for a specified channel.

    This process depends on the calibration of each channel, so the channel must
    be specified.

    @todo This assumes raw values.  Oversampling not supported as is.

    :param analogPortHandle: Handle to the analog port to use.
    :param voltage:          The voltage to convert.

    :returns: The raw value for the channel.
    """
def getBrownedOut() -> typing.Tuple[int, int]:
    """
    Gets if the system is in a browned out state.

    :returns: true if the system is in a low voltage brown out, false otherwise
    """
def getCompressor(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the compressor state (on or off).

    :param compressorHandle: the compressor handle

    :returns: true if the compressor is on, otherwise false
    """
def getCompressorClosedLoopControl(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets if the compressor is in closed loop mode.

    :param compressorHandle: the compressor handle

    :returns: true if the compressor is in closed loop mode,
              otherwise false
    """
def getCompressorCurrent(compressorHandle: int) -> typing.Tuple[float, int]:
    """
    Gets the compressor current.

    :param compressorHandle: the compressor handle

    :returns: the compressor current in amps
    """
def getCompressorCurrentTooHighFault(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets if the compressor is faulted because of too high of current.

    :param compressorHandle: the compressor handle

    :returns: true if falted, otherwise false
    """
def getCompressorCurrentTooHighStickyFault(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets if a sticky fauly is triggered because of too high of current.

    :param compressorHandle: the compressor handle

    :returns: true if falted, otherwise false
    """
def getCompressorNotConnectedFault(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets if the compressor is not connected.

    :param compressorHandle: the compressor handle

    :returns: true if not connected, otherwise false
    """
def getCompressorNotConnectedStickyFault(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets if a sticky fault is triggered of the compressor not connected.

    :param compressorHandle: the compressor handle

    :returns: true if falted, otherwise false
    """
def getCompressorPressureSwitch(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the compressor pressure switch state.

    :param compressorHandle: the compressor handle

    :returns: true if the pressure switch is triggered, otherwise
              false
    """
def getCompressorShortedFault(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets if the compressor is faulted because of a short.

    :param compressorHandle: the compressor handle

    :returns: true if shorted, otherwise false
    """
def getCompressorShortedStickyFault(compressorHandle: int) -> typing.Tuple[int, int]:
    """
    Gets if a sticky fauly is triggered because of a short.

    :param compressorHandle: the compressor handle

    :returns: true if falted, otherwise false
    """
def getControlWord(controlWord: ControlWord) -> int:
    """
    Gets the current control word of the driver station.

    The control work contains the robot state.

    :param controlWord: the control word (out)

    :returns: the error code, or 0 for success
    """
def getCounter(counterHandle: int) -> typing.Tuple[int, int]:
    """
    Reads the current counter value.

    Reads the value at this instant. It may still be running, so it reflects the
    current value. Next time it is read, it might have a different value.

    :param counterHandle: the counter handle

    :returns: the current counter value
    """
def getCounterDirection(counterHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the last direction the counter value changed.

    :param counterHandle: the counter handle

    :returns: the last direction the counter value changed
    """
def getCounterPeriod(counterHandle: int) -> typing.Tuple[float, int]:
    pass
def getCounterSamplesToAverage(counterHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the Samples to Average which specifies the number of samples of the
    timer to average when calculating the period. Perform averaging to account
    for mechanical imperfections or as oversampling to increase resolution.

    :param counterHandle: the counter handle

    :returns: SamplesToAverage The number of samples being averaged (from 1 to 127)
    """
def getCounterStopped(counterHandle: int) -> typing.Tuple[int, int]:
    """
    Determines if the clock is stopped.

    Determine if the clocked input is stopped based on the MaxPeriod value set
    using the SetMaxPeriod method. If the clock exceeds the MaxPeriod, then the
    device (and counter) are assumed to be stopped and it returns true.

    :param counterHandle: the counter handle

    :returns: true if the most recent counter period exceeds the
              MaxPeriod value set by SetMaxPeriod
    """
def getCurrentThreadPriority(isRealTime: int) -> typing.Tuple[int, int]:
    """
    Gets the thread priority for the current thread.

    :param handle:     Native handle pointer to the thread to get the priority for
    :param isRealTime: Set to true if thread is real-time, otherwise false.
    :param status:     Error status variable. 0 on success.

    :returns: The current thread priority. For real-time, this is 1-99
              with 99 being highest. For non-real-time, this is 0. See
              "man 7 sched" for details.
    """
def getDIO(dioPortHandle: int) -> typing.Tuple[int, int]:
    """
    Reads a digital value from a DIO channel.

    :param dioPortHandle: the digital port handle

    :returns: the state of the specified channel
    """
def getDIODirection(dioPortHandle: int) -> typing.Tuple[int, int]:
    """
    Reads the direction of a DIO channel.

    :param dioPortHandle: the digital port handle

    :returns: true for input, false for output
    """
def getDutyCycleFPGAIndex(dutyCycleHandle: int) -> typing.Tuple[int, int]:
    """
    Get the FPGA index for the DutyCycle.

    :param dutyCycleHandle: the duty cycle handle

    :returns: the FPGA index
    """
def getDutyCycleFrequency(dutyCycleHandle: int) -> typing.Tuple[int, int]:
    """
    Get the frequency of the duty cycle signal.

    :param dutyCycleHandle: the duty cycle handle

    :returns: frequency in Hertz
    """
def getDutyCycleOutput(dutyCycleHandle: int) -> typing.Tuple[float, int]:
    """
    Get the output ratio of the duty cycle signal.

    0 means always low, 1 means always high.

    :param dutyCycleHandle: the duty cycle handle

    :returns: output ratio between 0 and 1
    """
def getDutyCycleOutputRaw(dutyCycleHandle: int) -> typing.Tuple[int, int]:
    """
    Get the raw output ratio of the duty cycle signal.

    0 means always low, an output equal to
    GetOutputScaleFactor() means always high.

    :param dutyCycleHandle: the duty cycle handle

    :returns: output ratio in raw units
    """
def getDutyCycleOutputScaleFactor(dutyCycleHandle: int) -> typing.Tuple[int, int]:
    """
    Get the scale factor of the output.

    An output equal to this value is always high, and then linearly scales
    down to 0. Divide the result of getOutputRaw by this in order to get the
    percentage between 0 and 1.

    :param dutyCycleHandle: the duty cycle handle

    :returns: the output scale factor
    """
def getEncoder(encoderHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the current counts of the encoder after encoding type scaling.

    This is scaled by the value passed duing initialization to encodingType.

    :param encoderHandle: the encoder handle

    :returns: the current scaled count
    """
def getEncoderDecodingScaleFactor(encoderHandle: int) -> typing.Tuple[float, int]:
    """
    Gets the decoding scale factor of the encoder.

    This is used to perform the scaling from raw to type scaled values.

    :param encoderHandle: the encoder handle

    :returns: the scale value for the encoder
    """
def getEncoderDirection(encoderHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the last direction the encoder value changed.

    :param encoderHandle: the encoder handle

    :returns: the last direction the encoder value changed
    """
def getEncoderDistance(encoderHandle: int) -> typing.Tuple[float, int]:
    """
    Gets the current distance traveled by the encoder.

    This is the encoder count scaled by the distance per pulse set for the
    encoder.

    :param encoderHandle: the encoder handle

    :returns: the encoder distance (units are determined by the units
              passed to HAL_SetEncoderDistancePerPulse)
    """
def getEncoderDistancePerPulse(encoderHandle: int) -> typing.Tuple[float, int]:
    """
    Gets the user set distance per pulse of the encoder.

    :param encoderHandle: the encoder handle

    :returns: the set distance per pulse
    """
def getEncoderEncodingScale(encoderHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the encoder scale value.

    This is set by the value passed during initialization to encodingType.

    :param encoderHandle: the encoder handle

    :returns: the encoder scale value
    """
def getEncoderEncodingType(encoderHandle: int) -> typing.Tuple[EncoderEncodingType, int]:
    """
    Gets the encoding type of the encoder.

    :param encoderHandle: the encoder handle

    :returns: the encoding type
    """
def getEncoderFPGAIndex(encoderHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the FPGA index of the encoder.

    :param encoderHandle: the encoder handle

    :returns: the FPGA index of the encoder
    """
def getEncoderPeriod(encoderHandle: int) -> typing.Tuple[float, int]:
    pass
def getEncoderRate(encoderHandle: int) -> typing.Tuple[float, int]:
    """
    Gets the current rate of the encoder.

    This is the encoder period scaled by the distance per pulse set for the
    encoder.

    :param encoderHandle: the encoder handle

    :returns: the encoder rate (units are determined by the units
              passed to HAL_SetEncoderDistancePerPulse, time value is seconds)
    """
def getEncoderRaw(encoderHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the raw counts of the encoder.

    This is not scaled by any values.

    :param encoderHandle: the encoder handle

    :returns: the raw encoder count
    """
def getEncoderSamplesToAverage(encoderHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the current samples to average value.

    :param encoderHandle: the encoder handle

    :returns: the current samples to average value
    """
def getEncoderStopped(encoderHandle: int) -> typing.Tuple[int, int]:
    """
    Determines if the clock is stopped.

    Determines if the clocked input is stopped based on the MaxPeriod value set
    using the SetMaxPeriod method. If the clock exceeds the MaxPeriod, then the
    device (and encoder) are assumed to be stopped and it returns true.

    :param encoderHandle: the encoder handle

    :returns: true if the most recent encoder period exceeds the
              MaxPeriod value set by SetMaxPeriod
    """
def getErrorMessage(code: int) -> str:
    """
    Gets the error message for a specific status code.

    :param code: the status code

    :returns: the error message for the code. This does not need to be freed.
    """
def getFPGAButton() -> typing.Tuple[int, int]:
    """
    Gets the state of the "USER" button on the roboRIO.

    :returns: true if the button is currently pressed down
    """
def getFPGARevision() -> typing.Tuple[int, int]:
    """
    Returns the FPGA Revision number.

    The format of the revision is 3 numbers.
    The 12 most significant bits are the Major Revision.
    the next 8 bits are the Minor Revision.
    The 12 least significant bits are the Build Number.

    :returns: FPGA Revision number.
    """
def getFPGATime() -> typing.Tuple[int, int]:
    """
    Reads the microsecond-resolution timer on the FPGA.

    :returns: The current time in microseconds according to the FPGA (since FPGA
              reset).
    """
def getFPGAVersion() -> typing.Tuple[int, int]:
    """
    Returns the FPGA Version number.

    For now, expect this to be competition year.

    :returns: FPGA Version number.
    """
def getFilterPeriod(filterIndex: int) -> typing.Tuple[int, int]:
    """
    Gets the filter period for the specified filter index.

    Gets the filter period in FPGA cycles.  Even though there are 2 different
    filter index domains (MXP vs HDR), ignore that distinction for now since it
    compilicates the interface.  Set status to NiFpga_Status_SoftwareFault if the
    filter values miss-match.

    :param filterIndex: the filter index, 0 - 2
    :param value:       the number of cycles that the signal must not transition
                        to be counted as a transition.
    """
def getFilterSelect(dioPortHandle: int) -> typing.Tuple[int, int]:
    """
    Reads the filter index from the FPGA.

    Gets the filter index used to filter out short pulses.

    :param dioPortHandle: the digital port handle

    :returns: filterIndex  the filter index (Must be in the range 0 - 3,
              where 0 means "none" and 1 - 3 means filter # filterIndex - 1)
    """
def getHandleIndex(handle: int) -> int:
    """
    Get the handle index from a handle.

    :param handle: the handle

    :returns: the index
    """
def getHandleType(handle: int) -> HandleEnum:
    """
    Get the handle type from a handle.

    :param handle: the handle

    :returns: the type
    """
def getHandleTypedIndex(handle: int, enumType: HandleEnum, version: int) -> int:
    """
    Get if the handle is a correct type and version.

    Note the version is not checked on the roboRIO.

    :param handle:     the handle
    :param handleType: the type to check
    :param version:    the handle version to check

    :returns: true if the handle is proper version and type, otherwise
              false.
    """
def getJoystickAxes(joystickNum: int, axes: JoystickAxes) -> int:
    """
    Gets the axes of a specific joystick.

    :param joystickNum: the joystick number
    :param axes:        the axes values (output)

    :returns: the error code, or 0 for success
    """
def getJoystickAxisType(joystickNum: int, axis: int) -> int:
    """
    Gets the type of a specific joystick axis.

    This is device specific, and different depending on what system input type
    the joystick uses.

    :param joystickNum: the joystick number
    :param axis:        the axis number

    :returns: the enumerated axis type
    """
def getJoystickButtons(joystickNum: int, buttons: JoystickButtons) -> int:
    """
    Gets the buttons of a specific joystick.

    :param joystickNum: the joystick number
    :param buttons:     the button values (output)

    :returns: the error code, or 0 for success
    """
def getJoystickDescriptor(joystickNum: int, desc: JoystickDescriptor) -> int:
    """
    Retrieves the Joystick Descriptor for particular slot.

    :param desc: out] descriptor (data transfer object) to fill in.  desc is
                 filled in regardless of success. In other words, if descriptor is not
                 available, desc is filled in with default values matching the init-values in
                 Java and C++ Driverstation for when caller requests a too-large joystick
                 index.

    :returns: error code reported from Network Comm back-end.  Zero is good,
              nonzero is bad.
    """
def getJoystickIsXbox(joystickNum: int) -> int:
    """
    Gets is a specific joystick is considered to be an XBox controller.

    :param joystickNum: the joystick number

    :returns: true if xbox, false otherwise
    """
def getJoystickName(joystickNum: int) -> str:
    """
    Gets the name of a joystick.

    The returned array must be freed with HAL_FreeJoystickName.

    Will be null terminated.

    :param joystickNum: the joystick number

    :returns: the joystick name
    """
def getJoystickPOVs(joystickNum: int, povs: JoystickPOVs) -> int:
    """
    Gets the POVs of a specific joystick.

    :param joystickNum: the joystick number
    :param povs:        the POV values (output)

    :returns: the error code, or 0 for success
    """
def getJoystickType(joystickNum: int) -> int:
    """
    Gets the type of joystick connected.

    This is device specific, and different depending on what system input type
    the joystick uses.

    :param joystickNum: the joystick number

    :returns: the enumerated joystick type
    """
def getMatchInfo(info: MatchInfo) -> int:
    """
    Gets info about a specific match.

    :param info: the match info (output)

    :returns: the error code, or 0 for success
    """
def getMatchTime() -> typing.Tuple[float, int]:
    """
    Returns the approximate match time.

    The FMS does not send an official match time to the robots, but does send
    an approximate match time. The value will count down the time remaining in
    the current period (auto or teleop).

    Warning: This is not an official time (so it cannot be used to dispute ref
    calls or guarantee that a function will trigger before the match ends).

    The Practice Match function of the DS approximates the behavior seen on
    the field.

    :param status: the error code, or 0 for success

    :returns: time remaining in current match period (auto or teleop)
    """
def getNumAccumulators() -> int:
    """
    Gets the number of analog accumulators in the current system.

    :returns: the number of analog accumulators
    """
def getNumAddressableLEDs() -> int:
    """
    Gets the number of addressable LED generators in the current system.

    :returns: the number of Addressable LED generators
    """
def getNumAnalogInputs() -> int:
    """
    Gets the number of analog inputs in the current system.

    :returns: the number of analog inputs
    """
def getNumAnalogOutputs() -> int:
    """
    Gets the number of analog outputs in the current system.

    :returns: the number of analog outputs
    """
def getNumAnalogTriggers() -> int:
    """
    Gets the number of analog triggers in the current system.

    :returns: the number of analog triggers
    """
def getNumCounters() -> int:
    """
    Gets the number of analog counters in the current system.

    :returns: the number of counters
    """
def getNumDigitalChannels() -> int:
    """
    Gets the number of digital channels in the current system.

    :returns: the number of digital channels
    """
def getNumDigitalHeaders() -> int:
    """
    Gets the number of digital headers in the current system.

    :returns: the number of digital headers
    """
def getNumDigitalPWMOutputs() -> int:
    """
    Gets the number of digital IO PWM outputs in the current system.

    :returns: the number of digital IO PWM outputs
    """
def getNumDutyCycles() -> int:
    """
    Gets the number of duty cycle inputs in the current system.

    :returns: the number of Duty Cycle inputs
    """
def getNumEncoders() -> int:
    """
    Gets the number of quadrature encoders in the current system.

    :returns: the number of quadrature encoders
    """
def getNumInterrupts() -> int:
    """
    Gets the number of interrupts in the current system.

    :returns: the number of interrupts
    """
def getNumPCMModules() -> int:
    """
    Gets the number of PCM modules in the current system.

    :returns: the number of PCM modules
    """
def getNumPDPChannels() -> int:
    """
    Gets the number of PDP channels in the current system.

    :returns: the number of PDP channels
    """
def getNumPDPModules() -> int:
    """
    Gets the number of PDP modules in the current system.

    :returns: the number of PDP modules
    """
def getNumPWMChannels() -> int:
    """
    Gets the number of PWM channels in the current system.

    :returns: the number of PWM channels
    """
def getNumPWMHeaders() -> int:
    """
    Gets the number of PWM headers in the current system.

    :returns: the number of PWM headers
    """
def getNumRelayChannels() -> int:
    """
    Gets the number of relay channels in the current system.

    :returns: the number of relay channels
    """
def getNumRelayHeaders() -> int:
    """
    Gets the number of relay headers in the current system.

    :returns: the number of relay headers
    """
def getNumSolenoidChannels() -> int:
    """
    Gets the number of solenoid channels in the current system.

    :returns: the number of solenoid channels
    """
def getPCMSolenoidBlackList(module: int) -> typing.Tuple[int, int]:
    """
    Gets the channels blacklisted from being enabled on a module.

    :param module: the module to check
                   @retur        bitmask of the blacklisted channels, 1 for true 0 for false
    """
def getPCMSolenoidVoltageFault(module: int) -> typing.Tuple[int, int]:
    """
    Gets if a specific module has an over or under voltage fault.

    :param module: the module to check

    :returns: true if faulted, otherwise false
    """
def getPCMSolenoidVoltageStickyFault(module: int) -> typing.Tuple[int, int]:
    """
    Gets if a specific module has an over or under voltage sticky fault.

    :param module: the module to check

    :returns: true if a stick fault is set, otherwise false
    """
def getPDPAllChannelCurrents(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the current of all 16 channels on the PDP.

    The array must be large enough to hold all channels.

    :param handle:  the module handle
    :param current: the currents (output)
    """
def getPDPChannelCurrent(handle: int, channel: int) -> typing.Tuple[float, int]:
    """
    Gets the current of a specific PDP channel.

    :param module:  the module
    :param channel: the channel

    :returns: the channel current (amps)
    """
def getPDPTemperature(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the temperature of the PDP.

    :param handle: the module handle

    :returns: the module temperature (celsius)
    """
def getPDPTotalCurrent(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the total current of the PDP.

    :param handle: the module handle

    :returns: the total current (amps)
    """
def getPDPTotalEnergy(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the total energy of the PDP.

    :param handle: the module handle

    :returns: the total energy (joules)
    """
def getPDPTotalPower(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the total power of the PDP.

    :param handle: the module handle

    :returns: the total power (watts)
    """
def getPDPVoltage(handle: int) -> typing.Tuple[float, int]:
    """
    Gets the PDP input voltage.

    :param handle: the module handle

    :returns: the input voltage (volts)
    """
def getPWMConfigRaw(pwmPortHandle: int) -> typing.Tuple[int, int, int, int, int, int]:
    """
    Gets the raw pwm configuration settings for the PWM channel.

    Values are in raw FPGA units. These units have the potential to change for
    any FPGA release.

    :param pwmPortHandle:  the PWM handle
    :param maxPwm:         the maximum PWM value
    :param deadbandMaxPwm: the high range of the center deadband
    :param centerPwm:      the center PWM value
    :param deadbandMinPwm: the low range of the center deadband
    :param minPwm:         the minimum PWM value
    """
def getPWMCycleStartTime() -> typing.Tuple[int, int]:
    """
    Gets the pwm starting cycle time.

    This time is relative to the FPGA time.

    :returns: the pwm cycle start time
    """
def getPWMEliminateDeadband(pwmPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the current eliminate deadband value.

    :param pwmPortHandle: the PWM handle

    :returns: true if set, otherwise false
    """
def getPWMLoopTiming() -> typing.Tuple[int, int]:
    """
    Gets the loop timing of the PWM system.

    :returns: the loop time
    """
def getPWMPosition(pwmPortHandle: int) -> typing.Tuple[float, int]:
    """
    Gets a position value from a PWM channel.

    The values range from 0 to 1.

    :param pwmPortHandle: the PWM handle

    :returns: the current positional PWM value
    """
def getPWMRaw(pwmPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets a value from a PWM channel.

    The values are in raw FPGA units, and have the potential to change with any
    FPGA release.

    :param pwmPortHandle: the PWM handle

    :returns: the current raw PWM value
    """
def getPWMSpeed(pwmPortHandle: int) -> typing.Tuple[float, int]:
    """
    Gets a scaled value from a PWM channel.

    The values range from -1 to 1.

    :param pwmPortHandle: the PWM handle

    :returns: the current speed PWM value
    """
def getPort(channel: int) -> int:
    """
    Gets a port handle for a specific channel.

    The created handle does not need to be freed.

    :param channel: the channel number

    :returns: the created port
    """
def getPortHandleChannel(handle: int) -> int:
    """
    Gets the port channel of a port handle.

    :param handle: the port handle

    :returns: the port channel
    """
def getPortHandleModule(handle: int) -> int:
    """
    Gets the port module of a port handle.

    :param handle: the port handle

    :returns: the port module
    """
def getPortHandleSPIEnable(handle: int) -> int:
    """
    Gets the SPI channel of a port handle.

    :param handle: the port handle

    :returns: the port SPI channel
    """
def getPortWithModule(module: int, channel: int) -> int:
    """
    Gets a port handle for a specific channel and module.

    This is expected to be used for PCMs, as the roboRIO does not work with
    modules anymore.

    The created handle does not need to be freed.

    :param module:  the module number
    :param channel: the channel number

    :returns: the created port
    """
def getRelay(relayPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the current state of the relay channel.

    :param relayPortHandle: the relay handle

    :returns: true for on, false for off
    """
def getRuntimeType() -> RuntimeType:
    pass
def getSPIAutoDroppedCount(port: SPIPort) -> typing.Tuple[int, int]:
    """
    Gets the count of how many SPI accumulations have been missed.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                 MXP.

    :returns: The number of missed accumulations.
    """
def getSPIHandle(port: SPIPort) -> int:
    """
    Gets the stored handle for a SPI port.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for MXP

    :returns: The stored handle for the SPI port. 0 represents no stored
              handle.
    """
def getSerialBytesReceived(handle: int) -> typing.Tuple[int, int]:
    """
    Gets the number of bytes currently in the read buffer.

    :param handle: the serial port handle

    :returns: the number of bytes in the read buffer
    """
def getSerialFD(handle: int) -> typing.Tuple[int, int]:
    """
    Gets the raw serial port file descriptor from a handle.

    :param handle: the serial port handle

    :returns: the raw port descriptor
    """
def getSimValue(handle: int) -> HAL_Value:
    pass
def getSimValueBoolean(handle: int) -> int:
    """
    Gets a simulated value (boolean).

    :param handle: simulated value handle

    :returns: The current value
    """
def getSimValueDouble(handle: int) -> float:
    """
    Gets a simulated value (double).

    :param handle: simulated value handle

    :returns: The current value
    """
def getSimValueEnum(handle: int) -> int:
    """
    Gets a simulated value (enum).

    :param handle: simulated value handle

    :returns: The current value
    """
def getSimValueInt(handle: int) -> int:
    """
    Gets a simulated value (int).

    :param handle: simulated value handle

    :returns: The current value
    """
def getSimValueLong(handle: int) -> int:
    """
    Gets a simulated value (long).

    :param handle: simulated value handle

    :returns: The current value
    """
def getSolenoid(solenoidPortHandle: int) -> typing.Tuple[int, int]:
    """
    Gets the current solenoid output value.

    :param solenoidPortHandle: the solenoid handle

    :returns: true if the solenoid is on, otherwise false
    """
def getSystemActive() -> typing.Tuple[int, int]:
    """
    Gets if the system outputs are currently active

    :returns: true if the system outputs are active, false if disabled
    """
def getSystemClockTicksPerMicrosecond() -> int:
    """
    Gets the number of FPGA system clock ticks per microsecond.

    :returns: the number of clock ticks per microsecond
    """
def getUserActive3V3() -> typing.Tuple[int, int]:
    """
    Gets the active state of the 3V3 rail.

    :returns: true if the rail is active, otherwise false
    """
def getUserActive5V() -> typing.Tuple[int, int]:
    """
    Gets the active state of the 5V rail.

    :returns: true if the rail is active, otherwise false
    """
def getUserActive6V() -> typing.Tuple[int, int]:
    """
    Gets the active state of the 6V rail.

    :returns: true if the rail is active, otherwise false
    """
def getUserCurrent3V3() -> typing.Tuple[float, int]:
    """
    Gets the 3V3 rail current.

    :returns: the 3V3 rail current (amps)
    """
def getUserCurrent5V() -> typing.Tuple[float, int]:
    """
    Gets the 5V rail current.

    :returns: the 5V rail current (amps)
    """
def getUserCurrent6V() -> typing.Tuple[float, int]:
    """
    Gets the 6V rail current.

    :returns: the 6V rail current (amps)
    """
def getUserCurrentFaults3V3() -> typing.Tuple[int, int]:
    """
    Gets the fault count for the 3V3 rail.

    :returns: the number of 3V3 fault counts
    """
def getUserCurrentFaults5V() -> typing.Tuple[int, int]:
    """
    Gets the fault count for the 5V rail.

    :returns: the number of 5V fault counts
    """
def getUserCurrentFaults6V() -> typing.Tuple[int, int]:
    """
    Gets the fault count for the 6V rail.

    :returns: the number of 6V fault counts
    """
def getUserVoltage3V3() -> typing.Tuple[float, int]:
    """
    Gets the 3V3 rail voltage.

    :returns: the 3V3 rail voltage (volts)
    """
def getUserVoltage5V() -> typing.Tuple[float, int]:
    """
    Gets the 5V rail voltage.

    :returns: the 5V rail voltage (volts)
    """
def getUserVoltage6V() -> typing.Tuple[float, int]:
    """
    Gets the 6V rail voltage.

    :returns: the 6V rail voltage (volts)
    """
def getVinCurrent() -> typing.Tuple[float, int]:
    """
    Gets the roboRIO input current.

    :returns: the input current (amps)
    """
def getVinVoltage() -> typing.Tuple[float, int]:
    """
    Gets the roboRIO input voltage.

    :returns: the input voltage (volts)
    """
def hasMain() -> int:
    """
    Returns true if HAL_SetMain() has been called.

    :returns: True if HAL_SetMain() has been called, false otherwise.
    """
def initAccumulator(analogPortHandle: int) -> int:
    """
    Initialize the accumulator.

    :param analogPortHandle: Handle to the analog port.
    """
def initSPIAuto(port: SPIPort, bufferSize: int) -> int:
    """
    Initializes the SPI automatic accumulator.

    :param port:       The number of the port to use. 0-3 for Onboard CS0-CS2, 4
                       for MXP.
    :param bufferSize: The accumulator buffer size.
    """
def initialize(timeout: int, mode: int) -> int:
    """
    Call this to start up HAL. This is required for robot programs.

    This must be called before any other HAL functions. Failure to do so will
    result in undefined behavior, and likely segmentation faults. This means that
    any statically initialized variables in a program MUST call this function in
    their constructors if they want to use other HAL calls.

    The common parameters are 500 for timeout and 0 for mode.

    This function is safe to call from any thread, and as many times as you wish.
    It internally guards from any reentrancy.

    The applicable modes are:
    0: Try to kill an existing HAL from another program, if not successful,
    error.
    1: Force kill a HAL from another program.
    2: Just warn if another hal exists and cannot be killed. Will likely result
    in undefined behavior.

    :param timeout: the initialization timeout (ms)
    :param mode:    the initialization mode (see remarks)

    :returns: true if initialization was successful, otherwise false.
    """
def initializeAddressableLED(outputPort: int) -> typing.Tuple[int, int]:
    pass
def initializeAnalogGyro(handle: int) -> typing.Tuple[int, int]:
    """
    Initializes an analog gyro.

    :param handle: handle to the analog port

    :returns: the initialized gyro handle
    """
def initializeAnalogInputPort(portHandle: int) -> typing.Tuple[int, int]:
    """
    Initializes the analog input port using the given port object.

    :param portHandle: Handle to the port to initialize.

    :returns: the created analog input handle
    """
def initializeAnalogOutputPort(portHandle: int) -> typing.Tuple[int, int]:
    """
    Initializes the analog output port using the given port object.

    :param handle: handle to the port

    :returns: the created analog output handle
    """
def initializeAnalogTrigger(portHandle: int) -> typing.Tuple[int, int]:
    """
    Initializes an analog trigger.

    :param portHandle: the analog input to use for triggering

    :returns: the created analog trigger handle
    """
def initializeAnalogTriggerDutyCycle(dutyCycleHandle: int) -> typing.Tuple[int, int]:
    """
    Initializes an analog trigger with a Duty Cycle input
    """
def initializeCAN(manufacturer: CANManufacturer, deviceId: int, deviceType: CANDeviceType) -> typing.Tuple[int, int]:
    """
    Initializes a CAN device.

    These follow the FIRST standard CAN layout. Link TBD

    :param manufacturer: the can manufacturer
    :param deviceId:     the device ID (0-63)
    :param deviceType:   the device type

    :returns: the created CAN handle
    """
def initializeCompressor(module: int) -> typing.Tuple[int, int]:
    """
    Initializes a compressor on the given PCM module.

    :param module: the module number

    :returns: the created handle
    """
def initializeCounter(mode: CounterMode) -> typing.Tuple[int, int, int]:
    """
    Initializes a counter.

    :param mode:  the counter mode
    :param index: the compressor index (output)

    :returns: the created handle
    """
def initializeDIOPort(portHandle: int, input: int) -> typing.Tuple[int, int]:
    """
    Creates a new instance of a digital port.

    :param portHandle: the port handle to create from
    :param input:      true for input, false for output

    :returns: the created digital handle
    """
def initializeDriverStation() -> None:
    """
    Initializes the driver station communication. This will properly
    handle multiple calls. However note that this CANNOT be called from a library
    that interfaces with LabVIEW.
    """
def initializeDutyCycle(digitalSourceHandle: int, triggerType: AnalogTriggerType) -> typing.Tuple[int, int]:
    """
    Initialize a DutyCycle input.

    :param digitalSourceHandle: the digital source to use (either a
                                HAL_DigitalHandle or a HAL_AnalogTriggerHandle)
    :param triggerType:         the analog trigger type of the source if it is
                                an analog trigger

    :returns: thre created duty cycle handle
    """
def initializeEncoder(digitalSourceHandleA: int, analogTriggerTypeA: AnalogTriggerType, digitalSourceHandleB: int, analogTriggerTypeB: AnalogTriggerType, reverseDirection: int, encodingType: EncoderEncodingType) -> typing.Tuple[int, int]:
    """
    Initializes an encoder.

    :param digitalSourceHandleA: the A source (either a HAL_DigitalHandle or a
                                 HAL_AnalogTriggerHandle)
    :param analogTriggerTypeA:   the analog trigger type of the A source if it is
                                 an analog trigger
    :param digitalSourceHandleB: the B source (either a HAL_DigitalHandle or a
                                 HAL_AnalogTriggerHandle)
    :param analogTriggerTypeB:   the analog trigger type of the B source if it is
                                 an analog trigger
    :param reverseDirection:     true to reverse the counting direction from
                                 standard, otherwise false
    :param encodingType:         the encoding type

    :returns: the created encoder handle
    """
def initializeI2C(port: I2CPort) -> int:
    """
    Initializes the I2C port.

    Opens the port if necessary and saves the handle.
    If opening the MXP port, also sets up the channel functions appropriately.

    :param port: The port to open, 0 for the on-board, 1 for the MXP.
    """
def initializeInterrupts(watcher: int) -> typing.Tuple[int, int]:
    """
    Initializes an interrupt.

    :param watcher: true for synchronous interrupts, false for asynchronous

    :returns: the created interrupt handle
    """
def initializeNotifier() -> typing.Tuple[int, int]:
    """
    Initializes a notifier.

    A notifier is an FPGA controller timer that triggers at requested intervals
    based on the FPGA time. This can be used to make precise control loops.

    :returns: the created notifier
    """
def initializePDP(module: int) -> typing.Tuple[int, int]:
    """
    Initializes a Power Distribution Panel.

    :param module: the module number to initialize

    :returns: the created PDP
    """
def initializePWMPort(portHandle: int) -> typing.Tuple[int, int]:
    """
    Initializes a PWM port.

    :param portHandle: the port to initialize

    :returns: the created pwm handle
    """
def initializeRelayPort(portHandle: int, fwd: int) -> typing.Tuple[int, int]:
    """
    Initializes a relay.

    Note this call will only initialize either the forward or reverse port of the
    relay. If you need both, you will need to initialize 2 relays.

    :param portHandle: the port handle to initialize
    :param fwd:        true for the forward port, false for the reverse port

    :returns: the created relay handle
    """
def initializeSPI(port: SPIPort) -> int:
    """
    Initializes the SPI port. Opens the port if necessary and saves the handle.

    If opening the MXP port, also sets up the channel functions appropriately.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS3, 4 for MXP
    """
def initializeSerialPort(port: SerialPort) -> typing.Tuple[int, int]:
    """
    Initializes a serial port.

    The channels are either the onboard RS232, the mxp uart, or 2 USB ports. The
    top port is USB1, the bottom port is USB2.

    :param port: the serial port to initialize
    """
def initializeSerialPortDirect(port: SerialPort, portName: str) -> typing.Tuple[int, int]:
    """
    Initializes a serial port with a direct name.

    This name is the /dev name for a specific port.
    Note these are not always consistent between roboRIO reboots.

    :param port:     the serial port to initialize
    :param portName: the dev port name
    """
def initializeSolenoidPort(portHandle: int) -> typing.Tuple[int, int]:
    """
    Initializes a solenoid port.

    :param portHandle: the port handle of the module and channel to initialize

    :returns: the created solenoid handle
    """
def isAccumulatorChannel(analogPortHandle: int) -> typing.Tuple[int, int]:
    """
    Is the channel attached to an accumulator.

    :param analogPortHandle: Handle to the analog port.

    :returns: The analog channel is attached to an accumulator.
    """
def isAnyPulsing() -> typing.Tuple[int, int]:
    """
    Checks if any DIO line is currently generating a pulse.

    :returns: true if a pulse on some line is in progress
    """
def isHandleCorrectVersion(handle: int, version: int) -> bool:
    """
    Get if the version of the handle is correct.

    Do not use on the roboRIO, used specifically for the sim to handle resets.

    :param handle:  the handle
    :param version: the handle version to check

    :returns: true if the handle is the right version, otherwise false
    """
def isHandleType(handle: int, handleType: HandleEnum) -> bool:
    """
    Get if the handle is a specific type.

    :param handle:     the handle
    :param handleType: the type to check

    :returns: true if the type is correct, otherwise false
    """
def isNewControlData() -> int:
    """
    Has a new control packet from the driver station arrived since the last
    time this function was called?

    :returns: true if the control data has been updated since the last call
    """
def isPulsing(dioPortHandle: int) -> typing.Tuple[int, int]:
    """
    Checks a DIO line to see if it is currently generating a pulse.

    :returns: true if a pulse is in progress, otherwise false
    """
def latchPWMZero(pwmPortHandle: int) -> int:
    """
    Forces a PWM signal to go to 0 temporarily.

    :param pwmPortHandle: the PWM handle.
    """
def loadExtensions() -> int:
    """
    Loads any extra halsim libraries provided in the HALSIM_EXTENSIONS
    environment variable.

    :returns: the succes state of the initialization
    """
def loadOneExtension(library: str) -> int:
    """
    Loads a single extension from a direct path.

    Expected to be called internally, not by users.

    :param library: the library path

    :returns: the succes state of the initialization
    """
def observeUserProgramAutonomous() -> None:
    """
    Sets the autonomous enabled flag in the DS.

    This is used for the DS to ensure the robot is properly responding to its
    state request. Ensure this get called about every 50ms, or the robot will be
    disabled by the DS.
    """
def observeUserProgramDisabled() -> None:
    """
    Sets the disabled flag in the DS.

    This is used for the DS to ensure the robot is properly responding to its
    state request. Ensure this get called about every 50ms, or the robot will be
    disabled by the DS.
    """
def observeUserProgramStarting() -> None:
    """
    Sets the program starting flag in the DS.

    This is what changes the DS to showing robot code ready.
    """
def observeUserProgramTeleop() -> None:
    """
    Sets the teleoperated enabled flag in the DS.

    This is used for the DS to ensure the robot is properly responding to its
    state request. Ensure this get called about every 50ms, or the robot will be
    disabled by the DS.
    """
def observeUserProgramTest() -> None:
    """
    Sets the test mode flag in the DS.

    This is used for the DS to ensure the robot is properly responding to its
    state request. Ensure this get called about every 50ms, or the robot will be
    disabled by the DS.
    """
def pulse(dioPortHandle: int, pulseLength: float) -> int:
    """
    Generates a single digital pulse.

    Write a pulse to the specified digital output channel. There can only be a
    single pulse going at any time.

    :param dioPortHandle: the digital port handle
    :param pulseLength:   the active length of the pulse (in seconds)
    """
def readCANPacketLatest(handle: int, apiId: int, data: buffer) -> typing.Tuple[int, int, int]:
    """
    Reads a CAN packet. The will continuously return the last packet received,
    without accounting for packet age.

    :param handle:            the CAN handle
    :param apiId:             the ID to read (0-1023)
    :param data:              the packet data (8 bytes)
    :param length:            the received length (0-8 bytes)
    :param receivedTimestamp: the packet received timestamp (based off of
                              CLOCK_MONOTONIC)
    """
def readCANPacketNew(handle: int, apiId: int, data: buffer) -> typing.Tuple[int, int, int]:
    """
    Reads a new CAN packet.

    This will only return properly once per packet received. Multiple calls
    without receiving another packet will return an error code.

    :param handle:            the CAN handle
    :param apiId:             the ID to read (0-1023)
    :param data:              the packet data (8 bytes)
    :param length:            the received length (0-8 bytes)
    :param receivedTimestamp: the packet received timestamp (based off of
                              CLOCK_MONOTONIC)
    """
def readCANPacketTimeout(handle: int, apiId: int, data: buffer, timeoutMs: int) -> typing.Tuple[int, int, int]:
    """
    Reads a CAN packet. The will return the last packet received until the
    packet is older then the requested timeout. Then it will return an error
    code.

    :param handle:            the CAN handle
    :param apiId:             the ID to read (0-1023)
    :param data:              the packet data (8 bytes)
    :param length:            the received length (0-8 bytes)
    :param receivedTimestamp: the packet received timestamp (based off of
                              CLOCK_MONOTONIC)
    :param timeoutMs:         the timeout time for the packet
    """
def readI2C(port: I2CPort, deviceAddress: int, buffer: buffer) -> int:
    """
    Executes a read transaction with the device.

    Reads bytes from a device.
    Most I2C devices will auto-increment the register pointer internally allowing
    you to read consecutive registers on a device in a single transaction.

    :param port:            The I2C port, 0 for the on-board, 1 for the MXP.
    :param registerAddress: The register to read first in the transaction.
    :param count:           The number of bytes to read in the transaction.
    :param buffer:          A pointer to the array of bytes to store the data read from the
                            device.

    :returns: 0 on success or -1 on transfer abort.
    """
def readInterruptFallingTimestamp(interruptHandle: int) -> typing.Tuple[int, int]:
    """
    Returns the timestamp for the falling interrupt that occurred most recently.

    This is in the same time domain as HAL_GetFPGATime().  It only contains the
    bottom 32 bits of the timestamp.  If your robot has been running for over 1
    hour, you will need to fill in the upper 32 bits yourself.

    :param interruptHandle: the interrupt handle

    :returns: timestamp in microseconds since FPGA Initialization
    """
def readInterruptRisingTimestamp(interruptHandle: int) -> typing.Tuple[int, int]:
    """
    Returns the timestamp for the rising interrupt that occurred most recently.

    This is in the same time domain as HAL_GetFPGATime().  It only contains the
    bottom 32 bits of the timestamp.  If your robot has been running for over 1
    hour, you will need to fill in the upper 32 bits yourself.

    :param interruptHandle: the interrupt handle

    :returns: timestamp in microseconds since FPGA Initialization
    """
def readSPI(port: SPIPort, buffer: buffer) -> int:
    """
    Executes a read from the device.

    This method does not write any data out to the device.

    Most spi devices will require a register address to be written before they
    begin returning data.

    :param port:   The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                   MXP
    :param buffer: A pointer to the array of bytes to store the data read from the
                   device.
    :param count:  The number of bytes to read in the transaction. [1..7]

    :returns: Number of bytes read. -1 for error.
    """
def readSPIAutoReceivedData(port: SPIPort, buffer: buffer, timeout: float) -> typing.Tuple[int, int]:
    """
    Reads data received by the SPI accumulator.  Each received data sequence
    consists of a timestamp followed by the received data bytes, one byte per
    word (in the least significant byte).  The length of each received data
    sequence is the same as the combined dataSize + zeroSize set in
    HAL_SetSPIAutoTransmitData.

    :param port:      The number of the port to use. 0-3 for Onboard CS0-CS2, 4
                      for MXP.
    :param buffer:    The buffer to store the data into.
    :param numToRead: The number of words to read.
    :param timeout:   The read timeout (in seconds).

    :returns: The number of words actually read.
    """
def readSerial(handle: int, buffer: buffer) -> typing.Tuple[int, int]:
    """
    Reads data from the serial port.

    Will wait for either timeout (if set), the termination char (if set), or the
    count to be full. Whichever one comes first.

    :param handle: the serial port handle
    :param count:  the number of bytes maximum to read

    :returns: the number of bytes actually read
    """
def releaseDSMutex() -> None:
    """
    Releases the DS Mutex to allow proper shutdown of any threads that are
    waiting on it.
    """
def releaseWaitingInterrupt(interruptHandle: int) -> int:
    """
    Releases a waiting interrupt.

    This will release both rising and falling waiters.

    :param interruptHandle: the interrupt handle to release
    """
def report(resource: int, instanceNumber: int, context: int = 0, feature: str = None) -> int:
    """
    Reports a hardware usage to the HAL.

    :param resource:       the used resource
    :param instanceNumber: the instance of the resource
    :param context:        a user specified context index
    :param feature:        a user specified feature string

    :returns: the index of the added value in NetComm
    """
def requestInterrupts(interruptHandle: int, digitalSourceHandle: int, analogTriggerType: AnalogTriggerType) -> int:
    """
    Requests interrupts on a specific digital source.

    :param interruptHandle:     the interrupt handle
    :param digitalSourceHandle: the digital source handle (either a
                                HAL_AnalogTriggerHandle of a HAL_DigitalHandle)
    :param analogTriggerType:   the trigger type if the source is an AnalogTrigger
    """
def resetAccumulator(analogPortHandle: int) -> int:
    """
    Resets the accumulator to the initial value.

    :param analogPortHandle: Handle to the analog port.
    """
def resetAnalogGyro(handle: int) -> int:
    """
    Resets the analog gyro value to 0.

    :param handle: the gyro handle
    """
def resetCounter(counterHandle: int) -> int:
    """
    Resets the Counter to zero.

    Sets the counter value to zero. This does not effect the running state of the
    counter, just sets the current value to zero.

    :param counterHandle: the counter handle
    """
def resetEncoder(encoderHandle: int) -> int:
    """
    Reads the current encoder value.

    Read the value at this instant. It may still be running, so it reflects the
    current value. Next time it is read, it might have a different value.

    :param encoderHandle: the encoder handle

    :returns: the current encoder value
    """
def resetPDPTotalEnergy(handle: int) -> int:
    """
    Resets the PDP accumulated energy.

    :param handle: the module handle
    """
def resetSimValue(handle: int) -> None:
    """
    Resets a simulated double or integral value to 0.
    Has no effect on other value types.
    Use this instead of Set(0) for resetting incremental sensor values like
    encoder counts or gyro accumulated angle to ensure correct behavior in a
    distributed system (e.g. WebSockets).

    :param handle: simulated value handle
    """
def runMain() -> None:
    """
    Runs the main function provided to HAL_SetMain().

    If HAL_SetMain() has not been called, simply sleeps until HAL_ExitMain()
    is called.
    """
def sendConsoleLine(line: str) -> int:
    """
    Sends a line to the driver station console.

    :param line: the line to send (null terminated)
    """
def sendError(isError: int, errorCode: int, isLVCode: int, details: str, location: str, callStack: str, printMsg: int) -> int:
    """
    Sends an error to the driver station.

    :param isError:   true for error, false for warning
    :param errorCode: the error code
    :param isLVCode:  true for a LV error code, false for a standard error code
    :param details:   the details of the error
    :param location:  the file location of the errror
    :param callstack: the callstack of the error
    :param printMsg:  true to print the error message to stdout as well as to the
                      DS
    """
def setAccelerometerActive(active: int) -> None:
    """
    Sets the accelerometer to active or standby mode.

    It must be in standby mode to change any configuration.

    :param active: true to set to active, false for standby
    """
def setAccelerometerRange(range: AccelerometerRange) -> None:
    """
    Sets the range of values that can be measured (either 2, 4, or 8 g-forces).

    The accelerometer should be in standby mode when this is called.

    :param range: the accelerometer range
    """
def setAccumulatorCenter(analogPortHandle: int, center: int) -> int:
    """
    Set the center value of the accumulator.

    The center value is subtracted from each A/D value before it is added to the
    accumulator. This is used for the center value of devices like gyros and
    accelerometers to make integration work and to take the device offset into
    account when integrating.

    This center value is based on the output of the oversampled and averaged
    source from channel 1. Because of this, any non-zero oversample bits will
    affect the size of the value for this field.

    :param analogPortHandle: Handle to the analog port.
    :param center:           The center value of the accumulator.
    """
def setAccumulatorDeadband(analogPortHandle: int, deadband: int) -> int:
    """
    Set the accumulator's deadband.

    :param analogPortHandle: Handle to the analog port.
    :param deadband:         The deadband of the accumulator.
    """
def setAddressableLEDBitTiming(handle: int, lowTime0NanoSeconds: int, highTime0NanoSeconds: int, lowTime1NanoSeconds: int, highTime1NanoSeconds: int) -> int:
    pass
def setAddressableLEDLength(handle: int, length: int) -> int:
    pass
def setAddressableLEDOutputPort(handle: int, outputPort: int) -> int:
    pass
def setAddressableLEDSyncTime(handle: int, syncTimeMicroSeconds: int) -> int:
    pass
def setAllSolenoids(module: int, state: int) -> int:
    """
    Sets all channels on a specific module.

    :param module: the module to set the channels on
    :param state:  bitmask of the channels to set, 1 for on 0 for off
    """
def setAnalogAverageBits(analogPortHandle: int, bits: int) -> int:
    """
    Sets the number of averaging bits.

    This sets the number of averaging bits. The actual number of averaged samples
    is 2**bits. Use averaging to improve the stability of your measurement at the
    expense of sampling rate. The averaging is done automatically in the FPGA.

    :param analogPortHandle: Handle to the analog port to configure.
    :param bits:             Number of bits to average.
    """
def setAnalogGyroDeadband(handle: int, volts: float) -> int:
    """
    Sets the deadband of the analog gyro.

    :param handle: the gyro handle
    :param volts:  the voltage deadband
    """
def setAnalogGyroParameters(handle: int, voltsPerDegreePerSecond: float, offset: float, center: int) -> int:
    """
    Sets the analog gyro parameters to the specified values.

    This is meant to be used if you want to reuse the values from a previous
    calibration.

    :param handle:                  the gyro handle
    :param voltsPerDegreePerSecond: the gyro volts scaling
    :param offset:                  the gyro offset
    :param center:                  the gyro center
    """
def setAnalogGyroVoltsPerDegreePerSecond(handle: int, voltsPerDegreePerSecond: float) -> int:
    """
    Sets the analog gyro volts per degrees per second scaling.

    :param handle:                  the gyro handle
    :param voltsPerDegreePerSecond: the gyro volts scaling
    """
def setAnalogInputSimDevice(handle: int, device: int) -> None:
    """
    Indicates the analog input is used by a simulated device.

    :param handle: the analog input handle
    :param device: simulated device handle
    """
def setAnalogOutput(analogOutputHandle: int, voltage: float) -> int:
    """
    Sets an analog output value.

    :param analogOutputHandle: the analog output handle
    :param voltage:            the voltage (0-5v) to output
    """
def setAnalogOversampleBits(analogPortHandle: int, bits: int) -> int:
    """
    Sets the number of oversample bits.

    This sets the number of oversample bits. The actual number of oversampled
    values is 2**bits. Use oversampling to improve the resolution of your
    measurements at the expense of sampling rate. The oversampling is done
    automatically in the FPGA.

    :param analogPortHandle: Handle to the analog port to use.
    :param bits:             Number of bits to oversample.
    """
def setAnalogSampleRate(samplesPerSecond: float) -> int:
    """
    Sets the sample rate.

    This is a global setting for the Athena and effects all channels.

    :param samplesPerSecond: The number of samples per channel per second.
    """
def setAnalogTriggerAveraged(analogTriggerHandle: int, useAveragedValue: int) -> int:
    """
    Configures the analog trigger to use the averaged vs. raw values.

    If the value is true, then the averaged value is selected for the analog
    trigger, otherwise the immediate value is used.

    This is not allowed to be used if filtered mode is set.
    This is not allowed to be used with Duty Cycle based inputs.

    :param analogTriggerHandle: the trigger handle
    :param useAveragedValue:    true to use averaged values, false for raw
    """
def setAnalogTriggerFiltered(analogTriggerHandle: int, useFilteredValue: int) -> int:
    """
    Configures the analog trigger to use a filtered value.

    The analog trigger will operate with a 3 point average rejection filter. This
    is designed to help with 360 degree pot applications for the period where the
    pot crosses through zero.

    This is not allowed to be used if averaged mode is set.

    :param analogTriggerHandle: the trigger handle
    :param useFilteredValue:    true to use filtered values, false for average or
                                raw
    """
def setAnalogTriggerLimitsDutyCycle(analogTriggerHandle: int, lower: float, upper: float) -> int:
    pass
def setAnalogTriggerLimitsRaw(analogTriggerHandle: int, lower: int, upper: int) -> int:
    """
    Sets the raw ADC upper and lower limits of the analog trigger.

    HAL_SetAnalogTriggerLimitsVoltage or HAL_SetAnalogTriggerLimitsDutyCycle
    is likely better in most cases.

    :param analogTriggerHandle: the trigger handle
    :param lower:               the lower ADC value
    :param upper:               the upper ADC value
    """
def setAnalogTriggerLimitsVoltage(analogTriggerHandle: int, lower: float, upper: float) -> int:
    """
    Sets the upper and lower limits of the analog trigger.

    The limits are given as floating point voltage values.

    :param analogTriggerHandle: the trigger handle
    :param lower:               the lower voltage value
    :param upper:               the upper voltage value
    """
def setCompressorClosedLoopControl(compressorHandle: int, value: int) -> int:
    """
    Sets the compressor to closed loop mode.

    :param compressorHandle: the compressor handle
    :param value:            true for closed loop mode, false for off
    """
def setCounterAverageSize(counterHandle: int, size: int) -> int:
    """
    Sets the average sample size of a counter.

    :param counterHandle: the counter handle
    :param size:          the size of samples to average
    """
def setCounterDownSource(counterHandle: int, digitalSourceHandle: int, analogTriggerType: AnalogTriggerType) -> int:
    """
    Sets the source object that causes the counter to count down.

    :param counterHandle:       the counter handle
    :param digitalSourceHandle: the digital source handle (either a
                                HAL_AnalogTriggerHandle of a HAL_DigitalHandle)
    :param analogTriggerType:   the analog trigger type if the source is an analog
                                trigger
    """
def setCounterDownSourceEdge(counterHandle: int, risingEdge: int, fallingEdge: int) -> int:
    """
    Sets the down source to either detect rising edges or falling edges.
    Note that both are allowed to be set true at the same time without issues.

    :param counterHandle: the counter handle
    :param risingEdge:    true to trigger on rising
    :param fallingEdge:   true to trigger on falling
    """
def setCounterExternalDirectionMode(counterHandle: int) -> int:
    """
    Sets directional counting mode on this counter.

    The direction is determined by the B input, with counting happening with the
    A input.

    :param counterHandle: the counter handle
    """
def setCounterMaxPeriod(counterHandle: int, maxPeriod: float) -> int:
    """
    Sets the maximum period where the device is still considered "moving".

    Sets the maximum period where the device is considered moving. This value is
    used to determine the "stopped" state of the counter using the
    HAL_GetCounterStopped method.

    :param counterHandle: the counter handle
    :param maxPeriod:     the maximum period where the counted device is
                          considered moving in seconds
    """
def setCounterPulseLengthMode(counterHandle: int, threshold: float) -> int:
    """
    Configures the counter to count in up or down based on the length of the
    input pulse.

    This mode is most useful for direction sensitive gear tooth sensors.

    :param counterHandle: the counter handle
    :param threshold:     The pulse length beyond which the counter counts the
                          opposite direction (seconds)
    """
def setCounterReverseDirection(counterHandle: int, reverseDirection: int) -> int:
    """
    Sets the Counter to return reversed sensing on the direction.

    This allows counters to change the direction they are counting in the case of
    1X and 2X quadrature encoding only. Any other counter mode isn't supported.

    :param counterHandle:    the counter handle
    :param reverseDirection: true if the value counted should be negated.
    """
def setCounterSamplesToAverage(counterHandle: int, samplesToAverage: int) -> int:
    """
    Sets the Samples to Average which specifies the number of samples of the
    timer to average when calculating the period. Perform averaging to account
    for mechanical imperfections or as oversampling to increase resolution.

    :param counterHandle:    the counter handle
    :param samplesToAverage: The number of samples to average from 1 to 127
    """
def setCounterSemiPeriodMode(counterHandle: int, highSemiPeriod: int) -> int:
    """
    Sets Semi-period mode on this counter.

    The counter counts up based on the time the input is triggered. High or Low
    depends on the highSemiPeriod parameter.

    :param counterHandle:  the counter handle
    :param highSemiPeriod: true for counting when the input is high, false for low
    """
def setCounterUpDownMode(counterHandle: int) -> int:
    """
    Sets standard up / down counting mode on this counter.

    Up and down counts are sourced independently from two inputs.

    :param counterHandle: the counter handle
    """
def setCounterUpSource(counterHandle: int, digitalSourceHandle: int, analogTriggerType: AnalogTriggerType) -> int:
    """
    Sets the source object that causes the counter to count up.

    :param counterHandle:       the counter handle
    :param digitalSourceHandle: the digital source handle (either a
                                HAL_AnalogTriggerHandle of a HAL_DigitalHandle)
    :param analogTriggerType:   the analog trigger type if the source is an analog
                                trigger
    """
def setCounterUpSourceEdge(counterHandle: int, risingEdge: int, fallingEdge: int) -> int:
    """
    Sets the up source to either detect rising edges or falling edges.

    Note that both are allowed to be set true at the same time without issues.

    :param counterHandle: the counter handle
    :param risingEdge:    true to trigger on rising
    :param fallingEdge:   true to trigger on falling
    """
def setCounterUpdateWhenEmpty(counterHandle: int, enabled: int) -> int:
    """
    Selects whether you want to continue updating the event timer output when
    there are no samples captured.

    The output of the event timer has a buffer of periods that are averaged and
    posted to a register on the FPGA.  When the timer detects that the event
    source has stopped (based on the MaxPeriod) the buffer of samples to be
    averaged is emptied.

    If you enable the update when empty, you will be
    notified of the stopped source and the event time will report 0 samples.

    If you disable update when empty, the most recent average will remain on the
    output until a new sample is acquired.

    You will never see 0 samples output (except when there have been no events
    since an FPGA reset) and you will likely not see the stopped bit become true
    (since it is updated at the end of an average and there are no samples to
    average).

    :param counterHandle: the counter handle
    :param enabled:       true to enable counter updating with no samples
    """
def setCurrentThreadPriority(realTime: int, priority: int) -> typing.Tuple[int, int]:
    """
    Sets the thread priority for the current thread.

    :param thread:   Reference to the thread to set the priority of.
    :param realTime: Set to true to set a real-time priority, false for standard
                     priority.
    :param priority: Priority to set the thread to. For real-time, this is 1-99
                     with 99 being highest. For non-real-time, this is forced to
                     0. See "man 7 sched" for more details.
    :param status:   Error status variable. 0 on success.

    :returns: True on success.
    """
def setDIO(dioPortHandle: int, value: int) -> int:
    """
    Writes a digital value to a DIO channel.

    :param dioPortHandle: the digital port handle
    :param value:         the state to set the digital channel (if it is
                          configured as an output)
    """
def setDIODirection(dioPortHandle: int, input: int) -> int:
    """
    Sets the direction of a DIO channel.

    :param dioPortHandle: the digital port handle
    :param input:         true to set input, false for output
    """
def setDIOSimDevice(handle: int, device: int) -> None:
    """
    Indicates the DIO channel is used by a simulated device.

    :param handle: the DIO channel handle
    :param device: simulated device handle
    """
def setDigitalPWMDutyCycle(pwmGenerator: int, dutyCycle: float) -> int:
    """
    Configures the duty-cycle of the PWM generator.

    :param pwmGenerator: the digital PWM handle
    :param dutyCycle:    the percent duty cycle to output [0..1]
    """
def setDigitalPWMOutputChannel(pwmGenerator: int, channel: int) -> int:
    """
    Configures which DO channel the PWM signal is output on.

    :param pwmGenerator: the digital PWM handle
    :param channel:      the channel to output on
    """
def setDigitalPWMRate(rate: float) -> int:
    """
    Changes the frequency of the DO PWM generator.

    The valid range is from 0.6 Hz to 19 kHz.

    The frequency resolution is logarithmic.

    :param rate: the frequency to output all digital output PWM signals
    """
def setDutyCycleSimDevice(handle: int, device: int) -> None:
    """
    Indicates the duty cycle is used by a simulated device.

    :param handle: the duty cycle handle
    :param device: simulated device handle
    """
def setEncoderDistancePerPulse(encoderHandle: int, distancePerPulse: float) -> int:
    """
    Sets the distance traveled per encoder pulse. This is used as a scaling
    factor for the rate and distance calls.

    :param encoderHandle:    the encoder handle
    :param distancePerPulse: the distance traveled per encoder pulse (units user
                             defined)
    """
def setEncoderIndexSource(encoderHandle: int, digitalSourceHandle: int, analogTriggerType: AnalogTriggerType, type: EncoderIndexingType) -> int:
    """
    Sets the source for an index pulse on the encoder.

    The index pulse can be used to cause an encoder to reset based on an external
    input.

    :param encoderHandle:       the encoder handle
    :param digitalSourceHandle: the index source handle (either a
                                HAL_AnalogTriggerHandle of a HAL_DigitalHandle)
    :param analogTriggerType:   the analog trigger type if the source is an analog
                                trigger
    :param type:                the index triggering type
    """
def setEncoderMaxPeriod(encoderHandle: int, maxPeriod: float) -> int:
    """
    Sets the maximum period where the device is still considered "moving".

    Sets the maximum period where the device is considered moving. This value is
    used to determine the "stopped" state of the encoder using the
    HAL_GetEncoderStopped method.

    :param encoderHandle: the encoder handle
    :param maxPeriod:     the maximum period where the counted device is
                          considered moving in seconds
    """
def setEncoderMinRate(encoderHandle: int, minRate: float) -> int:
    """
    Sets the minimum rate to be considered moving by the encoder.

    Units need to match what is set by HAL_SetEncoderDistancePerPulse, with time
    as seconds.

    :param encoderHandle: the encoder handle
    :param minRate:       the minimum rate to be considered moving (units are
                          determined by the units passed to HAL_SetEncoderDistancePerPulse, time value
                          is seconds)
    """
def setEncoderReverseDirection(encoderHandle: int, reverseDirection: int) -> int:
    """
    Sets if to reverse the direction of the encoder.

    Note that this is not a toggle. It is an absolute set.

    :param encoderHandle:    the encoder handle
    :param reverseDirection: true to reverse the direction, false to not.
    """
def setEncoderSamplesToAverage(encoderHandle: int, samplesToAverage: int) -> int:
    """
    Sets the number of encoder samples to average when calculating encoder rate.

    :param encoderHandle:    the encoder handle
    :param samplesToAverage: the number of samples to average
    """
def setEncoderSimDevice(handle: int, device: int) -> None:
    """
    Indicates the encoder is used by a simulated device.

    :param handle: the encoder handle
    :param device: simulated device handle
    """
def setFilterPeriod(filterIndex: int, value: int) -> int:
    """
    Sets the filter period for the specified filter index.

    Sets the filter period in FPGA cycles.  Even though there are 2 different
    filter index domains (MXP vs HDR), ignore that distinction for now since it
    compilicates the interface.  That can be changed later.

    :param filterIndex: the filter index, 0 - 2
    :param value:       the number of cycles that the signal must not transition
                        to be counted as a transition.
    """
def setFilterSelect(dioPortHandle: int, filterIndex: int) -> int:
    """
    Writes the filter index from the FPGA.

    Set the filter index used to filter out short pulses.

    :param dioPortHandle: the digital port handle
    :param filterIndex:   the filter index (Must be in the range 0 - 3, where 0
                          means "none" and 1 - 3 means filter # filterIndex - 1)
    """
def setInterruptUpSourceEdge(interruptHandle: int, risingEdge: int, fallingEdge: int) -> int:
    """
    Sets the edges to trigger the interrupt on.

    Note that both edges triggered is a valid configuration.

    :param interruptHandle: the interrupt handle
    :param risingEdge:      true for triggering on rising edge
    :param fallingEdge:     true for triggering on falling edge
    """
def setJoystickOutputs(joystickNum: int, outputs: int, leftRumble: int, rightRumble: int) -> int:
    """
    Set joystick outputs.

    :param joystickNum: the joystick numer
    :param outputs:     bitmask of outputs, 1 for on 0 for off
    :param leftRumble:  the left rumble value (0-FFFF)
    :param rightRumble: the right rumble value (0-FFFF)

    :returns: the error code, or 0 for success
    """
def setNotifierName(notifierHandle: int, name: str) -> int:
    """
    Sets the name of a notifier.

    :param notifierHandle: the notifier handle
    :param name:           name
    """
def setNotifierThreadPriority(realTime: int, priority: int) -> typing.Tuple[int, int]:
    """
    Sets the HAL notifier thread priority.

    The HAL notifier thread is responsible for managing the FPGA's notifier
    interrupt and waking up user's Notifiers when it's their time to run.
    Giving the HAL notifier thread real-time priority helps ensure the user's
    real-time Notifiers, if any, are notified to run in a timely manner.

    :param realTime: Set to true to set a real-time priority, false for standard
                     priority.
    :param priority: Priority to set the thread to. For real-time, this is 1-99
                     with 99 being highest. For non-real-time, this is forced to
                     0. See "man 7 sched" for more details.
    :param status:   Error status variable. 0 on success.

    :returns: True on success.
    """
def setOneShotDuration(solenoidPortHandle: int, durMS: int) -> int:
    """
    Sets the one shot duration on a solenoid channel.

    :param solenoidPortHandle: the solenoid handle
    :param durMS:              the one shot duration in ms
    """
def setPWMConfig(pwmPortHandle: int, maxPwm: float, deadbandMaxPwm: float, centerPwm: float, deadbandMinPwm: float, minPwm: float) -> int:
    """
    Sets the configuration settings for the PWM channel.

    All values are in milliseconds.

    :param pwmPortHandle:  the PWM handle
    :param maxPwm:         the maximum PWM value
    :param deadbandMaxPwm: the high range of the center deadband
    :param centerPwm:      the center PWM value
    :param deadbandMinPwm: the low range of the center deadband
    :param minPwm:         the minimum PWM value
    """
def setPWMConfigRaw(pwmPortHandle: int, maxPwm: int, deadbandMaxPwm: int, centerPwm: int, deadbandMinPwm: int, minPwm: int) -> int:
    """
    Sets the raw configuration settings for the PWM channel.

    We recommend using HAL_SetPWMConfig() instead, as those values are properly
    scaled. Usually used for values grabbed by HAL_GetPWMConfigRaw().

    Values are in raw FPGA units.

    :param pwmPortHandle:  the PWM handle
    :param maxPwm:         the maximum PWM value
    :param deadbandMaxPwm: the high range of the center deadband
    :param centerPwm:      the center PWM value
    :param deadbandMinPwm: the low range of the center deadband
    :param minPwm:         the minimum PWM value
    """
def setPWMDisabled(pwmPortHandle: int) -> int:
    """
    Sets a PWM channel to be disabled.

    The channel is disabled until the next time it is set. Note this is different
    from just setting a 0 speed, as this will actively stop all signaling on the
    channel.

    :param pwmPortHandle: the PWM handle.
    """
def setPWMEliminateDeadband(pwmPortHandle: int, eliminateDeadband: int) -> int:
    """
    Sets if the FPGA should output the center value if the input value is within
    the deadband.

    :param pwmPortHandle:     the PWM handle
    :param eliminateDeadband: true to eliminate deadband, otherwise false
    """
def setPWMPeriodScale(pwmPortHandle: int, squelchMask: int) -> int:
    """
    Sets how how often the PWM signal is squelched, thus scaling the period.

    :param pwmPortHandle: the PWM handle.
    :param squelchMask:   the 2-bit mask of outputs to squelch
    """
def setPWMPosition(pwmPortHandle: int, position: float) -> int:
    """
    Sets a PWM channel to the desired position value.

    The values range from 0 to 1 and the period is controlled by the PWM Period
    and MinHigh registers.

    :param pwmPortHandle: the PWM handle
    :param value:         the positional PWM value to set
    """
def setPWMRaw(pwmPortHandle: int, value: int) -> int:
    """
    Sets a PWM channel to the desired value.

    The values are in raw FPGA units, and have the potential to change with any
    FPGA release.

    :param pwmPortHandle: the PWM handle
    :param value:         the PWM value to set
    """
def setPWMSpeed(pwmPortHandle: int, speed: float) -> int:
    """
    Sets a PWM channel to the desired scaled value.

    The values range from -1 to 1 and the period is controlled by the PWM Period
    and MinHigh registers.

    :param pwmPortHandle: the PWM handle
    :param value:         the scaled PWM value to set
    """
def setRelay(relayPortHandle: int, on: int) -> int:
    """
    Sets the state of a relay output.

    :param relayPortHandle: the relay handle
    :param on:              true for on, false for off
    """
def setSPIAutoTransmitData(port: SPIPort, dataToSend: buffer, zeroSize: int) -> int:
    """
    Sets the data to be transmitted to the device to initiate a read.

    :param port:       The number of the port to use. 0-3 for Onboard CS0-CS2, 4
                       for MXP.
    :param dataToSend: Pointer to the data to send (Gets copied for continue use,
                       so no need to keep alive).
    :param dataSize:   The length of the data to send.
    :param zeroSize:   The number of zeros to send after the data.
    """
def setSPIChipSelectActiveHigh(port: SPIPort) -> int:
    """
    Sets the CS Active high for a SPI port.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for MXP
    """
def setSPIChipSelectActiveLow(port: SPIPort) -> int:
    """
    Sets the CS Active low for a SPI port.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for MXP
    """
def setSPIHandle(port: SPIPort, handle: int) -> None:
    """
    Sets the stored handle for a SPI port.

    :param port:   The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                   MXP.
    :param handle: The value of the handle for the port.
    """
def setSPIOpts(port: SPIPort, msbFirst: int, sampleOnTrailing: int, clkIdleHigh: int) -> None:
    """
    Sets the SPI options.

    :param port:             The number of the port to use. 0-3 for Onboard
                             CS0-CS2, 4 for MXP
    :param msbFirst:         True to write the MSB first, False for LSB first
    :param sampleOnTrailing: True to sample on the trailing edge, False to sample
                             on the leading edge
    :param clkIdleHigh:      True to set the clock to active low, False to set the
                             clock active high
    """
def setSPISpeed(port: SPIPort, speed: int) -> None:
    """
    Sets the clock speed for the SPI bus.

    :param port:  The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                  MXP
    :param speed: The speed in Hz (0-1MHz)
    """
def setSerialBaudRate(handle: int, baud: int) -> int:
    """
    Sets the baud rate of a serial port.

    Any value between 0 and 0xFFFFFFFF may be used. Default is 9600.

    :param handle: the serial port handle
    :param baud:   the baud rate to set
    """
def setSerialDataBits(handle: int, bits: int) -> int:
    """
    Sets the number of data bits on a serial port.

    Defaults to 8.

    :param handle: the serial port handle
    :param bits:   the number of data bits (5-8)
    """
def setSerialFlowControl(handle: int, flow: int) -> int:
    """
    Sets the flow control mode of a serial port.

    Valid values are:
    0: None (default)
    1: XON-XOFF
    2: RTS-CTS
    3: DTR-DSR

    :param handle: the serial port handle
    :param flow:   the mode to set (see remarks for valid values)
    """
def setSerialParity(handle: int, parity: int) -> int:
    """
    Sets the number of parity bits on a serial port.

    Valid values are:
    0: None (default)
    1: Odd
    2: Even
    3: Mark - Means exists and always 1
    4: Space - Means exists and always 0

    :param handle: the serial port handle
    :param parity: the parity bit mode (see remarks for valid values)
    """
def setSerialReadBufferSize(handle: int, size: int) -> int:
    """
    Sets the size of the read buffer.

    :param handle: the serial port handle
    :param size:   the read buffer size
    """
def setSerialStopBits(handle: int, stopBits: int) -> int:
    """
    Sets the number of stop bits on a serial port.

    Valid values are:
    10: One stop bit (default)
    15: One and a half stop bits
    20: Two stop bits

    :param handle:   the serial port handle
    :param stopBits: the stop bit value (see remarks for valid values)
    """
def setSerialTimeout(handle: int, timeout: float) -> int:
    """
    Sets the minimum serial read timeout of a port.

    :param handle:  the serial port handle
    :param timeout: the timeout in milliseconds
    """
def setSerialWriteBufferSize(handle: int, size: int) -> int:
    """
    Sets the size of the write buffer.

    :param handle: the serial port handle
    :param size:   the write buffer size
    """
def setSerialWriteMode(handle: int, mode: int) -> int:
    """
    Sets the write mode on a serial port.

    Valid values are:
    1: Flush on access
    2: Flush when full (default)

    :param handle: the serial port handle
    :param mode:   the mode to set (see remarks for valid values)
    """
def setShowExtensionsNotFoundMessages(showMessage: int) -> None:
    """
    Enables or disables the message saying no HAL extensions were found.

    Some apps don't care, and the message create clutter. For general team code,
    we want it.

    This must be called before HAL_Initialize is called.

    This defaults to true.

    :param showMessage: true to show message, false to not.
    """
def setSimValue(handle: int, value: HAL_Value) -> None:
    pass
def setSimValueBoolean(handle: int, value: int) -> None:
    """
    Sets a simulated value (boolean).

    :param handle: simulated value handle
    :param value:  the value to set
    """
def setSimValueDouble(handle: int, value: float) -> None:
    """
    Sets a simulated value (double).

    :param handle: simulated value handle
    :param value:  the value to set
    """
def setSimValueEnum(handle: int, value: int) -> None:
    """
    Sets a simulated value (enum).

    :param handle: simulated value handle
    :param value:  the value to set
    """
def setSimValueInt(handle: int, value: int) -> None:
    """
    Sets a simulated value (int).

    :param handle: simulated value handle
    :param value:  the value to set
    """
def setSimValueLong(handle: int, value: int) -> None:
    """
    Sets a simulated value (long).

    :param handle: simulated value handle
    :param value:  the value to set
    """
def setSolenoid(solenoidPortHandle: int, value: int) -> int:
    """
    Sets a solenoid output value.

    :param solenoidPortHandle: the solenoid handle
    :param value:              true for on, false for off
    """
def setupAnalogGyro(handle: int) -> int:
    """
    Sets up an analog gyro with the proper offsets and settings for the KOP
    analog gyro.

    :param handle: the gyro handle
    """
def shutdown() -> None:
    """
    Call this to shut down HAL.

    This must be called at termination of the robot program to avoid potential
    segmentation faults with simulation extensions at exit.
    """
def simPeriodicAfter() -> None:
    """
    Calls registered SimPeriodic "after" callbacks (only in simulation mode).
    This should be called after user code periodic simulation functions.
    """
def simPeriodicBefore() -> None:
    """
    Calls registered SimPeriodic "before" callbacks (only in simulation mode).
    This should be called prior to user code periodic simulation functions.
    """
def startAddressableLEDOutput(handle: int) -> int:
    pass
def startSPIAutoRate(port: SPIPort, period: float) -> int:
    """
    Sets the period for automatic SPI accumulation.

    :param port:   The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                   MXP.
    :param period: The accumlation period (seconds).
    """
def startSPIAutoTrigger(port: SPIPort, digitalSourceHandle: int, analogTriggerType: AnalogTriggerType, triggerRising: int, triggerFalling: int) -> int:
    """
    Starts the auto SPI accumulator on a specific trigger.

    Note that triggering on both rising and falling edges is a valid
    configuration.

    :param port:                The number of the port to use. 0-3 for Onboard
                                CS0-CS2, 4 for MXP.
    :param digitalSourceHandle: The trigger source to use (Either
                                HAL_AnalogTriggerHandle or HAL_DigitalHandle).
    :param analogTriggerType:   The analog trigger type, if the source is an
                                analog trigger.
    :param triggerRising:       Trigger on the rising edge if true.
    :param triggerFalling:      Trigger on the falling edge if true.
    """
def stopAddressableLEDOutput(handle: int) -> int:
    pass
def stopCANPacketRepeating(handle: int, apiId: int) -> int:
    """
    Stops a repeating packet with a specific ID.

    This ID is 10 bits.

    :param handle: the CAN handle
    :param apiId:  the ID to stop repeating (0-1023)
    """
def stopNotifier(notifierHandle: int) -> int:
    """
    Stops a notifier from running.

    This will cause any call into HAL_WaitForNotifierAlarm to return.

    :param notifierHandle: the notifier handle
    """
def stopSPIAuto(port: SPIPort) -> int:
    """
    Stops an automatic SPI accumlation.

    :param port: The number of the port to use. 0-3 for Onboard CS0-CS2, 4 for
                 MXP.
    """
def transactionI2C(port: I2CPort, deviceAddress: int, dataToSend: buffer, dataReceived: buffer) -> int:
    """
    Generic I2C read/write transaction.

    This is a lower-level interface to the I2C hardware giving you more control
    over each transaction.

    :param port:         The I2C port, 0 for the on-board, 1 for the MXP.
    :param dataToSend:   Buffer of data to send as part of the transaction.
    :param sendSize:     Number of bytes to send as part of the transaction.
    :param dataReceived: Buffer to read data into.
    :param receiveSize:  Number of bytes to read from the device.

    :returns: 0 on success or -1 on transfer abort.
    """
def transactionSPI(port: SPIPort, dataToSend: buffer, dataReceived: buffer) -> int:
    """
    Performs an SPI send/receive transaction.

    This is a lower-level interface to the spi hardware giving you more control
    over each transaction.

    :param port:         The number of the port to use. 0-3 for Onboard CS0-CS2, 4
                         for MXP
    :param dataToSend:   Buffer of data to send as part of the transaction.
    :param dataReceived: Buffer to read data into.
    :param size:         Number of bytes to transfer. [0..7]

    :returns: Number of bytes transferred, -1 for error
    """
def updateNotifierAlarm(notifierHandle: int, triggerTime: int) -> int:
    """
    Updates the trigger time for a notifier.

    Note that this time is an absolute time relative to HAL_GetFPGATime()

    :param notifierHandle: the notifier handle
    :param triggerTime:    the updated trigger time
    """
def waitForDSData() -> None:
    """
    Waits for the newest DS packet to arrive. Note that this is a blocking call.
    Checks if new control data has arrived since the last HAL_WaitForDSData or
    HAL_IsNewControlData call. If new data has not arrived, waits for new data
    to arrive. Otherwise, returns immediately.
    """
def waitForDSDataTimeout(timeout: float) -> int:
    """
    Waits for the newest DS packet to arrive. If timeout is <= 0, this will wait
    forever. Otherwise, it will wait until either a new packet, or the timeout
    time has passed.

    :param timeout: timeout in seconds

    :returns: true for new data, false for timeout
    """
def waitForInterrupt(interruptHandle: int, timeout: float, ignorePrevious: int) -> typing.Tuple[int, int]:
    """
    In synchronous mode, waits for the defined interrupt to occur.

    :param interruptHandle: the interrupt handle
    :param timeout:         timeout in seconds
    :param ignorePrevious:  if true, ignore interrupts that happened before
                            waitForInterrupt was called

    :returns: the mask of interrupts that fired
    """
def waitForNotifierAlarm(notifierHandle: int) -> typing.Tuple[int, int]:
    pass
def writeAddressableLEDData(handle: int, data: AddressableLEDData, length: int) -> int:
    pass
def writeCANPacket(handle: int, data: buffer, apiId: int) -> int:
    """
    Writes a packet to the CAN device with a specific ID.

    This ID is 10 bits.

    :param handle: the CAN handle
    :param data:   the data to write (0-8 bytes)
    :param length: the length of data (0-8)
    :param apiId:  the ID to write (0-1023 bits)
    """
def writeCANPacketRepeating(handle: int, data: buffer, apiId: int, repeatMs: int) -> int:
    """
    Writes a repeating packet to the CAN device with a specific ID.

    This ID is 10 bits.

    The RoboRIO will automatically repeat the packet at the specified interval

    :param handle:   the CAN handle
    :param data:     the data to write (0-8 bytes)
    :param length:   the length of data (0-8)
    :param apiId:    the ID to write (0-1023)
    :param repeatMs: the period to repeat in ms
    """
def writeCANRTRFrame(handle: int, length: int, apiId: int) -> int:
    """
    Writes an RTR frame of the specified length to the CAN device with the
    specific ID.

    By spec, the length must be equal to the length sent by the other device,
    otherwise behavior is unspecified.

    :param handle: the CAN handle
    :param length: the length of data to request (0-8)
    :param apiId:  the ID to write (0-1023)
    """
def writeI2C(port: I2CPort, deviceAddress: int, dataToSend: buffer) -> int:
    """
    Executes a write transaction with the device.

    Writes a single byte to a register on a device and wait until the
    transaction is complete.

    :param port:            The I2C port, 0 for the on-board, 1 for the MXP.
    :param registerAddress: The address of the register on the device to be
                            written.
    :param data:            The byte to write to the register on the device.

    :returns: 0 on success or -1 on transfer abort.
    """
def writeSPI(port: SPIPort, dataToSend: buffer) -> int:
    """
    Executes a write transaction with the device.

    Writes to a device and wait until the transaction is complete.

    :param port:      The number of the port to use. 0-3 for Onboard CS0-CS2, 4
                      for MXP
    :param datToSend: The data to write to the register on the device.
    :param sendSize:  The number of bytes to be written

    :returns: The number of bytes written. -1 for an error
    """
def writeSerial(handle: int, buffer: buffer) -> typing.Tuple[int, int]:
    """
    Writes data to the serial port.

    :param handle: the serial port handle
    :param buffer: the buffer to write
    :param count:  the number of bytes to write from the buffer

    :returns: the number of bytes actually written
    """
__hal_simulation__ = True
__halplatform__ = 'sim'
_cleanup: PyCapsule # value = <capsule object NULL>
