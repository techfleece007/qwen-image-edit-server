Instance created. Preparing to start...

==========
== CUDA ==
==========

CUDA Version 12.1.1

Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.

Instance is starting... Waiting for health checks to pass.
Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1016, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/local/lib/python3.10/dist-packages/diffusers/loaders/lora_pipeline.py", line 34, in <module>
    from .lora_base import (  # noqa
  File "/usr/local/lib/python3.10/dist-packages/diffusers/loaders/lora_base.py", line 28, in <module>
    from ..models.modeling_utils import ModelMixin, load_state_dict
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/modeling_utils.py", line 68, in <module>
    from ._modeling_parallel import ContextParallelConfig, ContextParallelModelPlan, ParallelConfig
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/_modeling_parallel.py", line 41, in <module>
    class ContextParallelConfig:
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/_modeling_parallel.py", line 74, in ContextParallelConfig
    _mesh: torch.distributed.device_mesh.DeviceMesh = None
AttributeError: type object 'DeviceMesh' has no attribute 'DeviceMesh'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1016, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/local/lib/python3.10/dist-packages/diffusers/pipelines/qwenimage/pipeline_qwenimage_edit.py", line 24, in <module>
    from ...loaders import QwenImageLoraLoaderMixin
  File "<frozen importlib._bootstrap>", line 1075, in _handle_fromlist
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1006, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1018, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import diffusers.loaders.lora_pipeline because of the following error (look up to see its traceback):
type object 'DeviceMesh' has no attribute 'DeviceMesh'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1485, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1406, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1269, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 824, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/main.py", line 416, in main
    run(
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/main.py", line 587, in run
    server.run()
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/server.py", line 61, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/server.py", line 68, in serve
    config.load()
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/config.py", line 467, in load
    self.loaded_app = import_from_string(self.app)
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app.py", line 66, in <module>
    from diffusers import QwenImageEditPipeline
  File "<frozen importlib._bootstrap>", line 1075, in _handle_fromlist
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1007, in __getattr__
    value = getattr(module, name)
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1007, in __getattr__
    value = getattr(module, name)
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1006, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1018, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import diffusers.pipelines.qwenimage.pipeline_qwenimage_edit because of the following error (look up to see its traceback):
Failed to import diffusers.loaders.lora_pipeline because of the following error (look up to see its traceback):
type object 'DeviceMesh' has no attribute 'DeviceMesh'
Application exited with code 1. This usually indicates an application failure. Check that the command used to launch your application is correct.

==========
== CUDA ==
==========

CUDA Version 12.1.1

Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1016, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/local/lib/python3.10/dist-packages/diffusers/loaders/lora_pipeline.py", line 34, in <module>
    from .lora_base import (  # noqa
  File "/usr/local/lib/python3.10/dist-packages/diffusers/loaders/lora_base.py", line 28, in <module>
    from ..models.modeling_utils import ModelMixin, load_state_dict
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/modeling_utils.py", line 68, in <module>
    from ._modeling_parallel import ContextParallelConfig, ContextParallelModelPlan, ParallelConfig
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/_modeling_parallel.py", line 41, in <module>
    class ContextParallelConfig:
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/_modeling_parallel.py", line 74, in ContextParallelConfig
    _mesh: torch.distributed.device_mesh.DeviceMesh = None
AttributeError: type object 'DeviceMesh' has no attribute 'DeviceMesh'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1016, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/local/lib/python3.10/dist-packages/diffusers/pipelines/qwenimage/pipeline_qwenimage_edit.py", line 24, in <module>
    from ...loaders import QwenImageLoraLoaderMixin
  File "<frozen importlib._bootstrap>", line 1075, in _handle_fromlist
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1006, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1018, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import diffusers.loaders.lora_pipeline because of the following error (look up to see its traceback):
type object 'DeviceMesh' has no attribute 'DeviceMesh'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1485, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1406, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1269, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 824, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/main.py", line 416, in main
    run(
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/main.py", line 587, in run
    server.run()
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/server.py", line 61, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/server.py", line 68, in serve
    config.load()
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/config.py", line 467, in load
    self.loaded_app = import_from_string(self.app)
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app.py", line 66, in <module>
    from diffusers import QwenImageEditPipeline
  File "<frozen importlib._bootstrap>", line 1075, in _handle_fromlist
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1007, in __getattr__
    value = getattr(module, name)
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1007, in __getattr__
    value = getattr(module, name)
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1006, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1018, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import diffusers.pipelines.qwenimage.pipeline_qwenimage_edit because of the following error (look up to see its traceback):
Failed to import diffusers.loaders.lora_pipeline because of the following error (look up to see its traceback):
type object 'DeviceMesh' has no attribute 'DeviceMesh'
Application exited with code 1. This usually indicates an application failure. Check that the command used to launch your application is correct.
Instance created. Preparing to start...
Instance stopped.
Instance is starting... Waiting for health checks to pass.

==========
== CUDA ==
==========

CUDA Version 12.1.1

Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1016, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/local/lib/python3.10/dist-packages/diffusers/loaders/lora_pipeline.py", line 34, in <module>
    from .lora_base import (  # noqa
  File "/usr/local/lib/python3.10/dist-packages/diffusers/loaders/lora_base.py", line 28, in <module>
    from ..models.modeling_utils import ModelMixin, load_state_dict
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/modeling_utils.py", line 68, in <module>
    from ._modeling_parallel import ContextParallelConfig, ContextParallelModelPlan, ParallelConfig
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/_modeling_parallel.py", line 41, in <module>
    class ContextParallelConfig:
  File "/usr/local/lib/python3.10/dist-packages/diffusers/models/_modeling_parallel.py", line 74, in ContextParallelConfig
    _mesh: torch.distributed.device_mesh.DeviceMesh = None
AttributeError: type object 'DeviceMesh' has no attribute 'DeviceMesh'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1016, in _get_module
    return importlib.import_module("." + module_name, self.__name__)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/usr/local/lib/python3.10/dist-packages/diffusers/pipelines/qwenimage/pipeline_qwenimage_edit.py", line 24, in <module>
    from ...loaders import QwenImageLoraLoaderMixin
  File "<frozen importlib._bootstrap>", line 1075, in _handle_fromlist
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1006, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1018, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import diffusers.loaders.lora_pipeline because of the following error (look up to see its traceback):
type object 'DeviceMesh' has no attribute 'DeviceMesh'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/usr/local/bin/uvicorn", line 8, in <module>
    sys.exit(main())
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1485, in __call__
    return self.main(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1406, in main
    rv = self.invoke(ctx)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 1269, in invoke
    return ctx.invoke(self.callback, **ctx.params)
  File "/usr/local/lib/python3.10/dist-packages/click/core.py", line 824, in invoke
    return callback(*args, **kwargs)
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/main.py", line 416, in main
    run(
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/main.py", line 587, in run
    server.run()
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/server.py", line 61, in run
    return asyncio.run(self.serve(sockets=sockets))
  File "/usr/lib/python3.10/asyncio/runners.py", line 44, in run
    return loop.run_until_complete(main)
  File "uvloop/loop.pyx", line 1518, in uvloop.loop.Loop.run_until_complete
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/server.py", line 68, in serve
    config.load()
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/config.py", line 467, in load
    self.loaded_app = import_from_string(self.app)
  File "/usr/local/lib/python3.10/dist-packages/uvicorn/importer.py", line 21, in import_from_string
    module = importlib.import_module(module_str)
  File "/usr/lib/python3.10/importlib/__init__.py", line 126, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1050, in _gcd_import
  File "<frozen importlib._bootstrap>", line 1027, in _find_and_load
  File "<frozen importlib._bootstrap>", line 1006, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 688, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 883, in exec_module
  File "<frozen importlib._bootstrap>", line 241, in _call_with_frames_removed
  File "/app/app.py", line 66, in <module>
    from diffusers import QwenImageEditPipeline
  File "<frozen importlib._bootstrap>", line 1075, in _handle_fromlist
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1007, in __getattr__
    value = getattr(module, name)
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1007, in __getattr__
    value = getattr(module, name)
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1006, in __getattr__
    module = self._get_module(self._class_to_module[name])
  File "/usr/local/lib/python3.10/dist-packages/diffusers/utils/import_utils.py", line 1018, in _get_module
    raise RuntimeError(
RuntimeError: Failed to import diffusers.pipelines.qwenimage.pipeline_qwenimage_edit because of the following error (look up to see its traceback):
Failed to import diffusers.loaders.lora_pipeline because of the following error (look up to see its traceback):
type object 'DeviceMesh' has no attribute 'DeviceMesh'
Application exited with code 1. This usually indicates an application failure. Check that the command used to launch your application is correct.

==========
== CUDA ==
==========

CUDA Version 12.1.1

Container image Copyright (c) 2016-2023, NVIDIA CORPORATION & AFFILIATES. All rights reserved.

This container image and its contents are governed by the NVIDIA Deep Learning Container License.
By pulling and using the container, you accept the terms and conditions of this license:
https://developer.nvidia.com/ngc/nvidia-deep-learning-container-license

A copy of this license is made available in this container at /NGC-DL-CONTAINER-LICENSE for your convenience.
