import requests
#import torch
from time import sleep, time
import io
import base64
from PIL import Image
import datetime
import os

body = {
  "prompt": "A photograph of an astronaut riding a horse",
  "seed": -1,
  "sampler_name": "Euler a",
  "batch_size": 1,
  "n_iter": 10,
  "steps": 100,
  "cfg_scale": 7,
  "width": 512,
  "height": 512,
  "negative_prompt": ""
}


if __name__ == '__main__':
    #print(torch.cuda.is_available())
    #print(torch.cuda.get_device_name(0))
    address = "http://localhost"
    port = "7861"
    url = f"{address}:{port}/"
    i = 0
    now = datetime.datetime.now()
    os.makedirs(f"output/txt2img/{datetime.date.isoformat(now)}")
    

    print("Waiting for connection")

    connection = False
    while not connection:
        try:
            sleep(5)
            res = requests.get(f"{url}docs", timeout=5.0)
            if res.status_code == 200:
                connection = True
        except:
            print("Connection failed, trying again")

    print("Connection established")

    res = requests.get(f"{url}sdapi/v1/samplers")

    samplers = [x['name'] for x in res.json()]

    res = requests.get(f"{url}sdapi/v1/sd-models")

    models = [x['title'] for x in res.json()]
    requests.post(f"{url}sdapi/v1/options", json={"outdir_txt2img_samples": "/sd-opt/outputs/txt2img-images"})

    for model in models:
        requests.post(f"{url}sdapi/v1/options", json={"sd_model_checkpoint": model})
        for sam in samplers:
            body["sampler_name"] = sam
            start = time()
            res = requests.post(f"{url}sdapi/v1/txt2img", json=body)
            end = time()
            ttime = end - start
            img = res.json()
            for im in img['images']:
                image = Image.open(io.BytesIO(base64.b64decode(im.split(",",1)[0])))
                image.save(f"output/txt2img/{datetime.date.isoformat(now)}/{i}.png")
                i += 1
            print(f"Model: {model} \tSampler: {sam} \t {(len(img['images']) * body['steps']) / ttime} it/s\n")
