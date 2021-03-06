import unittest
import numpy as np
from op_test import OpTest


class TestMomentumOp1(OpTest):
    def setUp(self):
        self.op_type = "momentum"

        param = np.random.random((123, 321)).astype("float32")
        grad = np.random.random((123, 321)).astype("float32")
        velocity = np.zeros((123, 321)).astype("float32")
        learning_rate = np.array([0.001]).astype("float32")
        mu = 0.0001
        use_nesterov = False

        self.inputs = {
            'Param': param,
            'Grad': grad,
            'Velocity': velocity,
            'LearningRate': learning_rate
        }

        self.attrs = {'mu': mu}

        velocity_out = mu * velocity + grad
        if use_nesterov:
            param_out = param - grad * learning_rate + \
                        velocity_out * mu * learning_rate
        else:
            param_out = param - learning_rate * velocity_out

        self.outputs = {'ParamOut': param_out, 'VelocityOut': velocity_out}

    def test_check_output(self):
        self.check_output()


class TestMomentumOp2(OpTest):
    '''Test Momentum with defaukt values for attributes
    '''

    def setUp(self):
        self.op_type = "momentum"

        param = np.random.random((123, 321)).astype("float32")
        grad = np.random.random((123, 321)).astype("float32")
        velocity = np.zeros((123, 321)).astype("float32")
        learning_rate = np.array([0.001]).astype("float32")
        mu = 0.0001
        use_nesterov = True

        self.inputs = {
            'Param': param,
            'Grad': grad,
            'Velocity': velocity,
            'LearningRate': learning_rate
        }

        self.attrs = {'mu': mu, 'useNesterov': use_nesterov}

        velocity_out = mu * velocity + grad
        if use_nesterov:
            param_out = param - grad * learning_rate + \
                        velocity_out * mu * learning_rate
        else:
            param_out = param - learning_rate * velocity_out

        self.outputs = {'ParamOut': param_out, 'VelocityOut': velocity_out}

    def test_check_output(self):
        self.check_output()


if __name__ == "__main__":
    unittest.main()
