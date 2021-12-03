import wpilib.drive._drive
import typing
import wpilib._wpilib
import wpilib.interfaces._interfaces

__all__ = [
    "DifferentialDrive",
    "KilloughDrive",
    "MecanumDrive",
    "RobotDriveBase",
    "Vector2d"
]


class RobotDriveBase(wpilib._wpilib.MotorSafety, wpilib._wpilib.ErrorBase):
    """
    Common base class for drive platforms.
    """
    class MotorType():
        """
        The location of a motor on the robot for the purpose of driving.

        Members:

          kFrontLeft

          kFrontRight

          kRearLeft

          kRearRight

          kLeft

          kRight

          kBack
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
        __members__: dict # value = {'kFrontLeft': <MotorType.kFrontLeft: 0>, 'kFrontRight': <MotorType.kFrontRight: 1>, 'kRearLeft': <MotorType.kRearLeft: 2>, 'kRearRight': <MotorType.kRearRight: 3>, 'kLeft': <MotorType.kFrontLeft: 0>, 'kRight': <MotorType.kFrontRight: 1>, 'kBack': <MotorType.kRearLeft: 2>}
        kBack: wpilib.drive._drive.RobotDriveBase.MotorType # value = <MotorType.kRearLeft: 2>
        kFrontLeft: wpilib.drive._drive.RobotDriveBase.MotorType # value = <MotorType.kFrontLeft: 0>
        kFrontRight: wpilib.drive._drive.RobotDriveBase.MotorType # value = <MotorType.kFrontRight: 1>
        kLeft: wpilib.drive._drive.RobotDriveBase.MotorType # value = <MotorType.kFrontLeft: 0>
        kRearLeft: wpilib.drive._drive.RobotDriveBase.MotorType # value = <MotorType.kRearLeft: 2>
        kRearRight: wpilib.drive._drive.RobotDriveBase.MotorType # value = <MotorType.kRearRight: 3>
        kRight: wpilib.drive._drive.RobotDriveBase.MotorType # value = <MotorType.kFrontRight: 1>
        pass
    def __init__(self) -> None: ...
    def _applyDeadband(self, number: float, deadband: float) -> float: 
        """
        Returns 0.0 if the given value is within the specified range around zero.
        The remaining range between the deadband and 1.0 is scaled from 0.0 to 1.0.

        :param value:    value to clip
        :param deadband: range around zero
        """
    def feedWatchdog(self) -> None: 
        """
        Feed the motor safety object. Resets the timer that will stop the motors if
        it completes.

        @see MotorSafetyHelper::Feed()
        """
    def getDescription(self) -> str: ...
    def setDeadband(self, deadband: float) -> None: 
        """
        Sets the deadband applied to the drive inputs (e.g., joystick values).

        The default value is 0.02. Inputs smaller than the deadband are set to 0.0
        while inputs larger than the deadband are scaled from 0.0 to 1.0. See
        ApplyDeadband().

        :param deadband: The deadband to set.
        """
    def setMaxOutput(self, maxOutput: float) -> None: 
        """
        Configure the scaling factor for using RobotDrive with motor controllers in
        a mode other than PercentVbus or to limit the maximum output.

        :param maxOutput: Multiplied with the output percentage computed by the
                          drive functions.
        """
    def stopMotor(self) -> None: ...
    @property
    def _m_deadband(self) -> float:
        """
        :type: float
        """
    @_m_deadband.setter
    def _m_deadband(self, arg0: float) -> None:
        pass
    @property
    def _m_maxOutput(self) -> float:
        """
        :type: float
        """
    @_m_maxOutput.setter
    def _m_maxOutput(self, arg0: float) -> None:
        pass
    pass
class KilloughDrive(RobotDriveBase, wpilib._wpilib.MotorSafety, wpilib._wpilib.ErrorBase, wpilib._wpilib.Sendable):
    """
    A class for driving Killough drive platforms.

    Killough drives are triangular with one omni wheel on each corner.

    Drive base diagram:
    ::

       /_____ * / \   /  *    \ /
         ---

    Each Drive() function provides different inverse kinematic relations for a
    Killough drive. The default wheel vectors are parallel to their respective
    opposite sides, but can be overridden. See the constructor for more
    information.

    This library uses the NED axes convention (North-East-Down as external
    reference in the world frame):
    http://www.nuclearprojects.com/ins/images/axis_big.png.

    The positive X axis points ahead, the positive Y axis points right, and the
    and the positive Z axis points down. Rotations follow the right-hand rule, so
    clockwise rotation around the Z axis is positive.
    """
    @typing.overload
    def __init__(self, leftMotor: wpilib.interfaces._interfaces.SpeedController, rightMotor: wpilib.interfaces._interfaces.SpeedController, backMotor: wpilib.interfaces._interfaces.SpeedController) -> None: 
        """
        Construct a Killough drive with the given motors and default motor angles.

        The default motor angles make the wheels on each corner parallel to their
        respective opposite sides.

        If a motor needs to be inverted, do so before passing it in.

        :param leftMotor:  The motor on the left corner.
        :param rightMotor: The motor on the right corner.
        :param backMotor:  The motor on the back corner.

        Construct a Killough drive with the given motors.

        Angles are measured in degrees clockwise from the positive X axis.

        :param leftMotor:       The motor on the left corner.
        :param rightMotor:      The motor on the right corner.
        :param backMotor:       The motor on the back corner.
        :param leftMotorAngle:  The angle of the left wheel's forward direction of
                                travel.
        :param rightMotorAngle: The angle of the right wheel's forward direction of
                                travel.
        :param backMotorAngle:  The angle of the back wheel's forward direction of
                                travel.
        """
    @typing.overload
    def __init__(self, leftMotor: wpilib.interfaces._interfaces.SpeedController, rightMotor: wpilib.interfaces._interfaces.SpeedController, backMotor: wpilib.interfaces._interfaces.SpeedController, leftMotorAngle: float, rightMotorAngle: float, backMotorAngle: float) -> None: ...
    def driveCartesian(self, ySpeed: float, xSpeed: float, zRotation: float, gyroAngle: float = 0.0) -> None: 
        """
        Drive method for Killough platform.

        Angles are measured clockwise from the positive X axis. The robot's speed
        is independent from its angle or rotation rate.

        :param ySpeed:    The robot's speed along the Y axis [-1.0..1.0]. Right is
                          positive.
        :param xSpeed:    The robot's speed along the X axis [-1.0..1.0]. Forward is
                          positive.
        :param zRotation: The robot's rotation rate around the Z axis [-1.0..1.0].
                          Clockwise is positive.
        :param gyroAngle: The current angle reading from the gyro in degrees around
                          the Z axis. Use this to implement field-oriented controls.
        """
    def drivePolar(self, magnitude: float, angle: float, zRotation: float) -> None: 
        """
        Drive method for Killough platform.

        Angles are measured clockwise from the positive X axis. The robot's speed
        is independent from its angle or rotation rate.

        :param magnitude: The robot's speed at a given angle [-1.0..1.0]. Forward is
                          positive.
        :param angle:     The angle around the Z axis at which the robot drives in
                          degrees [-180..180].
        :param zRotation: The robot's rotation rate around the Z axis [-1.0..1.0].
                          Clockwise is positive.
        """
    def getDescription(self) -> str: ...
    def initSendable(self, builder: wpilib._wpilib.SendableBuilder) -> None: ...
    def stopMotor(self) -> None: ...
    kDefaultBackMotorAngle = 270.0
    kDefaultLeftMotorAngle = 60.0
    kDefaultRightMotorAngle = 120.0
    pass
class MecanumDrive(RobotDriveBase, wpilib._wpilib.MotorSafety, wpilib._wpilib.ErrorBase, wpilib._wpilib.Sendable):
    """
    A class for driving Mecanum drive platforms.

    Mecanum drives are rectangular with one wheel on each corner. Each wheel has
    rollers toed in 45 degrees toward the front or back. When looking at the
    wheels from the top, the roller axles should form an X across the robot.

    Drive base diagram:
    ::

      \\_______/
      \\ |   | /
        |   |
      /_|___|_\ * /       \ * </pre>
      
      Each Drive() function provides different inverse kinematic relations for a
      Mecanum drive robot. Motor outputs for the right side are negated, so motor
      direction inversion by the user is usually unnecessary.
      
      This library uses the NED axes convention (North-East-Down as external
      reference in the world frame):
      http://www.nuclearprojects.com/ins/images/axis_big.png.
      
      The positive X axis points ahead, the positive Y axis points to the right,
      and the positive Z axis points down. Rotations follow the right-hand rule, so
      clockwise rotation around the Z axis is positive.
      
      Inputs smaller then 0.02 will be set to 0, and larger values will be scaled
      so that the full range is still used. This deadband value can be changed
      with SetDeadband().
      
      RobotDrive porting guide:
      <br>In MecanumDrive, the right side speed controllers are automatically
      inverted, while in RobotDrive, no speed controllers are automatically
      inverted.
      <br>DriveCartesian(double, double, double, double) is equivalent to
      RobotDrive#MecanumDrive_Cartesian(double, double, double, double)
      if a deadband of 0 is used, and the ySpeed and gyroAngle values are inverted
      compared to RobotDrive (eg DriveCartesian(xSpeed, -ySpeed, zRotation,
      -gyroAngle).
      <br>DrivePolar(double, double, double) is equivalent to
      RobotDrive#MecanumDrive_Polar(double, double, double) if a
      deadband of 0 is used.
    """
    def __init__(self, frontLeftMotor: wpilib.interfaces._interfaces.SpeedController, rearLeftMotor: wpilib.interfaces._interfaces.SpeedController, frontRightMotor: wpilib.interfaces._interfaces.SpeedController, rearRightMotor: wpilib.interfaces._interfaces.SpeedController) -> None: 
        """
        Construct a MecanumDrive.

        If a motor needs to be inverted, do so before passing it in.
        """
    def driveCartesian(self, ySpeed: float, xSpeed: float, zRotation: float, gyroAngle: float = 0.0) -> None: 
        """
        Drive method for Mecanum platform.

        Angles are measured clockwise from the positive X axis. The robot's speed
        is independent from its angle or rotation rate.

        :param ySpeed:    The robot's speed along the Y axis [-1.0..1.0]. Right is
                          positive.
        :param xSpeed:    The robot's speed along the X axis [-1.0..1.0]. Forward is
                          positive.
        :param zRotation: The robot's rotation rate around the Z axis [-1.0..1.0].
                          Clockwise is positive.
        :param gyroAngle: The current angle reading from the gyro in degrees around
                          the Z axis. Use this to implement field-oriented controls.
        """
    def drivePolar(self, magnitude: float, angle: float, zRotation: float) -> None: 
        """
        Drive method for Mecanum platform.

        Angles are measured clockwise from the positive X axis. The robot's speed
        is independent from its angle or rotation rate.

        :param magnitude: The robot's speed at a given angle [-1.0..1.0]. Forward is
                          positive.
        :param angle:     The angle around the Z axis at which the robot drives in
                          degrees [-180..180].
        :param zRotation: The robot's rotation rate around the Z axis [-1.0..1.0].
                          Clockwise is positive.
        """
    def getDescription(self) -> str: ...
    def initSendable(self, builder: wpilib._wpilib.SendableBuilder) -> None: ...
    def isRightSideInverted(self) -> bool: 
        """
        Gets if the power sent to the right side of the drivetrain is multiplied by
        -1.

        :returns: true if the right side is inverted
        """
    def setRightSideInverted(self, rightSideInverted: bool) -> None: 
        """
        Sets if the power sent to the right side of the drivetrain should be
        multiplied by -1.

        :param rightSideInverted: true if right side power should be multiplied by
                                  -1
        """
    def stopMotor(self) -> None: ...
    pass
class DifferentialDrive(RobotDriveBase, wpilib._wpilib.MotorSafety, wpilib._wpilib.ErrorBase, wpilib._wpilib.Sendable):
    """
    A class for driving differential drive/skid-steer drive platforms such as
    the Kit of Parts drive base, "tank drive", or West Coast Drive.

    These drive bases typically have drop-center / skid-steer with two or more
    wheels per side (e.g., 6WD or 8WD). This class takes a SpeedController per
    side. For four and six motor drivetrains, construct and pass in
    :class:`SpeedControllerGroup` instances as follows.

    Four motor drivetrain::

      class Robot(wpilib.TimedRobot):
          def robotInit(self):
              self.front_left = wpilib.PWMVictorSPX(1)
              self.rear_left = wpilib.PWMVictorSPX(2)
              self.left = wpilib.SpeedControllerGroup(self.front_left, self.rear_left)

              self.front_right = wpilib.PWMVictorSPX(3)
              self.rear_right = wpilib.PWMVictorSPX(4)
              self.right = wpilib.SpeedControllerGroup(self.front_right, self.rear_right)

              self.drive = wpilib.DifferentialDrive(self.left, self.right)

    Six motor drivetrain::

      class Robot(wpilib.TimedRobot):
          def robotInit(self):
              self.front_left = wpilib.PWMVictorSPX(1)
              self.mid_left = wpilib.PWMVictorSPX(2)
              self.rear_left = wpilib.PWMVictorSPX(3)
              self.left = wpilib.SpeedControllerGroup(self.front_left, self.mid_left, self.rear_left)

              self.front_right = wpilib.PWMVictorSPX(4)
              self.mid_right = wpilib.PWMVictorSPX(5)
              self.rear_right = wpilib.PWMVictorSPX(6)
              self.right = wpilib.SpeedControllerGroup(self.front_right, self.mid_right, self.rear_right)

              self.drive = wpilib.DifferentialDrive(self.left, self.right)

    A differential drive robot has left and right wheels separated by an
    arbitrary width.

    Drive base diagram::

      |_______|
      | |   | |
        |   |
      |_|___|_|
      |       |

    Each Drive() function provides different inverse kinematic relations for a
    differential drive robot. Motor outputs for the right side are negated, so
    motor direction inversion by the user is usually unnecessary.

    This library uses the NED axes convention (North-East-Down as external
    reference in the world frame):
    http://www.nuclearprojects.com/ins/images/axis_big.png.

    The positive X axis points ahead, the positive Y axis points to the right,
    and the positive Z axis points down. Rotations follow the right-hand rule,
    so clockwise rotation around the Z axis is positive.

    Inputs smaller then 0.02 will be set to 0, and larger values will be scaled
    so that the full range is still used. This deadband value can be changed
    with SetDeadband().

    RobotDrive porting guide:

    * :meth:`tankDrive` is equivalent to ``RobotDrive.tankDrive``
      if a deadband of 0 is used.
    * :meth:`arcadeDrive` is equivalent to ``RobotDrive.arcadeDrive``
      if a deadband of 0 is used and the the rotation input is inverted,
      e.g. ``arcadeDrive(y, -rotation, squareInputs=False)``
    * :meth:`curvatureDrive` is similar in concept to
      ``RobotDrive.drive`` with the addition of a quick turn
      mode. However, it is not designed to give exactly the same response.
    """
    def __init__(self, leftMotor: wpilib.interfaces._interfaces.SpeedController, rightMotor: wpilib.interfaces._interfaces.SpeedController) -> None: 
        """
        Construct a DifferentialDrive.

        To pass multiple motors per side, use a SpeedControllerGroup. If a motor
        needs to be inverted, do so before passing it in.
        """
    def arcadeDrive(self, xSpeed: float, zRotation: float, squareInputs: bool = True) -> None: 
        """
        Arcade drive method for differential drive platform.

        Note: Some drivers may prefer inverted rotation controls. This can be done
        by negating the value passed for rotation.

        :param xSpeed:       The speed at which the robot should drive along the X
                             axis [-1.0..1.0]. Forward is positive.
        :param zRotation:    The rotation rate of the robot around the Z axis
                             [-1.0..1.0]. Clockwise is positive.
        :param squareInputs: If set, decreases the input sensitivity at low speeds.
        """
    def curvatureDrive(self, xSpeed: float, zRotation: float, isQuickTurn: bool) -> None: 
        """
        Curvature drive method for differential drive platform.

        The rotation argument controls the curvature of the robot's path rather
        than its rate of heading change. This makes the robot more controllable at
        high speeds. Also handles the robot's quick turn functionality - "quick
        turn" overrides constant-curvature turning for turn-in-place maneuvers.

        :param xSpeed:      The robot's speed along the X axis [-1.0..1.0]. Forward
                            is positive.
        :param zRotation:   The robot's rotation rate around the Z axis [-1.0..1.0].
                            Clockwise is positive.
        :param isQuickTurn: If set, overrides constant-curvature turning for
                            turn-in-place maneuvers.
        """
    def getDescription(self) -> str: ...
    def initSendable(self, builder: wpilib._wpilib.SendableBuilder) -> None: ...
    def isRightSideInverted(self) -> bool: 
        """
        Gets if the power sent to the right side of the drivetrain is multiplied by
        -1.

        :returns: true if the right side is inverted
        """
    def setQuickStopAlpha(self, alpha: float) -> None: 
        """
        Sets the low-pass filter gain for QuickStop in curvature drive.

        The low-pass filter filters incoming rotation rate commands to smooth out
        high frequency changes.

        :param alpha: Low-pass filter gain [0.0..2.0]. Smaller values result in
                      slower output changes. Values between 1.0 and 2.0 result in
                      output oscillation. Values below 0.0 and above 2.0 are
                      unstable.
        """
    def setQuickStopThreshold(self, threshold: float) -> None: 
        """
        Sets the QuickStop speed threshold in curvature drive.

        QuickStop compensates for the robot's moment of inertia when stopping after
        a QuickTurn.

        While QuickTurn is enabled, the QuickStop accumulator takes on the rotation
        rate value outputted by the low-pass filter when the robot's speed along
        the X axis is below the threshold. When QuickTurn is disabled, the
        accumulator's value is applied against the computed angular power request
        to slow the robot's rotation.

        :param threshold: X speed below which quick stop accumulator will receive
                          rotation rate values [0..1.0].
        """
    def setRightSideInverted(self, rightSideInverted: bool) -> None: 
        """
        Sets if the power sent to the right side of the drivetrain should be
        multiplied by -1.

        :param rightSideInverted: true if right side power should be multiplied by
                                  -1
        """
    def stopMotor(self) -> None: ...
    def tankDrive(self, leftSpeed: float, rightSpeed: float, squareInputs: bool = True) -> None: 
        """
        Tank drive method for differential drive platform.

        :param leftSpeed:    The robot left side's speed along the X axis
                             [-1.0..1.0]. Forward is positive.
        :param rightSpeed:   The robot right side's speed along the X axis
                             [-1.0..1.0]. Forward is positive.
        :param squareInputs: If set, decreases the input sensitivity at low speeds.
        """
    kDefaultQuickStopAlpha = 0.1
    kDefaultQuickStopThreshold = 0.2
    pass
class Vector2d():
    """
    This is a 2D vector struct that supports basic vector operations.
    """
    @typing.overload
    def __init__(self) -> None: ...
    @typing.overload
    def __init__(self, x: float, y: float) -> None: ...
    def dot(self, vec: Vector2d) -> float: 
        """
        Returns dot product of this vector with argument.

        :param vec: Vector with which to perform dot product.
        """
    def magnitude(self) -> float: 
        """
        Returns magnitude of vector.
        """
    def rotate(self, angle: float) -> None: 
        """
        Rotate a vector in Cartesian space.

        :param angle: angle in degrees by which to rotate vector counter-clockwise.
        """
    def scalarProject(self, vec: Vector2d) -> float: 
        """
        Returns scalar projection of this vector onto argument.

        :param vec: Vector onto which to project this vector.
        """
    @property
    def x(self) -> float:
        """
        :type: float
        """
    @x.setter
    def x(self, arg0: float) -> None:
        pass
    @property
    def y(self) -> float:
        """
        :type: float
        """
    @y.setter
    def y(self, arg0: float) -> None:
        pass
    pass
