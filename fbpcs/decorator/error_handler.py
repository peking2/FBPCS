#!/usr/bin/env python3
# Copyright (c) Facebook, Inc. and its affiliates.
#
# This source code is licensed under the MIT license found in the
# LICENSE file in the root directory of this source tree.

# pyre-strict

import typing
from typing import Callable

from botocore.exceptions import ClientError
from fbpcs.error.mapper.aws import map_aws_error
from fbpcs.error.pcs import PcsError


def error_handler(f: Callable[..., typing.Any]) -> Callable[..., typing.Any]:
    def wrap(*args: typing.Any, **kwargs: typing.Any) -> typing.Any:
        try:
            return f(*args, **kwargs)
        except ClientError as err:
            raise map_aws_error(err)
        except Exception as err:
            raise PcsError(err)

    return wrap
