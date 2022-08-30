# Copyright 2022 Huawei Technologies Co., Ltd
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ============================================================================
""""Classes and functions for Initializer"""

import math
import numpy as np
from mindspore.common.initializer import (Initializer, _calculate_fan_in_and_fan_out, _assignment)

class XavierNormal(Initializer):
    r"""
    Generates an array with values sampled from Xavier normal distribution
    :math::math:`\mathcal{N}(0, \text{std}^2)` in order to initialize a tensor, where

    .. math::
        boundary = gain * \sqrt{\frac{2}{n_{in} + n_{out}}}

    where :math:`gain` is an optional scaling factor, :math:`n_{in}` is the number of input units in the weight tensor,
    :math:`n_{out}` is the number of output units in the weight tensor.

    Args:
        gain (float): An optional scaling factor. Default: 1.

    Examples:
        >>> import mindspore
        >>> from mindspore.common.initializer import initializer
        >>> from text.common.initializer import XavierNormal
        >>> tensor1 = initializer(XavierNormal(), [1, 2, 3], mindspore.float32)
        >>> tensor2 = initializer('XavierNormal', [1, 2, 3], mindspore.float32)
    """
    def __init__(self, gain=1):
        super(XavierNormal, self).__init__(gain=gain)
        self.gain = gain

    def _initialize(self, arr):
        fan_in, fan_out = _calculate_fan_in_and_fan_out(arr.shape)

        std = self.gain * math.sqrt(2.0 / float(fan_in + fan_out))
        data = np.random.normal(0, std, arr.shape)

        _assignment(arr, data)
