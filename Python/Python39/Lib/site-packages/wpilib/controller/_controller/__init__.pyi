import wpilib.controller._controller
import typing
import wpilib._wpilib
import wpimath.geometry._geometry
import wpimath.kinematics._kinematics
import wpimath.trajectory._trajectory.Trajectory
import wpimath.trajectory._trajectory.TrapezoidProfile
import wpimath.trajectory._trajectory.TrapezoidProfileRadians

__all__ = [
    "HolonomicDriveController",
    "PIDController",
    "ProfiledPIDController",
    "ProfiledPIDControllerRadians",
    "RamseteController"
]


class HolonomicDriveController():
    """
    This holonomic drive controller can be used to follow trajectories using a
    holonomic drive train (i.e. swerve or mecanum). Holonomic trajectory
    following is a much simpler problem to solve compared to skid-steer style
    drivetrains because it is possible to individually control forward, sideways,
    and angular velocity.

    The holonomic drive controller takes in one PID controller for each
    direction, forward and sideways, and one profiled PID controller for the
    angular direction. Because the heading dynamics are decoupled from
    translations, users can specify a custom heading that the drivetrain should
    point toward. This heading reference is profiled for smoothness.
    """
    def __init__(self, xController: PIDController, yController: PIDController, thetaController: ProfiledPIDControllerRadians) -> None: 
        """
        Constructs a holonomic drive controller.

        :param xController:     A PID Controller to respond to error in the
                                field-relative x direction.
        :param yController:     A PID Controller to respond to error in the
                                field-relative y direction.
        :param thetaController: A profiled PID controller to respond to error in
                                angle.
        """
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, desiredState: wpimath.trajectory._trajectory.Trajectory.State, angleRef: wpimath.geometry._geometry.Rotation2d) -> wpimath.kinematics._kinematics.ChassisSpeeds: 
        """
        Returns the next output of the holonomic drive controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:       The current pose.
        :param poseRef:           The desired pose.
        :param linearVelocityRef: The desired linear velocity.
        :param angleRef:          The desired ending angle.

        Returns the next output of the holonomic drive controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:  The current pose.
        :param desiredState: The desired pose, linear velocity, and angular velocity
                             from a trajectory.
        :param angleRef:     The desired ending angle.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, poseRef: wpimath.geometry._geometry.Pose2d, linearVelocityRef: meters_per_second, angleRef: wpimath.geometry._geometry.Rotation2d) -> wpimath.kinematics._kinematics.ChassisSpeeds: ...
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enables and disables the controller for troubleshooting purposes. When
        Calculate() is called on a disabled controller, only feedforward values
        are returned.

        :param enabled: If the controller is enabled or not.
        """
    def setTolerance(self, tolerance: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Sets the pose error which is considered tolerable for use with
        AtReference().

        :param poseTolerance: Pose error which is tolerable.
        """
    pass
class PIDController(wpilib._wpilib.Sendable):
    """
    Implements a PID control loop.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, period: seconds = 0.02) -> None: 
        """
        Allocates a PIDController with the given constants for Kp, Ki, and Kd.

        :param Kp:     The proportional coefficient.
        :param Ki:     The integral coefficient.
        :param Kd:     The derivative coefficient.
        :param period: The period between controller updates in seconds. The
                       default is 20 milliseconds. Must be non-zero and positive.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the setpoint.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: float) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param setpoint:    The new setpoint of the controller.
        """
    @typing.overload
    def calculate(self, measurement: float, setpoint: float) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: float, maximumInput: float) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> float: 
        """
        Returns the difference between the setpoint and the measurement.
        """
    def getSetpoint(self) -> float: 
        """
        Returns the current setpoint of the PIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> float: 
        """
        Returns the velocity error.
        """
    def initSendable(self, builder: wpilib._wpilib.SendableBuilder) -> None: ...
    def isContinuousInputEnabled(self) -> bool: 
        """
        Returns true if continuous input is enabled.
        """
    def reset(self) -> None: 
        """
        Reset the previous error, the integral term, and disable the controller.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setSetpoint(self, setpoint: float) -> None: 
        """
        Sets the setpoint for the PIDController.

        :param setpoint: The desired setpoint.
        """
    def setTolerance(self, positionTolerance: float, velocityTolerance: float = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velociytTolerance: Velocity error which is tolerable.
        """
    pass
class ProfiledPIDController(wpilib._wpilib.Sendable):
    """
    Implements a PID control loop whose setpoint is constrained by a trapezoid
    profile.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, constraints: wpimath.trajectory._trajectory.TrapezoidProfile.Constraints, period: seconds = 0.02) -> None: 
        """
        Allocates a ProfiledPIDController with the given constants for Kp, Ki, and
        Kd. Users should call reset() when they first start running the controller
        to avoid unwanted behavior.

        :param Kp:          The proportional coefficient.
        :param Ki:          The integral coefficient.
        :param Kd:          The derivative coefficient.
        :param constraints: Velocity and acceleration constraints for goal.
        :param period:      The period between controller updates in seconds. The
                            default is 20 milliseconds.
        """
    def atGoal(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        This will return false until at least one input value has been computed.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        Currently this just reports on target as the actual value passes through
        the setpoint. Ideally it should be based on being within the tolerance for
        some period of time.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: float) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.
        :param constraints: Velocity and acceleration constraints for goal.
        """
    @typing.overload
    def calculate(self, measurement: float, goal: float) -> float: ...
    @typing.overload
    def calculate(self, measurement: float, goal: float, constraints: wpimath.trajectory._trajectory.TrapezoidProfile.Constraints) -> float: ...
    @typing.overload
    def calculate(self, measurement: float, goal: wpimath.trajectory._trajectory.TrapezoidProfile.State) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: float, maximumInput: float) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getGoal(self) -> wpimath.trajectory._trajectory.TrapezoidProfile.State: 
        """
        Gets the goal for the ProfiledPIDController.
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> float: 
        """
        Returns the difference between the setpoint and the measurement.

        :returns: The error.
        """
    def getSetpoint(self) -> wpimath.trajectory._trajectory.TrapezoidProfile.State: 
        """
        Returns the current setpoint of the ProfiledPIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> units_per_second: 
        """
        Returns the change in error per second.
        """
    def initSendable(self, builder: wpilib._wpilib.SendableBuilder) -> None: ...
    @typing.overload
    def reset(self, measuredPosition: float) -> None: 
        """
        Reset the previous error and the integral term.

        :param measurement: The current measured State of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system.
        :param measuredVelocity: The current measured velocity of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system. The
                                 velocity is assumed to be zero.
        """
    @typing.overload
    def reset(self, measuredPosition: float, measuredVelocity: units_per_second) -> None: ...
    @typing.overload
    def reset(self, measurement: wpimath.trajectory._trajectory.TrapezoidProfile.State) -> None: ...
    def setConstraints(self, constraints: wpimath.trajectory._trajectory.TrapezoidProfile.Constraints) -> None: 
        """
        Set velocity and acceleration constraints for goal.

        :param constraints: Velocity and acceleration constraints for goal.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    @typing.overload
    def setGoal(self, goal: float) -> None: 
        """
        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.

        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.
        """
    @typing.overload
    def setGoal(self, goal: wpimath.trajectory._trajectory.TrapezoidProfile.State) -> None: ...
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setTolerance(self, positionTolerance: float, velocityTolerance: units_per_second = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with
        AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velocityTolerance: Velocity error which is tolerable.
        """
    pass
class ProfiledPIDControllerRadians(wpilib._wpilib.Sendable):
    """
    Implements a PID control loop whose setpoint is constrained by a trapezoid
    profile.
    """
    def __init__(self, Kp: float, Ki: float, Kd: float, constraints: wpimath.trajectory._trajectory.TrapezoidProfileRadians.Constraints, period: seconds = 0.02) -> None: 
        """
        Allocates a ProfiledPIDController with the given constants for Kp, Ki, and
        Kd. Users should call reset() when they first start running the controller
        to avoid unwanted behavior.

        :param Kp:          The proportional coefficient.
        :param Ki:          The integral coefficient.
        :param Kd:          The derivative coefficient.
        :param constraints: Velocity and acceleration constraints for goal.
        :param period:      The period between controller updates in seconds. The
                            default is 20 milliseconds.
        """
    def atGoal(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        This will return false until at least one input value has been computed.
        """
    def atSetpoint(self) -> bool: 
        """
        Returns true if the error is within the tolerance of the error.

        Currently this just reports on target as the actual value passes through
        the setpoint. Ideally it should be based on being within the tolerance for
        some period of time.

        This will return false until at least one input value has been computed.
        """
    @typing.overload
    def calculate(self, measurement: radians) -> float: 
        """
        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.

        Returns the next output of the PID controller.

        :param measurement: The current measurement of the process variable.
        :param goal:        The new goal of the controller.
        :param constraints: Velocity and acceleration constraints for goal.
        """
    @typing.overload
    def calculate(self, measurement: radians, goal: radians) -> float: ...
    @typing.overload
    def calculate(self, measurement: radians, goal: radians, constraints: wpimath.trajectory._trajectory.TrapezoidProfileRadians.Constraints) -> float: ...
    @typing.overload
    def calculate(self, measurement: radians, goal: wpimath.trajectory._trajectory.TrapezoidProfileRadians.State) -> float: ...
    def disableContinuousInput(self) -> None: 
        """
        Disables continuous input.
        """
    def enableContinuousInput(self, minimumInput: radians, maximumInput: radians) -> None: 
        """
        Enables continuous input.

        Rather then using the max and min input range as constraints, it considers
        them to be the same point and automatically calculates the shortest route
        to the setpoint.

        :param minimumInput: The minimum value expected from the input.
        :param maximumInput: The maximum value expected from the input.
        """
    def getD(self) -> float: 
        """
        Gets the differential coefficient.

        :returns: differential coefficient
        """
    def getGoal(self) -> wpimath.trajectory._trajectory.TrapezoidProfileRadians.State: 
        """
        Gets the goal for the ProfiledPIDController.
        """
    def getI(self) -> float: 
        """
        Gets the integral coefficient.

        :returns: integral coefficient
        """
    def getP(self) -> float: 
        """
        Gets the proportional coefficient.

        :returns: proportional coefficient
        """
    def getPeriod(self) -> seconds: 
        """
        Gets the period of this controller.

        :returns: The period of the controller.
        """
    def getPositionError(self) -> radians: 
        """
        Returns the difference between the setpoint and the measurement.

        :returns: The error.
        """
    def getSetpoint(self) -> wpimath.trajectory._trajectory.TrapezoidProfileRadians.State: 
        """
        Returns the current setpoint of the ProfiledPIDController.

        :returns: The current setpoint.
        """
    def getVelocityError(self) -> radians_per_second: 
        """
        Returns the change in error per second.
        """
    def initSendable(self, builder: wpilib._wpilib.SendableBuilder) -> None: ...
    @typing.overload
    def reset(self, measuredPosition: radians) -> None: 
        """
        Reset the previous error and the integral term.

        :param measurement: The current measured State of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system.
        :param measuredVelocity: The current measured velocity of the system.

        Reset the previous error and the integral term.

        :param measuredPosition: The current measured position of the system. The
                                 velocity is assumed to be zero.
        """
    @typing.overload
    def reset(self, measuredPosition: radians, measuredVelocity: radians_per_second) -> None: ...
    @typing.overload
    def reset(self, measurement: wpimath.trajectory._trajectory.TrapezoidProfileRadians.State) -> None: ...
    def setConstraints(self, constraints: wpimath.trajectory._trajectory.TrapezoidProfileRadians.Constraints) -> None: 
        """
        Set velocity and acceleration constraints for goal.

        :param constraints: Velocity and acceleration constraints for goal.
        """
    def setD(self, Kd: float) -> None: 
        """
        Sets the differential coefficient of the PID controller gain.

        :param Kd: differential coefficient
        """
    @typing.overload
    def setGoal(self, goal: radians) -> None: 
        """
        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.

        Sets the goal for the ProfiledPIDController.

        :param goal: The desired unprofiled setpoint.
        """
    @typing.overload
    def setGoal(self, goal: wpimath.trajectory._trajectory.TrapezoidProfileRadians.State) -> None: ...
    def setI(self, Ki: float) -> None: 
        """
        Sets the integral coefficient of the PID controller gain.

        :param Ki: integral coefficient
        """
    def setIntegratorRange(self, minimumIntegral: float, maximumIntegral: float) -> None: 
        """
        Sets the minimum and maximum values for the integrator.

        When the cap is reached, the integrator value is added to the controller
        output rather than the integrator value times the integral gain.

        :param minimumIntegral: The minimum value of the integrator.
        :param maximumIntegral: The maximum value of the integrator.
        """
    def setP(self, Kp: float) -> None: 
        """
        Sets the proportional coefficient of the PID controller gain.

        :param Kp: proportional coefficient
        """
    def setPID(self, Kp: float, Ki: float, Kd: float) -> None: 
        """
        Sets the PID Controller gain parameters.

        Sets the proportional, integral, and differential coefficients.

        :param Kp: Proportional coefficient
        :param Ki: Integral coefficient
        :param Kd: Differential coefficient
        """
    def setTolerance(self, positionTolerance: radians, velocityTolerance: radians_per_second = inf) -> None: 
        """
        Sets the error which is considered tolerable for use with
        AtSetpoint().

        :param positionTolerance: Position error which is tolerable.
        :param velocityTolerance: Velocity error which is tolerable.
        """
    pass
class RamseteController():
    """
    Ramsete is a nonlinear time-varying feedback controller for unicycle models
    that drives the model to a desired pose along a two-dimensional trajectory.
    Why would we need a nonlinear control law in addition to the linear ones we
    have used so far like PID? If we use the original approach with PID
    controllers for left and right position and velocity states, the controllers
    only deal with the local pose. If the robot deviates from the path, there is
    no way for the controllers to correct and the robot may not reach the desired
    global pose. This is due to multiple endpoints existing for the robot which
    have the same encoder path arc lengths.

    Instead of using wheel path arc lengths (which are in the robot's local
    coordinate frame), nonlinear controllers like pure pursuit and Ramsete use
    global pose. The controller uses this extra information to guide a linear
    reference tracker like the PID controllers back in by adjusting the
    references of the PID controllers.

    The paper "Control of Wheeled Mobile Robots: An Experimental Overview"
    describes a nonlinear controller for a wheeled vehicle with unicycle-like
    kinematics; a global pose consisting of x, y, and theta; and a desired pose
    consisting of x_d, y_d, and theta_d. We call it Ramsete because that's the
    acronym for the title of the book it came from in Italian ("Robotica
    Articolata e Mobile per i SErvizi e le TEcnologie").

    See <https://file.tavsys.net/control/controls-engineering-in-frc.pdf> section
    on Ramsete unicycle controller for a derivation and analysis.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Construct a Ramsete unicycle controller.

        :param b:    Tuning parameter (b > 0) for which larger values make
                     convergence more aggressive like a proportional term.
        :param zeta: Tuning parameter (0 < zeta < 1) for which larger values provide
                     more damping in response.

        Construct a Ramsete unicycle controller. The default arguments for
        b and zeta of 2.0 and 0.7 have been well-tested to produce desirable
        results.
        """
    @typing.overload
    def __init__(self, b: float, zeta: float) -> None: ...
    def atReference(self) -> bool: 
        """
        Returns true if the pose error is within tolerance of the reference.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, desiredState: wpimath.trajectory._trajectory.Trajectory.State) -> wpimath.kinematics._kinematics.ChassisSpeeds: 
        """
        Returns the next output of the Ramsete controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:        The current pose.
        :param poseRef:            The desired pose.
        :param linearVelocityRef:  The desired linear velocity.
        :param angularVelocityRef: The desired angular velocity.

        Returns the next output of the Ramsete controller.

        The reference pose, linear velocity, and angular velocity should come from
        a drivetrain trajectory.

        :param currentPose:  The current pose.
        :param desiredState: The desired pose, linear velocity, and angular velocity
                             from a trajectory.
        """
    @typing.overload
    def calculate(self, currentPose: wpimath.geometry._geometry.Pose2d, poseRef: wpimath.geometry._geometry.Pose2d, linearVelocityRef: meters_per_second, angularVelocityRef: radians_per_second) -> wpimath.kinematics._kinematics.ChassisSpeeds: ...
    def setEnabled(self, enabled: bool) -> None: 
        """
        Enables and disables the controller for troubleshooting purposes.

        :param enabled: If the controller is enabled or not.
        """
    def setTolerance(self, poseTolerance: wpimath.geometry._geometry.Pose2d) -> None: 
        """
        Sets the pose error which is considered tolerable for use with
        AtReference().

        :param poseTolerance: Pose error which is tolerable.
        """
    pass
