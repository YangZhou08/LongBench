docker run -it --rm \
  -v $(pwd)/scripts:/workspace/scripts \
  -v /home/yangzho6/.cache/huggingface/hub:/root/.cache/huggingface/hub \
  cphsieh/ruler:0.2.0 /bin/bash 
