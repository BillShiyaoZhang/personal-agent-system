# Note on backend
This note documented the thinking and progress of the backend.

## Current progress
### MLX
Using [mlx-examples](https://github.com/ml-explore/mlx-examples) to download and start LLM server.  Later may implement better functions.  Commands are:
```
>> mlx_lm.manage --scan  // scan downloaded models on the device
>> mlx_lm.chat --model <model-name-on-hugging-face>  // start a CLI chat with a model.  Will download if not exists
>> mlx_lm.server --log-level DEBUG  // start a HTTP server
```

## Thinkings
### ChainGraph
This can be very helpful to develop a state-machine-based agent