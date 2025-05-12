# python -m sglang.launch_server \
#     --model-path YangZhoumill/scratch_234567_step360 \
#     --port 30003 \
#     --host 0.0.0.0   # Explicitly enabling Data Parallelism with 8 GPUs 

python -m sglang.launch_server \
    --model YangZhoumill/scratch_234567_step360 \
    --port 30004 \
    --dp-size 4 \
    --host 0.0.0.0 
