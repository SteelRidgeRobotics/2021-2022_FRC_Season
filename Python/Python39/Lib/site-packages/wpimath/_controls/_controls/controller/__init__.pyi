import wpimath._controls._controls.controller
import typing
import numpy
import wpimath._controls._controls.system
_Shape = typing.Tuple[int, ...]

__all__ = [
    "ArmFeedforward",
    "ControlAffinePlantInversionFeedforward_1_1",
    "ControlAffinePlantInversionFeedforward_2_1",
    "ControlAffinePlantInversionFeedforward_2_2",
    "ElevatorFeedforward",
    "LinearPlantInversionFeedforward_1_1",
    "LinearPlantInversionFeedforward_2_1",
    "LinearPlantInversionFeedforward_2_2",
    "LinearQuadraticRegulator_1_1",
    "LinearQuadraticRegulator_2_1",
    "LinearQuadraticRegulator_2_2",
    "SimpleMotorFeedforward",
    "SimpleMotorFeedforwardMeters"
]


class ArmFeedforward():
    """
    A helper class that computes feedforward outputs for a simple arm (modeled as
    a motor acting against the force of gravity on a beam suspended at an angle).
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new ArmFeedforward with the specified gains.

        :param kS:   The static gain, in volts.
        :param kCos: The gravity gain, in volts.
        :param kV:   The velocity gain, in volt seconds per radian.
        :param kA:   The acceleration gain, in volt seconds^2 per radian.
        """
    @typing.overload
    def __init__(self, kS: volts, kCos: volts, kV: volt_seconds_per_radian, kA: volt_seconds_squared_per_radian = 0.0) -> None: ...
    def calculate(self, angle: radians, velocity: radians_per_second, acceleration: radians_per_second_squared = 0.0) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param angle:        The angle setpoint, in radians.
        :param velocity:     The velocity setpoint, in radians per second.
        :param acceleration: The acceleration setpoint, in radians per second^2.

        :returns: The computed feedforward, in volts.
        """
    def maxAchievableAcceleration(self, maxVoltage: volts, angle: radians, velocity: radians_per_second) -> radians_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply, a position, and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the arm.
        :param angle:      The angle of the arm
        :param velocity:   The velocity of the arm.

        :returns: The maximum possible acceleration at the given velocity and angle.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, angle: radians, acceleration: radians_per_second_squared) -> radians_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply,
        a position, and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the arm.
        :param angle:        The angle of the arm
        :param acceleration: The acceleration of the arm.

        :returns: The maximum possible velocity at the given acceleration and angle.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, angle: radians, velocity: radians_per_second) -> radians_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply, a position, and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the arm.
        :param angle:      The angle of the arm
        :param velocity:   The velocity of the arm.

        :returns: The minimum possible acceleration at the given velocity and angle.
        """
    def minAchievableVelocity(self, maxVoltage: volts, angle: radians, acceleration: radians_per_second_squared) -> radians_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply,
        a position, and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the arm.
        :param angle:        The angle of the arm
        :param acceleration: The acceleration of the arm.

        :returns: The minimum possible velocity at the given acceleration and angle.
        """
    @property
    def kA(self) -> volt_seconds_squared_per_radian:
        """
        :type: volt_seconds_squared_per_radian
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared_per_radian) -> None:
        pass
    @property
    def kCos(self) -> volts:
        """
        :type: volts
        """
    @kCos.setter
    def kCos(self, arg0: volts) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds_per_radian:
        """
        :type: volt_seconds_per_radian
        """
    @kV.setter
    def kV(self, arg0: volt_seconds_per_radian) -> None:
        pass
    pass
class ControlAffinePlantInversionFeedforward_1_1():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one
        set using Reset(const Eigen::Matrix<double, States, 1>&).
        If the initial state is not set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[1, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param row: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class ControlAffinePlantInversionFeedforward_2_1():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[1, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one
        set using Reset(const Eigen::Matrix<double, States, 1>&).
        If the initial state is not set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param row: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class ControlAffinePlantInversionFeedforward_2_2():
    """
    Constructs a control-affine plant inversion model-based feedforward from
    given model dynamics.

    If given the vector valued function as f(x, u) where x is the state
    vector and u is the input vector, the B matrix(continuous input matrix)
    is calculated through a NumericalJacobian. In this case f has to be
    control-affine (of the form f(x) + Bu).

    The feedforward is calculated as
    :strong:` u_ff = B:sup:`+` (rDot - f(x)) `, where :strong:`
    B:sup:`+` ` is the pseudoinverse of B.

    This feedforward does not account for a dynamic B matrix, B is either
    determined or supplied when the feedforward is created and remains constant.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], dt: seconds) -> None: 
        """
        Constructs a feedforward with given model dynamics as a function
        of state and input.

        :param f:  A vector-valued function of x, the state, and
                   u, the input, that returns the derivative of
                   the state vector. HAS to be control-affine
                   (of the form f(x) + Bu).
        :param dt: The timestep between calls of calculate().

        Constructs a feedforward with given model dynamics as a function of state,
        and the plant's B matrix(continuous input matrix).

        :param f:  A vector-valued function of x, the state,
                   that returns the derivative of the state vector.
        :param B:  Continuous input matrix of the plant being controlled.
        :param dt: The timestep between calls of calculate().
        """
    @typing.overload
    def __init__(self, f: typing.Callable[[numpy.ndarray[numpy.float64, _Shape[2, 1]]], numpy.ndarray[numpy.float64, _Shape[2, 1]]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one
        set using Reset(const Eigen::Matrix<double, States, 1>&).
        If the initial state is not set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param row: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class ElevatorFeedforward():
    """
    A helper class that computes feedforward outputs for a simple elevator
    (modeled as a motor acting against the force of gravity).
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new ElevatorFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kG: The gravity gain, in volts.
        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds^2 per distance.
        """
    @typing.overload
    def __init__(self, kS: volts, kG: volts, kV: volt_seconds, kA: volt_seconds_squared = 0.0) -> None: ...
    def calculate(self, velocity: units_per_second, acceleration: units_per_second_squared = 0.0) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param velocity:     The velocity setpoint, in distance per second.
        :param acceleration: The acceleration setpoint, in distance per second^2.

        :returns: The computed feedforward, in volts.
        """
    def maxAchievableAcceleration(self, maxVoltage: volts, velocity: units_per_second) -> units_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the elevator.
        :param velocity:   The velocity of the elevator.

        :returns: The maximum possible acceleration at the given velocity.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, acceleration: units_per_second_squared) -> units_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the elevator.
        :param acceleration: The acceleration of the elevator.

        :returns: The maximum possible velocity at the given acceleration.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, velocity: units_per_second) -> units_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the elevator.
        :param velocity:   The velocity of the elevator.

        :returns: The minimum possible acceleration at the given velocity.
        """
    def minAchievableVelocity(self, maxVoltage: volts, acceleration: units_per_second_squared) -> units_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the elevator.
        :param acceleration: The acceleration of the elevator.

        :returns: The minimum possible velocity at the given acceleration.
        """
    @property
    def kA(self) -> volt_seconds_squared:
        """
        :type: volt_seconds_squared
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared) -> None:
        pass
    @property
    def kG(self) -> volts:
        """
        :type: volts
        """
    @kG.setter
    def kG(self, arg0: volts) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds:
        """
        :type: volt_seconds
        """
    @kV.setter
    def kV(self, arg0: volt_seconds) -> None:
        pass
    pass
class LinearPlantInversionFeedforward_1_1():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:         Continuous system matrix of the plant being controlled.
        :param B:         Continuous input matrix of the plant being controlled.
        :param dtSeconds: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one
        set using Reset(const Eigen::Matrix<double, States, 1>&).
        If the initial state is not set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[1, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[1, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param row: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearPlantInversionFeedforward_2_1():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:         Continuous system matrix of the plant being controlled.
        :param B:         Continuous input matrix of the plant being controlled.
        :param dtSeconds: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one
        set using Reset(const Eigen::Matrix<double, States, 1>&).
        If the initial state is not set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[1, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param row: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearPlantInversionFeedforward_2_2():
    """
    Constructs a plant inversion model-based feedforward from a LinearSystem.

    The feedforward is calculated as :strong:` u_ff = B:sup:`+` (r_k+1 - A
    r_k) `, where :strong:` B:sup:`+` ` is the pseudoinverse
    of B.

    For more on the underlying math, read
    https://file.tavsys.net/control/controls-engineering-in-frc.pdf.
    """
    @typing.overload
    def R(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the current reference vector r.

        :returns: The current reference vector.

        Returns an element of the reference vector r.

        :param i: Row of r.

        :returns: The row of the current reference vector.
        """
    @typing.overload
    def R(self, i: int) -> float: ...
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: 
        """
        Constructs a feedforward with the given coefficients.

        :param A:         Continuous system matrix of the plant being controlled.
        :param B:         Continuous input matrix of the plant being controlled.
        :param dtSeconds: Discretization timestep.
        """
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_1, arg1: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_2, arg1: seconds) -> None: ...
    @typing.overload
    def calculate(self, nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Calculate the feedforward with only the desired
        future reference. This uses the internally stored "current"
        reference.

        If this method is used the initial state of the system is the one
        set using Reset(const Eigen::Matrix<double, States, 1>&).
        If the initial state is not set it defaults to a zero vector.

        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.

        Calculate the feedforward with current and future reference vectors.

        :param r:     The reference state of the current timestep (k).
        :param nextR: The reference state of the future timestep (k + dt).

        :returns: The calculated feedforward.
        """
    @typing.overload
    def calculate(self, r: numpy.ndarray[numpy.float64, _Shape[2, 1]], nextR: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: ...
    @typing.overload
    def reset(self) -> None: 
        """
        Resets the feedforward with a specified initial state vector.

        :param initialState: The initial state vector.

        Resets the feedforward with a zero initial state vector.
        """
    @typing.overload
    def reset(self, initialState: numpy.ndarray[numpy.float64, _Shape[2, 1]]) -> None: ...
    @typing.overload
    def uff(self) -> numpy.ndarray[numpy.float64, _Shape[2, 1]]: 
        """
        Returns the previously calculated feedforward as an input vector.

        :returns: The calculated feedforward.

        Returns an element of the previously calculated feedforward.

        :param row: Row of uff.

        :returns: The row of the calculated feedforward.
        """
    @typing.overload
    def uff(self, i: int) -> float: ...
    pass
class LinearQuadraticRegulator_1_1():
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Q: numpy.ndarray[numpy.float64, _Shape[1, 1]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[1, 1]], B: numpy.ndarray[numpy.float64, _Shape[1, 1]], Qelems: typing.Tuple[float], Relems: typing.Tuple[float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_1, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_1_1_2, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    pass
class LinearQuadraticRegulator_2_1():
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[1, 1]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 1]], Qelems: typing.Tuple[float], Relems: typing.Tuple[float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_1, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_1_2, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    pass
class LinearQuadraticRegulator_2_2():
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Q: numpy.ndarray[numpy.float64, _Shape[2, 2]], R: numpy.ndarray[numpy.float64, _Shape[2, 2]], dt: seconds) -> None: 
        """
        Constructs a controller with the given coefficients and plant.

        :param A:      Continuous system matrix of the plant being controlled.
        :param B:      Continuous input matrix of the plant being controlled.
        :param Qelems: The maximum desired error tolerance for each state.
        :param Relems: The maximum desired control effort for each input.
        :param dt:     Discretization timestep.

        Constructs a controller with the given coefficients and plant.

        :param A:  Continuous system matrix of the plant being controlled.
        :param B:  Continuous input matrix of the plant being controlled.
        :param Q:  The state cost matrix.
        :param R:  The input cost matrix.
        :param dt: Discretization timestep.
        """
    @typing.overload
    def __init__(self, A: numpy.ndarray[numpy.float64, _Shape[2, 2]], B: numpy.ndarray[numpy.float64, _Shape[2, 2]], Qelems: typing.Tuple[float], Relems: typing.Tuple[float], dt: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_1, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    @typing.overload
    def __init__(self, arg0: wpimath._controls._controls.system.LinearSystem_2_2_2, arg1: typing.Tuple[float], arg2: typing.Tuple[float], arg3: seconds) -> None: ...
    pass
class SimpleMotorFeedforward():
    """
    A helper class that computes feedforward voltages for a simple
    permanent-magnet DC motor.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new SimpleMotorFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds^2 per distance.
        """
    @typing.overload
    def __init__(self, kS: volts, kV: volt_seconds, kA: volt_seconds_squared = 0.0) -> None: ...
    def calculate(self, velocity: units_per_second, acceleration: units_per_second_squared = 0.0) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param velocity:     The velocity setpoint, in distance per second.
        :param acceleration: The acceleration setpoint, in distance per second^2.

        :returns: The computed feedforward, in volts.
        """
    def maxAchievableAcceleration(self, maxVoltage: volts, velocity: units_per_second) -> units_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the motor.
        :param velocity:   The velocity of the motor.

        :returns: The maximum possible acceleration at the given velocity.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, acceleration: units_per_second_squared) -> units_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the motor.
        :param acceleration: The acceleration of the motor.

        :returns: The maximum possible velocity at the given acceleration.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, velocity: units_per_second) -> units_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the motor.
        :param velocity:   The velocity of the motor.

        :returns: The minimum possible acceleration at the given velocity.
        """
    def minAchievableVelocity(self, maxVoltage: volts, acceleration: units_per_second_squared) -> units_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the motor.
        :param acceleration: The acceleration of the motor.

        :returns: The minimum possible velocity at the given acceleration.
        """
    @property
    def kA(self) -> volt_seconds_squared:
        """
        :type: volt_seconds_squared
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds:
        """
        :type: volt_seconds
        """
    @kV.setter
    def kV(self, arg0: volt_seconds) -> None:
        pass
    pass
class SimpleMotorFeedforwardMeters():
    """
    A helper class that computes feedforward voltages for a simple
    permanent-magnet DC motor.
    """
    @typing.overload
    def __init__(self) -> None: 
        """
        Creates a new SimpleMotorFeedforward with the specified gains.

        :param kS: The static gain, in volts.
        :param kV: The velocity gain, in volt seconds per distance.
        :param kA: The acceleration gain, in volt seconds^2 per distance.
        """
    @typing.overload
    def __init__(self, kS: volts, kV: volt_seconds_per_meter, kA: volt_seconds_squared_per_meter = 0.0) -> None: ...
    def calculate(self, velocity: meters_per_second, acceleration: meters_per_second_squared = 0.0) -> volts: 
        """
        Calculates the feedforward from the gains and setpoints.

        :param velocity:     The velocity setpoint, in distance per second.
        :param acceleration: The acceleration setpoint, in distance per second^2.

        :returns: The computed feedforward, in volts.
        """
    def maxAchievableAcceleration(self, maxVoltage: volts, velocity: meters_per_second) -> meters_per_second_squared: 
        """
        Calculates the maximum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the motor.
        :param velocity:   The velocity of the motor.

        :returns: The maximum possible acceleration at the given velocity.
        """
    def maxAchievableVelocity(self, maxVoltage: volts, acceleration: meters_per_second_squared) -> meters_per_second: 
        """
        Calculates the maximum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the motor.
        :param acceleration: The acceleration of the motor.

        :returns: The maximum possible velocity at the given acceleration.
        """
    def minAchievableAcceleration(self, maxVoltage: volts, velocity: meters_per_second) -> meters_per_second_squared: 
        """
        Calculates the minimum achievable acceleration given a maximum voltage
        supply and a velocity. Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the velocity constraint, and this will give you
        a simultaneously-achievable acceleration constraint.

        :param maxVoltage: The maximum voltage that can be supplied to the motor.
        :param velocity:   The velocity of the motor.

        :returns: The minimum possible acceleration at the given velocity.
        """
    def minAchievableVelocity(self, maxVoltage: volts, acceleration: meters_per_second_squared) -> meters_per_second: 
        """
        Calculates the minimum achievable velocity given a maximum voltage supply
        and an acceleration.  Useful for ensuring that velocity and
        acceleration constraints for a trapezoidal profile are simultaneously
        achievable - enter the acceleration constraint, and this will give you
        a simultaneously-achievable velocity constraint.

        :param maxVoltage:   The maximum voltage that can be supplied to the motor.
        :param acceleration: The acceleration of the motor.

        :returns: The minimum possible velocity at the given acceleration.
        """
    @property
    def kA(self) -> volt_seconds_squared_per_meter:
        """
        :type: volt_seconds_squared_per_meter
        """
    @kA.setter
    def kA(self, arg0: volt_seconds_squared_per_meter) -> None:
        pass
    @property
    def kS(self) -> volts:
        """
        :type: volts
        """
    @kS.setter
    def kS(self, arg0: volts) -> None:
        pass
    @property
    def kV(self) -> volt_seconds_per_meter:
        """
        :type: volt_seconds_per_meter
        """
    @kV.setter
    def kV(self, arg0: volt_seconds_per_meter) -> None:
        pass
    pass
