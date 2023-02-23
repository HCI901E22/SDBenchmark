#FROM continuumio/miniconda3
#FROM huggingface/transformers-pytorch-gpu
#RUN apt-get update && \
#    apt-get install -y software-properties-common && \
#    add-apt-repository -y ppa:deadsnakes/ppa && \
#    apt-get update && \
#    apt install -y python3.10

FROM zip3rzaro/sd-simple

RUN pip install xformers

# The code to run when container is started:
ENTRYPOINT ["conda", "run", "--no-capture-output", "-n", "myenv", "python", "sd-org/scripts/txt2img.py","--prompt", "a professional photograph of an astronaut riding a horse","--ckpt", "sd2-1.ckpt","--config", "sd-org/configs/stable-diffusion/v2-inference-v.yaml", "--H", "768", "--W", "768"]
